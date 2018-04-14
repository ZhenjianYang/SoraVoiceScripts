from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 调试地图

    CreateScenaFile(
        FileName            = 'A0001   ._SN',
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
        '12050待机',                            # 9
        '12051移动',                            # 10
        '12052攻击',                            # 11
        '12053伤害',                            # 12
        '12054倒下',                            # 13
        '12060待机',                            # 14
        '12061移动',                            # 15
        '12062攻击',                            # 16
        '12063伤害',                            # 17
        '12064倒下',                            # 18
        '12070待机',                            # 19
        '12071移动',                            # 20
        '12072攻击',                            # 21
        '12073伤害',                            # 22
        '12074倒下',                            # 23
        '12080待机',                            # 24
        '12081移动',                            # 25
        '12082攻击',                            # 26
        '12083伤害',                            # 27
        '12084倒下',                            # 28
        '12090待机',                            # 29
        '12091移动',                            # 30
        '12092攻击',                            # 31
        '12093伤害',                            # 32
        '12094倒下',                            # 33
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
        'ED6_DT29/CH12050 ._CH',             # 00
        'ED6_DT29/CH12051 ._CH',             # 01
        'ED6_DT29/CH12052 ._CH',             # 02
        'ED6_DT29/CH12053 ._CH',             # 03
        'ED6_DT29/CH12054 ._CH',             # 04
        'ED6_DT29/CH12364 ._CH',             # 05
        'ED6_DT29/CH12364 ._CH',             # 06
        'ED6_DT29/CH12364 ._CH',             # 07
        'ED6_DT29/CH12364 ._CH',             # 08
        'ED6_DT29/CH12364 ._CH',             # 09
        'ED6_DT29/CH12060 ._CH',             # 0A
        'ED6_DT29/CH12061 ._CH',             # 0B
        'ED6_DT29/CH12062 ._CH',             # 0C
        'ED6_DT29/CH12063 ._CH',             # 0D
        'ED6_DT29/CH12064 ._CH',             # 0E
        'ED6_DT29/CH12364 ._CH',             # 0F
        'ED6_DT29/CH12364 ._CH',             # 10
        'ED6_DT29/CH12364 ._CH',             # 11
        'ED6_DT29/CH12364 ._CH',             # 12
        'ED6_DT29/CH12364 ._CH',             # 13
        'ED6_DT29/CH12070 ._CH',             # 14
        'ED6_DT29/CH12071 ._CH',             # 15
        'ED6_DT29/CH12072 ._CH',             # 16
        'ED6_DT29/CH12073 ._CH',             # 17
        'ED6_DT29/CH12074 ._CH',             # 18
        'ED6_DT29/CH12364 ._CH',             # 19
        'ED6_DT29/CH12364 ._CH',             # 1A
        'ED6_DT29/CH12364 ._CH',             # 1B
        'ED6_DT29/CH12364 ._CH',             # 1C
        'ED6_DT29/CH12364 ._CH',             # 1D
        'ED6_DT29/CH12080 ._CH',             # 1E
        'ED6_DT29/CH12081 ._CH',             # 1F
        'ED6_DT29/CH12082 ._CH',             # 20
        'ED6_DT29/CH12083 ._CH',             # 21
        'ED6_DT29/CH12084 ._CH',             # 22
        'ED6_DT29/CH12364 ._CH',             # 23
        'ED6_DT29/CH12364 ._CH',             # 24
        'ED6_DT29/CH12364 ._CH',             # 25
        'ED6_DT29/CH12364 ._CH',             # 26
        'ED6_DT29/CH12364 ._CH',             # 27
        'ED6_DT29/CH12090 ._CH',             # 28
        'ED6_DT29/CH12091 ._CH',             # 29
        'ED6_DT29/CH12092 ._CH',             # 2A
        'ED6_DT29/CH12093 ._CH',             # 2B
        'ED6_DT29/CH12094 ._CH',             # 2C
        'ED6_DT29/CH12364 ._CH',             # 2D
        'ED6_DT29/CH12364 ._CH',             # 2E
        'ED6_DT29/CH12364 ._CH',             # 2F
        'ED6_DT29/CH12364 ._CH',             # 30
        'ED6_DT29/CH12364 ._CH',             # 31
    )

    AddCharChipPat(
        'ED6_DT29/CH12050P._CP',             # 00
        'ED6_DT29/CH12051P._CP',             # 01
        'ED6_DT29/CH12052P._CP',             # 02
        'ED6_DT29/CH12053P._CP',             # 03
        'ED6_DT29/CH12054P._CP',             # 04
        'ED6_DT29/CH12364P._CP',             # 05
        'ED6_DT29/CH12364P._CP',             # 06
        'ED6_DT29/CH12364P._CP',             # 07
        'ED6_DT29/CH12364P._CP',             # 08
        'ED6_DT29/CH12364P._CP',             # 09
        'ED6_DT29/CH12060P._CP',             # 0A
        'ED6_DT29/CH12061P._CP',             # 0B
        'ED6_DT29/CH12062P._CP',             # 0C
        'ED6_DT29/CH12063P._CP',             # 0D
        'ED6_DT29/CH12064P._CP',             # 0E
        'ED6_DT29/CH12364P._CP',             # 0F
        'ED6_DT29/CH12364P._CP',             # 10
        'ED6_DT29/CH12364P._CP',             # 11
        'ED6_DT29/CH12364P._CP',             # 12
        'ED6_DT29/CH12364P._CP',             # 13
        'ED6_DT29/CH12070P._CP',             # 14
        'ED6_DT29/CH12071P._CP',             # 15
        'ED6_DT29/CH12072P._CP',             # 16
        'ED6_DT29/CH12073P._CP',             # 17
        'ED6_DT29/CH12074P._CP',             # 18
        'ED6_DT29/CH12364P._CP',             # 19
        'ED6_DT29/CH12364P._CP',             # 1A
        'ED6_DT29/CH12364P._CP',             # 1B
        'ED6_DT29/CH12364P._CP',             # 1C
        'ED6_DT29/CH12364P._CP',             # 1D
        'ED6_DT29/CH12080P._CP',             # 1E
        'ED6_DT29/CH12081P._CP',             # 1F
        'ED6_DT29/CH12082P._CP',             # 20
        'ED6_DT29/CH12083P._CP',             # 21
        'ED6_DT29/CH12084P._CP',             # 22
        'ED6_DT29/CH12364P._CP',             # 23
        'ED6_DT29/CH12364P._CP',             # 24
        'ED6_DT29/CH12364P._CP',             # 25
        'ED6_DT29/CH12364P._CP',             # 26
        'ED6_DT29/CH12364P._CP',             # 27
        'ED6_DT29/CH12090P._CP',             # 28
        'ED6_DT29/CH12091P._CP',             # 29
        'ED6_DT29/CH12092P._CP',             # 2A
        'ED6_DT29/CH12093P._CP',             # 2B
        'ED6_DT29/CH12094P._CP',             # 2C
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
        "嗷—\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_4_5D0 end

    SaveToFile()

Try(main)
