from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 卢安

    CreateScenaFile(
        FileName            = 'T2511   ._SN',
        MapName             = 'Ruan',
        Location            = 'T2511.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60014",
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
        '乔儿',                                 # 9
        '汉斯',                                 # 10
        '雷欧',                                 # 11
        '露西',                                 # 12
        '莫妮卡',                               # 13
        '克拉拉',                               # 14
        '雷克特',                               # 15
        '德波拉',                               # 16
        '碧欧拉老师',                           # 17
        '珐奥娜',                               # 18
        '巴克斯',                               # 19
        '罗伊斯',                               # 20
        '巴托姆',                               # 21
        '弗雷',                                 # 22
        '利戈尔',                               # 23
        '罗迪',                                 # 24
        '看板',                                 # 25
        '目标用照相机',                         # 26
        '',                                     # 27
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
        Unknown_24              = 2500,
        Unknown_28              = 2800,
        Unknown_2C              = 262,
        Unknown_30              = 45,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 1,
        Unknown_3A              = 1,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT07/CH01130 ._CH',             # 00
        'ED6_DT07/CH01080 ._CH',             # 01
        'ED6_DT07/CH02390 ._CH',             # 02
        'ED6_DT07/CH02550 ._CH',             # 03
        'ED6_DT07/CH01210 ._CH',             # 04
        'ED6_DT07/CH01580 ._CH',             # 05
        'ED6_DT07/CH01360 ._CH',             # 06
        'ED6_DT07/CH01093 ._CH',             # 07
        'ED6_DT07/CH02680 ._CH',             # 08
        'ED6_DT07/CH02690 ._CH',             # 09
        'ED6_DT07/CH01370 ._CH',             # 0A
        'ED6_DT07/CH01090 ._CH',             # 0B
        'ED6_DT07/CH02670 ._CH',             # 0C
        'ED6_DT07/CH01213 ._CH',             # 0D
        'ED6_DT07/CH02490 ._CH',             # 0E
        'ED6_DT07/CH01020 ._CH',             # 0F
        'ED6_DT07/CH01093 ._CH',             # 10
        'ED6_DT07/CH01373 ._CH',             # 11
        'ED6_DT07/CH01590 ._CH',             # 12
        'ED6_DT07/CH02910 ._CH',             # 13
        'ED6_DT26/CH20777 ._CH',             # 14
        'ED6_DT07/CH02393 ._CH',             # 15
        'ED6_DT07/CH02553 ._CH',             # 16
        'ED6_DT07/CH00043 ._CH',             # 17
        'ED6_DT26/CH20779 ._CH',             # 18
        'ED6_DT26/CH20780 ._CH',             # 19
        'ED6_DT26/CH20778 ._CH',             # 1A
    )

    AddCharChipPat(
        'ED6_DT07/CH01130P._CP',             # 00
        'ED6_DT07/CH01080P._CP',             # 01
        'ED6_DT07/CH02390P._CP',             # 02
        'ED6_DT07/CH02550P._CP',             # 03
        'ED6_DT07/CH01210P._CP',             # 04
        'ED6_DT07/CH01580P._CP',             # 05
        'ED6_DT07/CH01360P._CP',             # 06
        'ED6_DT07/CH01093P._CP',             # 07
        'ED6_DT07/CH02680P._CP',             # 08
        'ED6_DT07/CH02690P._CP',             # 09
        'ED6_DT07/CH01370P._CP',             # 0A
        'ED6_DT07/CH01090P._CP',             # 0B
        'ED6_DT07/CH02670P._CP',             # 0C
        'ED6_DT07/CH01213P._CP',             # 0D
        'ED6_DT07/CH02490P._CP',             # 0E
        'ED6_DT07/CH01020P._CP',             # 0F
        'ED6_DT07/CH01093P._CP',             # 10
        'ED6_DT07/CH01373P._CP',             # 11
        'ED6_DT07/CH01590P._CP',             # 12
        'ED6_DT07/CH02910P._CP',             # 13
        'ED6_DT26/CH20777P._CP',             # 14
        'ED6_DT07/CH02393P._CP',             # 15
        'ED6_DT07/CH02553P._CP',             # 16
        'ED6_DT07/CH00043P._CP',             # 17
        'ED6_DT26/CH20779P._CP',             # 18
        'ED6_DT26/CH20780P._CP',             # 19
        'ED6_DT26/CH20778P._CP',             # 1A
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
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
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 15,
    )

    DeclNpc(
        X                   = 28640,
        Z                   = 0,
        Y                   = 57160,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = 31500,
        Z                   = 0,
        Y                   = 58600,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
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
        X                   = 3500,
        Z                   = 0,
        Y                   = 4500,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 3940,
        Z                   = 100,
        Y                   = -4000,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 13,
        ChipIndex           = 0xD,
        NpcIndex            = 0x195,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = 3330,
        Z                   = 0,
        Y                   = 2500,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = -4660,
        Z                   = 0,
        Y                   = 2600,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 15,
        ChipIndex           = 0xF,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = -30680,
        Z                   = 0,
        Y                   = 28760,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 14,
    )

    DeclNpc(
        X                   = 31500,
        Z                   = 0,
        Y                   = 53100,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 2940,
        Z                   = 0,
        Y                   = 2450,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 18,
        ChipIndex           = 0x12,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 17,
    )

    DeclNpc(
        X                   = -28600,
        Z                   = 0,
        Y                   = 27930,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 19,
        ChipIndex           = 0x13,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 18,
    )

    DeclNpc(
        X                   = -31820,
        Z                   = 0,
        Y                   = 26670,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 19,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0xE8,
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
        NpcIndex            = 0x80,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclActor(
        TriggerX            = 30990,
        TriggerZ            = 0,
        TriggerY            = 55250,
        TriggerRange        = 1000,
        ActorX              = 30990,
        ActorZ              = 1100,
        ActorY              = 55250,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 37,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 29620,
        TriggerZ            = 0,
        TriggerY            = 60000,
        TriggerRange        = 1000,
        ActorX              = 29620,
        ActorZ              = 1500,
        ActorY              = 60000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 33,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 2020,
        TriggerZ            = 0,
        TriggerY            = 42880,
        TriggerRange        = 400,
        ActorX              = 2020,
        ActorZ              = 800,
        ActorY              = 42880,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 39,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 3020,
        TriggerZ            = 0,
        TriggerY            = 42000,
        TriggerRange        = 400,
        ActorX              = 3020,
        ActorZ              = 800,
        ActorY              = 42000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 40,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 3060,
        TriggerZ            = 0,
        TriggerY            = 2500,
        TriggerRange        = 400,
        ActorX              = 3500,
        ActorZ              = 1500,
        ActorY              = 4500,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_476",          # 00, 0
        "Function_1_6E5",          # 01, 1
        "Function_2_7C5",          # 02, 2
        "Function_3_942",          # 03, 3
        "Function_4_966",          # 04, 4
        "Function_5_98A",          # 05, 5
        "Function_6_98F",          # 06, 6
        "Function_7_DBF",          # 07, 7
        "Function_8_EB3",          # 08, 8
        "Function_9_10E0",         # 09, 9
        "Function_10_1328",        # 0A, 10
        "Function_11_18BA",        # 0B, 11
        "Function_12_1FF1",        # 0C, 12
        "Function_13_20AC",        # 0D, 13
        "Function_14_2134",        # 0E, 14
        "Function_15_224B",        # 0F, 15
        "Function_16_234E",        # 10, 16
        "Function_17_243B",        # 11, 17
        "Function_18_24ED",        # 12, 18
        "Function_19_268A",        # 13, 19
        "Function_20_29C2",        # 14, 20
        "Function_21_36A5",        # 15, 21
        "Function_22_3E28",        # 16, 22
        "Function_23_439B",        # 17, 23
        "Function_24_43FC",        # 18, 24
        "Function_25_4BC8",        # 19, 25
        "Function_26_4C7C",        # 1A, 26
        "Function_27_5591",        # 1B, 27
        "Function_28_55EB",        # 1C, 28
        "Function_29_5645",        # 1D, 29
        "Function_30_56A4",        # 1E, 30
        "Function_31_56FC",        # 1F, 31
        "Function_32_5754",        # 20, 32
        "Function_33_57EC",        # 21, 33
        "Function_34_5DEC",        # 22, 34
        "Function_35_5E52",        # 23, 35
        "Function_36_5EBC",        # 24, 36
        "Function_37_5F22",        # 25, 37
        "Function_38_5F81",        # 26, 38
        "Function_39_604F",        # 27, 39
        "Function_40_612F",        # 28, 40
    )


    def Function_0_476(): pass

    label("Function_0_476")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_65E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 7)), scpexpr(EXPR_END)), "loc_4FA")
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0x15, 2200, 0, 42000, 90)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x14, -150, 0, 42850, 90)
    OP_43(0x14, 0x0, 0x0, 0x4)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, -31600, 0, 58830, 0)
    ClearChrFlags(0x1C, 0x80)
    SetChrPos(0x1C, -28790, 0, 53110, 90)
    ClearChrFlags(0x1E, 0x80)
    Jump("loc_65E")

    label("loc_4FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 6)), scpexpr(EXPR_END)), "loc_509")
    ClearChrFlags(0x17, 0x80)
    Jump("loc_65E")

    label("loc_509")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 4)), scpexpr(EXPR_END)), "loc_57D")
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0x15, 2940, 0, 1420, 180)
    SetChrFlags(0x15, 0x10)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x14, 2940, 0, 490, 0)
    SetChrFlags(0x14, 0x10)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, -30690, 0, 27510, 0)
    ClearChrFlags(0x1D, 0x80)
    Jump("loc_65E")

    label("loc_57D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 3)), scpexpr(EXPR_END)), "loc_604")
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0x15, 6140, 100, -540, 180)
    SetChrFlags(0x15, 0x10)
    SetChrFlags(0x15, 0x4)
    OP_4A(0x15, 255)
    SetChrChipByIndex(0x15, 16)
    SetChrSubChip(0x15, 0)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x14, 6100, 100, -2320, 0)
    SetChrFlags(0x14, 0x10)
    SetChrFlags(0x14, 0x4)
    OP_4A(0x14, 255)
    SetChrChipByIndex(0x14, 17)
    SetChrSubChip(0x14, 0)
    ClearChrFlags(0x12, 0x80)
    OP_62(0x12, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    ClearChrFlags(0x1F, 0x80)
    Jump("loc_65E")

    label("loc_604")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EC, 5)), scpexpr(EXPR_END)), "loc_65E")
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, 31370, 0, 53040, 90)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EC, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EC, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_65E")
    ClearChrFlags(0x14, 0x80)
    SetChrFlags(0x14, 0x10)
    SetChrPos(0x14, 31040, 0, 26400, 90)
    ClearChrFlags(0x1A, 0x80)

    label("loc_65E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6E4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 4)), scpexpr(EXPR_END)), "loc_690")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_68D")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x4B), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    Event(0, 26)

    label("loc_68D")

    Jump("loc_6E4")

    label("loc_690")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 3)), scpexpr(EXPR_END)), "loc_6CC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 5)), scpexpr(EXPR_END)), "loc_6B6")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x2505)
    SetMapFlags(0x10000000)
    Event(0, 24)
    Jump("loc_6C9")

    label("loc_6B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_6C9")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    Event(0, 22)

    label("loc_6C9")

    Jump("loc_6E4")

    label("loc_6CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EC, 5)), scpexpr(EXPR_END)), "loc_6E4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6E4")
    SetMapFlags(0x10000000)
    Event(0, 20)

    label("loc_6E4")

    Return()

    # Function_0_476 end

    def Function_1_6E5(): pass

    label("Function_1_6E5")

    OP_B1("T2511_n")
    OP_82(0x82, 0x0)
    OP_64(0x0, 0x1)
    OP_64(0x1, 0x1)
    OP_64(0x2, 0x1)
    OP_64(0x3, 0x1)
    OP_64(0x4, 0x1)
    OP_71(0x404, 0x0)
    ExitThread()
    OP_71(0x4, 0x4)
    ExitThread()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7C4")
    OP_65(0x1, 0x1)
    OP_65(0x2, 0x1)
    OP_65(0x3, 0x1)
    OP_65(0x4, 0x1)
    OP_72(0x1001, 0x0)
    ExitThread()
    OP_A1(0x20, 0x4)
    SetChrPos(0x20, 2040, 0, 42880, 0)
    OP_D1(32, 0, 90000, 0, 0)
    OP_72(0x404, 0x0)
    ExitThread()
    OP_72(0x4, 0x4)
    ExitThread()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_786")
    OP_62(0x12, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)

    label("loc_786")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EC, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EC, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7B3")
    OP_71(0x1001, 0x0)
    ExitThread()
    OP_71(0x404, 0x0)
    ExitThread()
    OP_71(0x4, 0x4)
    ExitThread()
    OP_64(0x2, 0x1)
    OP_64(0x3, 0x1)

    label("loc_7B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 7)), scpexpr(EXPR_END)), "loc_7C4")
    OP_64(0x4, 0x1)
    OP_72(0x1001, 0x0)
    ExitThread()

    label("loc_7C4")

    Return()

    # Function_1_6E5 end

    def Function_2_7C5(): pass

    label("Function_2_7C5")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7EA")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_92C")

    label("loc_7EA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_803")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_92C")

    label("loc_803")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_81C")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_92C")

    label("loc_81C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_835")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_92C")

    label("loc_835")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_84E")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_92C")

    label("loc_84E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_867")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_92C")

    label("loc_867")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_880")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_92C")

    label("loc_880")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_899")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_92C")

    label("loc_899")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8B2")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_92C")

    label("loc_8B2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8CB")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_92C")

    label("loc_8CB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8E4")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_92C")

    label("loc_8E4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8FD")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_92C")

    label("loc_8FD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_916")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_92C")

    label("loc_916")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_92C")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_92C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_941")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_92C")

    label("loc_941")

    Return()

    # Function_2_7C5 end

    def Function_3_942(): pass

    label("Function_3_942")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_965")
    OP_8D(0xFE, -3430, 3160, -5050, 1500, 2000)
    Jump("Function_3_942")

    label("loc_965")

    Return()

    # Function_3_942 end

    def Function_4_966(): pass

    label("Function_4_966")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_989")
    OP_8D(0xFE, 510, 43490, -1140, 41320, 2000)
    Jump("Function_4_966")

    label("loc_989")

    Return()

    # Function_4_966 end

    def Function_5_98A(): pass

    label("Function_5_98A")

    Call(0, 6)
    Return()

    # Function_5_98A end

    def Function_6_98F(): pass

    label("Function_6_98F")

    TalkBegin(0x17)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 7)), scpexpr(EXPR_END)), "loc_A45")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_9F5")

    ChrTalk(    #0
        0x17,
        (
            "看你们这么精神，\x01",
            "我也很开心哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x17,
        (
            "喏，还没吃午饭的话\x01",
            "就赶快坐下来吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A42")

    label("loc_9F5")


    ChrTalk(    #2
        0x17,
        (
            "呼，\x01",
            "午饭时间终于结束了。\x02",
        )
    )

    Jump("loc_A1B")

    label("loc_A1B")

    CloseMessageWindow()

    ChrTalk(    #3
        0x17,
        (
            "你们这些学生\x01",
            "可真是精神呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_A42")

    Jump("loc_DBB")

    label("loc_A45")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 6)), scpexpr(EXPR_END)), "loc_B0C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_AAC")

    ChrTalk(    #4
        0x17,
        (
            "看你的脸色，\x01",
            "好像没什么精神嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x17,
        (
            "我们这里开到很晚的，\x01",
            "肚子饿了就来吃吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B09")

    label("loc_AAC")


    ChrTalk(    #6
        0x17,
        (
            "今天学生会的孩子们\x01",
            "好像待到很晚呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x17,
        (
            "我们这里开到很晚的。\x01",
            "肚子饿了就来吃吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_B09")

    Jump("loc_DBB")

    label("loc_B0C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 4)), scpexpr(EXPR_END)), "loc_B9F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_B3D")

    ChrTalk(    #8
        0x17,
        "好了好了，赶快坐下来吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_B9C")

    label("loc_B3D")


    ChrTalk(    #9
        0x17,
        "好忙好忙。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x17,
        (
            "每次考试一结束\x01",
            "就是这个样子。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x17,
        (
            "反正这也算是\x01",
            "食堂的惯例了吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_B9C")

    Jump("loc_DBB")

    label("loc_B9F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 3)), scpexpr(EXPR_END)), "loc_D0A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_BF7")

    ChrTalk(    #12
        0x17,
        "今天没见到过雷克特同学哦。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x17,
        (
            "巴克斯先生\x01",
            "可能知道些什么吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D07")

    label("loc_BF7")


    ChrTalk(    #14
        0x13B,
        (
            "#640F不好意思，德波拉阿姨。\x01",
            "有没有见到我们会长？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x17,
        "哎呀，又在找吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x152,
        (
            "#734F哈哈，\x01",
            "总是给您添麻烦……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x17,
        "这个啊，今天没见到过呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x17,
        (
            "他每次经过这里\x01",
            "都一定会打个招呼的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x105,
        "#044F是、是这样吗……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x13B,
        "#647F（唔，难以想象……）\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_D07")

    Jump("loc_DBB")

    label("loc_D0A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EC, 5)), scpexpr(EXPR_END)), "loc_DBB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_D60")

    ChrTalk(    #21
        0x17,
        (
            "你们这个年纪\x01",
            "饭量都不小呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x17,
        (
            "来来，\x01",
            "别客气哦！\x02",
        )
    )

    Jump("loc_D5C")

    label("loc_D5C")

    CloseMessageWindow()
    Jump("loc_DBB")

    label("loc_D60")


    ChrTalk(    #23
        0x17,
        (
            "哦？是没见过的生面孔呢。\x01",
            "是一年级的孩子吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x17,
        (
            "这里是食堂哦。\x01",
            "来吃点什么吧！\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_DBB")

    TalkEnd(0x17)
    Return()

    # Function_6_98F end

    def Function_7_DBF(): pass

    label("Function_7_DBF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 7)), scpexpr(EXPR_END)), "loc_DCC")
    Jump("loc_EAF")

    label("loc_DCC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 6)), scpexpr(EXPR_END)), "loc_DD6")
    Jump("loc_EAF")

    label("loc_DD6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 4)), scpexpr(EXPR_END)), "loc_DE0")
    Jump("loc_EAF")

    label("loc_DE0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 3)), scpexpr(EXPR_END)), "loc_DEA")
    Jump("loc_EAF")

    label("loc_DEA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EC, 5)), scpexpr(EXPR_END)), "loc_EAF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_E40")

    ChrTalk(    #25
        0xFE,
        (
            "刚才有个孩子\x01",
            "来找丢失的东西。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0xFE,
        "不知道是不是还在二楼呢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_EAF")

    label("loc_E40")


    ChrTalk(    #27
        0xFE,
        "呀，在找人吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0xFE,
        (
            "这么说来，\x01",
            "刚才有个孩子来找失物呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xFE,
        (
            "是说那孩子吗？\x01",
            "从那边的楼梯上去了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_EAF")

    TalkEnd(0xFE)
    Return()

    # Function_7_DBF end

    def Function_8_EB3(): pass

    label("Function_8_EB3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 7)), scpexpr(EXPR_END)), "loc_F6E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_F13")

    ChrTalk(    #30
        0xFE,
        "好像是把钥匙弄丢了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xFE,
        "唔，没办法呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xFE,
        "今天是独立训练……\x02",
    )

    CloseMessageWindow()
    Jump("loc_F6B")

    label("loc_F13")

    OP_8C(0xFE, 90, 0)

    ChrTalk(    #33
        0xFE,
        "哦？\x02",
    )

    Jump("loc_F2B")

    label("loc_F2B")

    CloseMessageWindow()

    ChrTalk(    #34
        0xFE,
        "……钥匙到哪儿去了？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xFE,
        "没有钥匙不就进不去了吗！\x02",
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_F6B")

    Jump("loc_10CC")

    label("loc_F6E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 6)), scpexpr(EXPR_END)), "loc_F78")
    Jump("loc_10CC")

    label("loc_F78")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 4)), scpexpr(EXPR_END)), "loc_102B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_FBF")

    ChrTalk(    #36
        0xFE,
        "三年级生还真是忙得够呛啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xFE,
        "真不明白……\x02",
    )

    CloseMessageWindow()
    Jump("loc_1028")

    label("loc_FBF")


    ChrTalk(    #38
        0xFE,
        (
            "三年级和二年级的\x01",
            "境界果然是不同啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xFE,
        (
            "莫妮卡，现在说这种话，\x01",
            "等你上三年级的时候会哭的哦？\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_1028")

    Jump("loc_10CC")

    label("loc_102B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 3)), scpexpr(EXPR_END)), "loc_10C5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_1081")

    ChrTalk(    #40
        0xFE,
        (
            "顺便也来\x01",
            "交换一些椰菜吧。\x02",
        )
    )

    Jump("loc_1065")

    label("loc_1065")

    CloseMessageWindow()

    ChrTalk(    #41
        0xFE,
        "嗯，就这么办吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_10C2")

    label("loc_1081")


    ChrTalk(    #42
        0xFE,
        "莫妮卡，把鸡蛋给我。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xFE,
        "作为回报我就给你胡萝卜吧。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_10C2")

    Jump("loc_10CC")

    label("loc_10C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EC, 5)), scpexpr(EXPR_END)), "loc_10CC")

    label("loc_10CC")

    TalkEnd(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_10DF")
    OP_4A(0xFE, 255)

    label("loc_10DF")

    Return()

    # Function_8_EB3 end

    def Function_9_10E0(): pass

    label("Function_9_10E0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 7)), scpexpr(EXPR_END)), "loc_11CA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_115A")

    ChrTalk(    #44
        0xFE,
        (
            "因为实在没办法，\x01",
            "所以我也来帮忙一起找了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xFE,
        (
            "最后可别告诉我\x01",
            "『其实是自己的脚踩到了』哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11C7")

    label("loc_115A")


    ChrTalk(    #46
        0xFE,
        (
            "克拉拉学长\x01",
            "把钥匙弄丢了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0xFE,
        (
            "上次我弄丢的时候\x01",
            "可被她训得很惨的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0xFE,
        "真是没资格说别人啊～。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_11C7")

    Jump("loc_1314")

    label("loc_11CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 6)), scpexpr(EXPR_END)), "loc_11D4")
    Jump("loc_1314")

    label("loc_11D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 4)), scpexpr(EXPR_END)), "loc_1282")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_1226")

    ChrTalk(    #49
        0xFE,
        "那只是借口啦～。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0xFE,
        (
            "因为克拉拉学长\x01",
            "完全都没有学习嘛。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_127F")

    label("loc_1226")


    ChrTalk(    #51
        0xFE,
        (
            "我可是拿到\x01",
            "平均水平的分数的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0xFE,
        (
            "好好学习\x01",
            "就不会那么辛苦啦～。\x02",
        )
    )

    Jump("loc_127B")

    label("loc_127B")

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_127F")

    Jump("loc_1314")

    label("loc_1282")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 3)), scpexpr(EXPR_END)), "loc_1309")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_12CF")

    ChrTalk(    #53
        0xFE,
        "因为自己是学长就那么专横……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0xFE,
        "太卑鄙了～～～！\x02",
    )

    CloseMessageWindow()
    Jump("loc_1306")

    label("loc_12CF")


    ChrTalk(    #55
        0xFE,
        "克拉拉学长那么专横……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0xFE,
        "哇～住手啊～！\x02",
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_1306")

    Jump("loc_1314")

    label("loc_1309")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EC, 5)), scpexpr(EXPR_END)), "loc_1314")
    Call(0, 21)

    label("loc_1314")

    TalkEnd(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1327")
    OP_4A(0xFE, 255)

    label("loc_1327")

    Return()

    # Function_9_10E0 end

    def Function_10_1328(): pass

    label("Function_10_1328")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 7)), scpexpr(EXPR_END)), "loc_13FE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_1365")

    ChrTalk(    #57
        0x12,
        "#1782F……今天之内抓捕归案。\x02",
    )

    CloseMessageWindow()
    Jump("loc_13FB")

    label("loc_1365")


    ChrTalk(    #58
        0x12,
        (
            "#1782F明天就是学生大会了。\x02\x03",

            "……尽快把他抓捕归案。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x105,
        (
            "#042F是、是！\x02\x03",

            "#045F（雷欧学长，\x01",
            "  说话还是那么简洁……）\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)

    label("loc_13FB")

    Jump("loc_18B6")

    label("loc_13FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 6)), scpexpr(EXPR_END)), "loc_1408")
    Jump("loc_18B6")

    label("loc_1408")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 4)), scpexpr(EXPR_END)), "loc_165E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EF, 0)), scpexpr(EXPR_END)), "loc_148D")
    OP_8C(0xFE, 90, 0)

    ChrTalk(    #60
        0x12,
        (
            "#1782F…………到月底了吗。\x02\x03",

            "差不多是雷克特\x01",
            "开始行动的时候了。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x105, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)
    Jump("loc_165B")

    label("loc_148D")


    ChrTalk(    #61
        0x12,
        (
            "#1780F那个信封是…………\x02\x03",

            "#1782F被雷克特硬塞的吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x105,
        (
            "#045F啊、啊哈哈……\x02\x03",

            "#040F那个，没关系的。\x01",
            "我拿去交给市长就行了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x12,
        "#1780F……………………\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #64
        "\x07\x00得到了\x07\x02２００米拉\x07\x00。\x02",
    )

    Jump("loc_1587")

    label("loc_1587")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    AddMira(200)

    ChrTalk(    #65
        0x12,
        (
            "#1782F卢安在沿街道往南走的方向，\x01",
            "市长邸在卢安南街区东侧。\x02\x03",

            "不要迷路哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x105,
        (
            "#045F啊，是。\x01",
            "谢谢。\x02\x03",

            "（这算是\x01",
            "  打杂的小费吗……？）\x02",
        )
    )

    Jump("loc_1657")

    label("loc_1657")

    CloseMessageWindow()
    OP_A2(0x2F78)

    label("loc_165B")

    Jump("loc_18B6")

    label("loc_165E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 3)), scpexpr(EXPR_END)), "loc_1820")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_16C9")
    OP_63(0x12)
    Sleep(200)

    ChrTalk(    #67
        0x12,
        (
            "#1780F普通业务由我来处理。\x02\x03",

            "你们赶快去找人。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x12, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_181D")

    label("loc_16C9")

    OP_63(0x12)
    Sleep(200)

    ChrTalk(    #68
        0x12,
        "#1780F……有什么事吗。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x13B,
        (
            "#645F不、不是，那个……\x02\x03",

            "还是没能抓到\x01",
            "雷克特学长呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x152,
        (
            "#734F已经搜索了三天了，\x01",
            "还是放弃吧……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x12,
        (
            "#1782F那家伙可不是\x01",
            "随随便便就能找到的。\x02\x03",

            "但是他一定\x01",
            "潜伏在学院里面。\x02\x03",

            "#1783F…………去把他抓回来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x152,
        "#733F是、是！\x02",
    )

    CloseMessageWindow()
    OP_62(0x12, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_A2(0x5)

    label("loc_181D")

    Jump("loc_18B6")

    label("loc_1820")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EC, 5)), scpexpr(EXPR_END)), "loc_18B6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_187F")

    ChrTalk(    #73
        0x12,
        (
            "#1782F那家伙是危险人物。\x01",
            "不要轻易和他接触，见到后立刻来通知我们。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18B6")

    label("loc_187F")


    ChrTalk(    #74
        0x12,
        (
            "#1780F如果看见学生会长\x01",
            "请立即通知我们。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)

    label("loc_18B6")

    TalkEnd(0xFE)
    Return()

    # Function_10_1328 end

    def Function_11_18BA(): pass

    label("Function_11_18BA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 7)), scpexpr(EXPR_END)), "loc_18C7")
    Jump("loc_1FED")

    label("loc_18C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 6)), scpexpr(EXPR_END)), "loc_1B21")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EF, 2)), scpexpr(EXPR_END)), "loc_1931")

    ChrTalk(    #75
        0x13,
        (
            "#1790F已经进入宵禁时间了呢。\x02\x03",

            "科洛丝，\x01",
            "你也早点回去为好。\x02",
        )
    )

    Jump("loc_192D")

    label("loc_192D")

    CloseMessageWindow()
    Jump("loc_1B1E")

    label("loc_1931")


    ChrTalk(    #76
        0x105,
        (
            "#043F啊，露西学姐……\x02\x03",

            "你一直工作到\x01",
            "这么晚吗……？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0x13,
        (
            "#1791F嗯嗯，稍微拖久了一点……\x02\x03",

            "刚刚才把工作做完。\x01",
            "得赶快回去才行呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0x105,
        "#049F啊，是…………\x02",
    )

    CloseMessageWindow()
    OP_62(0x13, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #79
        0x13,
        (
            "#1792F科洛丝，怎么了？\x02\x03",

            "你好像没什么精神……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0x105,
        (
            "#047F不…………\x01",
            "没什么事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0x13,
        (
            "#1790F…………是吗……\x02\x03",

            "已经进入宵禁时间了，\x01",
            "你也赶快回去为好。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0x105,
        (
            "#042F是…………\x02\x03",

            "#049F（不过，现在…………\x01",
            "  ……我不想回去……）\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2F7A)

    label("loc_1B1E")

    Jump("loc_1FED")

    label("loc_1B21")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 4)), scpexpr(EXPR_END)), "loc_1BFB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_1B85")

    ChrTalk(    #83
        0x13,
        (
            "#1793F一看到那张脸，\x01",
            "我就忍不住想揍他一顿。\x02\x03",

            "这是我的本能吗……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BF8")

    label("loc_1B85")


    ChrTalk(    #84
        0x13,
        (
            "#1793F又打了他一顿。\x02\x03",

            "……为什么呢。\x02\x03",

            "#1795F一看到那张脸，\x01",
            "我就忍不住想揍他一顿呢……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x6)

    label("loc_1BF8")

    Jump("loc_1FED")

    label("loc_1BFB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 3)), scpexpr(EXPR_END)), "loc_1C05")
    Jump("loc_1FED")

    label("loc_1C05")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EC, 5)), scpexpr(EXPR_END)), "loc_1FED")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EF, 1)), scpexpr(EXPR_END)), "loc_1D47")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_1C84")

    ChrTalk(    #85
        0x13,
        (
            "#1790F如果对学生会有意见的话，\x01",
            "请不要客气，尽管提出来哦。\x02\x03",

            "#1794F……我会想办法的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D44")

    label("loc_1C84")


    ChrTalk(    #86
        0x13,
        (
            "#1790F在今后的校园生活中\x01",
            "应该还会遇到许多事……\x02\x03",

            "如果对学生会有意见的话，\x01",
            "请不要客气，尽管提出来哦。\x02\x03",

            "#1794F……我会想办法的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0x105,
        "#044F？？？　好、好的。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x6)

    label("loc_1D44")

    Jump("loc_1FED")

    label("loc_1D47")


    ChrTalk(    #88
        0x13,
        (
            "#1790F哎呀，你…………\x02\x03",

            "难道是那个插班生？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0x105,
        (
            "#044F啊……是、是的……\x02\x03",

            "那个，嗯……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0x13,
        (
            "#1790F第一次来学生会室吗。\x01",
            "不用那么紧张啦。\x02\x03",

            "#1794F我是副会长露西。\x01",
            "露西·赛兰德。\x02\x03",

            "这位是书记兼会计雷欧同学。\x02\x03",

            "#1791F幸会。\x01",
            "欢迎你来我们这里。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0x105,
        (
            "#044F…………………………\x02\x03",

            "#540F（好漂亮的人呢……）\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_62(0x105, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(    #92
        0x105,
        (
            "#542F那个，\x01",
            "我叫做科洛丝·琳希。\x02\x03",

            "#045F请、请多指教。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0x13,
        (
            "#1794F彼此彼此，请多指教，\x01",
            "科洛丝同学。\x02\x03",

            "#1790F在今后的校园生活中\x01",
            "应该还会遇到许多事……\x02\x03",

            "加油哦。\x01",
            "我相信你一定没问题的。\x02",
        )
    )

    Jump("loc_1FCD")

    label("loc_1FCD")

    CloseMessageWindow()

    ChrTalk(    #94
        0x105,
        "#542F是、是……\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2F79)

    label("loc_1FED")

    TalkEnd(0xFE)
    Return()

    # Function_11_18BA end

    def Function_12_1FF1(): pass

    label("Function_12_1FF1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 4)), scpexpr(EXPR_END)), "loc_20A8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_205B")

    ChrTalk(    #95
        0xFE,
        (
            "之后还有一堆\x01",
            "考卷等着批改……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0xFE,
        (
            "啊啊～真没干劲啊～。\x01",
            "今天就休息一整天吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_20A8")

    label("loc_205B")


    ChrTalk(    #97
        0xFE,
        (
            "呼～\x01",
            "考试总算结束了呢。\x02",
        )
    )

    Jump("loc_207F")

    label("loc_207F")

    CloseMessageWindow()

    ChrTalk(    #98
        0xFE,
        (
            "考试的时候\x01",
            "老师也够辛苦的呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x7)

    label("loc_20A8")

    TalkEnd(0xFE)
    Return()

    # Function_12_1FF1 end

    def Function_13_20AC(): pass

    label("Function_13_20AC")

    TalkBegin(0x19)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 7)), scpexpr(EXPR_END)), "loc_2130")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_210C")

    ChrTalk(    #99
        0x19,
        "哎呀，科洛丝同学。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0x19,
        (
            "呵呵，\x01",
            "我偶尔也会离开接待岗位的。\x02",
        )
    )

    Jump("loc_2108")

    label("loc_2108")

    CloseMessageWindow()
    Jump("loc_2130")

    label("loc_210C")

    OP_8C(0xFE, 0, 0)

    ChrTalk(    #101
        0x19,
        "麻烦要一份Ａ套餐。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x8)

    label("loc_2130")

    TalkEnd(0x19)
    Return()

    # Function_13_20AC end

    def Function_14_2134(): pass

    label("Function_14_2134")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 4)), scpexpr(EXPR_END)), "loc_2247")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_21A6")
    OP_8C(0xFE, 180, 0)

    ChrTalk(    #102
        0xFE,
        (
            "啊啊，\x01",
            "那个我来送吧。\x02",
        )
    )

    Jump("loc_2171")

    label("loc_2171")

    CloseMessageWindow()

    ChrTalk(    #103
        0xFE,
        (
            "部长应该\x01",
            "也知道记录的方法……\x02",
        )
    )

    Jump("loc_21A2")

    label("loc_21A2")

    CloseMessageWindow()
    Jump("loc_2247")

    label("loc_21A6")


    ChrTalk(    #104
        0xFE,
        "哦？科洛丝同学。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0xFE,
        "今天练习暂停哦。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0x105,
        (
            "#040F啊，我知道。\x02\x03",

            "明天起再开始练习对吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0xFE,
        (
            "嗯，\x01",
            "大会也快临近了。\x02",
        )
    )

    Jump("loc_222B")

    label("loc_222B")

    CloseMessageWindow()

    ChrTalk(    #108
        0xFE,
        "鼓起劲头努力吧。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x9)

    label("loc_2247")

    TalkEnd(0xFE)
    Return()

    # Function_14_2134 end

    def Function_15_224B(): pass

    label("Function_15_224B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 4)), scpexpr(EXPR_END)), "loc_234A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_22B9")
    OP_8C(0xFE, 0, 0)

    ChrTalk(    #109
        0x11,
        (
            "#730F嗯嗯，\x01",
            "关于社团活动的预算……\x02\x03",

            "利戈尔部长\x01",
            "还在教室里面吗。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_234A")

    label("loc_22B9")


    ChrTalk(    #110
        0x11,
        (
            "#733F啊啊，对了科洛丝。\x01",
            "我忘记说了……\x02\x03",

            "#730F去卢安之前\x01",
            "先要取得外出许可才行啊。\x02\x03",

            "跟校长说明情况\x01",
            "应该能得到许可的。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xA)

    label("loc_234A")

    TalkEnd(0xFE)
    Return()

    # Function_15_224B end

    def Function_16_234E(): pass

    label("Function_16_234E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 7)), scpexpr(EXPR_END)), "loc_2437")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_23BA")

    ChrTalk(    #111
        0xFE,
        (
            "话说回来，\x01",
            "要一个人处理这么多事啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0xFE,
        (
            "唔，学长的工作方法\x01",
            "看来很值得学习啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2437")

    label("loc_23BA")


    ChrTalk(    #113
        0xFE,
        (
            "我今天来这里\x01",
            "帮雷欧学长的忙。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0xFE,
        (
            "不过我能做的\x01",
            "也只有收集资料了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0xFE,
        (
            "哈哈，\x01",
            "一直承蒙他的照顾嘛。\x02",
        )
    )

    Jump("loc_2433")

    label("loc_2433")

    CloseMessageWindow()
    OP_A2(0xB)

    label("loc_2437")

    TalkEnd(0xFE)
    Return()

    # Function_16_234E end

    def Function_17_243B(): pass

    label("Function_17_243B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 4)), scpexpr(EXPR_END)), "loc_24E9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_2496")

    ChrTalk(    #116
        0xFE,
        "首先是罗基克同学吧～。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0xFE,
        (
            "然后打算去问问\x01",
            "三年级比较闲的人。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_24E9")

    label("loc_2496")


    ChrTalk(    #118
        0xFE,
        (
            "好了，\x01",
            "考试也顺利结束了。\x02",
        )
    )

    Jump("loc_24BF")

    label("loc_24BF")

    CloseMessageWindow()

    ChrTalk(    #119
        0xFE,
        "今天要不要组织部员聚会一下呢？\x02",
    )

    CloseMessageWindow()
    OP_A2(0xC)

    label("loc_24E9")

    TalkEnd(0xFE)
    Return()

    # Function_17_243B end

    def Function_18_24ED(): pass

    label("Function_18_24ED")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 7)), scpexpr(EXPR_END)), "loc_2686")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_END)), "loc_2565")

    ChrTalk(    #120
        0x1E,
        (
            "科洛丝，\x01",
            "等你愿意的时候就再来吧。\x02",
        )
    )

    Jump("loc_2532")

    label("loc_2532")

    CloseMessageWindow()

    ChrTalk(    #121
        0x1E,
        (
            "偶尔也要\x01",
            "来参加一下练习啊。\x02",
        )
    )

    Jump("loc_2561")

    label("loc_2561")

    CloseMessageWindow()
    Jump("loc_2686")

    label("loc_2565")


    ChrTalk(    #122
        0x1E,
        (
            "科洛丝，\x01",
            "你最近好像都没有参加练习……\x02",
        )
    )

    Jump("loc_259D")

    label("loc_259D")

    CloseMessageWindow()

    ChrTalk(    #123
        0x105,
        (
            "#044F啊，对不起，利戈尔部长。\x02\x03",

            "#043F那个，\x01",
            "我最近比较忙……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0x1E,
        "是吗……既然是你，\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0x1E,
        (
            "也没什么可奇怪的。\x01",
            "一定是有什么原因的吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0x1E,
        (
            "等你愿意的时候再来吧。\x01",
            "偶尔也要来露个脸啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0x105,
        (
            "#040F是、是的。\x01",
            "非常感谢！\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xD)

    label("loc_2686")

    TalkEnd(0xFE)
    Return()

    # Function_18_24ED end

    def Function_19_268A(): pass

    label("Function_19_268A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 3)), scpexpr(EXPR_END)), "loc_29BE")
    TurnDirection(0xFE, 0x152, 400)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F0, 0)), scpexpr(EXPR_END)), "loc_26E3")

    ChrTalk(    #128
        0xFE,
        "我不会把露西学姐交给任何人的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0xFE,
        "汉斯，你放弃吧！\x02",
    )

    CloseMessageWindow()
    Jump("loc_29BE")

    label("loc_26E3")


    ChrTalk(    #130
        0xFE,
        "啊，汉斯。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0xFE,
        (
            "你运动神经那么好，\x01",
            "怎么不加入我们社团呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0x152,
        (
            "#735F哼，我才不干。\x02\x03",

            "#730F我对露西学姐是一心一意的！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0x13B,
        (
            "#659F…………哦～？\x01",
            "所以才加入学生会啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0x152,
        (
            "#733F咦…………？\x02\x03",

            "#735F不、不是\x01",
            "这个意思啦……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0x13B,
        (
            "#649F从你说出\x01",
            "要加入学生会的时候\x01",
            "我就觉得奇怪了。\x02\x03",

            "你以为\x01",
            "工作是什么～？\x02",
        )
    )

    Jump("loc_2836")

    label("loc_2836")

    CloseMessageWindow()

    ChrTalk(    #136
        0xFE,
        "是啊，汉斯。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0xFE,
        (
            "居然带着这种不纯的动机\x01",
            "接近露西学姐……\x02",
        )
    )

    CloseMessageWindow()
    SetMapFlags(0x20)
    Sleep(100)

    ChrTalk(    #138
        0xFE,
        (
            "#3S我不会把露西学姐交给你的！\x01",
            "你放弃吧，汉斯！#2S\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(    #139
        0x152,
        (
            "#735F说什么呢。\x01",
            "露西学姐是我命中注定的人。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)

    ChrTalk(    #140
        0x152,
        (
            "#732F#3S要放弃的是你，\x01",
            "罗迪！#2S\x02",
        )
    )

    Jump("loc_2935")

    label("loc_2935")

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    ClearMapFlags(0x20)

    ChrTalk(    #141
        0x13B,
        (
            "#645F这两个人，\x01",
            "又发傻了…………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0x105,
        (
            "#045F哈、哈哈…………\x02\x03",

            "（露西学姐果然\x01",
            "  很受欢迎呢……）\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2F80)

    label("loc_29BE")

    TalkEnd(0xFE)
    Return()

    # Function_19_268A end

    def Function_20_29C2(): pass

    label("Function_20_29C2")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_6D(1200, 0, 900, 0)
    OP_67(0, 5120, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x1A, 0x80)
    SetChrFlags(0x10, 0x40)
    SetChrFlags(0x11, 0x40)
    SetChrFlags(0x12, 0x40)
    SetChrFlags(0x13, 0x40)
    OP_4A(0x10, 255)
    OP_4A(0x11, 255)
    OP_4A(0x12, 255)
    OP_4A(0x13, 255)
    SetChrPos(0x12, 540, 0, 540, 180)
    SetChrPos(0x13, -500, 0, 700, 180)
    SetChrPos(0x11, 1140, 0, -840, 0)
    SetChrPos(0x10, -60, 0, -1000, 0)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_2A9C"),
        (101, "loc_2ABB"),
        (SWITCH_DEFAULT, "loc_2ADA"),
    )


    label("loc_2A9C")

    SetChrPos(0x105, 100, -500, -9200, 180)
    OP_9F(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    Jump("loc_2ADA")

    label("loc_2ABB")

    SetChrPos(0x105, -9240, -250, -3100, 90)
    OP_9F(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    Jump("loc_2ADA")

    label("loc_2ADA")


    def lambda_2AE0():
        OP_6B(3100, 2000)
        ExitThread()

    QueueWorkItem(0x21, 0, lambda_2AE0)
    FadeToBright(2000, 0)
    OP_0D()

    ChrTalk(    #143
        0x10,
        (
            "#645F#12P呼，呼…………\x02\x03",

            "#646F那个混蛋……\x01",
            "到底藏在哪里啦！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0x11,
        (
            "#734F#12P都这样找了\x01",
            "居然还找不到……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x11, 0x13, 400)
    OP_62(0x11, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(    #145
        0x11,
        (
            "#737F露西学姐～！\x01",
            "我也到极限了啊～！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x10, 0x11, 400)

    ChrTalk(    #146
        0x10,
        (
            "#1891F#6P喂，那边的！\x01",
            "不许偷懒！\x02\x03",

            "#646F……汉斯，\x01",
            "你实际上是在偷懒吧！？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x11, 0x10, 400)

    ChrTalk(    #147
        0x11,
        (
            "#732F#11P没有，我真的是很认真在找啦。\x02\x03",

            "目击情报堆积如山，\x01",
            "为什么还找不到！？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x13, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x13)
    Sleep(200)
    OP_8C(0x13, 135, 400)
    Sleep(300)

    ChrTalk(    #148
        0x13,
        (
            "#1794F#1P今天之内果然\x01",
            "是很难抓到他了……\x02\x03",

            "#1792F雷欧同学，怎么办呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0x12,
        (
            "#1782F#5P……没办法了。\x02\x03",

            "#1780F学生会的工作\x01",
            "就靠我和露西来做吧。\x02\x03",

            "但是最后的盖章还是需要那家伙。\x01",
            "你们赶紧找吧。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2D9B():
        OP_8C(0xFE, 0, 500)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_2D9B)

    def lambda_2DA9():
        OP_8C(0xFE, 0, 500)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_2DA9)
    WaitChrThread(0x11, 0x2)
    WaitChrThread(0x10, 0x2)

    ChrTalk(    #150
        0x10,
        "#642F#3P是、是！\x02",
    )


    ChrTalk(    #151
        0x11,
        "#732F是、是！\x02",
    )

    OP_56(0x1)
    OP_59()
    OP_8C(0x12, 0, 500)

    def lambda_2DFB():
        OP_8E(0xFE, 0x21C, 0xDAC, 0x1D38, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_2DFB)
    Sleep(1000)
    OP_8C(0x13, 180, 400)

    ChrTalk(    #152
        0x13,
        "#1791F#5P你们俩，待会儿见哦。\x02",
    )

    CloseMessageWindow()

    def lambda_2E4C():

        label("loc_2E4C")

        TurnDirection(0xFE, 0x13, 400)
        OP_48()
        Jump("loc_2E4C")

    QueueWorkItem2(0x11, 2, lambda_2E4C)

    ChrTalk(    #153
        0x11,
        "#738F好……㈱\x02",
    )

    CloseMessageWindow()
    OP_8C(0x13, 0, 500)

    def lambda_2E7E():
        OP_8E(0xFE, 0xC8, 0xDAC, 0x1D38, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_2E7E)
    WaitChrThread(0x13, 0x1)
    WaitChrThread(0x12, 0x1)
    Sleep(500)

    def lambda_2EA8():
        TurnDirection(0xFE, 0x11, 400)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_2EA8)
    Sleep(100)

    def lambda_2EBB():
        TurnDirection(0xFE, 0x10, 400)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_2EBB)
    Sleep(300)

    ChrTalk(    #154
        0x10,
        "#645F#6P……那么，重新开始搜索吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #155
        0x11,
        "#734F#11P唉，心情沉重啊……\x02",
    )

    CloseMessageWindow()
    OP_22(0x6, 0x0, 0x64)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_2F34"),
        (101, "loc_2F81"),
        (SWITCH_DEFAULT, "loc_2FD5"),
    )


    label("loc_2F34")


    def lambda_2F3A():
        OP_6D(1200, 0, -800, 3000)
        ExitThread()

    QueueWorkItem(0x21, 0, lambda_2F3A)

    def lambda_2F52():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_2F52)

    def lambda_2F64():
        OP_8E(0xFE, 0x64, 0xFFFFFE0C, 0xFFFFF448, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_2F64)
    WaitChrThread(0x105, 0x1)
    Jump("loc_2FD5")

    label("loc_2F81")


    def lambda_2F87():
        OP_6D(400, 0, -1000, 3000)
        ExitThread()

    QueueWorkItem(0x21, 0, lambda_2F87)

    def lambda_2F9F():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_2F9F)

    def lambda_2FB1():
        OP_8E(0xFE, 0xFFFFF9E8, 0xFFFFFF06, 0xFFFFF3E4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_2FB1)
    WaitChrThread(0x105, 0x1)
    OP_8C(0x105, 45, 400)
    Jump("loc_2FD5")

    label("loc_2FD5")

    OP_62(0x10, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_62(0x11, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_3013"),
        (101, "loc_303C"),
        (SWITCH_DEFAULT, "loc_3065"),
    )


    label("loc_3013")


    def lambda_3019():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_3019)
    Sleep(100)

    def lambda_302C():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_302C)
    Sleep(300)
    Jump("loc_3065")

    label("loc_303C")


    def lambda_3042():
        OP_8C(0xFE, 225, 400)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_3042)
    Sleep(100)

    def lambda_3055():
        OP_8C(0xFE, 225, 400)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_3055)
    Sleep(300)
    Jump("loc_3065")

    label("loc_3065")


    ChrTalk(    #156
        0x10,
        (
            "#643F#5P啊，科洛丝……？\x02\x03",

            "怎么了，\x01",
            "拿着那么多资料……\x02",
        )
    )

    Jump("loc_30B9")

    label("loc_30B9")

    CloseMessageWindow()

    ChrTalk(    #157
        0x105,
        (
            "#044F啊……………………\x01",
            "乔儿同学……还有汉斯同学？\x02\x03",

            "#045F嗯，这是……\x02\x03",

            "#542F我正给碧欧拉老师\x01",
            "稍微帮一点忙……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #158
        0x11,
        (
            "#733F所以才在\x01",
            "放学后到处发放？\x02\x03",

            "#735F唔，\x01",
            "要是我肯定就拒绝了。\x02",
        )
    )

    Jump("loc_3199")

    label("loc_3199")

    CloseMessageWindow()

    ChrTalk(    #159
        0x10,
        (
            "#640F#5P我说…………\x01",
            "对了，科洛丝……\x02\x03",

            "#648F要不，\x01",
            "我们也来帮忙吧？\x02\x03",

            "正好现在\x01",
            "有事要到处跑……\x02",
        )
    )

    Jump("loc_321E")

    label("loc_321E")

    CloseMessageWindow()

    ChrTalk(    #160
        0x105,
        (
            "#543F不用，这是我的工作。\x02\x03",

            "#048F乔儿同学，汉斯同学。\x01",
            "那我先告辞了。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_327C():

        label("loc_327C")

        TurnDirection(0xFE, 0x105, 400)
        OP_48()
        Jump("loc_327C")

    QueueWorkItem2(0x10, 2, lambda_327C)

    def lambda_328D():
        OP_8F(0xFE, 0x44C, 0x0, 0xFFFFFF10, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_328D)

    def lambda_32A8():

        label("loc_32A8")

        TurnDirection(0xFE, 0x105, 400)
        OP_48()
        Jump("loc_32A8")

    QueueWorkItem2(0x11, 2, lambda_32A8)

    def lambda_32B9():
        OP_8F(0xFE, 0x7BC, 0x0, 0xFFFFFCB8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_32B9)
    Sleep(200)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_32E3"),
        (101, "loc_3306"),
        (SWITCH_DEFAULT, "loc_3349"),
    )


    label("loc_32E3")


    def lambda_32E9():
        OP_8E(0xFE, 0x64, 0xDAC, 0x1D4C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_32E9)
    WaitChrThread(0x105, 0x1)
    Jump("loc_3349")

    label("loc_3306")


    def lambda_330C():
        OP_8E(0xFE, 0x64, 0x0, 0xFFFFFA60, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_330C)
    WaitChrThread(0x105, 0x1)

    def lambda_332C():
        OP_8E(0xFE, 0x64, 0xDAC, 0x1D4C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_332C)
    WaitChrThread(0x105, 0x1)
    Jump("loc_3349")

    label("loc_3349")


    def lambda_334F():
        OP_6D(2540, 0, 460, 2000)
        ExitThread()

    QueueWorkItem(0x21, 0, lambda_334F)
    WaitChrThread(0x21, 0x0)
    OP_62(0x10, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x11, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x10)
    OP_63(0x11)
    Sleep(500)

    ChrTalk(    #161
        0x10,
        (
            "#645F#5P喂，听我说……\x02\x03",

            "#1890F我被分配和她住在一起了。\x01",
            "…………就是宿舍房间。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #162
        0x11,
        (
            "#733F#12P啊，什么。\x01",
            "是这样啊。\x02\x03",

            "#730F……插班生科洛丝·琳希。\x01",
            "到处都听说她是个超级天才呢。\x02\x03",

            "#731F没什么不好嘛。\x01",
            "可以让她每天教你功课哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #163
        0x10,
        (
            "#1892F#5P唔，但是啊。\x01",
            "怎么说才好呢……\x02\x03",

            "虽然她气质又高贵\x01",
            "又非常有礼貌……\x02\x03",

            "#645F……但总觉得很见外呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #164
        0x11,
        (
            "#735F#12P就是有点……\x01",
            "拒人千里的感觉吧。\x02\x03",

            "#730F但是既然你们同屋，\x01",
            "多少能聊上几句吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #165
        0x10,
        (
            "#1892F#5P不…………\x02\x03",

            "她跟我平时\x01",
            "也就是打招呼的程度。\x02\x03",

            "#1890F（要是能\x01",
            "  更平常地交流\x01",
            "  就好了啊……）\x02",
        )
    )

    CloseMessageWindow()

    def lambda_360C():
        OP_6B(3000, 2000)
        ExitThread()

    QueueWorkItem(0x21, 0, lambda_360C)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_44(0x21, 0xFF)
    ClearChrFlags(0x10, 0x40)
    ClearChrFlags(0x11, 0x40)
    ClearChrFlags(0x12, 0x40)
    ClearChrFlags(0x13, 0x40)
    OP_4F(0x0, (scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6D(0, 0, 51650, 0)
    OP_67(0, 6150, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    SetChrPos(0x105, 0, 0, 51650, 0)
    FadeToBright(1000, 0)
    OP_0D()
    ClearChrFlags(0x1A, 0x80)
    OP_A2(0x2F6A)
    EventEnd(0x0)
    Return()

    # Function_20_29C2 end

    def Function_21_36A5(): pass

    label("Function_21_36A5")

    EventBegin(0x0)
    Fade(1000)
    OP_6D(31620, 0, 27480, 0)
    OP_67(0, 5200, -10000, 0)
    OP_6B(3040, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    SetChrPos(0x105, 29660, 0, 26400, 90)
    SetChrSubChip(0x14, 0)
    Sleep(1000)

    ChrTalk(    #166
        0x14,
        "#5P咦，到哪儿去了呢……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #167
        0x14,
        "#5P哦，有了有了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #168
        0x105,
        "#043F#6P抱歉，打扰一下…………\x02",
    )

    CloseMessageWindow()
    OP_62(0x14, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0x14, 0x105, 400)
    Sleep(300)

    ChrTalk(    #169
        0x14,
        (
            "#11P啊，插班生……\x01",
            "是叫科洛丝同学吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #170
        0x14,
        "#11P有什么事吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #171
        0x105,
        (
            "#047F#6P是的。\x01",
            "嗯…………\x02\x03",

            "#542F碧欧拉老师\x01",
            "给了我这些资料……\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #172
        "\x07\x05把资料交给莫妮卡。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #173
        0x14,
        "#11P啊，是学分表吗。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #174
        0x14,
        (
            "#11P呜呜，有这么多课啊。\x01",
            "升了二年级还真是辛苦啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #175
        0x14,
        (
            "#11P嗯，\x01",
            "不过这并不是很要紧的事吧。\x02",
        )
    )

    Jump("loc_390A")

    label("loc_390A")

    CloseMessageWindow()
    OP_62(0x105, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #176
        0x105,
        (
            "#044F#6P哎…………\x02\x03",

            "……是这样吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #177
        0x14,
        (
            "#11P嗯，\x01",
            "碧欧拉老师去年也忘了发的。\x02",
        )
    )

    Jump("loc_3992")

    label("loc_3992")

    CloseMessageWindow()

    ChrTalk(    #178
        0x14,
        "#11P我记得是很晚才拿到的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #179
        0x14,
        (
            "#11P老师虽然是个美女，\x01",
            "但有时候挺糊涂的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #180
        0x14,
        "#11P科洛丝同学也要小心哦。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #181
        0x14,
        (
            "#11P要是过分努力的话，\x01",
            "可是会被人家利用的哦？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #182
        0x105,
        "#049F#6P…………………………\x02",
    )

    CloseMessageWindow()
    OP_22(0x6, 0x0, 0x64)
    ClearChrFlags(0x15, 0x80)
    SetChrFlags(0x15, 0x40)
    OP_4A(0x15, 255)
    SetChrPos(0x15, 25000, 0, 26000, 90)
    OP_9F(0x15, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_3AB1():
        OP_8E(0xFE, 0x64C8, 0x0, 0x6590, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_3AB1)
    OP_9F(0x15, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
    WaitChrThread(0x15, 0x1)
    Sleep(300)

    ChrTalk(    #183
        0x15,
        (
            "#5P啊，莫妮卡。\x01",
            "你在这里啊！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #184
        0x15,
        (
            "#5P真是的，\x01",
            "会议都开始了啦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #185
        0x14,
        (
            "#11P啊，好～！\x01",
            "我这就去～！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #186
        0x14,
        (
            "#11P回头见哦，科洛丝同学。\x01",
            "谢谢你送资料过来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #187
        0x105,
        "#045F#6P啊，嗯…………\x02",
    )

    CloseMessageWindow()
    OP_8C(0x15, 270, 400)

    def lambda_3BBD():
        OP_8E(0xFE, 0x61A8, 0x0, 0x6590, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_3BBD)

    def lambda_3BD8():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_3BD8)

    def lambda_3BEA():
        OP_8E(0xFE, 0x75E4, 0x0, 0x639C, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_3BEA)
    WaitChrThread(0x14, 0x1)

    def lambda_3C0A():
        OP_8E(0xFE, 0x61A8, 0x0, 0x639C, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_3C0A)
    Sleep(1100)

    def lambda_3C2A():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_3C2A)
    WaitChrThread(0x14, 0x1)
    OP_22(0x7, 0x0, 0x64)
    OP_62(0x105, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x105)
    Sleep(500)

    ChrTalk(    #188
        0x105,
        (
            "#047F#5P……但是…………\x02\x03",

            "#042F我必须振作才行……！\x02",
        )
    )

    CloseMessageWindow()
    OP_20(0x7D0)

    def lambda_3CB1():
        OP_6B(2940, 3000)
        ExitThread()

    QueueWorkItem(0x21, 0, lambda_3CB1)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_21()
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #189
        (
            "\x18\x07\x0C我或许只是\x01",
            "拼命想抓住什么而已。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #190
        (
            "\x18\x07\x0C不依赖任何人的我所能触碰到的太少了。\x01",
            "什么也看不见的我无法容纳任何东西。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #191
        (
            "\x18\x07\x0C正因为如此，\x01",
            "我不断对自己说，必须努力下去。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #192
        (
            "\x18\x07\x0C――为了不被抛下。\x01",
            "――为了不被舍弃。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #193
        "\x18\x07\x0C我仿佛，就要迷失了自我―――……\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(100)
    OP_C4(0x1, 0x800)
    OP_A2(0x2504)
    NewScene("ED6_DT21/T2500   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_21_36A5 end

    def Function_22_3E28(): pass

    label("Function_22_3E28")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_6D(3840, 0, 50680, 0)
    OP_67(0, 5260, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(58000, 0)
    OP_6E(280, 0)
    SetChrPos(0x105, 2920, 0, 49940, 0)
    SetChrFlags(0x105, 0x8)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x10, 0x40)
    SetChrFlags(0x11, 0x40)
    SetChrPos(0x10, 4500, 0, 50100, 270)
    SetChrPos(0x11, 4500, 0, 50100, 270)
    OP_9F(0x10, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x11, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_4A(0x10, 255)
    OP_4A(0x11, 255)

    def lambda_3EE1():
        OP_6B(2900, 3000)
        ExitThread()

    QueueWorkItem(0x21, 0, lambda_3EE1)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x21, 0x0)
    OP_C4(0x1, 0x800)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #194
        (
            "\x07\x05　　　　　　　　 『　学生会　』\x01",
            "学院的学生们自主运营的组织。\x01",
            "统管学院的纪律秩序和学生的各种活动，\x01",
            "拥有自治的权限和责任。#13000W \x01",
            "#20W　\x01",
            "而学生会最重要的任务……#4500W \x01",
            "#20W　\x01",
            "　　　　　　　　　　　#3S―――就是『捜索』！#2S\x02",
        )
    )

    Jump("loc_4006")

    label("loc_4006")

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_C4(0x1, 0x800)
    Sleep(500)

    NpcTalk(    #195
        0x105,
        "声音",
        "#3S#6P也不在这里……！！\x02",
    )

    Jump("loc_4056")

    label("loc_4056")

    OP_7C(0x0, 0x64, 0xBB8, 0x64)
    CloseMessageWindow()
    Sleep(500)
    OP_72(0x1000, 0x0)
    ExitThread()
    OP_70(0x0, 0x1E)

    def lambda_4080():
        OP_6D(3460, 0, 51800, 2000)
        ExitThread()

    QueueWorkItem(0x21, 0, lambda_4080)

    def lambda_4098():
        OP_67(0, 4780, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_4098)

    def lambda_40B0():
        OP_6C(45000, 2000)
        ExitThread()

    QueueWorkItem(0x21, 2, lambda_40B0)

    def lambda_40C0():
        OP_6B(3000, 2000)
        ExitThread()

    QueueWorkItem(0x21, 3, lambda_40C0)

    def lambda_40D0():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_40D0)

    def lambda_40E2():
        OP_8E(0xFE, 0x898, 0x0, 0xC3B4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_40E2)
    WaitChrThread(0x10, 0x1)

    def lambda_4102():
        OP_8E(0xFE, 0x898, 0x0, 0xC800, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_4102)

    def lambda_411D():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_411D)

    def lambda_412F():
        OP_8E(0xFE, 0x898, 0x0, 0xC3B4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_412F)
    WaitChrThread(0x10, 0x1)
    WaitChrThread(0x11, 0x1)
    OP_72(0x0, 0x8)
    ExitThread()
    OP_6F(0x0, 30)
    OP_70(0x0, 0x0)
    OP_22(0x7, 0x0, 0x64)
    OP_62(0x10, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #196
        0x10,
        (
            "#646F#5P可恶……\x01",
            "那个混帐学生会长！\x02\x03",

            "#1891F我还以为\x01",
            "这次一定是按照逆向思维\x01",
            "回到学生会室去了…………！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #197
        0x11,
        (
            "#734F#12P雷克特同学每次逃跑\x01",
            "的方法越来越巧妙了啊。\x02\x03",

            "#735F唔，校园里都找遍了，\x01",
            "宿舍也都转了一圈……\x02\x03",

            "#732F只剩下中庭的树丛了吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #198
        0x10,
        (
            "#646F#5P唔唔…………\x01",
            "真是把人当傻瓜……！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_42D2():
        TurnDirection(0xFE, 0x11, 500)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_42D2)
    Sleep(200)
    TurnDirection(0x11, 0x10, 500)
    Sleep(500)

    ChrTalk(    #199
        0x10,
        (
            "#1891F#5P走吧，汉斯！\x02\x03",

            "无论如何都要抓到他，\x01",
            "让他把积累下来的工作做完！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #200
        0x11,
        "#732F#12P哦！\x02",
    )

    CloseMessageWindow()
    OP_8C(0x10, 0, 600)
    OP_43(0x10, 0x3, 0x0, 0x17)
    Sleep(100)
    OP_43(0x11, 0x3, 0x0, 0x17)
    Sleep(500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    ClearChrFlags(0x105, 0x8)
    OP_A2(0x2504)
    NewScene("ED6_DT21/T2500   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_22_3E28 end

    def Function_23_439B(): pass

    label("Function_23_439B")


    def lambda_43A1():
        OP_8E(0xFE, 0x898, 0x0, 0xC9F4, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_43A1)
    WaitChrThread(0xFE, 0x1)

    def lambda_43C1():
        OP_8E(0xFE, 0xC8, 0x0, 0xC9F4, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_43C1)
    WaitChrThread(0xFE, 0x1)

    def lambda_43E1():
        OP_8E(0xFE, 0xC8, 0xFFFFF830, 0xB98C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_43E1)
    WaitChrThread(0xFE, 0x1)
    Return()

    # Function_23_439B end

    def Function_24_43FC(): pass

    label("Function_24_43FC")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #201
        (
            "\x07\x00#40W──其后，\x01",
            "科洛丝为了不荒废尤莉亚教的剑术\x01",
            "而加入了击剑部。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #202
        (
            "\x07\x00#40W在参加社团活动之余，\x01",
            "还经常陪着乔儿和汉斯\x01",
            "寻找雷克特。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(1000)
    SetChrName("")

    AnonymousTalk(    #203
        "\x07\x00#40W其后大约过了一个月──\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #204
        (
            "\x07\x00#40W王立学院\x01",
            "终于也到了那个季节！！\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(100)
    OP_C4(0x1, 0x800)
    OP_6D(31040, 0, 57300, 0)
    OP_67(0, 5240, -10000, 0)
    OP_6B(2900, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    SetChrFlags(0x105, 0x8)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x13, 0x80)
    OP_4A(0x11, 255)
    OP_4A(0x16, 255)
    OP_4A(0x13, 255)
    SetChrFlags(0x12, 0x80)
    OP_63(0x12)
    SetChrFlags(0x16, 0x40)
    SetChrFlags(0x13, 0x40)
    OP_9F(0x16, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x13, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrFlags(0x11, 0x4)
    SetChrChipByIndex(0x11, 22)
    SetChrSubChip(0x11, 0)
    SetChrPos(0x11, 28740, 250, 54300, 90)
    SetChrPos(0x16, 25000, 0, 56000, 90)
    SetChrPos(0x13, 25000, 0, 56000, 90)
    OP_1D(0x4B)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #205
        0x11,
        (
            "#732F#5P嗯，这里用公式……\x02\x03",

            "#733F咦、咦？\x01",
            "好像不对劲啊……！？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x11, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)
    OP_22(0x6, 0x0, 0x64)

    def lambda_4662():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x16, 2, lambda_4662)

    def lambda_4674():
        OP_8E(0xFE, 0x6C5C, 0x0, 0xDAC0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_4674)
    WaitChrThread(0x16, 0x1)
    OP_22(0x7, 0x0, 0x64)
    TurnDirection(0x16, 0x11, 400)
    Sleep(300)
    OP_62(0x16, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1800)

    ChrTalk(    #206
        0x16,
        (
            "#1776F#5P啊啊，定期考试的季节吗。\x02\x03",

            "#1771F当学生可真是辛苦啊～。\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0x16, 0x4)

    def lambda_4719():
        OP_8E(0xFE, 0x6C5C, 0x0, 0xE380, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_4719)
    WaitChrThread(0x16, 0x1)

    def lambda_4739():
        OP_8E(0xFE, 0x7148, 0x0, 0xE380, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_4739)
    WaitChrThread(0x16, 0x1)
    Sleep(300)
    Fade(500)
    OP_22(0x8F, 0x0, 0x64)
    SetChrPos(0x16, 29840, 250, 58240, 180)
    SetChrChipByIndex(0x16, 20)
    SetChrSubChip(0x16, 0)
    OP_0D()
    SetChrSubChip(0x11, 1)
    OP_62(0x11, 0x0, 1700, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #207
        0x11,
        (
            "#735F#12P学长（姑且）也是个学生吧。\x02\x03",

            "#732F你不用为考试复习的吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #208
        0x16,
        (
            "#1776F#5P考试啊～……\x02\x03",

            "#1775F考试～考试～……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x11, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #209
        0x11,
        "#734F#12P（毫无干劲的样子…………）\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    OP_22(0x6, 0x0, 0x64)

    def lambda_4890():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_4890)

    def lambda_48A2():
        OP_8E(0xFE, 0x69A0, 0x0, 0xDAC0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_48A2)
    Sleep(500)
    WaitChrThread(0x13, 0x1)
    TurnDirection(0x13, 0x16, 400)
    Sleep(300)

    ChrTalk(    #210
        0x13,
        "#1792F#6P啊，你在这里啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #211
        0x11,
        "#738F#11P（啊，露西学姐……！）\x02",
    )

    CloseMessageWindow()
    OP_62(0x11, 0x0, 1700, 0xA, 0xB, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    SetChrFlags(0x13, 0x4)

    def lambda_4941():
        OP_8E(0xFE, 0x6D88, 0x0, 0xE36C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_4941)
    WaitChrThread(0x13, 0x1)

    def lambda_4961():
        OP_8E(0xFE, 0x7044, 0x0, 0xE36C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_4961)
    WaitChrThread(0x13, 0x1)

    ChrTalk(    #212
        0x13,
        "#1794F#6P喂，雷克特，去复习啦！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #213
        0x16,
        (
            "#1772F#5P等、等等露西。\x01",
            "我啊…………\x02",
        )
    )

    CloseMessageWindow()

    def lambda_49DE():
        OP_8F(0xFE, 0x729C, 0x0, 0xE36C, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_49DE)
    WaitChrThread(0x13, 0x1)
    OP_22(0x8E, 0x0, 0x64)

    def lambda_4A03():
        OP_9E(0xFE, 0x14, 0x0, 0x3E8, 0x7D0)
        ExitThread()

    QueueWorkItem(0x16, 3, lambda_4A03)
    OP_62(0x16, 0xAA, 1650, 0x28, 0x2B, 0x82, 0x2)
    Sleep(1000)
    Fade(250)
    SetChrFlags(0x16, 0x20)
    OP_0D()
    OP_8C(0x13, 270, 400)
    OP_43(0x16, 0x3, 0x0, 0x19)

    def lambda_4A4D():
        OP_8E(0xFE, 0x6C34, 0x0, 0xE36C, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_4A4D)
    WaitChrThread(0x13, 0x1)

    def lambda_4A6D():
        OP_8E(0xFE, 0x6C34, 0x0, 0xDAC0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_4A6D)
    WaitChrThread(0x13, 0x1)

    def lambda_4A8D():
        OP_8E(0xFE, 0x61A8, 0x0, 0xDAC0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_4A8D)
    Sleep(1000)

    def lambda_4AAD():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_4AAD)
    WaitChrThread(0x13, 0x1)
    WaitChrThread(0x16, 0x3)
    OP_22(0x7, 0x0, 0x64)
    OP_44(0x11, 0x2)
    Sleep(1000)

    ChrTalk(    #214
        0x11,
        (
            "#735F#11P露、露西学姐……\x02\x03",

            "#737F那副样子也好美㈱\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    OP_62(0x11, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    SetChrSubChip(0x11, 0)
    Sleep(100)
    OP_62(0x11, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(    #215
        0x11,
        (
            "#733F#5P啊，糟糕糟糕。\x02\x03",

            "#735F赶快复习……！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4B97():
        OP_6B(2800, 3000)
        ExitThread()

    QueueWorkItem(0x21, 0, lambda_4B97)
    FadeToDark(2000, 0, -1)
    OP_0D()
    Sleep(1000)
    ClearChrFlags(0x105, 0x8)
    SetMapFlags(0x2000000)
    OP_A2(0x2504)
    NewScene("ED6_DT21/T2510   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_24_43FC end

    def Function_25_4BC8(): pass

    label("Function_25_4BC8")


    def lambda_4BCE():
        OP_8F(0xFE, 0x6C34, 0x0, 0xE36C, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_4BCE)
    Sleep(300)
    Fade(250)
    OP_8C(0x16, 270, 0)
    OP_22(0x20C, 0x0, 0x64)
    SetChrChipByIndex(0x16, 26)
    SetChrSubChip(0x16, 0)
    WaitChrThread(0x16, 0x1)

    def lambda_4C0E():
        OP_8C(0xFE, 180, 1000)
        ExitThread()

    QueueWorkItem(0x16, 2, lambda_4C0E)

    def lambda_4C1C():
        OP_8F(0xFE, 0x6C34, 0x0, 0xDAC0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_4C1C)
    WaitChrThread(0x16, 0x1)

    def lambda_4C3C():
        OP_8C(0xFE, 270, 1000)
        ExitThread()

    QueueWorkItem(0x16, 2, lambda_4C3C)

    def lambda_4C4A():
        OP_8F(0xFE, 0x61A8, 0x0, 0xDAC0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_4C4A)
    Sleep(1000)

    def lambda_4C6A():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x16, 2, lambda_4C6A)
    WaitChrThread(0x16, 0x1)
    Return()

    # Function_25_4BC8 end

    def Function_26_4C7C(): pass

    label("Function_26_4C7C")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_6D(31040, 0, 57300, 0)
    OP_67(0, 5240, -10000, 0)
    OP_6B(2900, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    SetChrChipByIndex(0x16, 20)
    SetChrSubChip(0x16, 0)
    SetChrFlags(0x16, 0x4)
    SetChrPos(0x16, 29840, 250, 58240, 180)
    SetChrChipByIndex(0x12, 24)
    SetChrSubChip(0x12, 0)
    SetChrFlags(0x12, 0x4)
    SetChrPos(0x12, 28740, 250, 56300, 90)
    SetChrChipByIndex(0x13, 25)
    SetChrSubChip(0x13, 0)
    SetChrFlags(0x13, 0x4)
    SetChrPos(0x13, 30860, 250, 56080, 270)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x10, 0x40)
    SetChrFlags(0x11, 0x40)
    SetChrPos(0x10, 25000, 0, 56000, 90)
    SetChrPos(0x11, 25000, 0, 56000, 90)
    SetChrPos(0x105, 25000, 0, 56000, 90)
    OP_9F(0x10, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x11, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_4A(0x16, 255)
    OP_4A(0x12, 255)
    OP_4A(0x13, 255)
    OP_4A(0x10, 255)
    OP_4A(0x11, 255)
    OP_63(0x12)
    FadeToBright(2000, 0)
    OP_0D()
    OP_22(0x6, 0x0, 0x64)
    OP_43(0x10, 0x3, 0x0, 0x1B)
    Sleep(500)
    OP_43(0x11, 0x3, 0x0, 0x1C)
    Sleep(500)
    OP_43(0x105, 0x3, 0x0, 0x1D)
    WaitChrThread(0x105, 0x3)

    ChrTalk(    #216
        0x10,
        (
            "#641F#6P早～……\x02\x03",

            "#643F啊，\x01",
            "雷克特学长居然在……\x02",
        )
    )

    Jump("loc_4E2F")

    label("loc_4E2F")

    CloseMessageWindow()

    ChrTalk(    #217
        0x16,
        (
            "#1772F#5P什么叫居然啊，居然。\x02\x03",

            "我不是经常\x01",
            "在这里高谈阔论的吗！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #218
        0x105,
        (
            "#045F#6P（不干正经事这点\x01",
            "  你也不否认啊……）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #219
        0x11,
        (
            "#738F#6P露西学姐，\x01",
            "好久不见了～㈱\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #220
        0x13,
        (
            "#1791F#11P汉斯君，看起来很精神呢。\x02\x03",

            "考试没问题吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #221
        0x11,
        (
            "#738F#6P啊哈哈～这个嘛……\x02\x03",

            "#737F别问我啦～㈱\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #222
        0x10,
        "#649F#5P……看来不行啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #223
        0x12,
        "#1782F#5P你们赶快坐下吧。\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    SetMessageWindowPos(120, 300, -1, -1)
    SetChrName("一年级学生们")

    AnonymousTalk(    #224
        "\x07\x00#3S是、是！#2S\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    OP_43(0x105, 0x3, 0x0, 0x20)
    Sleep(500)
    OP_43(0x11, 0x3, 0x0, 0x1F)
    Sleep(200)
    OP_43(0x10, 0x3, 0x0, 0x1E)
    WaitChrThread(0x105, 0x3)
    Sleep(500)

    ChrTalk(    #225
        0x12,
        (
            "#1780F#6P……全员都到齐了吧。\x02\x03",

            "#1782F那么关于今天的议题，\x01",
            "首先是……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #226
        0x16,
        (
            "#1777F#5P想听听各位\x01",
            "将来的梦想！\x02\x03",

            "#1771F那边的三个！\x01",
            "一个一个来说说将来的梦想！\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x12, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x12)
    Sleep(500)
    Fade(250)
    SetChrChipByIndex(0x13, 9)
    SetChrSubChip(0x13, 0)
    SetChrPos(0x13, 30860, 0, 56800, 270)
    OP_0D()
    OP_8C(0x13, 0, 500)

    def lambda_5141():
        OP_8E(0xFE, 0x788C, 0x0, 0xE2F4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_5141)
    WaitChrThread(0x13, 0x1)
    OP_8C(0x13, 270, 500)
    Sleep(300)

    def lambda_516D():
        OP_8F(0xFE, 0x76E8, 0x0, 0xE2F4, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_516D)
    WaitChrThread(0x13, 0x1)
    OP_22(0x8E, 0x0, 0x64)
    OP_62(0x16, 0xAA, 1650, 0x28, 0x2B, 0x82, 0x2)

    def lambda_51A4():
        OP_9E(0xFE, 0xF, 0xF, 0x3E8, 0x7D0)
        ExitThread()

    QueueWorkItem(0x16, 3, lambda_51A4)

    def lambda_51BE():
        OP_8F(0xFE, 0x788C, 0x0, 0xE2F4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_51BE)
    WaitChrThread(0x13, 0x1)
    Sleep(300)
    OP_62(0x105, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(50)
    OP_62(0x10, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(50)
    OP_62(0x11, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x13, 180, 500)

    def lambda_523E():
        OP_8E(0xFE, 0x788C, 0x0, 0xDDE0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_523E)
    WaitChrThread(0x13, 0x1)
    OP_8C(0x13, 270, 500)
    Sleep(300)
    Fade(250)
    OP_22(0x8F, 0x0, 0x64)
    SetChrChipByIndex(0x13, 25)
    SetChrSubChip(0x13, 0)
    SetChrPos(0x13, 30860, 250, 56080, 270)
    OP_0D()
    Sleep(500)

    ChrTalk(    #227
        0x13,
        "#1794F#11P雷欧君，继续……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #228
        0x12,
        (
            "#1782F#6P……首先把本年度的\x01",
            "学生会活动整体说明一下。\x02\x03",

            "#1780F然后打算\x01",
            "确定一下具体活动内容\x01",
            "和年度预算的分配………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #229
        0x16,
        (
            "#1778F#5P首先是乔儿，从你开始！\x02\x03",

            "#1778F把你现在所感受到的，\x01",
            "少女热诚的心意\x01",
            "简洁地表达出来！\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x10, 1)
    Sleep(300)

    ChrTalk(    #230
        0x10,
        "#1891F#6P#3S……打倒学生会长！！#2S\x02",
    )

    Sleep(100)
    OP_7C(0x0, 0x64, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(    #231
        0x16,
        "#1773F#5P#3S呃啊…………！？#2S\x02",
    )

    OP_7C(0x0, 0x64, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_62(0x12, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x12)
    Sleep(500)

    ChrTalk(    #232
        0x12,
        (
            "#1782F#6P如你所见，这个不算战斗力。\x01",
            "请不要对他有任何期待。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #233
        0x105,
        "#045F#11P（雷克特学长……）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #234
        0x11,
        (
            "#734F#6P（无论在或者不在\x01",
            "  都是个麻烦人物啊……）\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x10, 0)
    Sleep(300)

    ChrTalk(    #235
        0x12,
        (
            "#1780F#6P那么关于今年的活动内容，\x01",
            "依照每年的惯例从下个月开始……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_555F():
        OP_6B(3000, 3000)
        ExitThread()

    QueueWorkItem(0x21, 0, lambda_555F)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_20(0xFA0)
    OP_21()
    Sleep(1000)
    ClearMapFlags(0x2000000)
    OP_A2(0x2504)
    NewScene("ED6_DT21/T2500   ._SN", 109, 0, 0)
    IdleLoop()
    Return()

    # Function_26_4C7C end

    def Function_27_5591(): pass

    label("Function_27_5591")


    def lambda_5597():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_5597)

    def lambda_55A9():
        OP_8E(0xFE, 0x6978, 0x0, 0xDAC0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_55A9)
    WaitChrThread(0x10, 0x1)

    def lambda_55C9():
        OP_8E(0xFE, 0x6B44, 0x0, 0xDC8C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_55C9)
    WaitChrThread(0x10, 0x1)
    OP_8C(0x10, 90, 400)
    Return()

    # Function_27_5591 end

    def Function_28_55EB(): pass

    label("Function_28_55EB")


    def lambda_55F1():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_55F1)

    def lambda_5603():
        OP_8E(0xFE, 0x6978, 0x0, 0xDAC0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_5603)
    WaitChrThread(0x11, 0x1)

    def lambda_5623():
        OP_8E(0xFE, 0x6B94, 0x0, 0xD8A4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_5623)
    WaitChrThread(0x11, 0x1)
    OP_8C(0x11, 90, 400)
    Return()

    # Function_28_55EB end

    def Function_29_5645(): pass

    label("Function_29_5645")


    def lambda_564B():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_564B)

    def lambda_565D():
        OP_8E(0xFE, 0x6978, 0x0, 0xDAC0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_565D)
    WaitChrThread(0x105, 0x1)
    OP_22(0x7, 0x0, 0x64)

    def lambda_5682():
        OP_8E(0xFE, 0x6978, 0x0, 0xD2C8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_5682)
    WaitChrThread(0x105, 0x1)
    OP_8C(0x105, 45, 400)
    Return()

    # Function_29_5645 end

    def Function_30_56A4(): pass

    label("Function_30_56A4")

    SetChrFlags(0x10, 0x4)

    def lambda_56AF():
        OP_8E(0xFE, 0x6CFC, 0x0, 0xD7A0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_56AF)
    WaitChrThread(0x10, 0x1)
    OP_8C(0x10, 90, 400)
    Sleep(300)
    Fade(250)
    OP_22(0x8F, 0x0, 0x64)
    SetChrChipByIndex(0x10, 21)
    SetChrSubChip(0x10, 0)
    SetChrPos(0x10, 28740, 250, 55300, 90)
    OP_0D()
    Return()

    # Function_30_56A4 end

    def Function_31_56FC(): pass

    label("Function_31_56FC")

    SetChrFlags(0x11, 0x4)

    def lambda_5707():
        OP_8E(0xFE, 0x6CFC, 0x0, 0xD354, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_5707)
    WaitChrThread(0x11, 0x1)
    OP_8C(0x11, 90, 400)
    Sleep(300)
    Fade(250)
    OP_22(0x8F, 0x0, 0x64)
    SetChrChipByIndex(0x11, 22)
    SetChrSubChip(0x11, 0)
    SetChrPos(0x11, 28740, 250, 54300, 90)
    OP_0D()
    Return()

    # Function_31_56FC end

    def Function_32_5754(): pass

    label("Function_32_5754")

    SetChrFlags(0x105, 0x4)

    def lambda_575F():
        OP_8E(0xFE, 0x6E00, 0x0, 0xCF1C, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_575F)
    WaitChrThread(0x105, 0x1)

    def lambda_577F():
        OP_8E(0xFE, 0x788C, 0x0, 0xCF1C, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_577F)
    WaitChrThread(0x105, 0x1)

    def lambda_579F():
        OP_8E(0xFE, 0x788C, 0x0, 0xD2B4, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_579F)
    WaitChrThread(0x105, 0x1)
    OP_8C(0x105, 270, 400)
    Sleep(300)
    Fade(250)
    OP_22(0x8F, 0x0, 0x64)
    SetChrChipByIndex(0x105, 23)
    SetChrSubChip(0x105, 0)
    SetChrPos(0x105, 30860, 250, 54700, 270)
    OP_0D()
    Return()

    # Function_32_5754 end

    def Function_33_57EC(): pass

    label("Function_33_57EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 7)), scpexpr(EXPR_END)), "loc_5945")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F0, 1)), scpexpr(EXPR_END)), "loc_588E")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "爬上屋顶看看\x01",      # 0
            "不上去\x01",            # 1
        )
    )

    Jump("loc_5833")

    label("loc_5833")

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_588B")
    FadeToDark(1000, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EE, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EE, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5874")
    OP_A2(0x2505)
    Jump("loc_587F")

    label("loc_5874")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F4, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_587F")
    OP_A2(0x2506)

    label("loc_587F")

    NewScene("ED6_DT21/T2500   ._SN", 131, 0, 0)
    IdleLoop()
    Jump("loc_588B")

    label("loc_588B")

    Jump("loc_5942")

    label("loc_588E")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #236
        "\x07\x05窗外有根绳子垂下。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_0D()
    OP_62(0x105, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #237
        0x105,
        (
            "#044F嗯？这是……\x02\x03",

            "难不成，\x01",
            "是为了爬上屋顶……？\x02",
        )
    )

    Jump("loc_593E")

    label("loc_593E")

    CloseMessageWindow()
    OP_A2(0x2F81)

    label("loc_5942")

    Jump("loc_5DE8")

    label("loc_5945")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 6)), scpexpr(EXPR_END)), "loc_5A08")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F0, 1)), scpexpr(EXPR_END)), "loc_596A")
    FadeToDark(1000, 0, -1)
    OP_0D()
    NewScene("ED6_DT21/T2800   ._SN", 131, 0, 0)
    IdleLoop()
    Jump("loc_5A05")

    label("loc_596A")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #238
        "\x07\x05窗外有根绳子垂下。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_0D()

    ChrTalk(    #239
        0x105,
        (
            "#047F…………………………\x02\x03",

            "#040F这个好像\x01",
            "是延伸到屋顶上的呢……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2F81)

    label("loc_5A05")

    Jump("loc_5DE8")

    label("loc_5A08")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 4)), scpexpr(EXPR_END)), "loc_5B3E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F0, 1)), scpexpr(EXPR_END)), "loc_5A8E")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "爬上屋顶看看\x01",      # 0
            "不上去\x01",            # 1
        )
    )

    Jump("loc_5A4F")

    label("loc_5A4F")

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5A8B")
    FadeToDark(1000, 0, -1)
    OP_0D()
    NewScene("ED6_DT21/T2500   ._SN", 131, 0, 0)
    IdleLoop()
    Jump("loc_5A8B")

    label("loc_5A8B")

    Jump("loc_5B3B")

    label("loc_5A8E")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #240
        "\x07\x05窗外有根绳子垂下。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_0D()
    OP_62(0x105, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #241
        0x105,
        (
            "#044F嗯？这是……\x02\x03",

            "#042F难不成，\x01",
            "是为了爬上屋顶……？\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2F81)

    label("loc_5B3B")

    Jump("loc_5DE8")

    label("loc_5B3E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 3)), scpexpr(EXPR_END)), "loc_5D02")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F0, 1)), scpexpr(EXPR_END)), "loc_5BC4")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "爬上屋顶看看\x01",      # 0
            "不上去\x01",            # 1
        )
    )

    Jump("loc_5B85")

    label("loc_5B85")

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5BC1")
    FadeToDark(1000, 0, -1)
    OP_0D()
    NewScene("ED6_DT21/T2500   ._SN", 131, 0, 0)
    IdleLoop()
    Jump("loc_5BC1")

    label("loc_5BC1")

    Jump("loc_5CFF")

    label("loc_5BC4")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #242
        "\x07\x05窗外有根绳子垂下。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_0D()
    OP_62(0x105, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #243
        0x105,
        (
            "#044F嗯？这是……\x02\x03",

            "用来做什么的呢……？？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #244
        0x152,
        (
            "#734F啊啊，\x01",
            "这个是雷克特同学弄的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #245
        0x13B,
        (
            "#645F那个学生会长，\x01",
            "好像经常使用这根绳子\x01",
            "爬到屋顶上去哦。\x02\x03",

            "超越常识也要有个限度啊……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2F81)

    label("loc_5CFF")

    Jump("loc_5DE8")

    label("loc_5D02")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EC, 5)), scpexpr(EXPR_END)), "loc_5DE8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_5D58")
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #246
        "\x07\x05窗外有根绳子垂下。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jump("loc_5DE8")

    label("loc_5D58")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #247
        "\x07\x05窗外有根绳子垂下。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_0D()
    OP_62(0x105, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #248
        0x105,
        "#044F（是做什么用的呢……？？）\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_5DE8")

    TalkEnd(0xFF)
    Return()

    # Function_33_57EC end

    def Function_34_5DEC(): pass

    label("Function_34_5DEC")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, 25010, 0, 55900, 90)

    def lambda_5E13():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5E13)
    OP_62(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_8E(0xFE, 0x6C66, 0x0, 0xDA84, 0x1388, 0x0)
    WaitChrThread(0xFE, 0x1)
    OP_8C(0xFE, 45, 400)
    Return()

    # Function_34_5DEC end

    def Function_35_5E52(): pass

    label("Function_35_5E52")

    OP_8C(0xFE, 270, 400)
    Sleep(300)
    OP_8E(0xFE, 0x6892, 0x0, 0xDA52, 0x7D0, 0x0)
    OP_8E(0xFE, 0x6892, 0x0, 0xDA52, 0x7D0, 0x0)

    def lambda_5E8C():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5E8C)
    OP_8E(0xFE, 0x61A8, 0x0, 0xDB06, 0x7D0, 0x0)
    WaitChrThread(0xFE, 0x1)
    SetChrFlags(0xFE, 0x80)
    OP_22(0x7, 0x0, 0x64)
    Return()

    # Function_35_5E52 end

    def Function_36_5EBC(): pass

    label("Function_36_5EBC")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, 25010, 0, 55900, 90)

    def lambda_5EE3():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5EE3)
    OP_62(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_8E(0xFE, 0x6C66, 0x0, 0xDA84, 0x1388, 0x0)
    WaitChrThread(0xFE, 0x1)
    OP_8C(0xFE, 45, 400)
    Return()

    # Function_36_5EBC end

    def Function_37_5F22(): pass

    label("Function_37_5F22")

    OP_82(0x82, 0x2)
    Sleep(500)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #249
        "\x07\x00得到了\x1F\x5A\x03\x07\x00。\x02",
    )

    Jump("loc_5F5B")

    label("loc_5F5B")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_E3(0x4, 0x8, 0x1)
    OP_3E(0x35A, 1)
    OP_64(0x0, 0x1)
    TalkEnd(0xFF)
    Return()

    # Function_37_5F22 end

    def Function_38_5F81(): pass

    label("Function_38_5F81")

    EventBegin(0x2)
    OP_8C(0x105, 90, 500)
    OP_62(0x105, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x105)
    Sleep(500)

    ChrTalk(    #250
        0x105,
        (
            "#047F（好像有人在换衣服。）\x02\x03",

            "#040F（……稍后再来吧。）\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    Fade(500)
    SetChrPos(0x105, 1200, 0, 42000, 270)
    OP_6D(1200, 0, 42000, 0)
    OP_67(0, 6150, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    Sleep(500)
    EventEnd(0x4)
    Return()

    # Function_38_5F81 end

    def Function_39_604F(): pass

    label("Function_39_604F")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #251
        (
            "\x07\x05　　　\x01",
            "　换　\x01",
            "　衣　\x01",
            "　服　\x01",
            "　中　\x01",
            "　　　\x02",
        )
    )

    Jump("loc_60CA")

    label("loc_60CA")

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_0D()

    ChrTalk(    #252
        0x105,
        (
            "#047F（现在好像进不去呢。）\x02\x03",

            "#040F（……稍后再来吧。）\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFF)
    Return()

    # Function_39_604F end

    def Function_40_612F(): pass

    label("Function_40_612F")

    OP_62(0x105, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x105)
    Sleep(500)

    ChrTalk(    #253
        0x105,
        (
            "#047F（好像有人在换衣服。）\x02\x03",

            "#040F（……稍后再来吧。）\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    TalkEnd(0xFF)
    Return()

    # Function_40_612F end

    SaveToFile()

Try(main)
