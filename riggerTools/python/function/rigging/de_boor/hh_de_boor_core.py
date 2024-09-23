def get_open_uniform_kv(n, d):
    """
    Get open uniform knot vector

    Examples:
        import de_boor_core as core
        import importlib
        importlib.reload(core)


        core.get_open_uniform_kv(4, 1)
        core.get_open_uniform_kv(4, 2)
        core.get_open_uniform_kv(4, 3)

    Attributes:
        n (int): the number of control vertices
        d (int): degree of outputs

    Returns:
        list: open uniform knot vector
    """

    return [0] * (d + 1) + [(i - d) / (n - d) for i in range(d + 1, n)] + [1] * (d + 1)


def get_periodic_uniform_kv(n, d):
    """
    Get periodic uniform knot vector.  Append d values to the start and end

    Examples:
        import de_boor_core as core
        import importlib
        importlib.reload(core)


        core.get_periodic_uniform_kv(4, 2)

    Attributes:
        n (int): the number of control vertices
        d (int): degree of outputs

    Returns:
        list: periodic uniform knot vector with d additional values at the start and end
    """

    i = 1.0 / (n + d)
    return  [-i * a for a in range(d, 0, -1)] + [i * a for a in range(n + d + 1)] + [i * a + 1 for a in range(1, d + 1)]


def knot_vector(kv_type, cvs, d):
    """
    Convenience function for creating knot vectors and editing cv/joint/controls/etc lists

    Examples:
        import de_boor_core as core
        import importlib
        importlib.reload(core)


        core.knot_vector('open', ['a', 'b', 'c', 'd'], 2)
        core.knot_vector('periodic', ['a', 'b', 'c', 'd'], 1)

    Attributes:
        kv_type (str): knot vector type to be created
        cvs (list): list of objects to be associated with the knot vector
        d (int): degree of outputs

    Returns:
        tuple: knot vector and (modified) cvs list
    """

    cvs_copy = cvs[:]

    if kv_type == 'open':

        kv = get_open_uniform_kv(len(cvs), d)

    else:

        kv = get_periodic_uniform_kv(len(cvs), d)

        for i in range(d):
            cvs_copy.insert(0, cvs[len(cvs) - i - 1])
            cvs_copy.append(cvs[i])

    return kv, cvs_copy


def de_boor(n, d, t, kv, tol=0.000001):
    """
    Examples:
        from maya import cmds
        import de_boor_core as core
        import importlib
        importlib.reload(core)


        # example 1
        cmds.file(new=True, f=True)

        group_0 = cmds.group(em=True, n='GRP_0')
        group_1 = cmds.group(em=True, n='GRP_1')
        group_2 = cmds.group(em=True, n='GRP_2')
        group_3 = cmds.group(em=True, n='GRP_3')

        n = 8
        d = 2
        kv = [-0.333, -0.167, 0.0, 0.167, 0.333, 0.5, 0.667, 0.833, 1.0, 1.167, 1.333]
        parents = [group_2, group_3, group_0, group_1, group_2, group_3, group_0, group_1]
        samples = 100

        for sample in range(samples):
            t = float(sample) / (samples - 1)
            wts = core.de_boor(n, d, t, kv)

            grp_wts = {group_0: 0, group_1: 0, group_2: 0, group_3: 0}
            for i, wt in enumerate(wts):
                grp_wts[parents[i]] += wt

            for i, grp in enumerate([group_0, group_1, group_2, group_3]):
                loc = cmds.spaceLocator()[0]
                cmds.parent(loc, grp)

                cmds.setAttr('{}.t'.format(loc), *(t, grp_wts[grp], 0))
                loc_shp = cmds.listRelatives(loc, s=True)[0]
                cmds.setAttr('{}.localScale'.format(loc_shp), *(0.01, 0.01, 0.01))

        # example 2
        cmds.file(new=True, f=True)

        group_0 = cmds.group(em=True, n='GRP_0')
        group_1 = cmds.group(em=True, n='GRP_1')
        group_2 = cmds.group(em=True, n='GRP_2')
        group_3 = cmds.group(em=True, n='GRP_3')

        n = 4
        d = 3
        kv = core.get_open_uniform_kv(n, d)
        samples = 100

        for sample in range(samples):
            t = float(sample) / (samples - 1)
            wts = core.de_boor(n, d, t, kv)
            for i, wt in enumerate(wts):
                loc = cmds.spaceLocator()[0]
                cmds.parent(loc, 'GRP_{}'.format(i % 4))
                cmds.setAttr('{}.t'.format(loc), *(t, wt, 0))
                loc_shp = cmds.listRelatives(loc, s=True)[0]
                cmds.setAttr('{}.localScale'.format(loc_shp), *(0.01, 0.01, 0.01))

    Attributes:
        n (integer): number of control vertices
        d (integer): degree of the resulting curve
        t (float): parametric value along the curve that we use to query the value
        kv (list or tuple): represents the knot vector which is used to calculate the basis function weights

    Returns:
        list: contains float values between 0 and 1
    """

    if t + tol > 1:
        return [0.0 if i != n - 1 else 1.0 for i in range(n)]

    weights = [1.0 if kv[i] <= t < kv[i + 1] else 0.0 for i in range(n + d)]

    basis_width = n + d - 1

    for degree in range(1, d + 1):

        for i in range(basis_width):

            if weights[i] == 0 and weights[i + 1] == 0:
                continue

            a_denom = kv[i + degree] - kv[i]
            b_denom = kv[i + degree + 1] - kv[i + 1]
            a = (t - kv[i]) * weights[i] / a_denom if a_denom != 0 else 0.0
            b = (kv[i + degree + 1] - t) * weights[i + 1] / b_denom if b_denom != 0 else 0.0

            weights[i] = a + b

        basis_width -= 1

    return weights[:n]
