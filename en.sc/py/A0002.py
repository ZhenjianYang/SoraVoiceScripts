from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 调试地图

    CreateScenaFile(
        FileName            = 'A0002   ._SN',
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
        '12100待機',                            # 9
        '12101移動',                            # 10
        '12102攻撃',                            # 11
        '12103ダメージ',                        # 12
        '12104倒れ',                            # 13
        '12110待機',                            # 14
        '12111移動',                            # 15
        '12112攻撃',                            # 16
        '12113ダメージ',                        # 17
        '12114倒れ',                            # 18
        '12120待機',                            # 19
        '12121移動',                            # 20
        '12122攻撃',                            # 21
        '12123ダメージ',                        # 22
        '12124倒れ',                            # 23
        '12130待機',                            # 24
        '12131移動',                            # 25
        '12132攻撃',                            # 26
        '12133ダメージ',                        # 27
        '12134倒れ',                            # 28
        '12140待機',                            # 29
        '12141移動',                            # 30
        '12142攻撃',                            # 31
        '12143ダメージ',                        # 32
        '12144倒れ',                            # 33
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
        'ED6_DT29/CH12100 ._CH',             # 00
        'ED6_DT29/CH12101 ._CH',             # 01
        'ED6_DT29/CH12102 ._CH',             # 02
        'ED6_DT29/CH12103 ._CH',             # 03
        'ED6_DT29/CH12104 ._CH',             # 04
        'ED6_DT29/CH12364 ._CH',             # 05
        'ED6_DT29/CH12364 ._CH',             # 06
        'ED6_DT29/CH12364 ._CH',             # 07
        'ED6_DT29/CH12364 ._CH',             # 08
        'ED6_DT29/CH12364 ._CH',             # 09
        'ED6_DT29/CH12110 ._CH',             # 0A
        'ED6_DT29/CH12111 ._CH',             # 0B
        'ED6_DT29/CH12112 ._CH',             # 0C
        'ED6_DT29/CH12113 ._CH',             # 0D
        'ED6_DT29/CH12114 ._CH',             # 0E
        'ED6_DT29/CH12364 ._CH',             # 0F
        'ED6_DT29/CH12364 ._CH',             # 10
        'ED6_DT29/CH12364 ._CH',             # 11
        'ED6_DT29/CH12364 ._CH',             # 12
        'ED6_DT29/CH12364 ._CH',             # 13
        'ED6_DT29/CH12120 ._CH',             # 14
        'ED6_DT29/CH12121 ._CH',             # 15
        'ED6_DT29/CH12122 ._CH',             # 16
        'ED6_DT29/CH12123 ._CH',             # 17
        'ED6_DT29/CH12124 ._CH',             # 18
        'ED6_DT29/CH12364 ._CH',             # 19
        'ED6_DT29/CH12364 ._CH',             # 1A
        'ED6_DT29/CH12364 ._CH',             # 1B
        'ED6_DT29/CH12364 ._CH',             # 1C
        'ED6_DT29/CH12364 ._CH',             # 1D
        'ED6_DT29/CH12130 ._CH',             # 1E
        'ED6_DT29/CH12131 ._CH',             # 1F
        'ED6_DT29/CH12132 ._CH',             # 20
        'ED6_DT29/CH12133 ._CH',             # 21
        'ED6_DT29/CH12134 ._CH',             # 22
        'ED6_DT29/CH12364 ._CH',             # 23
        'ED6_DT29/CH12364 ._CH',             # 24
        'ED6_DT29/CH12364 ._CH',             # 25
        'ED6_DT29/CH12364 ._CH',             # 26
        'ED6_DT29/CH12364 ._CH',             # 27
        'ED6_DT29/CH12140 ._CH',             # 28
        'ED6_DT29/CH12141 ._CH',             # 29
        'ED6_DT29/CH12142 ._CH',             # 2A
        'ED6_DT29/CH12143 ._CH',             # 2B
        'ED6_DT29/CH12144 ._CH',             # 2C
        'ED6_DT29/CH12364 ._CH',             # 2D
        'ED6_DT29/CH12364 ._CH',             # 2E
        'ED6_DT29/CH12364 ._CH',             # 2F
        'ED6_DT29/CH12364 ._CH',             # 30
        'ED6_DT29/CH12364 ._CH',             # 31
    )

    AddCharChipPat(
        'ED6_DT29/CH12100P._CP',             # 00
        'ED6_DT29/CH12101P._CP',             # 01
        'ED6_DT29/CH12102P._CP',             # 02
        'ED6_DT29/CH12103P._CP',             # 03
        'ED6_DT29/CH12104P._CP',             # 04
        'ED6_DT29/CH12364P._CP',             # 05
        'ED6_DT29/CH12364P._CP',             # 06
        'ED6_DT29/CH12364P._CP',             # 07
        'ED6_DT29/CH12364P._CP',             # 08
        'ED6_DT29/CH12364P._CP',             # 09
        'ED6_DT29/CH12110P._CP',             # 0A
        'ED6_DT29/CH12111P._CP',             # 0B
        'ED6_DT29/CH12112P._CP',             # 0C
        'ED6_DT29/CH12113P._CP',             # 0D
        'ED6_DT29/CH12114P._CP',             # 0E
        'ED6_DT29/CH12364P._CP',             # 0F
        'ED6_DT29/CH12364P._CP',             # 10
        'ED6_DT29/CH12364P._CP',             # 11
        'ED6_DT29/CH12364P._CP',             # 12
        'ED6_DT29/CH12364P._CP',             # 13
        'ED6_DT29/CH12120P._CP',             # 14
        'ED6_DT29/CH12121P._CP',             # 15
        'ED6_DT29/CH12122P._CP',             # 16
        'ED6_DT29/CH12123P._CP',             # 17
        'ED6_DT29/CH12124P._CP',             # 18
        'ED6_DT29/CH12364P._CP',             # 19
        'ED6_DT29/CH12364P._CP',             # 1A
        'ED6_DT29/CH12364P._CP',             # 1B
        'ED6_DT29/CH12364P._CP',             # 1C
        'ED6_DT29/CH12364P._CP',             # 1D
        'ED6_DT29/CH12130P._CP',             # 1E
        'ED6_DT29/CH12131P._CP',             # 1F
        'ED6_DT29/CH12132P._CP',             # 20
        'ED6_DT29/CH12133P._CP',             # 21
        'ED6_DT29/CH12134P._CP',             # 22
        'ED6_DT29/CH12364P._CP',             # 23
        'ED6_DT29/CH12364P._CP',             # 24
        'ED6_DT29/CH12364P._CP',             # 25
        'ED6_DT29/CH12364P._CP',             # 26
        'ED6_DT29/CH12364P._CP',             # 27
        'ED6_DT29/CH12140P._CP',             # 28
        'ED6_DT29/CH12141P._CP',             # 29
        'ED6_DT29/CH12142P._CP',             # 2A
        'ED6_DT29/CH12143P._CP',             # 2B
        'ED6_DT29/CH12144P._CP',             # 2C
        'ED6_DT29/CH12364P._CP',             # 2D
        'ED6_DT29/CH12364P._CP',             # 2E
        'ED6_DT29/CH12364P._CP',             # 2F
        'ED6_DT29/CH12364P._CP',             # 30
        'ED6_DT29/CH12364P._CP',             # 31
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
        TalkScenaIndex      = 4,
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
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
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
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
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
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
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
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
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
        TalkScenaIndex      = 4,
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
        TalkScenaIndex      = 4,
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
        TalkScenaIndex      = 4,
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
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
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
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
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
        TalkScenaIndex      = 4,
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
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
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
        TalkScenaIndex      = 4,
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
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
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
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
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
        TalkScenaIndex      = 4,
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
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
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
        TalkScenaIndex      = 4,
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
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
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
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 20000,
        Z                   = 0,
        Y                   = 4000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 40,
        ChipIndex           = 0x28,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 20000,
        Z                   = 0,
        Y                   = 8000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 41,
        ChipIndex           = 0x29,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 20000,
        Z                   = 0,
        Y                   = 12000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 42,
        ChipIndex           = 0x2A,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 20000,
        Z                   = 0,
        Y                   = 16000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 43,
        ChipIndex           = 0x2B,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 20000,
        Z                   = 0,
        Y                   = 20000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 44,
        ChipIndex           = 0x2C,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )


    ScpFunction(
        "Function_0_55A",          # 00, 0
        "Function_1_55B",          # 01, 1
        "Function_2_55C",          # 02, 2
        "Function_3_5CF",          # 03, 3
        "Function_4_5D0",          # 04, 4
    )


    def Function_0_55A(): pass

    label("Function_0_55A")

    Return()

    # Function_0_55A end

    def Function_1_55B(): pass

    label("Function_1_55B")

    Return()

    # Function_1_55B end

    def Function_2_55C(): pass

    label("Function_2_55C")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_END)),
        (0, "loc_589"),
        (1, "loc_591"),
        (2, "loc_599"),
        (3, "loc_5A1"),
        (4, "loc_5A9"),
        (5, "loc_5B1"),
        (SWITCH_DEFAULT, "loc_5B9"),
    )


    label("loc_589")

    Sleep(100)
    Jump("loc_5B9")

    label("loc_591")

    Sleep(100)
    Jump("loc_5B9")

    label("loc_599")

    Sleep(200)
    Jump("loc_5B9")

    label("loc_5A1")

    Sleep(300)
    Jump("loc_5B9")

    label("loc_5A9")

    Sleep(400)
    Jump("loc_5B9")

    label("loc_5B1")

    Sleep(500)
    Jump("loc_5B9")

    label("loc_5B9")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5CE")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_5B9")

    label("loc_5CE")

    Return()

    # Function_2_55C end

    def Function_3_5CF(): pass

    label("Function_3_5CF")

    Return()

    # Function_3_5CF end

    def Function_4_5D0(): pass

    label("Function_4_5D0")

    TalkBegin(0xFE)

    ChrTalk(    #0
        0xFE,
        "がおー\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_4_5D0 end

    SaveToFile()

Try(main)
