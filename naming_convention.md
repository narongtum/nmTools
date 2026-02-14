# Naming Convention Documentation

This document outlines the naming conventions used in the auto-rigging system, based on the analysis of `core.py` and `generic_maya_dict.py`.

## 1. General Structure

The system supports two primary naming styles. The `core.parse_node_name` and `core.check_name_style` functions are used to detect and handle these styles.

### Style A: Prefix Style (Capital Lead)
Used when the side indicator is at the beginning of the name.
*   **Format**: `[Side]_[BaseName]_[Type]`
*   **Examples**: `L_arm_jnt`, `R_leg_ctrl`, `C_spine_grp`
*   **Side Indicators**: `L`, `R`, `C`, `M`

### Style B: Suffix Style (Side Follows)
Used when the side indicator follows the name but precedes the type.
*   **Format**: `[BaseName][Side]_[Type]`
*   **Examples**: `armLFT_jnt`, `legRGT_ctrl`, `spineCEN_grp`
*   **Side Indicators**: `LFT`, `RGT`, `CEN`

## 2. Side Indicators

| Side | Prefix Style | Suffix Style | Color Code |
| :--- | :--- | :--- | :--- |
| **Left** | `L` | `LFT` | Blue / SoftBlue |
| **Right** | `R` | `RGT` | Red |
| **Center** | `C`, `M` | `CEN` | Yellow / Primary |

## 3. Node Type Suffixes

Standard suffixes are defined in `generic_maya_dict.py` (`NODE_short_dict` and `NODE_dict`).

### Node Type Shortcuts

| Node Type | Suffix |
| :--- | :--- |
| **addDoubleLinear** | `adl` |
| **aimConstraint** | `aimCons` |
| **aimMatrix** | `aimMat` |
| **animCurveU** | `animCrv` |
| **animCurveUL** | `animCurveUL` |
| **animCurveUU** | `animUU` |
| **blendColors** | `blc` |
| **blendMatrix** | `blendMat` |
| **blendShape** | `bsh` |
| **blendTwoAttr** | `bta` |
| **blendWeighted** | `blendWeighted` |
| **cMuscleSmartConstraint** | `musleCons` |
| **clamp** | `cmp` |
| **cluster** | `clus` |
| **composeMatrix** | `composeMatrix` |
| **condition** | `cnd` |
| **curveInfo** | `crvInfo` |
| **decomposeMatrix** | `deComp` |
| **deformSine** | `defSine` |
| **deformSquash** | `defSquash` |
| **distanceBetween** | `dtw` |
| **eulerToQuat** | `eulToQuat` |
| **expression** | `exp` |
| **file** | `file` |
| **follicle** | `flc` |
| **fourByFourMatrix** | `fBFMat` |
| **group** | `grp` |
| **ikEffector** | `ike` |
| **ikHandle** | `ikh` |
| **joint** | `jnt` |
| **lambert** | `lambert` |
| **locator** | `loc` |
| **mesh** | `ply` |
| **motionPath** | `mp` |
| **multDoubleLinear** | `mdl` |
| **multMatrix** | `multMatrix` |
| **multiplyDivide** | `mdv` |
| **network** | `meta` |
| **nurbsCurve** | `ctrl` |
| **nurbsSurface** | `nrb` |
| **orientConstraint** | `orienCons` |
| **parentConstraint** | `parCons` |
| **phong** | `phong` |
| **pickMatrix** | `pickMat` |
| **place2dTexture** | `place2d` |
| **plusMinusAverage** | `pma` |
| **pointConstraint** | `poinCons` |
| **pointOnCurveInfo** | `poci` |
| **poleVectorConstraint** | `poleCons` |
| **quatInvert** | `quatInv` |
| **quatProd** | `quatProd` |
| **quatToEuler** | `quatToEul` |
| **remapValue** | `remap` |
| **reverse** | `rev` |
| **scaleConstraint** | `scaleCons` |
| **setRange** | `setRange` |
| **shadingEngine** | `sg` |
| **skinCluster** | `skc` |
| **vectorProduct** | `vecProd` |
| **wtAddMatrix** | `wtAddMat` |

## 4. Specific Rigging Suffixes

*   **Zero Group**: `[Name]_Zro` or `[Name]Zro_grp` (Hierarchy root for a controller)
*   **Offset Group**: `[Name]_Offset` (Secondary group under Zero)
*   **Gimbal Controller**: `[Name]_Gmbl` (Gimbal correction controller)

## 5. Color Coding Standards

Defined in `generic_maya_dict.COLOR_part_dict`:
*   **Left (`LFT`/`L`)**: Blue
*   **Right (`RGT`/`R`)**: Red
*   **Center / Primary**: Yellow
*   **Dynamic**: White
*   **Secondary**: White
*   **Tertiary**: SoftBlue

## 6. Joint Naming Standards
Standard joint lists are pre-defined for auto-rigging purposes:
*   **Standard List**: `ankleLFT_bJnt`, `wristRGT_bJnt`, etc.
*   **Binder Joint Suffix**: `_bJnt` (commonly used for skinning joints)
