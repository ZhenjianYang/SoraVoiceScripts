from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 调试地图

    CreateScenaFile(
        FileName            = 'A0023   ._SN',
        MapName             = 'map1',
        Location            = 'T0030.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60010",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            '',
            '',
            '',
            '',
            '',
            '',
            ''
        ],
    )

    BuildStringList(
        '@FileName',                            # 8
        '04080ケビン待機',                      # 9
        '04081ケビン移動',                      # 10
        '04082ケビン攻撃',                      # 11
        '04083ケビン弾かれ',                    # 12
        '04084ケビン倒れ',                      # 13
        '04085ケビン魔法詠唱',                  # 14
        '04086ケビン魔法発射',                  # 15
        '04087ケビン勝利',                      # 16
        '04090アネラス待機',                    # 17
        '04091アネラス移動',                    # 18
        '04092アネラス攻撃',                    # 19
        '04093アネラス弾かれ',                  # 20
        '04094アネラス倒れ',                    # 21
        '04095アネラス魔法詠唱',                # 22
        '04096アネラス魔法発射',                # 23
        '04097アネラス勝利',                    # 24
        '04100ジョゼット待機',                  # 25
        '04101ジョゼット移動',                  # 26
        '04102ジョゼット攻撃',                  # 27
        '04103ジョゼット弾かれ',                # 28
        '04104ジョゼット倒れ',                  # 29
        '04105ジョゼット魔法詠唱',              # 30
        '04106ジョゼット魔法発射',              # 31
        '04107ジョゼット勝利',                  # 32
        '04130クルツ待機',                      # 33
        '04131クルツ移動',                      # 34
        '04132クルツ攻撃',                      # 35
        '04133クルツ弾かれ',                    # 36
        '04134クルツ倒れ',                      # 37
        '04135クルツ魔法詠唱',                  # 38
        '04136クルツ魔法発射',                  # 39
    )

    DeclEntryPoint(
        Unknown_00              = 0,
        Unknown_04              = 0,
        Unknown_08              = 0,
        Unknown_0C              = 4,
        Unknown_0E              = 5,
        Unknown_10              = 0,
        Unknown_14              = 9500,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 0,
        Unknown_28              = 2800,
        Unknown_2C              = 262,
        Unknown_30              = 315,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 0,
        Unknown_3A              = 0,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT27/CH04080 ._CH',             # 00
        'ED6_DT27/CH04081 ._CH',             # 01
        'ED6_DT27/CH04082 ._CH',             # 02
        'ED6_DT27/CH04083 ._CH',             # 03
        'ED6_DT27/CH04084 ._CH',             # 04
        'ED6_DT27/CH04085 ._CH',             # 05
        'ED6_DT27/CH04086 ._CH',             # 06
        'ED6_DT27/CH04087 ._CH',             # 07
        'ED6_DT27/CH04083 ._CH',             # 08
        'ED6_DT27/CH04083 ._CH',             # 09
        'ED6_DT07/CH00420 ._CH',             # 0A
        'ED6_DT07/CH00421 ._CH',             # 0B
        'ED6_DT07/CH00422 ._CH',             # 0C
        'ED6_DT07/CH00423 ._CH',             # 0D
        'ED6_DT07/CH00424 ._CH',             # 0E
        'ED6_DT07/CH00425 ._CH',             # 0F
        'ED6_DT07/CH00426 ._CH',             # 10
        'ED6_DT27/CH04097 ._CH',             # 11
        'ED6_DT07/CH00423 ._CH',             # 12
        'ED6_DT07/CH00423 ._CH',             # 13
        'ED6_DT07/CH00310 ._CH',             # 14
        'ED6_DT07/CH00311 ._CH',             # 15
        'ED6_DT07/CH00312 ._CH',             # 16
        'ED6_DT07/CH00313 ._CH',             # 17
        'ED6_DT07/CH00314 ._CH',             # 18
        'ED6_DT07/CH00315 ._CH',             # 19
        'ED6_DT07/CH00316 ._CH',             # 1A
        'ED6_DT27/CH04107 ._CH',             # 1B
        'ED6_DT07/CH00313 ._CH',             # 1C
        'ED6_DT07/CH00313 ._CH',             # 1D
        'ED6_DT07/CH00410 ._CH',             # 1E
        'ED6_DT07/CH00411 ._CH',             # 1F
        'ED6_DT07/CH00412 ._CH',             # 20
        'ED6_DT07/CH00413 ._CH',             # 21
        'ED6_DT07/CH00414 ._CH',             # 22
        'ED6_DT07/CH00415 ._CH',             # 23
        'ED6_DT07/CH00416 ._CH',             # 24
        'ED6_DT07/CH00413 ._CH',             # 25
        'ED6_DT07/CH00413 ._CH',             # 26
        'ED6_DT07/CH00413 ._CH',             # 27
    )

    AddCharChipPat(
        'ED6_DT27/CH04080P._CP',             # 00
        'ED6_DT27/CH04081P._CP',             # 01
        'ED6_DT27/CH04082P._CP',             # 02
        'ED6_DT27/CH04083P._CP',             # 03
        'ED6_DT27/CH04084P._CP',             # 04
        'ED6_DT27/CH04085P._CP',             # 05
        'ED6_DT27/CH04086P._CP',             # 06
        'ED6_DT27/CH04087P._CP',             # 07
        'ED6_DT27/CH04083P._CP',             # 08
        'ED6_DT27/CH04083P._CP',             # 09
        'ED6_DT07/CH00420P._CP',             # 0A
        'ED6_DT07/CH00421P._CP',             # 0B
        'ED6_DT07/CH00422P._CP',             # 0C
        'ED6_DT07/CH00423P._CP',             # 0D
        'ED6_DT07/CH00424P._CP',             # 0E
        'ED6_DT07/CH00425P._CP',             # 0F
        'ED6_DT07/CH00426P._CP',             # 10
        'ED6_DT27/CH04097P._CP',             # 11
        'ED6_DT07/CH00423P._CP',             # 12
        'ED6_DT07/CH00423P._CP',             # 13
        'ED6_DT07/CH00310P._CP',             # 14
        'ED6_DT07/CH00311P._CP',             # 15
        'ED6_DT07/CH00312P._CP',             # 16
        'ED6_DT07/CH00313P._CP',             # 17
        'ED6_DT07/CH00314P._CP',             # 18
        'ED6_DT07/CH00315P._CP',             # 19
        'ED6_DT07/CH00316P._CP',             # 1A
        'ED6_DT27/CH04107P._CP',             # 1B
        'ED6_DT07/CH00313P._CP',             # 1C
        'ED6_DT07/CH00313P._CP',             # 1D
        'ED6_DT07/CH00410P._CP',             # 1E
        'ED6_DT07/CH00411P._CP',             # 1F
        'ED6_DT07/CH00412P._CP',             # 20
        'ED6_DT07/CH00413P._CP',             # 21
        'ED6_DT07/CH00414P._CP',             # 22
        'ED6_DT07/CH00415P._CP',             # 23
        'ED6_DT07/CH00416P._CP',             # 24
        'ED6_DT07/CH00413P._CP',             # 25
        'ED6_DT07/CH00413P._CP',             # 26
        'ED6_DT07/CH00413P._CP',             # 27
    )

    DeclNpc(
        X                   = 4000,
        Z                   = 0,
        Y                   = 4000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 4000,
        Z                   = 0,
        Y                   = 8000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 4000,
        Z                   = 0,
        Y                   = 12000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 6,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 4000,
        Z                   = 0,
        Y                   = 16000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 4000,
        Z                   = 0,
        Y                   = 20000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 5,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 4000,
        Z                   = 0,
        Y                   = 24000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 7,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 4000,
        Z                   = 0,
        Y                   = 28000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 8,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 4000,
        Z                   = 0,
        Y                   = 32000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 9,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 8000,
        Z                   = 0,
        Y                   = 4000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 8000,
        Z                   = 0,
        Y                   = 8000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 8000,
        Z                   = 0,
        Y                   = 12000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 8000,
        Z                   = 0,
        Y                   = 16000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 13,
        ChipIndex           = 0xD,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 8000,
        Z                   = 0,
        Y                   = 20000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 5,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 8000,
        Z                   = 0,
        Y                   = 24000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 15,
        ChipIndex           = 0xF,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 7,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 8000,
        Z                   = 0,
        Y                   = 28000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 16,
        ChipIndex           = 0x10,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 10,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 8000,
        Z                   = 0,
        Y                   = 32000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 17,
        ChipIndex           = 0x11,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 11,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 12000,
        Z                   = 0,
        Y                   = 4000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 20,
        ChipIndex           = 0x14,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 12000,
        Z                   = 0,
        Y                   = 8000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 21,
        ChipIndex           = 0x15,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 12000,
        Z                   = 0,
        Y                   = 12000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 22,
        ChipIndex           = 0x16,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 12000,
        Z                   = 0,
        Y                   = 16000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 23,
        ChipIndex           = 0x17,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 12000,
        Z                   = 0,
        Y                   = 20000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 24,
        ChipIndex           = 0x18,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 5,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 12000,
        Z                   = 0,
        Y                   = 24000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 25,
        ChipIndex           = 0x19,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 7,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 12000,
        Z                   = 0,
        Y                   = 28000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 26,
        ChipIndex           = 0x1A,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 12,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 12000,
        Z                   = 0,
        Y                   = 32000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 27,
        ChipIndex           = 0x1B,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 13,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 16000,
        Z                   = 0,
        Y                   = 4000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 30,
        ChipIndex           = 0x1E,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 16000,
        Z                   = 0,
        Y                   = 8000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 31,
        ChipIndex           = 0x1F,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 16000,
        Z                   = 0,
        Y                   = 12000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 32,
        ChipIndex           = 0x20,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 16000,
        Z                   = 0,
        Y                   = 16000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 33,
        ChipIndex           = 0x21,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 16000,
        Z                   = 0,
        Y                   = 20000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 34,
        ChipIndex           = 0x22,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 5,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 16000,
        Z                   = 0,
        Y                   = 24000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 35,
        ChipIndex           = 0x23,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 7,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 16000,
        Z                   = 0,
        Y                   = 28000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 36,
        ChipIndex           = 0x24,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 14,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )


    ScpFunction(
        "Function_0_5CA",          # 00, 0
        "Function_1_5CB",          # 01, 1
        "Function_2_5CC",          # 02, 2
        "Function_3_5E2",          # 03, 3
        "Function_4_5F8",          # 04, 4
        "Function_5_613",          # 05, 5
        "Function_6_62E",          # 06, 6
        "Function_7_71B",          # 07, 7
        "Function_8_768",          # 08, 8
        "Function_9_824",          # 09, 9
        "Function_10_936",         # 0A, 10
        "Function_11_9F2",         # 0B, 11
        "Function_12_B04",         # 0C, 12
        "Function_13_BC0",         # 0D, 13
        "Function_14_CB2",         # 0E, 14
        "Function_15_D6E",         # 0F, 15
        "Function_16_E60",         # 10, 16
    )


    def Function_0_5CA(): pass

    label("Function_0_5CA")

    Return()

    # Function_0_5CA end

    def Function_1_5CB(): pass

    label("Function_1_5CB")

    Return()

    # Function_1_5CB end

    def Function_2_5CC(): pass

    label("Function_2_5CC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5E1")
    OP_99(0xFE, 0x0, 0x7, 0x640)
    Jump("Function_2_5CC")

    label("loc_5E1")

    Return()

    # Function_2_5CC end

    def Function_3_5E2(): pass

    label("Function_3_5E2")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5F7")
    OP_99(0xFE, 0x0, 0x7, 0x7D0)
    Jump("Function_3_5E2")

    label("loc_5F7")

    Return()

    # Function_3_5E2 end

    def Function_4_5F8(): pass

    label("Function_4_5F8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_612")
    OP_99(0xFE, 0x0, 0x0, 0x5DC)
    Sleep(500)
    Jump("Function_4_5F8")

    label("loc_612")

    Return()

    # Function_4_5F8 end

    def Function_5_613(): pass

    label("Function_5_613")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_62D")
    OP_99(0xFE, 0x0, 0x3, 0x3E8)
    Sleep(500)
    Jump("Function_5_613")

    label("loc_62D")

    Return()

    # Function_5_613 end

    def Function_6_62E(): pass

    label("Function_6_62E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_71A")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(80)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(80)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(80)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(80)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(80)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(80)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(240)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(50)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(50)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(80)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(240)
    Jump("Function_6_62E")

    label("loc_71A")

    Return()

    # Function_6_62E end

    def Function_7_71B(): pass

    label("Function_7_71B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_767")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    Jump("Function_7_71B")

    label("loc_767")

    Return()

    # Function_7_71B end

    def Function_8_768(): pass

    label("Function_8_768")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_823")
    SetChrChipByIndex(0xFE, 5)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    SetChrChipByIndex(0xFE, 6)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(240)
    Sleep(1000)
    Jump("Function_8_768")

    label("loc_823")

    Return()

    # Function_8_768 end

    def Function_9_824(): pass

    label("Function_9_824")

    SetChrFlags(0xFE, 0x2)

    label("loc_829")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_935")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(120)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(120)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(120)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(120)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(120)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(120)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(120)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(90)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(80)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(80)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(80)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(360)
    Jump("loc_829")

    label("loc_935")

    Return()

    # Function_9_824 end

    def Function_10_936(): pass

    label("Function_10_936")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_9F1")
    SetChrChipByIndex(0xFE, 15)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    SetChrChipByIndex(0xFE, 16)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(240)
    Sleep(1000)
    Jump("Function_10_936")

    label("loc_9F1")

    Return()

    # Function_10_936 end

    def Function_11_9F2(): pass

    label("Function_11_9F2")

    SetChrFlags(0xFE, 0x2)

    label("loc_9F7")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_B03")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(360)
    Jump("loc_9F7")

    label("loc_B03")

    Return()

    # Function_11_9F2 end

    def Function_12_B04(): pass

    label("Function_12_B04")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_BBF")
    SetChrChipByIndex(0xFE, 25)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    SetChrChipByIndex(0xFE, 26)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(240)
    Sleep(1000)
    Jump("Function_12_B04")

    label("loc_BBF")

    Return()

    # Function_12_B04 end

    def Function_13_BC0(): pass

    label("Function_13_BC0")

    SetChrFlags(0xFE, 0x2)

    label("loc_BC5")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_CB1")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(360)
    Jump("loc_BC5")

    label("loc_CB1")

    Return()

    # Function_13_BC0 end

    def Function_14_CB2(): pass

    label("Function_14_CB2")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_D6D")
    SetChrChipByIndex(0xFE, 35)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    SetChrChipByIndex(0xFE, 36)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(240)
    Sleep(1000)
    Jump("Function_14_CB2")

    label("loc_D6D")

    Return()

    # Function_14_CB2 end

    def Function_15_D6E(): pass

    label("Function_15_D6E")

    SetChrFlags(0xFE, 0x2)

    label("loc_D73")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_E5F")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(360)
    Jump("loc_D73")

    label("loc_E5F")

    Return()

    # Function_15_D6E end

    def Function_16_E60(): pass

    label("Function_16_E60")

    TalkBegin(0xFE)

    ChrTalk(    #0
        0xFE,
        "はにゃ。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_16_E60 end

    SaveToFile()

Try(main)
