from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 卢安

    CreateScenaFile(
        FileName            = 'T2102   ._SN',
        MapName             = 'Ruan',
        Location            = 'T2102.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60012",
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
        '城中老年男子',                         # 9
        '城中中年妇女',                         # 10
        '城中小男孩',                           # 11
        '森特',                                 # 12
        '贵族中年男子',                         # 13
        '贵族女孩',                             # 14
        '哈尔德',                               # 15
        '林德号',                               # 16
        '林德号影子',                           # 17
        '爱德望',                               # 18
        '克拉姆',                               # 19
        '波利',                                 # 20
        '玛丽',                                 # 21
        '达尼艾尔',                             # 22
        '乔儿',                                 # 23
        '汉斯',                                 # 24
        '特蕾莎院长',                           # 25
        '科林兹校长',                           # 26
        '库莱泽',                               # 27
        '萨马里奥',                             # 28
        '豆豆',                                 # 29
        '哈尔德',                               # 30
        '森特',                                 # 31
        '孩子',                                 # 32
        '贵族女子',                             # 33
        '贵族男子',                             # 34
        '卢安市·北街区',                       # 35
    )

    DeclEntryPoint(
        Unknown_00              = 0,
        Unknown_04              = 0,
        Unknown_08              = 6000,
        Unknown_0C              = 4,
        Unknown_0E              = 0,
        Unknown_10              = 0,
        Unknown_14              = 9500,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 0,
        Unknown_28              = 2800,
        Unknown_2C              = 262,
        Unknown_30              = 45,
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
        'ED6_DT07/CH01100 ._CH',             # 00
        'ED6_DT07/CH01020 ._CH',             # 01
        'ED6_DT07/CH01160 ._CH',             # 02
        'ED6_DT07/CH01660 ._CH',             # 03
        'ED6_DT07/CH01130 ._CH',             # 04
        'ED6_DT07/CH01210 ._CH',             # 05
        'ED6_DT07/CH01030 ._CH',             # 06
        'ED6_DT07/CH01290 ._CH',             # 07
        'ED6_DT07/CH02590 ._CH',             # 08
        'ED6_DT07/CH02500 ._CH',             # 09
        'ED6_DT07/CH02630 ._CH',             # 0A
        'ED6_DT07/CH02640 ._CH',             # 0B
        'ED6_DT07/CH02390 ._CH',             # 0C
        'ED6_DT07/CH02550 ._CH',             # 0D
        'ED6_DT07/CH02570 ._CH',             # 0E
        'ED6_DT07/CH02600 ._CH',             # 0F
        'ED6_DT07/CH01450 ._CH',             # 10
        'ED6_DT07/CH01450 ._CH',             # 11
        'ED6_DT07/CH01470 ._CH',             # 12
        'ED6_DT07/CH01120 ._CH',             # 13
        'ED6_DT07/CH01660 ._CH',             # 14
        'ED6_DT07/CH01470 ._CH',             # 15
        'ED6_DT07/CH01200 ._CH',             # 16
        'ED6_DT07/CH01180 ._CH',             # 17
    )

    AddCharChipPat(
        'ED6_DT07/CH01100P._CP',             # 00
        'ED6_DT07/CH01020P._CP',             # 01
        'ED6_DT07/CH01160P._CP',             # 02
        'ED6_DT07/CH01660P._CP',             # 03
        'ED6_DT07/CH01130P._CP',             # 04
        'ED6_DT07/CH01210P._CP',             # 05
        'ED6_DT07/CH01030P._CP',             # 06
        'ED6_DT07/CH01290P._CP',             # 07
        'ED6_DT07/CH02590P._CP',             # 08
        'ED6_DT07/CH02500P._CP',             # 09
        'ED6_DT07/CH02630P._CP',             # 0A
        'ED6_DT07/CH02640P._CP',             # 0B
        'ED6_DT07/CH02390P._CP',             # 0C
        'ED6_DT07/CH02550P._CP',             # 0D
        'ED6_DT07/CH02570P._CP',             # 0E
        'ED6_DT07/CH02600P._CP',             # 0F
        'ED6_DT07/CH01450P._CP',             # 10
        'ED6_DT07/CH01450P._CP',             # 11
        'ED6_DT07/CH01470P._CP',             # 12
        'ED6_DT07/CH01120P._CP',             # 13
        'ED6_DT07/CH01660P._CP',             # 14
        'ED6_DT07/CH01470P._CP',             # 15
        'ED6_DT07/CH01200P._CP',             # 16
        'ED6_DT07/CH01180P._CP',             # 17
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 19,
        ChipIndex           = 0x13,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x184,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x184,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 101700,
        Z                   = 0,
        Y                   = 83800,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 13,
        ChipIndex           = 0xD,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 15,
        ChipIndex           = 0xF,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 111220,
        Z                   = 6150,
        Y                   = 101150,
        Direction           = 45,
        Unknown2            = 0,
        Unknown3            = 16,
        ChipIndex           = 0x10,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 112530,
        Z                   = 6150,
        Y                   = 102340,
        Direction           = 225,
        Unknown2            = 0,
        Unknown3            = 17,
        ChipIndex           = 0x11,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = 129990,
        Z                   = 8150,
        Y                   = 92560,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 18,
        ChipIndex           = 0x12,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 111500,
        Z                   = 4150,
        Y                   = 85650,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 19,
        ChipIndex           = 0x13,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 108620,
        Z                   = 6150,
        Y                   = 95510,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 20,
        ChipIndex           = 0x14,
        NpcIndex            = 0x191,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 21,
        ChipIndex           = 0x15,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 22,
        ChipIndex           = 0x16,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 23,
        ChipIndex           = 0x17,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 71170,
        Z                   = 0,
        Y                   = 80860,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0xFF,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclActor(
        TriggerX            = 100400,
        TriggerZ            = 0,
        TriggerY            = 83700,
        TriggerRange        = 1000,
        ActorX              = 101700,
        ActorZ              = 1500,
        ActorY              = 83800,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 9,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 108610,
        TriggerZ            = 6150,
        TriggerY            = 96910,
        TriggerRange        = 800,
        ActorX              = 108610,
        ActorZ              = 8350,
        ActorY              = 96910,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 41,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 127080,
        TriggerZ            = 6150,
        TriggerY            = 100740,
        TriggerRange        = 800,
        ActorX              = 127080,
        ActorZ              = 8350,
        ActorY              = 100740,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 42,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 122620,
        TriggerZ            = 400,
        TriggerY            = 100640,
        TriggerRange        = 800,
        ActorX              = 122620,
        ActorZ              = 1600,
        ActorY              = 100640,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 43,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 140870,
        TriggerZ            = 1000,
        TriggerY            = 108000,
        TriggerRange        = 800,
        ActorX              = 140870,
        ActorZ              = 2000,
        ActorY              = 108000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 11,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 149330,
        TriggerZ            = 1000,
        TriggerY            = 108000,
        TriggerRange        = 800,
        ActorX              = 149330,
        ActorZ              = 2000,
        ActorY              = 108000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 11,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 103030,
        TriggerZ            = 1000,
        TriggerY            = 108000,
        TriggerRange        = 800,
        ActorX              = 103030,
        ActorZ              = 2000,
        ActorY              = 108000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 11,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 96980,
        TriggerZ            = 1000,
        TriggerY            = 108000,
        TriggerRange        = 800,
        ActorX              = 96980,
        ActorZ              = 2000,
        ActorY              = 108000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 11,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_5EA",          # 00, 0
        "Function_1_72C",          # 01, 1
        "Function_2_74F",          # 02, 2
        "Function_3_8CC",          # 03, 3
        "Function_4_957",          # 04, 4
        "Function_5_A13",          # 05, 5
        "Function_6_DAF",          # 06, 6
        "Function_7_E3B",          # 07, 7
        "Function_8_10D7",         # 08, 8
        "Function_9_156C",         # 09, 9
        "Function_10_1571",        # 0A, 10
        "Function_11_18C2",        # 0B, 11
        "Function_12_1908",        # 0C, 12
        "Function_13_1D58",        # 0D, 13
        "Function_14_1D9A",        # 0E, 14
        "Function_15_1DDC",        # 0F, 15
        "Function_16_1E19",        # 10, 16
        "Function_17_1E42",        # 11, 17
        "Function_18_227F",        # 12, 18
        "Function_19_3B90",        # 13, 19
        "Function_20_3BB9",        # 14, 20
        "Function_21_3BFC",        # 15, 21
        "Function_22_3C2A",        # 16, 22
        "Function_23_3C6D",        # 17, 23
        "Function_24_3C9B",        # 18, 24
        "Function_25_3CDF",        # 19, 25
        "Function_26_3D23",        # 1A, 26
        "Function_27_3D67",        # 1B, 27
        "Function_28_3DAB",        # 1C, 28
        "Function_29_3DEF",        # 1D, 29
        "Function_30_3E33",        # 1E, 30
        "Function_31_3E77",        # 1F, 31
        "Function_32_3EBB",        # 20, 32
        "Function_33_3EEB",        # 21, 33
        "Function_34_3F23",        # 22, 34
        "Function_35_3F60",        # 23, 35
        "Function_36_3F9D",        # 24, 36
        "Function_37_3FDA",        # 25, 37
        "Function_38_3FFA",        # 26, 38
        "Function_39_4013",        # 27, 39
        "Function_40_403D",        # 28, 40
        "Function_41_40D6",        # 29, 41
        "Function_42_4185",        # 2A, 42
        "Function_43_41EB",        # 2B, 43
    )


    def Function_0_5EA(): pass

    label("Function_0_5EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_659")
    SetChrFlags(0x1A, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_634")
    SetChrPos(0x11, 108580, 6150, 96500, 0)
    SetChrPos(0x1B, 136340, 8150, 95080, 270)
    SetChrPos(0x1C, 135340, 8150, 95080, 90)
    Jump("loc_656")

    label("loc_634")

    SetChrPos(0x11, 111500, 4150, 80040, 100)
    SetChrPos(0x1B, 134010, 8150, 92800, 270)

    label("loc_656")

    Jump("loc_715")

    label("loc_659")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_68F")
    SetChrPos(0x1A, 139320, 6150, 99610, 180)
    SetChrPos(0x1B, 130460, 8150, 98040, 180)
    SetChrFlags(0x1C, 0x10)
    ClearChrFlags(0x1D, 0x80)
    Jump("loc_715")

    label("loc_68F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_6CF")
    SetChrPos(0x1A, 139320, 6150, 99610, 180)
    SetChrPos(0x1B, 129990, 8150, 92560, 90)
    SetChrFlags(0x1C, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x66, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_6CC")
    ClearChrFlags(0x1E, 0x80)

    label("loc_6CC")

    Jump("loc_715")

    label("loc_6CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_6FF")
    SetChrPos(0x1A, 111460, 4150, 79470, 90)
    SetChrPos(0x1B, 141100, 6150, 100100, 39)
    Jump("loc_715")

    label("loc_6FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_END)), "loc_715")
    SetChrFlags(0x1A, 0x10)
    SetChrFlags(0x1B, 0x10)
    SetChrFlags(0x1C, 0x10)

    label("loc_715")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_72B")
    ClearMapFlags(0x10)
    SetMapFlags(0x10000000)
    Event(0, 12)

    label("loc_72B")

    Return()

    # Function_0_5EA end

    def Function_1_72C(): pass

    label("Function_1_72C")

    OP_16(0x2, 0xFA0, 0x4E20, 0xFFFF63C0, 0x230049)
    OP_22(0x1C5, 0x1, 0x64)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_74E")
    OP_64(0x0, 0x1)

    label("loc_74E")

    Return()

    # Function_1_72C end

    def Function_2_74F(): pass

    label("Function_2_74F")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_774")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_8B6")

    label("loc_774")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_78D")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_8B6")

    label("loc_78D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7A6")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_8B6")

    label("loc_7A6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7BF")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_8B6")

    label("loc_7BF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7D8")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_8B6")

    label("loc_7D8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7F1")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_8B6")

    label("loc_7F1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_80A")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_8B6")

    label("loc_80A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_823")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_8B6")

    label("loc_823")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_83C")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_8B6")

    label("loc_83C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_855")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_8B6")

    label("loc_855")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_86E")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_8B6")

    label("loc_86E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_887")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_8B6")

    label("loc_887")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8A0")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_8B6")

    label("loc_8A0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8B6")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_8B6")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_8CB")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_8B6")

    label("loc_8CB")

    Return()

    # Function_2_74F end

    def Function_3_8CC(): pass

    label("Function_3_8CC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_91B")

    ChrTalk(    #0
        0xFE,
        (
            "定期船来之前\x01",
            "还有相当长的时间呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "要不要先\x01",
            "去吃饭呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_953")

    label("loc_91B")

    OP_A2(0x5)

    ChrTalk(    #2
        0xFE,
        "～前往王都的船是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        "嗯，还有空闲呢。\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xFE, 0x10)

    label("loc_953")

    TalkEnd(0xFE)
    Return()

    # Function_3_8CC end

    def Function_4_957(): pass

    label("Function_4_957")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_9A9")

    ChrTalk(    #4
        0x1D,
        (
            "前往王都的船就快到了呢。\x02\x03",

            "最近都没有误点过，\x01",
            "还是定期船方便啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A0F")

    label("loc_9A9")

    OP_A2(0x4)

    ChrTalk(    #5
        0x1D,
        (
            "这次的视察\x01",
            "成果丰厚啊。\x02\x03",

            "旅游向导指出的\x01",
            "景点也不少。\x02\x03",

            "那么，接着是去王都\x01",
            "跟飞船公社的谈判了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A0F")

    TalkEnd(0xFE)
    Return()

    # Function_4_957 end

    def Function_5_A13(): pass

    label("Function_5_A13")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_B22")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AC9")

    ChrTalk(    #6
        0xFE,
        (
            "检查了几十次\x01",
            "却没有任何异常。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        (
            "尽管如此，却怎么也\x01",
            "动不了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xFE,
        (
            "但是，要是这就放弃\x01",
            "我作为维修员就失职了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xFE,
        (
            "没发现原因之前\x01",
            "几百次都要检查下去！\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)
    Jump("loc_B1F")

    label("loc_AC9")


    ChrTalk(    #10
        0xFE,
        (
            "维修的基本就是检查，\x01",
            "哥哥就是这么说的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xFE,
        (
            "没发现原因之前\x01",
            "几百次都要检查下去！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B1F")

    Jump("loc_DAB")

    label("loc_B22")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_BFD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BAF")

    ChrTalk(    #12
        0xFE,
        (
            "库莱泽哥哥\x01",
            "都乘上『埃尔赛尤』了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xFE,
        (
            "因为哥哥很优秀，\x01",
            "现在一定在修理导力器。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        "所以我、我们也不能输，要努力！\x02",
    )

    CloseMessageWindow()
    OP_A2(0x3)
    Jump("loc_BFA")

    label("loc_BAF")


    ChrTalk(    #15
        0xFE,
        (
            "库莱泽哥哥\x01",
            "现在一定在修理导力器。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xFE,
        "所以我、我们也不能输，要努力！\x02",
    )

    CloseMessageWindow()

    label("loc_BFA")

    Jump("loc_DAB")

    label("loc_BFD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_CA5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_C5E")

    ChrTalk(    #17
        0xFE,
        (
            "我的工作\x01",
            "也渐渐增多了哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xFE,
        (
            "要更加更加熟练，\x01",
            "以后成为独当一面的维修士。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CA2")

    label("loc_C5E")

    OP_A2(0x3)

    ChrTalk(    #19
        0xFE,
        "舷梯的导力机构ＯＫ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xFE,
        "好，这样靠岸准备就完成了。\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xFE, 0x10)

    label("loc_CA2")

    Jump("loc_DAB")

    label("loc_CA5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_D46")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_CFA")

    ChrTalk(    #21
        0xFE,
        (
            "我要努力\x01",
            "早日独当一面！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xFE,
        (
            "为此还有很多事\x01",
            "要学习才行……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D43")

    label("loc_CFA")

    OP_A2(0x3)

    ChrTalk(    #23
        0xFE,
        (
            "库莱泽哥哥\x01",
            "一定也是想认真做研究的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0xFE,
        (
            "我要努力\x01",
            "早日独当一面！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D43")

    Jump("loc_DAB")

    label("loc_D46")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_END)), "loc_DAB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_D6F")

    ChrTalk(    #25
        0xFE,
        "我是见习的维修员。\x02",
    )

    CloseMessageWindow()
    Jump("loc_DAB")

    label("loc_D6F")

    OP_A2(0x3)

    ChrTalk(    #26
        0xFE,
        "导力机构锁定确认完毕！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xFE,
        "嗯，没有任何问题。\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xFE, 0x10)

    label("loc_DAB")

    TalkEnd(0xFE)
    Return()

    # Function_5_A13 end

    def Function_6_DAF(): pass

    label("Function_6_DAF")


    ChrTalk(    #28
        0x1A,
        (
            "萨马里奥\x01",
            "去确认诱导灯。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x1A,
        "豆豆那小家伙去哪了？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x1B,
        (
            "豆豆去检查\x01",
            "靠岸装置了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x1A,
        "是吗，那就交给他了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x1A,
        "时间不多，要慎重。\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x1B, 0x10)
    Return()

    # Function_6_DAF end

    def Function_7_E3B(): pass

    label("Function_7_E3B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_F22")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_EA0")

    ChrTalk(    #33
        0xFE,
        (
            "那么… \x01",
            "接着即将到达的是『赛希莉亚号』。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xFE,
        (
            "如果要乘坐\x01",
            "最好赶快办手续哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F1F")

    label("loc_EA0")

    OP_A2(0x1)

    ChrTalk(    #35
        0xFE,
        (
            "那么… \x01",
            "接着即将到达的是『赛希莉亚号』。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0xFE,
        (
            "正准备到达卢安，\x01",
            "并发来了准点的联络。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xFE,
        (
            "如果要乘坐\x01",
            "最好赶快办手续哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F1F")

    Jump("loc_10D3")

    label("loc_F22")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_FB1")

    ChrTalk(    #38
        0xFE,
        (
            "最近的豆豆\x01",
            "变得像个维修员的样子了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xFE,
        (
            "即使不作细节的指示，\x01",
            "一般的工作也能处理了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0xFE,
        (
            "哈哈，偶尔不在\x01",
            "就能体会到他的成长了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10D3")

    label("loc_FB1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1076")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1010")

    ChrTalk(    #41
        0xFE,
        (
            "中央工房的新型引擎\x01",
            "据说终于完成了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0xFE,
        (
            "作为技术人员\x01",
            "真想看一次啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1073")

    label("loc_1010")

    OP_A2(0x1)

    ChrTalk(    #43
        0xFE,
        (
            "中央工房的新型引擎\x01",
            "据说终于完成了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0xFE,
        (
            "这样的话，『埃尔赛尤』\x01",
            "应该也能发挥本来的性能了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1073")

    Jump("loc_10D3")

    label("loc_1076")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_END)), "loc_10D3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_10C1")
    OP_4A(0x1B, 255)

    ChrTalk(    #45
        0xFE,
        "时间不多，要慎重。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0xFE,
        "很快就会再有船来了。\x02",
    )

    CloseMessageWindow()
    OP_4B(0x1B, 255)
    Jump("loc_10D3")

    label("loc_10C1")

    OP_A2(0x1)
    OP_A2(0x2)
    OP_4A(0x1B, 255)
    Call(0, 6)
    OP_4B(0x1B, 255)

    label("loc_10D3")

    TalkEnd(0xFE)
    Return()

    # Function_7_E3B end

    def Function_8_10D7(): pass

    label("Function_8_10D7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_11B5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1172")

    ChrTalk(    #47
        0xFE,
        (
            "嗯，结晶回路还有效，\x01",
            "导力器实体也没有异常……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0xFE,
        (
            "但是，重要的装置\x01",
            "为什么不能动呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0xFE,
        (
            "这可能有什么\x01",
            "根本性的问题也不一定。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_11B2")

    label("loc_1172")


    ChrTalk(    #50
        0xFE,
        (
            "所有导力器\x01",
            "都找不到异常。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0xFE,
        (
            "不过……\x01",
            "装置就是不能动了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11B2")

    Jump("loc_1568")

    label("loc_11B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_12CA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1272")

    ChrTalk(    #52
        0xFE,
        (
            "导力器停止的原因\x01",
            "我们维修员也不明白。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0xFE,
        (
            "如果库莱泽在\x01",
            "说不定能知道些什么……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0xFE,
        (
            "他现在肯定作为『埃尔赛尤』的乘员\x01",
            "在那边努力吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0xFE,
        (
            "我们也只能\x01",
            "尽自己所能了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_12C7")

    label("loc_1272")


    ChrTalk(    #56
        0xFE,
        (
            "导力器停止的原因\x01",
            "还完全不明白。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0xFE,
        (
            "库莱泽也一定\x01",
            "在『埃尔赛尤』舰上\x01",
            "努力着吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12C7")

    Jump("loc_1568")

    label("loc_12CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_1362")

    ChrTalk(    #58
        0xFE,
        (
            "豆豆作为维修员\x01",
            "离能够独当一面的时候\x01",
            "也不远了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0xFE,
        (
            "这样库莱泽就能\x01",
            "安心投入研究工作了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0xFE,
        (
            "工作变得更忙了…\x01",
            "不过，为了伙伴要加油啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1568")

    label("loc_1362")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_13B8")

    ChrTalk(    #61
        0xFE,
        (
            "呼，下一艘船的接纳准备\x01",
            "只能靠我们来做了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0xFE,
        (
            "因为豆豆\x01",
            "去了主日学校。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1568")

    label("loc_13B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1522")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1437")

    ChrTalk(    #63
        0xFE,
        (
            "为了让哥哥库莱泽放心，\x01",
            "豆豆比别的孩子更加努力呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0xFE,
        (
            "再过一阵子，那孩子\x01",
            "一定能成为出色的维修员的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_151F")

    label("loc_1437")

    OP_A2(0x2)

    ChrTalk(    #65
        0xFE,
        (
            "库莱泽身为研究者\x01",
            "也受到了极高评价。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0xFE,
        (
            "中央工房都来邀请他\x01",
            "参加新型引擎的开发计划。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0xFE,
        (
            "但是他为了照料豆豆\x01",
            "就拒绝了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0xFE,
        (
            "就是因为这个吧，\x01",
            "豆豆比别的孩子更加努力呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0xFE,
        (
            "再过一阵子，那孩子\x01",
            "一定能成为独当一面的维修员哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_151F")

    Jump("loc_1568")

    label("loc_1522")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_END)), "loc_1568")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1556")

    ChrTalk(    #70
        0xFE,
        (
            "不好意思，\x01",
            "我们正在商量工作。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1568")

    label("loc_1556")

    OP_A2(0x2)
    OP_A2(0x1)
    OP_4A(0x1A, 255)
    Call(0, 6)
    OP_4B(0x1A, 255)

    label("loc_1568")

    TalkEnd(0xFE)
    Return()

    # Function_8_10D7 end

    def Function_9_156C(): pass

    label("Function_9_156C")

    Call(0, 10)
    Return()

    # Function_9_156C end

    def Function_10_1571(): pass

    label("Function_10_1571")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_158C")
    OP_4A(0x11, 255)
    Call(0, 17)
    OP_4B(0x11, 255)
    Jump("loc_18C1")

    label("loc_158C")

    TalkBegin(0x11)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_1612")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15EC")

    ChrTalk(    #71
        0x11,
        (
            "飞船公社\x01",
            "也没有发来什么联络。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x11,
        (
            "导力通讯不能使用，\x01",
            "这也难怪了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_160F")

    label("loc_15EC")


    ChrTalk(    #73
        0x11,
        (
            "飞船公社\x01",
            "也没有发来什么联络。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_160F")

    Jump("loc_18BE")

    label("loc_1612")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_16D4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1683")

    ChrTalk(    #74
        0x11,
        "咦，怎么了？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x11,
        (
            "抱歉，定期船\x01",
            "还没有恢复的迹象。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x11,
        (
            "现在，时刻表上面\x01",
            "都贴着那张纸。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_16D1")

    label("loc_1683")


    ChrTalk(    #77
        0x11,
        (
            "定期船好像都停在\x01",
            "各地的飞船坪呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0x11,
        (
            "不过，没有出现坠落\x01",
            "就算是万幸了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16D1")

    Jump("loc_18BE")

    label("loc_16D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_1776")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1716")

    ChrTalk(    #79
        0x11,
        (
            "哼，可惜已经结束了。\x01",
            "明明马上就要去帮忙了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1773")

    label("loc_1716")

    OP_A2(0x0)

    ChrTalk(    #80
        0x11,
        (
            "噢，好像两阵营之间\x01",
            "有发生争执嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0x11,
        (
            "哼，可惜已经结束了。\x01",
            "明明马上就要赶去帮忙了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1773")

    Jump("loc_18BE")

    label("loc_1776")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1843")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_17ED")

    ChrTalk(    #82
        0x11,
        (
            "当然我是支持旅游推进派\x01",
            "的诺曼先生啦！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0x11,
        (
            "海运业的复活是不可能的啦。\x01",
            "港口已经落后于时代啦～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1840")

    label("loc_17ED")

    OP_A2(0x0)

    ChrTalk(    #84
        0x11,
        (
            "这次的选举对这个飞船坪\x01",
            "也有很大影响啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0x11,
        (
            "候选人说的话\x01",
            "我一直有注意的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1840")

    Jump("loc_18BE")

    label("loc_1843")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_END)), "loc_18BE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1879")

    ChrTalk(    #86
        0x11,
        (
            "选举中也有选举中的\x01",
            "精彩之处啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18BE")

    label("loc_1879")

    OP_A2(0x0)

    ChrTalk(    #87
        0x11,
        (
            "呼哈啊～\x01",
            "最近有点闲呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0x11,
        (
            "因为在选举，\x01",
            "游客好像都不来了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18BE")

    TalkEnd(0x11)

    label("loc_18C1")

    Return()

    # Function_10_1571 end

    def Function_11_18C2(): pass

    label("Function_11_18C2")

    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #89
        "\x07\x05门上着锁。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_11_18C2 end

    def Function_12_1908(): pass

    label("Function_12_1908")

    FadeToDark(0, 0, -1)
    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_1922")
    AddParty(0x2, 0xF7, 0xFF)
    Jump("loc_1926")

    label("loc_1922")

    AddParty(0x5, 0xF7, 0xFF)

    label("loc_1926")

    SetChrFlags(0x101, 0x8)
    SetChrFlags(0xF7, 0x8)
    OP_6D(132050, 8360, 87990, 0)
    OP_67(0, 9030, -10000, 0)
    OP_6B(7800, 0)
    OP_6C(102000, 0)
    OP_6E(262, 0)
    OP_22(0x79, 0x0, 0x64)
    OP_71(0xA, 0x4)
    OP_6F(0x7, 100)
    OP_72(0xA, 0x4)
    SetChrPos(0xF, 136000, 7500, 82500, 90)
    SetChrPos(0x10, 136000, 5500, 82500, 90)
    SetChrFlags(0xF, 0x4)
    ClearChrFlags(0xF, 0x40)
    OP_A1(0xF, 0x8)
    OP_72(0x8, 0x4)
    OP_72(0x8, 0x20)
    OP_72(0x8, 0x2)
    OP_71(0x8, 0x400)
    OP_71(0x8, 0x40)
    OP_A1(0x10, 0x9)
    OP_72(0x9, 0x4)
    SetChrFlags(0x10, 0x4)
    SetChrPos(0x1A, 134820, 8150, 93440, 180)
    SetChrPos(0x1B, 132030, 8150, 94310, 180)
    SetChrPos(0x1C, 134350, 8150, 92500, 180)
    OP_C8(0x200, 0x46, "C_PLAC04._CH", 0x1, 0x7D0)
    FadeToBright(2000, 0)

    def lambda_1A33():
        OP_6D(131670, 8360, 81790, 8000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_1A33)

    def lambda_1A4B():
        OP_67(0, 8000, -10000, 8000)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_1A4B)

    def lambda_1A63():
        OP_6B(3500, 8000)
        ExitThread()

    QueueWorkItem(0x1, 2, lambda_1A63)

    def lambda_1A73():
        OP_6C(134000, 8000)
        ExitThread()

    QueueWorkItem(0x1, 3, lambda_1A73)

    def lambda_1A83():
        OP_8F(0xFE, 0x21340, 0x9C4, 0x14244, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 2, lambda_1A83)

    def lambda_1A9E():
        OP_8F(0xFE, 0x21340, 0x7D0, 0x14244, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_1A9E)
    WaitChrThread(0xF, 0x2)
    WaitChrThread(0x10, 0x2)

    def lambda_1AC3():
        OP_8F(0xFE, 0x21340, 0x3E8, 0x14244, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 3, lambda_1AC3)

    def lambda_1ADE():
        OP_8F(0xFE, 0x21340, 0x3E8, 0x14244, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 3, lambda_1ADE)
    WaitChrThread(0xF, 0x3)
    WaitChrThread(0x10, 0x3)
    WaitChrThread(0x0, 0x0)
    WaitChrThread(0x0, 0x1)
    WaitChrThread(0x0, 0x2)
    WaitChrThread(0x0, 0x3)
    OP_23(0x79)
    OP_22(0xC8, 0x0, 0x64)
    OP_7C(0x0, 0x64, 0xBB8, 0x64)
    OP_B0(0x8, 0x32)
    OP_B0(0x9, 0x32)
    OP_6F(0x8, 100)
    OP_70(0x8, 0x1)
    OP_6F(0x9, 100)
    OP_70(0x9, 0x1)
    OP_22(0x76, 0x0, 0x64)
    OP_73(0x8)
    OP_73(0x9)
    Sleep(400)
    OP_B0(0x7, 0x2D)
    OP_6F(0x7, 100)
    OP_70(0x7, 0x0)
    OP_71(0xA, 0x4)
    OP_22(0x78, 0x0, 0x64)
    OP_73(0x7)
    Sleep(1000)
    OP_6F(0x8, 410)
    OP_70(0x8, 0x1CC)
    OP_22(0x6, 0x0, 0x64)
    Sleep(800)
    OP_22(0x6, 0x0, 0x64)
    OP_73(0x8)
    ClearChrFlags(0x101, 0x8)
    ClearChrFlags(0xF7, 0x8)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0x101, 0x40)
    SetChrFlags(0xF7, 0x40)
    SetChrFlags(0x8, 0x40)
    SetChrFlags(0x9, 0x40)
    SetChrFlags(0xA, 0x40)
    SetChrFlags(0xB, 0x40)
    SetChrFlags(0xC, 0x40)
    SetChrFlags(0xD, 0x40)
    SetChrFlags(0xE, 0x40)
    SetChrBattleFlags(0x101, 0x20)
    SetChrBattleFlags(0xF7, 0x20)
    SetChrBattleFlags(0x8, 0x20)
    SetChrBattleFlags(0x9, 0x20)
    SetChrBattleFlags(0xA, 0x20)
    SetChrBattleFlags(0xB, 0x20)
    SetChrBattleFlags(0xC, 0x20)
    SetChrBattleFlags(0xD, 0x20)
    SetChrBattleFlags(0xE, 0x20)
    OP_48()
    OP_89(0x101, 137100, 8200, 82210, 90)
    OP_89(0xF7, 137100, 8200, 82210, 90)
    OP_89(0x8, 137100, 8200, 82210, 90)
    OP_89(0x9, 137100, 8200, 82210, 90)
    OP_89(0xA, 137100, 8200, 82210, 90)
    OP_89(0xB, 137100, 8200, 82210, 90)
    OP_89(0xC, 142970, 8300, 85160, 272)
    OP_89(0xD, 137100, 8200, 82210, 90)
    OP_89(0xE, 142970, 8300, 85160, 272)
    OP_43(0xA, 0x1, 0x0, 0xE)
    Sleep(1000)
    OP_43(0x9, 0x1, 0x0, 0xE)
    Sleep(500)
    OP_43(0x8, 0x1, 0x0, 0xD)
    Sleep(1000)
    OP_43(0xB, 0x1, 0x0, 0xD)
    Sleep(1200)
    OP_43(0xC, 0x1, 0x0, 0x10)
    OP_43(0x101, 0x1, 0x0, 0xF)
    Sleep(1000)
    OP_43(0xF7, 0x1, 0x0, 0xF)
    Sleep(200)
    OP_43(0xE, 0x1, 0x0, 0x10)
    Sleep(1200)
    OP_43(0xD, 0x1, 0x0, 0xD)
    FadeToDark(2000, 0, -1)
    OP_0D()
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x10, 0x80)
    OP_71(0x7, 0x4)
    OP_71(0x8, 0x4)
    OP_71(0x9, 0x4)
    OP_72(0xA, 0x4)
    NewScene("ED6_DT21/T2120   ._SN", 105, 0, 0)
    IdleLoop()
    Return()

    # Function_12_1908 end

    def Function_13_1D58(): pass

    label("Function_13_1D58")

    OP_8E(0xFE, 0x20ADA, 0x2008, 0x14294, 0x7D0, 0x0)
    OP_8E(0xFE, 0x20274, 0x2008, 0x14C3A, 0x7D0, 0x0)
    OP_8E(0xFE, 0x2031E, 0x1F9A, 0x179D0, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_13_1D58 end

    def Function_14_1D9A(): pass

    label("Function_14_1D9A")

    OP_8E(0xFE, 0x2092C, 0x2008, 0x14262, 0x1388, 0x0)
    OP_8E(0xFE, 0x20274, 0x2008, 0x14C3A, 0x1388, 0x0)
    OP_8E(0xFE, 0x2031E, 0x1F9A, 0x179D0, 0x1388, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_14_1D9A end

    def Function_15_1DDC(): pass

    label("Function_15_1DDC")

    OP_8E(0xFE, 0x20ADA, 0x2008, 0x14294, 0x7D0, 0x0)
    OP_8E(0xFE, 0x20274, 0x2008, 0x14C3A, 0x7D0, 0x0)
    OP_8E(0xFE, 0x2031E, 0x1F9A, 0x179D0, 0x7D0, 0x0)
    Return()

    # Function_15_1DDC end

    def Function_16_1E19(): pass

    label("Function_16_1E19")

    OP_8E(0xFE, 0x20314, 0x2008, 0x14EBA, 0x7D0, 0x0)
    OP_8E(0xFE, 0x2031E, 0x1F9A, 0x179D0, 0x7D0, 0x0)
    Return()

    # Function_16_1E19 end

    def Function_17_1E42(): pass

    label("Function_17_1E42")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1E5C")
    Call(0, 40)
    FadeToBright(0, 0)

    label("loc_1E5C")

    EventBegin(0x0)
    Fade(1000)
    OP_6D(100140, 0, 83780, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(3180, 0)
    OP_6C(134000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 99550, 0, 84460, 90)
    SetChrPos(0xF7, 99470, 0, 83460, 90)
    SetChrPos(0x105, 98390, 0, 84500, 90)
    SetChrPos(0x104, 98500, 0, 83270, 90)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_20B4")
    OP_A2(0x1402)

    ChrTalk(    #90
        0x11,
        "#5P噢，欢迎。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0x11,
        (
            "#5P去蔡斯的\x01",
            "游击士一行吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0x101,
        "#1011F啊，嗯，是的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0x11,
        (
            "#5P我收到嘉恩的联络了。\x01",
            "据说船票费用协会包了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0x11,
        "#5P赶快办乘船手续吧？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xF7, 0x101, 400)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_1FE2")

    ChrTalk(    #95
        0x106,
        (
            "#050F办好手续，就在这里\x01",
            "等船来就行了。\x02\x03",

            "在卢安地区\x01",
            "还有事情吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2027")

    label("loc_1FE2")


    ChrTalk(    #96
        0x103,
        (
            "#020F办好手续，就在这里\x01",
            "等船来就行了。\x02\x03",

            "在卢安地区\x01",
            "还有事情吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2027")

    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【还有事情】\x01",          # 0
            "【办理乘船手续】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_20B1")

    ChrTalk(    #97
        0x11,
        (
            "#5P那么，事情办完\x01",
            "再来找我好了。\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x0)
    Return()

    label("loc_20B1")

    Jump("loc_2164")

    label("loc_20B4")


    ChrTalk(    #98
        0x11,
        (
            "#5P快快，怎样。\x01",
            "办理乘船手续吗？\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【还有事情】\x01",          # 0
            "【办理乘船手续】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2164")

    ChrTalk(    #99
        0x11,
        (
            "#5P那么，事情办完\x01",
            "再来找我好了。\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x0)
    Return()

    label("loc_2164")

    OP_8C(0xF7, 90, 400)

    ChrTalk(    #100
        0x11,
        "#5P好的！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0x11,
        (
            "#5P那么所有人\x01",
            "都在纸上签字。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0x101,
        "#1006F嗯，明白了。\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(72, 320, 56, 3)

    AnonymousTalk(    #103
        "\x07\x05艾丝蒂尔等人办完了乘船手续。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(    #104
        0x11,
        "#5P所有人都没问题。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0x11,
        (
            "#5P那么定期船到来之前\x01",
            "就在飞船坪等等吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0x101,
        "#1001F好～\x02",
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_C0(0x15, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Call(0, 18)
    Return()

    # Function_17_1E42 end

    def Function_18_227F(): pass

    label("Function_18_227F")

    ClearMapFlags(0x1)
    OP_6D(132370, 8150, 95580, 0)
    OP_67(0, 8500, -10000, 0)
    OP_6B(3050, 0)
    OP_6C(146000, 0)
    OP_6E(302, 0)
    SetChrPos(0xF, 136000, 1000, 82200, 90)
    SetChrPos(0x10, 136000, 1000, 82200, 90)
    SetChrFlags(0xF, 0x4)
    ClearChrFlags(0xF, 0x40)
    SetChrFlags(0x10, 0x4)
    SetChrFlags(0x10, 0x40)
    OP_A1(0xF, 0xB)
    OP_A1(0x10, 0x9)
    OP_71(0x8, 0x4)
    OP_72(0x9, 0x4)
    OP_72(0xB, 0x4)
    SetChrPos(0x21, 132100, 8150, 96320, 185)
    SetChrPos(0x1F, 132680, 8150, 94880, 197)
    SetChrPos(0xC, 131790, 8150, 94810, 185)
    SetChrPos(0xB, 130490, 8150, 95130, 175)
    SetChrPos(0x20, 131360, 8150, 96150, 177)
    SetChrPos(0xE, 130240, 8150, 96640, 185)
    SetChrFlags(0x1A, 0x80)
    SetChrFlags(0x1B, 0x80)
    SetChrFlags(0x1C, 0x80)
    OP_71(0xA, 0x4)
    ClearChrFlags(0x21, 0x80)
    ClearChrFlags(0x1F, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0x20, 0x80)
    ClearChrFlags(0xE, 0x80)
    SetChrBattleFlags(0x21, 0x20)
    SetChrBattleFlags(0x1F, 0x20)
    SetChrBattleFlags(0xC, 0x20)
    SetChrBattleFlags(0xB, 0x20)
    SetChrBattleFlags(0x20, 0x20)
    SetChrBattleFlags(0xE, 0x20)
    OP_48()
    SetChrFlags(0x21, 0x40)
    SetChrFlags(0x1F, 0x40)
    SetChrFlags(0xC, 0x40)
    SetChrFlags(0xB, 0x40)
    SetChrFlags(0x20, 0x40)
    SetChrFlags(0xE, 0x40)
    SetChrPos(0x101, 132260, 8150, 97290, 184)
    SetChrPos(0xF7, 131250, 8150, 97380, 184)
    SetChrPos(0x104, 131250, 8150, 98500, 184)
    SetChrPos(0x105, 132310, 8150, 98400, 184)
    Sleep(2000)
    OP_22(0xE2, 0x0, 0x64)
    OP_22(0x75, 0x0, 0x64)
    Sleep(2000)
    OP_22(0xC8, 0x0, 0x64)
    Sleep(500)
    OP_22(0x76, 0x0, 0x64)
    OP_22(0x78, 0x0, 0x64)
    Sleep(2000)
    OP_6F(0xB, 1)
    OP_6F(0x7, 0)
    FadeToBright(1500, 0)
    OP_0D()
    OP_62(0x1F, 0x0, 1700, 0x8, 0x9, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)
    OP_43(0x1F, 0x1, 0x0, 0x15)
    OP_62(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_43(0xC, 0x1, 0x0, 0x16)
    Sleep(300)
    OP_43(0xB, 0x1, 0x0, 0x17)
    Sleep(500)
    OP_43(0x21, 0x1, 0x0, 0x17)
    Sleep(1300)
    OP_43(0x20, 0x1, 0x0, 0x17)
    Sleep(200)
    OP_43(0xE, 0x1, 0x0, 0x17)
    Sleep(2000)
    OP_6D(131700, 8150, 97100, 1000)

    ChrTalk(    #107
        0x101,
        (
            "#1006F#5P那么……\x01",
            "我们也上去吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0x105,
        "#542F#6P嗯，是啊……\x02",
    )

    CloseMessageWindow()

    def lambda_2540():
        OP_8E(0xFE, 0x204A4, 0x1FD6, 0x174B2, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2540)
    Sleep(50)

    def lambda_2560():
        OP_8E(0xFE, 0x200B2, 0x1FD6, 0x175AC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF7, 0, lambda_2560)
    Sleep(50)

    def lambda_2580():
        OP_8E(0xFE, 0x2049A, 0x1FD6, 0x17A52, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_2580)
    Sleep(50)

    def lambda_25A0():
        OP_8E(0xFE, 0x20030, 0x1FD6, 0x17B42, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_25A0)
    Sleep(300)
    SetChrPos(0x12, 122550, 6150, 101030, 90)

    NpcTalk(    #109
        0x12,
        "男孩子的声音",
        "#1P啊～找到了找到了！\x02",
    )

    WaitChrThread(0x101, 0x0)
    WaitChrThread(0xF7, 0x0)
    WaitChrThread(0x105, 0x0)
    WaitChrThread(0x104, 0x0)
    CloseMessageWindow()
    OP_20(0x3E8)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0xF7, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_2678():
        OP_8C(0xFE, 334, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2678)

    def lambda_2686():
        OP_8C(0xFE, 334, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_2686)
    Sleep(100)

    def lambda_2699():
        OP_8C(0xFE, 334, 400)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2699)

    def lambda_26A7():
        OP_8C(0xFE, 334, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_26A7)
    OP_21()
    OP_1D(0x58)
    Sleep(500)

    def lambda_26BD():
        OP_6D(124110, 8150, 100440, 2000)
        ExitThread()

    QueueWorkItem(0x12, 3, lambda_26BD)

    def lambda_26D5():
        OP_67(0, 8000, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x12, 3, lambda_26D5)
    SetChrPos(0x12, 122550, 6150, 101430, 90)
    SetChrPos(0x14, 121550, 6150, 101430, 90)
    SetChrPos(0x13, 120550, 6150, 101430, 90)
    SetChrPos(0x15, 119550, 6150, 101430, 90)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    SetChrFlags(0x12, 0x40)
    SetChrFlags(0x13, 0x40)
    SetChrFlags(0x14, 0x40)
    SetChrFlags(0x15, 0x40)
    OP_43(0x12, 0x1, 0x0, 0x18)
    Sleep(100)
    OP_43(0x14, 0x1, 0x0, 0x19)
    Sleep(50)
    OP_43(0x13, 0x1, 0x0, 0x1A)
    Sleep(100)
    OP_43(0x15, 0x1, 0x0, 0x1B)
    Sleep(3000)

    def lambda_2789():
        OP_6D(133070, 8150, 96500, 2000)
        ExitThread()

    QueueWorkItem(0x1, 2, lambda_2789)

    def lambda_27A1():
        OP_67(0, 8000, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x1, 3, lambda_27A1)

    def lambda_27B9():
        OP_8E(0xFE, 0x2060C, 0x1FD6, 0x17CE6, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_27B9)
    Sleep(100)

    def lambda_27D9():
        OP_8E(0xFE, 0x20666, 0x1FD6, 0x17854, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_27D9)
    Sleep(200)

    def lambda_27F9():
        OP_8E(0xFE, 0x201A2, 0x1FD6, 0x17854, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xF7, 0, lambda_27F9)
    Sleep(100)

    def lambda_2819():
        OP_8E(0xFE, 0x200A8, 0x1FD6, 0x17DD6, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_2819)
    WaitChrThread(0x101, 0x0)

    def lambda_2839():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2839)
    WaitChrThread(0x105, 0x0)

    def lambda_284C():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_284C)
    WaitChrThread(0xF7, 0x0)

    def lambda_285F():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_285F)
    WaitChrThread(0x104, 0x0)

    def lambda_2872():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2872)
    WaitChrThread(0x1, 0x2)
    WaitChrThread(0x1, 0x3)

    ChrTalk(    #110
        0x101,
        "#1004F#2P你、你们！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0x105,
        "#044F大家，怎么了……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0x13,
        "#5P来送你们了～\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0x12,
        (
            "#772F#5P真是的，你们俩\x01",
            "也太薄情啦。\x02\x03",

            "居然瞒着我们\x01",
            "就出发了～！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0x14,
        "#5P真是，生气了哦！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0x15,
        (
            "#6P科洛丝姐姐。\x01",
            "真的要走吗～？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x15, 400)

    ChrTalk(    #116
        0x105,
        (
            "#542F#5P嗯……对不起。\x02\x03",

            "本来想打个招呼的，\x01",
            "但听说你们不在家……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0x101,
        (
            "#1016F#2P原来都跑到卢安来了啊。\x02\x03",

            "#1004F啊，那么\x01",
            "难道特蕾莎院长也……\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0x18, 0x40)
    SetChrFlags(0x16, 0x40)
    SetChrFlags(0x17, 0x40)
    SetChrFlags(0x19, 0x40)
    SetChrPos(0x18, 125500, 6400, 101150, 90)
    ClearChrFlags(0x18, 0x80)
    SetChrPos(0x16, 125500, 6400, 101150, 90)
    ClearChrFlags(0x16, 0x80)
    SetChrPos(0x17, 125500, 6400, 101150, 90)
    ClearChrFlags(0x17, 0x80)
    SetChrPos(0x19, 125500, 6400, 101150, 90)
    ClearChrFlags(0x19, 0x80)

    NpcTalk(    #118
        0x18,
        "女性的声音",
        (
            "#5P呜呼呼。\x01",
            "看来赶上了呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_43(0x18, 0x3, 0x0, 0x25)
    OP_43(0x18, 0x1, 0x0, 0x1C)
    Sleep(500)
    OP_43(0x16, 0x1, 0x0, 0x1D)

    def lambda_2AD0():

        label("loc_2AD0")

        TurnDirection(0xFE, 0x18, 400)
        OP_48()
        Jump("loc_2AD0")

    QueueWorkItem2(0x101, 1, lambda_2AD0)

    def lambda_2AE1():

        label("loc_2AE1")

        TurnDirection(0xFE, 0x18, 400)
        OP_48()
        Jump("loc_2AE1")

    QueueWorkItem2(0xF7, 1, lambda_2AE1)
    OP_43(0x104, 0x0, 0x0, 0x27)
    OP_43(0x105, 0x0, 0x0, 0x26)
    Sleep(500)

    def lambda_2B05():
        OP_6D(133670, 8150, 96500, 2000)
        ExitThread()

    QueueWorkItem(0x1, 2, lambda_2B05)

    def lambda_2B1D():
        OP_67(0, 8000, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x1, 3, lambda_2B1D)
    OP_43(0x17, 0x1, 0x0, 0x1E)
    OP_43(0x19, 0x1, 0x0, 0x1F)
    WaitChrThread(0x18, 0x1)

    ChrTalk(    #119
        0x101,
        (
            "#1008F#2P院长老师！\x01",
            "还有乔儿你们……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0x16,
        (
            "#641F#5P啊哈哈！\x01",
            "感觉真是刚刚好啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0x17,
        (
            "#734F哈，突然想\x01",
            "给你们个惊喜，\x01",
            "于是就这样了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0x16,
        "#648F#5P嗯，结果是万事大吉啦。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0x18,
        (
            "#751F#5P其实是乔儿他们\x01",
            "告诉我\x01",
            "你们要出发的。\x02\x03",

            "所以，机会难得\x01",
            "就大家一起来送行了。\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x19, 0x1)
    OP_44(0x101, 0x1)
    OP_44(0xF7, 0x1)
    OP_44(0x104, 0x1)
    OP_44(0x105, 0x1)

    ChrTalk(    #124
        0x19,
        (
            "#781F#5P呵呵，既然顺路\x01",
            "我也陪着来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0x105,
        "#542F#6P是这样啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0x12,
        (
            "#775F#5P……对了，艾丝蒂尔姐姐。\x02\x03",

            "约修亚哥哥……\x01",
            "离家出走了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0x101,
        "#1026F#2P啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0x14,
        (
            "#5P我们听老师\x01",
            "说了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0x101,
        (
            "#1007F#2P是吗……\x02\x03",

            "#1003F抱歉哦，瞒着大家。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0x14,
        "#5P不，没关系的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0x14,
        (
            "#5P那个，我们\x01",
            "会每天向女神祈祷的！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0x14,
        (
            "#5P希望约修亚哥哥\x01",
            "能早日回来！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0x15,
        "#6P我也会祈祷的～！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0x13,
        "#5P一定会实现的～\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0x101,
        "#1025F#2P大家……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0x105,
        "#048F#6P呵呵，谢谢你们。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0x16,
        (
            "#644F#5P还有我们\x01",
            "也会向女神祈祷的。\x02\x03",

            "#648F艾丝蒂尔、科洛丝。\x01",
            "你们也要多加小心哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0x17,
        (
            "#730F你们虽然要加油，\x01",
            "但可别太勉强而招致危险哦。\x02\x03",

            "如果发生危险，那家伙\x01",
            "绝对无法原谅自己的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0x105,
        "#542F#6P乔儿、汉斯……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0x101,
        (
            "#1017F#2P嗯……\x01",
            "我会铭记于心的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0x18,
        (
            "#750F#5P艾丝蒂尔，科洛丝\x01",
            "就请你们多多关照了。\x02\x03",

            "虽然看起来坚强，\x01",
            "其实她也是有脆弱一面的女孩子……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x105, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    ChrTalk(    #142
        0x105,
        "#540F#6P老，老师……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0x101,
        (
            "#1008F#2P嘿嘿，交给我吧。\x02\x03",

            "#1016F话虽这么说，其实是她经常\x01",
            "帮助我才对。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0x18,
        (
            "#751F#5P呵呵……\x02\x03",

            "#750F科洛丝，要趁此机会\x01",
            "好好看清楚自己。\x02\x03",

            "自己应该做什么\x01",
            "慢慢找到答案就行了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0x105,
        "#048F#6P是……我明白了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #146
        0x19,
        (
            "#783F#5P游击士和学生……\x01",
            "两者都有自己的目标。\x02\x03",

            "#780F两人应该都在之前的日子里\x01",
            "充分成长了。\x02\x03",

            "不要过于相信自己的力量，\x01",
            "能运用自如就好。\x02\x03",

            "#781F这样的话就一定\x01",
            "能渡过重重难关。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0x101,
        "#1006F#2P#1K是！\x02",
    )


    ChrTalk(    #148
        0x105,
        "#041F#6P#1K是！\x02",
    )

    OP_56(0x1)
    OP_59()
    Sleep(500)
    OP_22(0xA6, 0x0, 0x64)
    Sleep(500)
    SetChrName("女性的声音")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #149
        (
            "\x07\x05前往蔡斯方向的定期船，\x01",
            "『赛希莉亚号』即将升空。\x02\x03",

            "需要乘坐的旅客请立即登船。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)

    ChrTalk(    #150
        0x101,
        "#1004F#2P啊，不好……！\x02",
    )

    CloseMessageWindow()
    Sleep(200)

    def lambda_31F0():

        label("loc_31F0")

        TurnDirection(0xFE, 0x101, 400)
        OP_48()
        Jump("loc_31F0")

    QueueWorkItem2(0x12, 1, lambda_31F0)

    def lambda_3201():

        label("loc_3201")

        TurnDirection(0xFE, 0x101, 400)
        OP_48()
        Jump("loc_3201")

    QueueWorkItem2(0x14, 1, lambda_3201)
    Sleep(100)

    def lambda_3217():

        label("loc_3217")

        TurnDirection(0xFE, 0x101, 400)
        OP_48()
        Jump("loc_3217")

    QueueWorkItem2(0x13, 1, lambda_3217)

    def lambda_3228():

        label("loc_3228")

        TurnDirection(0xFE, 0x101, 400)
        OP_48()
        Jump("loc_3228")

    QueueWorkItem2(0x15, 1, lambda_3228)
    Sleep(100)

    def lambda_323E():

        label("loc_323E")

        TurnDirection(0xFE, 0x101, 400)
        OP_48()
        Jump("loc_323E")

    QueueWorkItem2(0x18, 1, lambda_323E)

    def lambda_324F():

        label("loc_324F")

        TurnDirection(0xFE, 0x101, 400)
        OP_48()
        Jump("loc_324F")

    QueueWorkItem2(0x16, 1, lambda_324F)

    def lambda_3260():

        label("loc_3260")

        TurnDirection(0xFE, 0x101, 400)
        OP_48()
        Jump("loc_3260")

    QueueWorkItem2(0x17, 1, lambda_3260)

    def lambda_3271():

        label("loc_3271")

        TurnDirection(0xFE, 0x101, 400)
        OP_48()
        Jump("loc_3271")

    QueueWorkItem2(0x19, 1, lambda_3271)
    OP_43(0x101, 0x1, 0x0, 0x20)
    Sleep(800)
    OP_43(0xF7, 0x1, 0x0, 0x20)
    Sleep(300)
    OP_43(0x105, 0x1, 0x0, 0x20)
    Sleep(500)
    OP_43(0x104, 0x1, 0x0, 0x20)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_44(0x101, 0x1)
    OP_44(0xF7, 0x1)
    OP_44(0x105, 0x1)
    OP_44(0x104, 0x1)
    OP_44(0x12, 0x1)
    OP_44(0x14, 0x1)
    OP_44(0x13, 0x1)
    OP_44(0x15, 0x1)
    OP_44(0x18, 0x1)
    OP_44(0x16, 0x1)
    OP_44(0x17, 0x1)
    OP_44(0x19, 0x1)
    SetChrPos(0x12, 133000, 8090, 94500, 180)
    SetChrPos(0x14, 132610, 8090, 95000, 180)
    SetChrPos(0x13, 131710, 8090, 94500, 180)
    SetChrPos(0x15, 131100, 8090, 94800, 180)
    SetChrPos(0x18, 133310, 8090, 95600, 180)
    SetChrPos(0x16, 132610, 8090, 96200, 180)
    SetChrPos(0x17, 131610, 8090, 96200, 180)
    SetChrPos(0x19, 132300, 8150, 97250, 180)
    SetChrFlags(0x0, 0x20)
    SetChrFlags(0x1, 0x20)
    SetChrFlags(0x2, 0x20)
    SetChrFlags(0x3, 0x20)
    OP_48()
    SetChrPos(0xF7, 133390, 8200, 84310, 0)
    SetChrPos(0x101, 132420, 8200, 84780, 0)
    SetChrPos(0x105, 131400, 8200, 84690, 0)
    SetChrPos(0x104, 132250, 8200, 83530, 0)
    SetChrSubChip(0xF7, 0)
    SetChrSubChip(0x101, 0)
    SetChrSubChip(0x105, 0)
    SetChrSubChip(0x104, 0)
    OP_6D(132310, 8090, 90270, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(3690, 0)
    OP_6C(33000, 0)
    OP_6E(262, 0)
    Sleep(500)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #151
        0x101,
        "#1018F#2P那么，再见了！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #152
        0x105,
        "#048F#5P大家……多保重。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0x12,
        "#771F#7P姐姐你们也多保重啊！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #154
        0x16,
        (
            "#641F#6P期待你们的旅行见闻\x01",
            "和约修亚哟！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(1000)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0xF7, 0x80)
    SetChrFlags(0x105, 0x80)
    SetChrFlags(0x104, 0x80)
    ClearMapFlags(0x10)
    OP_6D(132160, 8200, 85340, 0)
    OP_67(0, 11210, -10000, 0)
    OP_6B(4730, 0)
    OP_6C(45000, 0)
    OP_6E(302, 0)
    OP_0D()
    OP_22(0xE2, 0x0, 0x64)
    OP_22(0x78, 0x0, 0x64)
    OP_6F(0x7, 0)
    OP_70(0x7, 0x64)
    OP_73(0x7)
    OP_22(0x76, 0x0, 0x64)
    OP_6F(0xB, 1)
    OP_70(0xB, 0x3C)
    OP_73(0xB)
    Sleep(500)
    SetChrFlags(0x0, 0x20)
    SetChrFlags(0x1, 0x20)
    SetChrFlags(0x2, 0x20)
    SetChrFlags(0x3, 0x20)
    OP_23(0x75)
    OP_22(0x77, 0x0, 0x64)
    OP_43(0xF, 0x2, 0x0, 0x13)

    def lambda_3572():
        OP_6D(160160, 8200, 85340, 12000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_3572)

    def lambda_358A():

        label("loc_358A")

        TurnDirection(0xFE, 0x13, 400)
        OP_48()
        Jump("loc_358A")

    QueueWorkItem2(0x101, 2, lambda_358A)

    def lambda_359B():

        label("loc_359B")

        TurnDirection(0xFE, 0x12, 400)
        OP_48()
        Jump("loc_359B")

    QueueWorkItem2(0xF7, 2, lambda_359B)

    def lambda_35AC():

        label("loc_35AC")

        TurnDirection(0xFE, 0x14, 400)
        OP_48()
        Jump("loc_35AC")

    QueueWorkItem2(0x105, 2, lambda_35AC)

    def lambda_35BD():

        label("loc_35BD")

        TurnDirection(0xFE, 0x15, 400)
        OP_48()
        Jump("loc_35BD")

    QueueWorkItem2(0x104, 2, lambda_35BD)

    def lambda_35CE():

        label("loc_35CE")

        TurnDirection(0xFE, 0x101, 400)
        OP_48()
        Jump("loc_35CE")

    QueueWorkItem2(0x13, 2, lambda_35CE)

    def lambda_35DF():

        label("loc_35DF")

        TurnDirection(0xFE, 0xF7, 400)
        OP_48()
        Jump("loc_35DF")

    QueueWorkItem2(0x12, 2, lambda_35DF)

    def lambda_35F0():

        label("loc_35F0")

        TurnDirection(0xFE, 0x105, 400)
        OP_48()
        Jump("loc_35F0")

    QueueWorkItem2(0x14, 2, lambda_35F0)

    def lambda_3601():

        label("loc_3601")

        TurnDirection(0xFE, 0x104, 400)
        OP_48()
        Jump("loc_3601")

    QueueWorkItem2(0x15, 2, lambda_3601)

    def lambda_3612():

        label("loc_3612")

        TurnDirection(0xFE, 0x101, 400)
        OP_48()
        Jump("loc_3612")

    QueueWorkItem2(0x16, 2, lambda_3612)

    def lambda_3623():

        label("loc_3623")

        TurnDirection(0xFE, 0xF7, 400)
        OP_48()
        Jump("loc_3623")

    QueueWorkItem2(0x18, 2, lambda_3623)

    def lambda_3634():

        label("loc_3634")

        TurnDirection(0xFE, 0x105, 400)
        OP_48()
        Jump("loc_3634")

    QueueWorkItem2(0x17, 2, lambda_3634)

    def lambda_3645():

        label("loc_3645")

        TurnDirection(0xFE, 0x104, 400)
        OP_48()
        Jump("loc_3645")

    QueueWorkItem2(0x19, 2, lambda_3645)

    def lambda_3656():
        OP_8F(0xFE, 0x27100, 0xDDE, 0x14050, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_3656)

    def lambda_3671():
        OP_8F(0xFE, 0x27100, 0x4B0, 0x14050, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_3671)

    def lambda_368C():
        OP_91(0xFE, 0x5DC0, 0xA5A, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_368C)

    def lambda_36A7():
        OP_91(0xFE, 0x5DC0, 0xA5A, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_36A7)

    def lambda_36C2():
        OP_91(0xFE, 0x5DC0, 0xA5A, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_36C2)

    def lambda_36DD():
        OP_91(0xFE, 0x5DC0, 0xA5A, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_36DD)
    Sleep(600)

    def lambda_36FD():
        OP_8F(0xFE, 0x27100, 0x11C6, 0x14050, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_36FD)

    def lambda_3718():
        OP_8F(0xFE, 0x27100, 0x4B0, 0x14050, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_3718)

    def lambda_3733():
        OP_91(0xFE, 0x5DC0, 0xA5A, 0x0, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_3733)

    def lambda_374E():
        OP_91(0xFE, 0x5DC0, 0xA5A, 0x0, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_374E)

    def lambda_3769():
        OP_91(0xFE, 0x5DC0, 0xA5A, 0x0, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_3769)

    def lambda_3784():
        OP_91(0xFE, 0x5DC0, 0xA5A, 0x0, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_3784)
    Sleep(700)

    def lambda_37A4():
        OP_8F(0xFE, 0x27100, 0x15AE, 0x14050, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_37A4)

    def lambda_37BF():
        OP_8F(0xFE, 0x27100, 0x4B0, 0x14050, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_37BF)

    def lambda_37DA():
        OP_91(0xFE, 0x5DC0, 0xA5A, 0x0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_37DA)

    def lambda_37F5():
        OP_91(0xFE, 0x5DC0, 0xA5A, 0x0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_37F5)

    def lambda_3810():
        OP_91(0xFE, 0x5DC0, 0xA5A, 0x0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_3810)

    def lambda_382B():
        OP_91(0xFE, 0x5DC0, 0xA5A, 0x0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_382B)
    Sleep(800)
    OP_43(0x12, 0x0, 0x0, 0x21)
    OP_43(0x14, 0x0, 0x0, 0x22)
    OP_43(0x13, 0x0, 0x0, 0x23)
    OP_43(0x15, 0x0, 0x0, 0x24)

    def lambda_3867():
        OP_8F(0xFE, 0x27100, 0x1996, 0x14050, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_3867)

    def lambda_3882():
        OP_8F(0xFE, 0x27100, 0x4B0, 0x14050, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_3882)

    def lambda_389D():
        OP_91(0xFE, 0x5DC0, 0xA5A, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_389D)

    def lambda_38B8():
        OP_91(0xFE, 0x5DC0, 0xA5A, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_38B8)

    def lambda_38D3():
        OP_91(0xFE, 0x5DC0, 0xA5A, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_38D3)

    def lambda_38EE():
        OP_91(0xFE, 0x5DC0, 0xA5A, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_38EE)
    Sleep(900)

    def lambda_390E():
        OP_8F(0xFE, 0x27100, 0x1D7E, 0x14050, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_390E)

    def lambda_3929():
        OP_8F(0xFE, 0x27100, 0x4B0, 0x14050, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_3929)

    def lambda_3944():
        OP_91(0xFE, 0x5DC0, 0xA5A, 0x0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_3944)

    def lambda_395F():
        OP_91(0xFE, 0x5DC0, 0xA5A, 0x0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_395F)

    def lambda_397A():
        OP_91(0xFE, 0x5DC0, 0xA5A, 0x0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_397A)

    def lambda_3995():
        OP_91(0xFE, 0x5DC0, 0xA5A, 0x0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_3995)
    Sleep(1500)

    def lambda_39B5():
        OP_8F(0xFE, 0x27100, 0x2166, 0x14050, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_39B5)

    def lambda_39D0():
        OP_8F(0xFE, 0x27100, 0x4B0, 0x14050, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_39D0)

    def lambda_39EB():
        OP_91(0xFE, 0x5DC0, 0xA5A, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_39EB)

    def lambda_3A06():
        OP_91(0xFE, 0x5DC0, 0xA5A, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_3A06)

    def lambda_3A21():
        OP_91(0xFE, 0x5DC0, 0xA5A, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_3A21)

    def lambda_3A3C():
        OP_91(0xFE, 0x5DC0, 0xA5A, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_3A3C)
    Sleep(1500)
    OP_20(0xFA0)
    FadeToDark(2000, 0, -1)
    Sleep(1000)
    OP_43(0xF, 0x3, 0x0, 0x14)

    def lambda_3A77():
        OP_8F(0xFE, 0x27100, 0x254E, 0x14050, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_3A77)

    def lambda_3A92():
        OP_8F(0xFE, 0x27100, 0x4B0, 0x14050, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_3A92)

    def lambda_3AAD():
        OP_91(0xFE, 0x5DC0, 0xA5A, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_3AAD)

    def lambda_3AC8():
        OP_91(0xFE, 0x5DC0, 0xA5A, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_3AC8)

    def lambda_3AE3():
        OP_91(0xFE, 0x5DC0, 0xA5A, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_3AE3)

    def lambda_3AFE():
        OP_91(0xFE, 0x5DC0, 0xA5A, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_3AFE)
    OP_0D()
    ClearChrFlags(0x0, 0x4)
    ClearChrFlags(0x1, 0x4)
    ClearChrFlags(0x2, 0x4)
    ClearChrFlags(0x3, 0x4)
    ClearChrFlags(0x0, 0x20)
    ClearChrFlags(0x1, 0x20)
    ClearChrFlags(0x2, 0x20)
    ClearChrFlags(0x3, 0x20)
    RemoveParty(0x5, 0xFF)
    RemoveParty(0x2, 0xFF)
    RemoveParty(0x4, 0xFF)
    RemoveParty(0x3, 0xFF)
    OP_A2(0x1403)
    OP_A2(0x10F1)
    OP_28(0x65, 0x4, 0x40)
    OP_28(0x66, 0x4, 0x40)
    OP_28(0x67, 0x4, 0x40)
    OP_28(0x68, 0x4, 0x40)
    OP_28(0x69, 0x4, 0x40)
    OP_28(0x6B, 0x4, 0x40)
    OP_28(0xA1, 0x4, 0x40)
    OP_28(0xA2, 0x4, 0x40)
    OP_28(0xA3, 0x4, 0x40)
    OP_28(0xA4, 0x4, 0x40)
    OP_21()
    Sleep(1000)
    NewScene("ED6_DT21/E0001   ._SN", 104, 0, 0)
    IdleLoop()
    Return()

    # Function_18_227F end

    def Function_19_3B90(): pass

    label("Function_19_3B90")

    OP_B0(0xB, 0x32)
    OP_6F(0xB, 61)
    OP_70(0xB, 0xA0)
    OP_73(0xB)
    OP_71(0xB, 0x20)
    OP_6F(0xB, 161)
    OP_70(0xB, 0x104)
    Return()

    # Function_19_3B90 end

    def Function_20_3BB9(): pass

    label("Function_20_3BB9")

    OP_24(0x77, 0x5A)
    Sleep(300)
    OP_24(0x77, 0x50)
    Sleep(300)
    OP_24(0x77, 0x46)
    Sleep(300)
    OP_24(0x77, 0x3C)
    Sleep(300)
    OP_24(0x77, 0x32)
    Sleep(300)
    OP_24(0x77, 0x28)
    Sleep(300)
    OP_24(0x77, 0x1E)
    Sleep(300)
    OP_23(0x77)
    Return()

    # Function_20_3BB9 end

    def Function_21_3BFC(): pass

    label("Function_21_3BFC")

    OP_8E(0xFE, 0x20350, 0x206C, 0x16E7C, 0x1770, 0x0)
    OP_8E(0xFE, 0x2035A, 0x1FD6, 0x13FCE, 0x1770, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_21_3BFC end

    def Function_22_3C2A(): pass

    label("Function_22_3C2A")

    OP_62(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_8E(0xFE, 0x20350, 0x206C, 0x16E7C, 0xFA0, 0x0)
    OP_8E(0xFE, 0x2035A, 0x1FD6, 0x13FCE, 0xFA0, 0x0)
    SetChrFlags(0xFE, 0x80)
    OP_63(0xFE)
    Return()

    # Function_22_3C2A end

    def Function_23_3C6D(): pass

    label("Function_23_3C6D")

    OP_8E(0xFE, 0x20350, 0x206C, 0x16E7C, 0x7D0, 0x0)
    OP_8E(0xFE, 0x2035A, 0x1FD6, 0x13FCE, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_23_3C6D end

    def Function_24_3C9B(): pass

    label("Function_24_3C9B")

    OP_8E(0xFE, 0x20EB8, 0x1FD6, 0x1895C, 0xFA0, 0x0)
    OP_8E(0xFE, 0x20E4A, 0x1FD6, 0x18042, 0xFA0, 0x0)
    OP_8E(0xFE, 0x20A62, 0x1FD6, 0x173AE, 0xFA0, 0x0)
    TurnDirection(0xFE, 0x101, 400)
    Return()

    # Function_24_3C9B end

    def Function_25_3CDF(): pass

    label("Function_25_3CDF")

    OP_8E(0xFE, 0x20EB8, 0x1FD6, 0x1895C, 0xFA0, 0x0)
    OP_8E(0xFE, 0x20FC6, 0x1FD6, 0x18240, 0xFA0, 0x0)
    OP_8E(0xFE, 0x20AF8, 0x1FD6, 0x1776E, 0xFA0, 0x0)
    OP_8C(0xFE, 270, 400)
    Return()

    # Function_25_3CDF end

    def Function_26_3D23(): pass

    label("Function_26_3D23")

    OP_8E(0xFE, 0x20EB8, 0x1FD6, 0x1895C, 0xFA0, 0x0)
    OP_8E(0xFE, 0x20EEA, 0x1FD6, 0x1825E, 0xFA0, 0x0)
    OP_8E(0xFE, 0x209CC, 0x1FD6, 0x17B88, 0xFA0, 0x0)
    OP_8C(0xFE, 270, 400)
    Return()

    # Function_26_3D23 end

    def Function_27_3D67(): pass

    label("Function_27_3D67")

    OP_8E(0xFE, 0x20EB8, 0x1FD6, 0x1895C, 0xFA0, 0x0)
    OP_8E(0xFE, 0x20F44, 0x1FD6, 0x18222, 0xFA0, 0x0)
    OP_8E(0xFE, 0x207BA, 0x1FD6, 0x17F84, 0xFA0, 0x0)
    TurnDirection(0xFE, 0x105, 400)
    Return()

    # Function_27_3D67 end

    def Function_28_3DAB(): pass

    label("Function_28_3DAB")

    OP_8E(0xFE, 0x1F8E2, 0x1806, 0x18C04, 0xBB8, 0x0)
    OP_8E(0xFE, 0x20EB8, 0x1FD6, 0x1895C, 0xBB8, 0x0)
    OP_8E(0xFE, 0x20E36, 0x1FD6, 0x178EA, 0xBB8, 0x0)
    TurnDirection(0xFE, 0x101, 400)
    Return()

    # Function_28_3DAB end

    def Function_29_3DEF(): pass

    label("Function_29_3DEF")

    OP_8E(0xFE, 0x1F8E2, 0x1806, 0x18C04, 0xBB8, 0x0)
    OP_8E(0xFE, 0x20EB8, 0x1FD6, 0x1895C, 0xBB8, 0x0)
    OP_8E(0xFE, 0x20D32, 0x1FD6, 0x17D36, 0xBB8, 0x0)
    OP_8C(0xFE, 270, 400)
    Return()

    # Function_29_3DEF end

    def Function_30_3E33(): pass

    label("Function_30_3E33")

    OP_8E(0xFE, 0x1F8E2, 0x1806, 0x18C04, 0xBB8, 0x0)
    OP_8E(0xFE, 0x20EB8, 0x1FD6, 0x1895C, 0xBB8, 0x0)
    OP_8E(0xFE, 0x210FC, 0x1FD6, 0x17BE2, 0xBB8, 0x0)
    OP_8C(0xFE, 270, 400)
    Return()

    # Function_30_3E33 end

    def Function_31_3E77(): pass

    label("Function_31_3E77")

    OP_8E(0xFE, 0x1F8E2, 0x1806, 0x18C04, 0x7D0, 0x0)
    OP_8E(0xFE, 0x20EB8, 0x1FD6, 0x1895C, 0x7D0, 0x0)
    OP_8E(0xFE, 0x20FE4, 0x1FD6, 0x1809C, 0x7D0, 0x0)
    OP_8C(0xFE, 270, 400)
    Return()

    # Function_31_3E77 end

    def Function_32_3EBB(): pass

    label("Function_32_3EBB")

    OP_8C(0xFE, 180, 400)
    OP_8E(0xFE, 0x20378, 0x1FD6, 0x170F2, 0x7D0, 0x0)
    OP_8E(0xFE, 0x20422, 0x1F9A, 0x154B4, 0x7D0, 0x0)
    Return()

    # Function_32_3EBB end

    def Function_33_3EEB(): pass

    label("Function_33_3EEB")

    OP_44(0xFE, 0x2)
    OP_8C(0xFE, 90, 600)
    OP_8E(0xFE, 0x224D4, 0x1FD6, 0x16F30, 0xFA0, 0x0)
    OP_8C(0xFE, 185, 400)

    def lambda_3F17():

        label("loc_3F17")

        TurnDirection(0xFE, 0xF7, 400)
        OP_48()
        Jump("loc_3F17")

    QueueWorkItem2(0x12, 2, lambda_3F17)
    Return()

    # Function_33_3EEB end

    def Function_34_3F23(): pass

    label("Function_34_3F23")

    Sleep(300)
    OP_44(0xFE, 0x2)
    OP_8C(0xFE, 90, 600)
    OP_8E(0xFE, 0x222E0, 0x1FD6, 0x171CE, 0xFA0, 0x0)
    OP_8C(0xFE, 185, 400)

    def lambda_3F54():

        label("loc_3F54")

        TurnDirection(0xFE, 0x105, 400)
        OP_48()
        Jump("loc_3F54")

    QueueWorkItem2(0x14, 2, lambda_3F54)
    Return()

    # Function_34_3F23 end

    def Function_35_3F60(): pass

    label("Function_35_3F60")

    Sleep(500)
    OP_44(0xFE, 0x2)
    OP_8C(0xFE, 90, 600)
    OP_8E(0xFE, 0x21E9E, 0x1FD6, 0x16FC6, 0xFA0, 0x0)
    OP_8C(0xFE, 185, 400)

    def lambda_3F91():

        label("loc_3F91")

        TurnDirection(0xFE, 0x101, 400)
        OP_48()
        Jump("loc_3F91")

    QueueWorkItem2(0x13, 2, lambda_3F91)
    Return()

    # Function_35_3F60 end

    def Function_36_3F9D(): pass

    label("Function_36_3F9D")

    Sleep(800)
    OP_44(0xFE, 0x2)
    OP_8C(0xFE, 90, 600)
    OP_8E(0xFE, 0x21C46, 0x1FD6, 0x1721E, 0xFA0, 0x0)
    OP_8C(0xFE, 185, 400)

    def lambda_3FCE():

        label("loc_3FCE")

        TurnDirection(0xFE, 0x104, 400)
        OP_48()
        Jump("loc_3FCE")

    QueueWorkItem2(0x15, 2, lambda_3FCE)
    Return()

    # Function_36_3F9D end

    def Function_37_3FDA(): pass

    label("Function_37_3FDA")

    OP_8C(0x101, 354, 400)
    Sleep(500)
    OP_8C(0xF7, 354, 400)
    Sleep(500)
    OP_8C(0x104, 354, 400)
    Return()

    # Function_37_3FDA end

    def Function_38_3FFA(): pass

    label("Function_38_3FFA")

    OP_8C(0xFE, 315, 400)

    def lambda_4007():

        label("loc_4007")

        TurnDirection(0xFE, 0x18, 400)
        OP_48()
        Jump("loc_4007")

    QueueWorkItem2(0x105, 1, lambda_4007)
    Return()

    # Function_38_3FFA end

    def Function_39_4013(): pass

    label("Function_39_4013")

    OP_8C(0xFE, 315, 400)
    Sleep(500)
    OP_8C(0xFE, 0, 400)
    Sleep(500)

    def lambda_4031():

        label("loc_4031")

        TurnDirection(0xFE, 0x18, 400)
        OP_48()
        Jump("loc_4031")

    QueueWorkItem2(0x104, 1, lambda_4031)
    Return()

    # Function_39_4013 end

    def Function_40_403D(): pass

    label("Function_40_403D")

    FadeToDark(0, 0, -1)
    OP_A3(0x1200)
    OP_A3(0x1201)
    RemoveParty(0x2, 0xFF)
    RemoveParty(0x5, 0xFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【◇选择雪拉扎德为队友】\x01",      # 0
            "【◇选择阿加特为队友】\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_40B7"),
        (1, "loc_40BD"),
        (SWITCH_DEFAULT, "loc_40C3"),
    )


    label("loc_40B7")

    OP_A2(0x1200)
    Jump("loc_40C3")

    label("loc_40BD")

    OP_A2(0x1201)
    Jump("loc_40C3")

    label("loc_40C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_40D1")
    AddParty(0x2, 0xF7, 0xFF)
    Jump("loc_40D5")

    label("loc_40D1")

    AddParty(0x5, 0xF7, 0xFF)

    label("loc_40D5")

    Return()

    # Function_40_403D end

    def Function_41_40D6(): pass

    label("Function_41_40D6")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_413D")

    AnonymousTalk(    #155
        (
            "\x07\x05定期船起降坪\x01",
            "※所有航班暂时停开。\x01",
            "　　　　　　　　　飞船坪接待处\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Jump("loc_416F")

    label("loc_413D")


    AnonymousTalk(    #156
        (
            "\x07\x05定期船起降坪\x01",
            "≡　开往柏斯市\x01",
            "≡　前往蔡斯市\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_416F")

    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_41_40D6 end

    def Function_42_4185(): pass

    label("Function_42_4185")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #157
        (
            "\x07\x05※请勿携带易燃物和危险品\x01",
            "　　　　『利贝尔飞船公社』\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_42_4185 end

    def Function_43_41EB(): pass

    label("Function_43_41EB")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #158
        (
            "\x07\x05　　　飞船坪塔台　　　　\x01",
            "　※无关人员禁止入内　　\x01",
            "   『利贝尔飞船公社』　\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_43_41EB end

    SaveToFile()

Try(main)
