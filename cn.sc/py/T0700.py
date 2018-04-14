from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'T0700   ._SN',
        MapName             = 'Rolent',
        Location            = 'T0700.x',
        MapIndex            = 9,
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
        '乘客',                                 # 9
        '乘客',                                 # 10
        '乘客',                                 # 11
        '乘客',                                 # 12
        '乘客',                                 # 13
        '乘客',                                 # 14
        '乘客',                                 # 15
        '乘客',                                 # 16
        '乘客',                                 # 17
        '乘客',                                 # 18
        '乘客',                                 # 19
        '乘客',                                 # 20
        '阿兰',                                 # 21
        '凯文神父',                             # 22
        '赛希莉亚号',                           # 23
        '赛希莉亚号影',                         # 24
        '赛希莉亚号',                           # 25
        '桥',                                   # 26
        '斯库拉特',                             # 27
        '法布利',                               # 28
        '提克',                                 # 29
        '莫莉',                                 # 30
        '乘客',                                 # 31
        '乘客',                                 # 32
        '乘客',                                 # 33
        '戴恩副队长',                           # 34
        '古兰托机长',                           # 35
        '乘务员卡拉莉丝',                       # 36
        '乘务员迪蒙',                           # 37
        '安敦',                                 # 38
        '利库斯',                               # 39
        '林德号的乘客',                         # 40
        '林德号的乘客',                         # 41
        '洛连特市街区',                         # 42
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
        'ED6_DT07/CH01200 ._CH',             # 00
        'ED6_DT07/CH01110 ._CH',             # 01
        'ED6_DT07/CH01490 ._CH',             # 02
        'ED6_DT07/CH01130 ._CH',             # 03
        'ED6_DT07/CH01140 ._CH',             # 04
        'ED6_DT07/CH01150 ._CH',             # 05
        'ED6_DT07/CH01290 ._CH',             # 06
        'ED6_DT27/CH03080 ._CH',             # 07
        'ED6_DT07/CH01450 ._CH',             # 08
        'ED6_DT07/CH01040 ._CH',             # 09
        'ED6_DT07/CH01050 ._CH',             # 0A
        'ED6_DT07/CH01020 ._CH',             # 0B
        'ED6_DT07/CH01300 ._CH',             # 0C
        'ED6_DT07/CH01440 ._CH',             # 0D
        'ED6_DT07/CH01540 ._CH',             # 0E
        'ED6_DT07/CH01460 ._CH',             # 0F
    )

    AddCharChipPat(
        'ED6_DT07/CH01200P._CP',             # 00
        'ED6_DT07/CH01110P._CP',             # 01
        'ED6_DT07/CH01490P._CP',             # 02
        'ED6_DT07/CH01130P._CP',             # 03
        'ED6_DT07/CH01140P._CP',             # 04
        'ED6_DT07/CH01150P._CP',             # 05
        'ED6_DT07/CH01290P._CP',             # 06
        'ED6_DT27/CH03080P._CP',             # 07
        'ED6_DT07/CH01450P._CP',             # 08
        'ED6_DT07/CH01040P._CP',             # 09
        'ED6_DT07/CH01050P._CP',             # 0A
        'ED6_DT07/CH01020P._CP',             # 0B
        'ED6_DT07/CH01300P._CP',             # 0C
        'ED6_DT07/CH01440P._CP',             # 0D
        'ED6_DT07/CH01540P._CP',             # 0E
        'ED6_DT07/CH01460P._CP',             # 0F
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
        X                   = 36100,
        Z                   = 0,
        Y                   = 35620,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
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
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x185,
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
        NpcIndex            = 0x185,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 44350,
        Z                   = 4000,
        Y                   = 39550,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 31840,
        Z                   = 0,
        Y                   = 51530,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 39680,
        Z                   = 4000,
        Y                   = 35470,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = 39680,
        Z                   = 4000,
        Y                   = 36730,
        Direction           = 180,
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
        X                   = 36520,
        Z                   = 0,
        Y                   = 33790,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = 37790,
        Z                   = 0,
        Y                   = 32820,
        Direction           = 315,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = 35870,
        Z                   = 0,
        Y                   = 32330,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 15,
        ChipIndex           = 0xF,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 14,
    )

    DeclNpc(
        X                   = 34280,
        Z                   = 0,
        Y                   = 30400,
        Direction           = 45,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 15,
    )

    DeclNpc(
        X                   = 43580,
        Z                   = 4000,
        Y                   = 30220,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 13,
        ChipIndex           = 0xD,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 44340,
        Z                   = 4000,
        Y                   = 35280,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 17,
    )

    DeclNpc(
        X                   = 42290,
        Z                   = 4000,
        Y                   = 31720,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 18,
    )

    DeclNpc(
        X                   = 45360,
        Z                   = 4000,
        Y                   = 54040,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x191,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = 45360,
        Z                   = 4000,
        Y                   = 55190,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x191,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = 36820,
        Z                   = 0,
        Y                   = 27490,
        Direction           = 360,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 19,
    )

    DeclNpc(
        X                   = 33120,
        Z                   = 0,
        Y                   = 30640,
        Direction           = 45,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 20,
    )

    DeclNpc(
        X                   = 35320,
        Z                   = 0,
        Y                   = -13920,
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
        TriggerX            = 36142,
        TriggerZ            = 0,
        TriggerY            = 34342,
        TriggerRange        = 1000,
        ActorX              = 36095,
        ActorZ              = 1500,
        ActorY              = 35619,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 38000,
        TriggerZ            = 0,
        TriggerY            = 30000,
        TriggerRange        = 800,
        ActorX              = 38000,
        ActorZ              = 2200,
        ActorY              = 30000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 38,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 40000,
        TriggerZ            = 4000,
        TriggerY            = 41300,
        TriggerRange        = 800,
        ActorX              = 40000,
        ActorZ              = 5500,
        ActorY              = 41800,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 39,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 34500,
        TriggerZ            = 0,
        TriggerY            = 46570,
        TriggerRange        = 800,
        ActorX              = 35000,
        ActorZ              = 1500,
        ActorY              = 46570,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 40,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_5FA",          # 00, 0
        "Function_1_6F8",          # 01, 1
        "Function_2_7FA",          # 02, 2
        "Function_3_977",          # 03, 3
        "Function_4_99B",          # 04, 4
        "Function_5_9A0",          # 05, 5
        "Function_6_19CA",         # 06, 6
        "Function_7_1CF6",         # 07, 7
        "Function_8_218F",         # 08, 8
        "Function_9_224C",         # 09, 9
        "Function_10_2350",        # 0A, 10
        "Function_11_23AA",        # 0B, 11
        "Function_12_248A",        # 0C, 12
        "Function_13_24C5",        # 0D, 13
        "Function_14_25BA",        # 0E, 14
        "Function_15_263A",        # 0F, 15
        "Function_16_272A",        # 10, 16
        "Function_17_29B2",        # 11, 17
        "Function_18_2B46",        # 12, 18
        "Function_19_2D08",        # 13, 19
        "Function_20_2E46",        # 14, 20
        "Function_21_2F42",        # 15, 21
        "Function_22_363D",        # 16, 22
        "Function_23_369C",        # 17, 23
        "Function_24_36EF",        # 18, 24
        "Function_25_3CD7",        # 19, 25
        "Function_26_3D3A",        # 1A, 26
        "Function_27_3D9D",        # 1B, 27
        "Function_28_3E00",        # 1C, 28
        "Function_29_3E5C",        # 1D, 29
        "Function_30_3EBF",        # 1E, 30
        "Function_31_3F22",        # 1F, 31
        "Function_32_3F85",        # 20, 32
        "Function_33_4C3A",        # 21, 33
        "Function_34_4C81",        # 22, 34
        "Function_35_4CDC",        # 23, 35
        "Function_36_4D4B",        # 24, 36
        "Function_37_4EB9",        # 25, 37
        "Function_38_4F8B",        # 26, 38
        "Function_39_5027",        # 27, 39
        "Function_40_50A3",        # 28, 40
    )


    def Function_0_5FA(): pass

    label("Function_0_5FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_618")
    ClearChrFlags(0x22, 0x80)
    ClearChrFlags(0x24, 0x80)
    ClearChrFlags(0x27, 0x80)
    ClearChrFlags(0x28, 0x80)
    Jump("loc_6C7")

    label("loc_618")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 0)), scpexpr(EXPR_END)), "loc_622")
    Jump("loc_6C7")

    label("loc_622")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_END)), "loc_66B")
    SetChrPos(0x1B, 42670, 4000, 39780, 90)
    OP_43(0x1B, 0x0, 0x0, 0x2)
    SetChrPos(0x14, 43140, 4000, 38650, 45)
    SetChrPos(0x1A, 44350, 4000, 39550, 270)
    ClearChrFlags(0x21, 0x80)
    Jump("loc_6C7")

    label("loc_66B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 4)), scpexpr(EXPR_END)), "loc_69F")
    ClearChrFlags(0x1C, 0x80)
    SetChrPos(0x1C, 36940, 0, 31150, 0)
    SetChrFlags(0x14, 0x10)
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x1F, 0x80)
    ClearChrFlags(0x20, 0x80)
    Jump("loc_6C7")

    label("loc_69F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 4)), scpexpr(EXPR_END)), "loc_6C7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x313, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6B3")
    SetChrFlags(0x14, 0x10)

    label("loc_6B3")

    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x25, 0x80)
    ClearChrFlags(0x26, 0x80)

    label("loc_6C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_6E6")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x51), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10F0)
    SetMapFlags(0x10000000)
    Event(0, 24)
    Jump("loc_6F7")

    label("loc_6E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6F7")
    SetMapFlags(0x10000000)
    Event(0, 21)

    label("loc_6F7")

    Return()

    # Function_0_5FA end

    def Function_1_6F8(): pass

    label("Function_1_6F8")

    OP_16(0x2, 0xFA0, 0xFFFE98A0, 0xFFFE8518, 0x230007)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_74C")
    OP_B5(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 4)), scpexpr(EXPR_END)), "loc_737")
    SetMapFlags(0x10)
    OP_11(0xE6, 0xF0, 0xFF, 0x0, 0xEA60, 0x0)
    Jump("loc_74C")

    label("loc_737")

    SetMapFlags(0x10)
    OP_11(0xE6, 0xF0, 0xFF, 0x0, 0x13880, 0x0)

    label("loc_74C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_77B")
    OP_A1(0x18, 0xB)
    SetChrPos(0x18, 56000, -3075, 35200, 0)
    OP_72(0xB, 0x4)
    OP_71(0xD, 0x4)
    Jump("loc_7E4")

    label("loc_77B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 0)), scpexpr(EXPR_END)), "loc_794")
    OP_71(0xB, 0x4)
    OP_71(0xC, 0x4)
    OP_71(0xD, 0x4)
    Jump("loc_7E4")

    label("loc_794")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 3)), scpexpr(EXPR_END)), "loc_7E4")
    OP_71(0xB, 0x4)
    OP_72(0xF, 0x4)
    OP_A1(0x18, 0xF)
    SetChrPos(0x18, 56000, -3075, 35200, 0)
    OP_72(0xC, 0x4)
    OP_A1(0x17, 0xC)
    SetChrPos(0x17, 55800, -3070, 35000, 0)
    OP_6F(0xF, 1)
    OP_70(0xF, 0x1)

    label("loc_7E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 0)), scpexpr(EXPR_END)), "loc_7EE")
    Jump("loc_7F9")

    label("loc_7EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_END)), "loc_7F9")
    OP_64(0x0, 0x1)

    label("loc_7F9")

    Return()

    # Function_1_6F8 end

    def Function_2_7FA(): pass

    label("Function_2_7FA")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_81F")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_961")

    label("loc_81F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_838")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_961")

    label("loc_838")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_851")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_961")

    label("loc_851")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_86A")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_961")

    label("loc_86A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_883")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_961")

    label("loc_883")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_89C")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_961")

    label("loc_89C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8B5")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_961")

    label("loc_8B5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8CE")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_961")

    label("loc_8CE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8E7")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_961")

    label("loc_8E7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_900")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_961")

    label("loc_900")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_919")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_961")

    label("loc_919")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_932")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_961")

    label("loc_932")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_94B")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_961")

    label("loc_94B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_961")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_961")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_976")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_961")

    label("loc_976")

    Return()

    # Function_2_7FA end

    def Function_3_977(): pass

    label("Function_3_977")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_99A")
    OP_8D(0xFE, 29021, 54795, 33637, 48557, 2000)
    Jump("Function_3_977")

    label("loc_99A")

    Return()

    # Function_3_977 end

    def Function_4_99B(): pass

    label("Function_4_99B")

    Call(0, 5)
    Return()

    # Function_4_99B end

    def Function_5_9A0(): pass

    label("Function_5_9A0")

    TalkBegin(0x14)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_E58")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x414, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B99")

    ChrTalk(    #0
        0x14,
        "呀，艾丝蒂尔和约修亚。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x14,
        "怎么，回来了吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x101,
        "#1000F嗯，好久不见。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x102,
        (
            "#1040F阿兰也\x01",
            "还和以前一样，没什么变化啊。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x14, 0x102, 400)

    ChrTalk(    #4
        0x14,
        (
            "很有精神嘛！\x01",
            "本来是想这么说……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x14,
        (
            "但定期船再这么停航下去的话，\x01",
            "实在让人受不了了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x101,
        (
            "#1007F是、是吗……\x02\x03",

            "对客人解释原因\x01",
            "也是阿兰的工作啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x102,
        "#1035F确实是个麻烦的工作啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x14,
        (
            "嗯，确实\x01",
            "很棘手…\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x14,
        (
            "世界上最痛苦的事情\x01",
            "就是没有女孩子可以欣赏！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x14,
        (
            "啊啊！！那可是我\x01",
            "唯一的乐趣啊！\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #11
        0x102,
        "#1048F完、完全没变啊。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x3)
    OP_A2(0x20A7)
    Jump("loc_E55")

    label("loc_B99")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_BFD")

    ChrTalk(    #12
        0x14,
        (
            "虽然向客人解释很累，\x01",
            "但要是没有客人就更累。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x14,
        (
            "欣赏漂亮女孩\x01",
            "是我在这里的唯一乐趣。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E55")

    label("loc_BFD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 5)), scpexpr(EXPR_END)), "loc_D4D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CF0")

    ChrTalk(    #14
        0x14,
        (
            "虽然维修员做过检查，\x01",
            "但却没有发现任何异常。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x14,
        (
            "这种时候唯一的精神安慰\x01",
            "就是看漂亮女孩了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x101,
        "#1019F（阿兰还是和平时一样……）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x14,
        (
            "啊，那里的女孩…\x01",
            "还蛮可爱的啊！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x14,
        (
            "……嗯，不过只能给７８分。\x01",
            "毕竟不是很完美。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_D4A")

    label("loc_CF0")


    ChrTalk(    #19
        0x14,
        (
            "那边的女孩……\x01",
            "还算可爱啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x14,
        (
            "……嗯，不过只能给７８分。\x01",
            "这种程度还是不能满足我。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D4A")

    Jump("loc_E55")

    label("loc_D4D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E05")

    ChrTalk(    #21
        0x14,
        (
            "现在停在飞船坪的是\x01",
            "『林德号』。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x14,
        (
            "在起飞前往王都之前\x01",
            "发生了那种现象。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x14,
        (
            "确保客人们的住宿，\x01",
            "也费了不少力气呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x14,
        (
            "最近总发生意外事件，\x01",
            "公社这边快忙不过来了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_E55")

    label("loc_E05")


    ChrTalk(    #25
        0x14,
        (
            "现在停在飞船坪的是\x01",
            "『林德号』。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x14,
        (
            "因为异变无法出航，\x01",
            "大家都要挤在这里。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E55")

    Jump("loc_19C6")

    label("loc_E58")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E6B")
    Call(0, 32)
    Jump("loc_19C6")

    label("loc_E6B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_END)), "loc_F2F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_EC2")

    ChrTalk(    #27
        0x14,
        (
            "我也打算过一阵子\x01",
            "就回去了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x14,
        (
            "在这种大雾之下\x01",
            "根本没法工作啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F2C")

    label("loc_EC2")


    ChrTalk(    #29
        0x14,
        (
            "上午来的客人\x01",
            "总算是回来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x14,
        (
            "我也打算过一阵子\x01",
            "就回去了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x14,
        (
            "在这种大雾之下\x01",
            "根本没法工作啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_F2C")

    Jump("loc_19C6")

    label("loc_F2F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 4)), scpexpr(EXPR_END)), "loc_FF2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_F7B")

    ChrTalk(    #32
        0x14,
        (
            "恢复航行的时间\x01",
            "还是没有决定下来！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x14,
        "十、十分抱歉！\x02",
    )

    CloseMessageWindow()
    Jump("loc_FEF")

    label("loc_F7B")


    ChrTalk(    #34
        0x14,
        (
            "十、十分抱歉！\x01",
            "定期船还没有恢复正常！！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x14,
        (
            "请、请各位\x01",
            "再耐心等等！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x14,
        (
            "我代表飞船公社\x01",
            "向大家诚恳道歉！！\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_FEF")

    Jump("loc_19C6")

    label("loc_FF2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 4)), scpexpr(EXPR_END)), "loc_17F8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x313, 2)), scpexpr(EXPR_END)), "loc_10B9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1060")

    ChrTalk(    #37
        0x14,
        (
            "王立学院的制服\x01",
            "果然看多少次也不腻。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x14,
        (
            "呀～～不能输给大雾，\x01",
            "我也要努力工作了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10B6")

    label("loc_1060")


    ChrTalk(    #39
        0x14,
        (
            "定期船停运的话，\x01",
            "也就没有女孩子可以欣赏了！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x14,
        (
            "……嗯～讨厌。\x01",
            "这可是大问题啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10B6")

    Jump("loc_17F5")

    label("loc_10B9")


    ChrTalk(    #41
        0x14,
        (
            "……７２分、８０分、７５分……\x01",
            "呼～今天的质量很一般嘛。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_127A")
    OP_62(0x14, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0x14, 0x105, 400)
    Sleep(1000)

    ChrTalk(    #42
        0x14,
        "嗯嗯，那长袜还有\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x14,
        "清纯的白色裙子…\x02",
    )

    CloseMessageWindow()
    OP_62(0x14, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #44
        0x14,
        (
            "噢噢！！这、这不就是\x01",
            "杰尼丝王立学院的制服吗！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x14,
        (
            "还有完全配得上制服\x01",
            "的出众气质！！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x14,
        (
            "太、太完美了！！！\x01",
            "绝对可以给１００分！！\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(400)

    ChrTalk(    #47
        0x105,
        "#542F那、那个……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x101,
        (
            "#1007F好啦，科洛丝都被你吓到了。\x02\x03",

            "#1019F……你还是一点也没变啊，阿兰。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_1685")

    label("loc_127A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1293")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1358")

    label("loc_1293")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12AC")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1358")

    label("loc_12AC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12C5")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1358")

    label("loc_12C5")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12DE")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1358")

    label("loc_12DE")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12F7")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1358")

    label("loc_12F7")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1310")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1358")

    label("loc_1310")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1329")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1358")

    label("loc_1329")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1342")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1358")

    label("loc_1342")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1358")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1358")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_END)),
        (2, "loc_136D"),
        (6, "loc_1466"),
        (0, "loc_1599"),
        (SWITCH_DEFAULT, "loc_1685"),
    )


    label("loc_136D")

    OP_62(0x14, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    TurnDirection(0x14, 0x103, 400)
    Sleep(1000)

    ChrTalk(    #49
        0x14,
        (
            "噢噢！这种大胆的装扮……\x01",
            "充满魔性吸引力……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x14,
        (
            "还有魅惑力十足\x01",
            "却不低俗的气质。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x14,
        "可以给９７分！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x103,
        "#526F哎呀，不是１００分吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x14,
        "哈哈，哪有那么简单就给满分。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x101,
        "#1019F你还是一点也没变啊，阿兰。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1685")

    label("loc_1466")

    OP_62(0x14, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    TurnDirection(0x14, 0x107, 400)
    Sleep(1000)

    ChrTalk(    #55
        0x14,
        (
            "嗯，那金色的头发，\x01",
            "还有让人可以联想到夏日海洋的眼睛…\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x14,
        (
            "虽然还没有发育完全，\x01",
            "不过确实有种说不出的魅力。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x14,
        (
            "嗯，现在可以打８０分，\x01",
            "不过将来还是很有发展前途的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x107,
        "#065F啊、啊啊啊……！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x101,
        (
            "#1007F好啦！提妲都\x01",
            "被你吓到了！\x02\x03",

            "#1019F你还是一点也没变啊，阿兰。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1685")

    label("loc_1599")

    OP_62(0x14, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    TurnDirection(0x14, 0x101, 400)
    Sleep(1000)

    ChrTalk(    #60
        0x14,
        (
            "啊，这修长的美腿……\x01",
            "清纯的服装……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x14,
        (
            "虽然欠缺女人的魅力，\x01",
            "但这也正是年轻女孩的健康美啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x14,
        "嗯，这样的话，可以给９０分！\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(400)

    ChrTalk(    #63
        0x101,
        "#1019F你还是一点也没变啊，阿兰。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1685")

    label("loc_1685")

    TurnDirection(0x14, 0x101, 400)

    ChrTalk(    #64
        0x14,
        (
            "呀，欢迎回家，艾丝蒂尔。\x01",
            "很有潜力呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x14,
        (
            "嗯，成长下去的话，\x01",
            "将来一定会更完美的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x101,
        (
            "#1007F你还有力气说这种轻浮的话吗？\x02\x03",

            "定期船停运了，\x01",
            "现在的状况可是很紧张啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x14,
        (
            "哈哈哈～\x01",
            "别这么说嘛，艾丝蒂尔。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x14,
        (
            "这也是保持工作\x01",
            "精力的秘诀之一呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x14,
        (
            "不过，这雾\x01",
            "还真是讨厌啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x14,
        (
            "拜它所赐，\x01",
            "一个女孩也看不见了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x101,
        "#1019F……最后总算是安定下来了啊。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x189A)
    ClearChrFlags(0x14, 0x10)

    label("loc_17F5")

    Jump("loc_19C6")

    label("loc_17F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 3)), scpexpr(EXPR_END)), "loc_19C6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x204, 7)), scpexpr(EXPR_END)), "loc_1861")

    ChrTalk(    #72
        0x14,
        (
            "参加女王诞辰庆典的人们\x01",
            "也终于都安顿下来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x14,
        (
            "洛连特又回到\x01",
            "平时的正常生活了呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_19C6")

    label("loc_1861")


    ChrTalk(    #74
        0x14,
        (
            "……９０分、７０分、８４分……\x01",
            "呼呼～今天还算不错……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x14, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    TurnDirection(0x14, 0x101, 400)
    Sleep(600)

    ChrTalk(    #75
        0x14,
        (
            "啊，栗色头发……\x01",
            "还有那清澈的眼神……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x14,
        (
            "虽然充满活力，\x01",
            "但还是缺少女性的魅力啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0x14,
        "嗯，给８２分好了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0x101,
        "#509F……谁是８２分啊！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x14,
        (
            "……什么啊，仔细一看，\x01",
            "这不是艾丝蒂尔吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0x14,
        "好久不见呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0x101,
        (
            "#007F你在说什么啊，\x01",
            "还真是一点都没变呢，阿兰……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1027)

    label("loc_19C6")

    TalkEnd(0x14)
    Return()

    # Function_5_9A0 end

    def Function_6_19CA(): pass

    label("Function_6_19CA")

    TalkBegin(0x1A)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 5)), scpexpr(EXPR_END)), "loc_1A27")

    ChrTalk(    #82
        0xFE,
        (
            "虽然已经检查过好几次，\x01",
            "但哪里也没发现异常。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0xFE,
        (
            "果然原因还是\x01",
            "因为异变吗。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1CF2")

    label("loc_1A27")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1A76")

    ChrTalk(    #84
        0xFE,
        "引擎没问题，\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0xFE,
        (
            "也没有发现其他什么异常……\x01",
            "究竟是怎么回事呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1CF2")

    label("loc_1A76")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 0)), scpexpr(EXPR_END)), "loc_1AC9")

    ChrTalk(    #86
        0xFE,
        "乘船手续已经办好了吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0xFE,
        (
            "要想乘坐定期船的话，\x01",
            "就来这里办手续吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1CF2")

    label("loc_1AC9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_END)), "loc_1B24")

    ChrTalk(    #88
        0xFE,
        (
            "本以为今天雾就会散去了，\x01",
            "都打算准备开始工作了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0xFE,
        "嗯，看来还是不行啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1CF2")

    label("loc_1B24")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 4)), scpexpr(EXPR_END)), "loc_1B93")

    ChrTalk(    #90
        0xFE,
        (
            "林德号\x01",
            "在洛连特之外的４座城市\x01",
            "往返飞行。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0xFE,
        (
            "这样的飞行方式，\x01",
            "自之前的空贼事件之后可是首次啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1CF2")

    label("loc_1B93")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 4)), scpexpr(EXPR_END)), "loc_1CA1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1BFC")

    ChrTalk(    #92
        0xFE,
        (
            "刚才的着陆\x01",
            "真是吓了我一跳。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0xFE,
        (
            "能在那种状况下成功着陆，\x01",
            "佩特洛夫船长真了不起啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C9E")

    label("loc_1BFC")


    ChrTalk(    #94
        0xFE,
        (
            "呼～定期船的着陆\x01",
            "真是吓了我一跳。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0xFE,
        (
            "虽然进行了引导，\x01",
            "但毕竟视线实在太差了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0xFE,
        (
            "能在那种状况下成功着陆，\x01",
            "佩特洛夫船长真了不起啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0xFE,
        "真是很危险呢。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_1C9E")

    Jump("loc_1CF2")

    label("loc_1CA1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 3)), scpexpr(EXPR_END)), "loc_1CF2")

    ChrTalk(    #98
        0xFE,
        (
            "王都来的林德号\x01",
            "就要到达了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0xFE,
        (
            "为了避免发生事故，\x01",
            "要好好准备一下。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1CF2")

    TalkEnd(0x1A)
    Return()

    # Function_6_19CA end

    def Function_7_1CF6(): pass

    label("Function_7_1CF6")

    TalkBegin(0x1B)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 5)), scpexpr(EXPR_END)), "loc_1DF3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D9A")

    ChrTalk(    #100
        0xFE,
        (
            "听说军队的警备艇\x01",
            "也在附近迫降了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0xFE,
        (
            "导力停止现象\x01",
            "发生在整个王国…\x01",
            "看来传闻果然是真的呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0xFE,
        (
            "这个怎么办才好，\x01",
            "难道我们要失业了吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_1DF0")

    label("loc_1D9A")


    ChrTalk(    #103
        0xFE,
        (
            "听说军队的警备艇\x01",
            "也在附近迫降了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0xFE,
        (
            "这种现象似乎真的\x01",
            "已经覆盖到整个王国了呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1DF0")

    Jump("loc_218B")

    label("loc_1DF3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1EBA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E69")

    ChrTalk(    #105
        0xFE,
        (
            "可恶…\x01",
            "到底是哪里出了问题呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0xFE,
        (
            "『林德号』的装置部分\x01",
            "很正常。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0xFE,
        (
            "其他零件也\x01",
            "没有问题。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_1EB7")

    label("loc_1E69")


    ChrTalk(    #108
        0xFE,
        (
            "可恶…\x01",
            "究竟是哪里出了问题呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0xFE,
        (
            "为什么『林德号』\x01",
            "的引擎无法运转了呢？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1EB7")

    Jump("loc_218B")

    label("loc_1EBA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 0)), scpexpr(EXPR_END)), "loc_1F7C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1F0B")

    ChrTalk(    #110
        0xFE,
        (
            "赛希莉亚号\x01",
            "似乎也是一样呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0xFE,
        (
            "难道是因为\x01",
            "引擎过热了吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F79")

    label("loc_1F0B")


    ChrTalk(    #112
        0xFE,
        (
            "嘿嘿，航行终于再开始了，\x01",
            "接下来又要忙了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0xFE,
        (
            "赛希莉亚号\x01",
            "似乎也是一样呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0xFE,
        (
            "今天也要努力\x01",
            "起飞啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_1F79")

    Jump("loc_218B")

    label("loc_1F7C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_END)), "loc_1FE0")

    ChrTalk(    #115
        0xFE,
        (
            "赛希莉亚号\x01",
            "已经准备完毕了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0xFE,
        (
            "雾如果还是那么厉害的话，\x01",
            "今天也准备撤销出航计划了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_218B")

    label("loc_1FE0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 4)), scpexpr(EXPR_END)), "loc_2021")

    ChrTalk(    #117
        0xFE,
        "阿兰那里也很忙。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0xFE,
        (
            "一直要向乘客们\x01",
            "拼命解释啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_218B")

    label("loc_2021")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 4)), scpexpr(EXPR_END)), "loc_2134")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2084")

    ChrTalk(    #119
        0xFE,
        (
            "管制塔、我们整备屋，\x01",
            "还有定期船……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0xFE,
        (
            "只有三者协力\x01",
            "才能让飞船坪正常运营。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2131")

    label("loc_2084")


    ChrTalk(    #121
        0xFE,
        (
            "定期船的着陆\x01",
            "需要大家齐心协力。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0xFE,
        (
            "管制塔、我们整备屋，\x01",
            "还有定期船……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0xFE,
        (
            "那样的话，\x01",
            "工作就可以顺利完成。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0xFE,
        (
            "没有我们完美配合的话，\x01",
            "很难在这种恶劣条件下着陆。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_2131")

    Jump("loc_218B")

    label("loc_2134")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 3)), scpexpr(EXPR_END)), "loc_218B")

    ChrTalk(    #125
        0xFE,
        (
            "想看一看传闻中\x01",
            "王室的埃尔赛尤号。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0xFE,
        (
            "不过，它一般也不会\x01",
            "在洛连特着陆的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_218B")

    TalkEnd(0x1B)
    Return()

    # Function_7_1CF6 end

    def Function_8_218F(): pass

    label("Function_8_218F")

    TalkBegin(0x1C)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 4)), scpexpr(EXPR_END)), "loc_21E5")

    ChrTalk(    #127
        0xFE,
        "定期船今天还是不行吗……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0xFE,
        (
            "昨天的雾那么大，\x01",
            "这也是没办法的事吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2248")

    label("loc_21E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 4)), scpexpr(EXPR_END)), "loc_2248")

    ChrTalk(    #129
        0xFE,
        (
            "真是让人没办法啊……\x01",
            "即使降落在洛连特也很麻烦啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0xFE,
        (
            "呼～本来还要去哈肯大门\x01",
            "参观呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2248")

    TalkEnd(0x1C)
    Return()

    # Function_8_218F end

    def Function_9_224C(): pass

    label("Function_9_224C")

    TalkBegin(0x1D)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 4)), scpexpr(EXPR_END)), "loc_234C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_22B0")

    ChrTalk(    #131
        0xFE,
        (
            "虽然在洛连特\x01",
            "也有想去的地方…\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0xFE,
        (
            "但雾这么大，摄影旅行的话\x01",
            "根本不可能啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_234C")

    label("loc_22B0")


    ChrTalk(    #133
        0xFE,
        (
            "虽然在洛连特\x01",
            "也有想去的地方…\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0xFE,
        (
            "但雾这么大，摄影旅行的话\x01",
            "根本不可能啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0xFE,
        (
            "但要一直只在旅馆休息的话，\x01",
            "未免太让人不爽了…\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0xFE,
        "……嗯，真头疼。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_234C")

    TalkEnd(0x1D)
    Return()

    # Function_9_224C end

    def Function_10_2350(): pass

    label("Function_10_2350")

    TalkBegin(0x25)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 4)), scpexpr(EXPR_END)), "loc_23A6")

    ChrTalk(    #137
        0xFE,
        (
            "啊，本来是想\x01",
            "要去柏斯的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0xFE,
        (
            "连、连自然现象\x01",
            "都要妨碍我的人生吗？！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_23A6")

    TalkEnd(0x25)
    Return()

    # Function_10_2350 end

    def Function_11_23AA(): pass

    label("Function_11_23AA")

    TalkBegin(0x26)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 4)), scpexpr(EXPR_END)), "loc_2486")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_240A")

    ChrTalk(    #139
        0xFE,
        (
            "安敦…\x01",
            "怨天尤人是没有用的喔。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0xFE,
        (
            "不管怎样，先去协会\x01",
            "试着商谈一下吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2486")

    label("loc_240A")


    ChrTalk(    #141
        0xFE,
        (
            "安敦…\x01",
            "怨天尤人是没有用的喔。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0xFE,
        (
            "不管怎样，先去协会\x01",
            "试着商谈一下吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0xFE,
        (
            "如果可能的话，\x01",
            "也许可以走陆路去柏斯呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xB)

    label("loc_2486")

    TalkEnd(0x26)
    Return()

    # Function_11_23AA end

    def Function_12_248A(): pass

    label("Function_12_248A")

    TalkBegin(0x1E)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 4)), scpexpr(EXPR_END)), "loc_24C1")

    ChrTalk(    #144
        0xFE,
        (
            "嗯，真麻烦啊。\x01",
            "定期船还没有恢复正常吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_24C1")

    TalkEnd(0x1E)
    Return()

    # Function_12_248A end

    def Function_13_24C5(): pass

    label("Function_13_24C5")

    TalkBegin(0x1F)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 4)), scpexpr(EXPR_END)), "loc_25B6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_2526")

    ChrTalk(    #145
        0xFE,
        "定期船看起来还是不行啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #146
        0xFE,
        (
            "没办法，在城里随便看看，\x01",
            "然后再回旅馆吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_25B6")

    label("loc_2526")


    ChrTalk(    #147
        0xFE,
        "定期船看起来还是不行啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0xFE,
        (
            "没办法，死心了，\x01",
            "回旅馆吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0xFE,
        (
            "啊，不过在那之前\x01",
            "还是想在城里逛逛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #150
        0xFE,
        (
            "也许会找到不错\x01",
            "的店也说不定啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)

    label("loc_25B6")

    TalkEnd(0x1F)
    Return()

    # Function_13_24C5 end

    def Function_14_25BA(): pass

    label("Function_14_25BA")

    TalkBegin(0x20)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 4)), scpexpr(EXPR_END)), "loc_2636")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_25EF")

    ChrTalk(    #151
        0xFE,
        (
            "唉，死心了，\x01",
            "今天也不行吗。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2636")

    label("loc_25EF")


    ChrTalk(    #152
        0xFE,
        (
            "唉，死心了，\x01",
            "今天也不行吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0xFE,
        (
            "呼～还要再和妻子\x01",
            "联络一次啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x6)

    label("loc_2636")

    TalkEnd(0x20)
    Return()

    # Function_14_25BA end

    def Function_15_263A(): pass

    label("Function_15_263A")

    TalkBegin(0x21)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_END)), "loc_2726")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_26A2")

    ChrTalk(    #154
        0xFE,
        (
            "嗯，飞船的乘客\x01",
            "也增多了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #155
        0xFE,
        (
            "虽然明白您的心情，\x01",
            "不过现在还是先待在旅馆吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2726")

    label("loc_26A2")


    ChrTalk(    #156
        0xFE,
        (
            "嗯，飞船的乘客\x01",
            "也增多了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #157
        0xFE,
        (
            "虽然明白您的心情，\x01",
            "不过现在还是先待在旅馆吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #158
        0xFE,
        (
            "轻易外出的话，\x01",
            "警备工作的负担会加重的。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x7)

    label("loc_2726")

    TalkEnd(0x21)
    Return()

    # Function_15_263A end

    def Function_16_272A(): pass

    label("Function_16_272A")

    TalkBegin(0x22)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 5)), scpexpr(EXPR_END)), "loc_288B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_27FD")

    ChrTalk(    #159
        0xFE,
        (
            "对引擎进行了检查，\x01",
            "没发现任何毛病。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #160
        0xFE,
        (
            "果然是全国性质\x01",
            "的大异变啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #161
        0xFE,
        (
            "失去导力的话，\x01",
            "我们就不能再次飞行了，\x01",
            "只能在陆地上行走。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #162
        0xFE,
        (
            "不知从何时开始，\x01",
            "我们似乎就忘记了自身的力量。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x8)
    Jump("loc_2888")

    label("loc_27FD")


    ChrTalk(    #163
        0xFE,
        (
            "失去导力之后\x01",
            "我们就变得不知所措。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #164
        0xFE,
        (
            "…不但无法在天空飞行，\x01",
            "连在陆地上行走都有问题。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #165
        0xFE,
        (
            "不过，我们自身的能力\x01",
            "本来不就是如此的吗。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2888")

    Jump("loc_29AE")

    label("loc_288B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_29AE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_294C")

    ChrTalk(    #166
        0xFE,
        (
            "导力引擎为什么无法发动，\x01",
            "原因还在调查中。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #167
        0xFE,
        (
            "有家人的成员很着急地\x01",
            "回王都了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #168
        0xFE,
        (
            "导力突然消失，\x01",
            "对我们来说完全是未知现象啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #169
        0xFE,
        (
            "解决这些异变\x01",
            "大概还要花些时间吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x8)
    Jump("loc_29AE")

    label("loc_294C")


    ChrTalk(    #170
        0xFE,
        (
            "导力引擎为什么无法发动，\x01",
            "原因还在调查中。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #171
        0xFE,
        (
            "就算原因解明了，\x01",
            "重新恢复航运也需要一些时间。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_29AE")

    TalkEnd(0x22)
    Return()

    # Function_16_272A end

    def Function_17_29B2(): pass

    label("Function_17_29B2")

    TalkBegin(0x23)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 5)), scpexpr(EXPR_END)), "loc_2A40")

    ChrTalk(    #172
        0xFE,
        (
            "定期船的恢复工作\x01",
            "现在还没有头绪啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #173
        0xFE,
        (
            "虽然很遗憾，\x01",
            "但也是没有办法的事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #174
        0xFE,
        (
            "引擎为什么停止运转，\x01",
            "其原因现在还不得而知。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B42")

    label("loc_2A40")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_2B42")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2AE5")

    ChrTalk(    #175
        0xFE,
        (
            "虽然航行停止\x01",
            "给客人们带来不少麻烦……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #176
        0xFE,
        (
            "但至少没有人员伤亡，\x01",
            "就算是幸运的了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #177
        0xFE,
        (
            "如果是在起飞后\x01",
            "引擎才停止运转…\x01",
            "那后果就不堪设想了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x9)
    Jump("loc_2B42")

    label("loc_2AE5")


    ChrTalk(    #178
        0xFE,
        (
            "总之，客人们\x01",
            "就算是幸运的了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #179
        0xFE,
        (
            "如果是在起飞后\x01",
            "引擎才停止运转…\x01",
            "那后果就不堪设想了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B42")

    TalkEnd(0x23)
    Return()

    # Function_17_29B2 end

    def Function_18_2B46(): pass

    label("Function_18_2B46")

    TalkBegin(0x24)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 5)), scpexpr(EXPR_END)), "loc_2BAF")

    ChrTalk(    #180
        0xFE,
        (
            "船上也没有\x01",
            "发现什么异常啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #181
        0xFE,
        (
            "整备屋的人真可怜，\x01",
            "……大家全都一筹莫展，抱头呻吟着。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D04")

    label("loc_2BAF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_2D04")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C9F")

    ChrTalk(    #182
        0xFE,
        (
            "真奇怪…\x01",
            "这样的情况还是第一次见。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #183
        0xFE,
        (
            "一般情况下，出现故障\x01",
            "之前都会有相应的反应。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #184
        0xFE,
        (
            "比如装置部分异常加热、\x01",
            "船体振动之类的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #185
        0xFE,
        (
            "但这次却没有发生\x01",
            "任何不正常的状况。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #186
        0xFE,
        (
            "真是太突然了。\x01",
            "突然之间，引擎就停止了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xA)
    Jump("loc_2D04")

    label("loc_2C9F")


    ChrTalk(    #187
        0xFE,
        (
            "这次的故障完全\x01",
            "没有任何前兆。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #188
        0xFE,
        (
            "我当时也是\x01",
            "完全不敢相信。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #189
        0xFE,
        (
            "出力针的指数\x01",
            "瞬间就滑到了０。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D04")

    TalkEnd(0x24)
    Return()

    # Function_18_2B46 end

    def Function_19_2D08(): pass

    label("Function_19_2D08")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 5)), scpexpr(EXPR_END)), "loc_2E04")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D88")

    ChrTalk(    #190
        0xFE,
        (
            "呼，可也不能\x01",
            "一直待在洛连特呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #191
        0xFE,
        (
            "虽然也想过走陆路\x01",
            "回去，可是……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #192
        0xFE,
        "呼～果然还是太麻烦了啊。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x5)
    Jump("loc_2E01")

    label("loc_2D88")


    ChrTalk(    #193
        0xFE,
        (
            "啊，可是走陆路回去的话\x01",
            "还是太危险了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #194
        0xFE,
        (
            "要是遇到魔兽的话…\x01",
            "后悔也来不及了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #195
        0xFE,
        (
            "所以还是老老实实\x01",
            "等飞船恢复吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E01")

    Jump("loc_2E42")

    label("loc_2E04")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_2E42")

    ChrTalk(    #196
        0xFE,
        (
            "呼～今天\x01",
            "飞船还是不行吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #197
        0xFE,
        "唉，早已经想到了。\x02",
    )

    CloseMessageWindow()

    label("loc_2E42")

    TalkEnd(0xFE)
    Return()

    # Function_19_2D08 end

    def Function_20_2E46(): pass

    label("Function_20_2E46")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 5)), scpexpr(EXPR_END)), "loc_2EC0")

    ChrTalk(    #198
        0xFE,
        (
            "恢复时间还不知道。\x01",
            "故障的原因也不清楚。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #199
        0xFE,
        (
            "那种话\x01",
            "我也会说啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #200
        0xFE,
        (
            "那些工作人员\x01",
            "真的在认真工作吗？！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2F3E")

    label("loc_2EC0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_2F3E")

    ChrTalk(    #201
        0xFE,
        (
            "那种不负责任的话\x01",
            "真是听够了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #202
        0xFE,
        (
            "哪怕是说谎也好，\x01",
            "我也希望听到一些明确的答复。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #203
        0xFE,
        (
            "那？明白了吧？\x01",
            "我想说的话。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F3E")

    TalkEnd(0xFE)
    Return()

    # Function_20_2E46 end

    def Function_21_2F42(): pass

    label("Function_21_2F42")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    ClearMapFlags(0x1)
    OP_11(0xA4, 0xB7, 0xFF, 0xA7F8, 0x493E0, 0x0)
    OP_71(0xA, 0x4)
    OP_71(0xB, 0x4)
    OP_72(0xF, 0x4)
    OP_72(0xC, 0x4)
    OP_A1(0x18, 0xF)
    SetChrPos(0x18, 55700, -300, 35000, 0)
    OP_A1(0x17, 0xC)
    SetChrPos(0x17, 55800, -1000, 35000, 0)
    SetChrFlags(0x18, 0x4)
    SetChrFlags(0x17, 0x4)
    ClearMapFlags(0x2000000)
    OP_6D(47960, 26950, 30490, 0)
    OP_67(0, 27020, -10000, 0)
    OP_6B(2480, 0)
    OP_6C(62000, 0)
    OP_6E(262, 0)
    OP_22(0x79, 0x0, 0x64)
    OP_C8(0x200, 0x46, "C_PLAC00._CH", 0x1, 0xBB8)
    FadeToBright(3000, 0)
    OP_6F(0xD, 200)
    OP_70(0xD, 0xC8)
    StopSound(0xA7F8, 0x3D090, 0x2710)

    def lambda_3033():
        OP_6D(53380, 4050, 31110, 10000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3033)

    def lambda_304B():
        OP_67(0, 9500, -10000, 10000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_304B)

    def lambda_3063():
        OP_6B(3300, 10000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3063)

    def lambda_3073():
        OP_6C(65000, 10000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_3073)

    def lambda_3083():
        OP_91(0xFE, 0x0, 0xFFFFF441, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 0, lambda_3083)

    def lambda_309E():
        OP_91(0xFE, 0x0, 0xFFFFF829, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 0, lambda_309E)
    OP_6F(0xF, 130)
    WaitChrThread(0x18, 0x0)
    OP_23(0x79)
    OP_22(0xC8, 0x0, 0x64)
    OP_7C(0x0, 0xC8, 0xBB8, 0x12C)
    Sleep(1000)
    OP_B0(0xF, 0x32)
    OP_6F(0xF, 130)
    OP_70(0xF, 0x1)
    Sleep(900)
    OP_22(0x76, 0x0, 0x46)
    OP_73(0xF)
    Sleep(400)
    OP_22(0x78, 0x0, 0x64)
    OP_B0(0xD, 0x64)
    OP_6F(0xD, 200)
    OP_70(0xD, 0x0)
    OP_73(0xD)
    Sleep(1000)
    OP_22(0x6, 0x0, 0x64)
    OP_6F(0xF, 411)
    OP_70(0xF, 0x1C2)
    OP_22(0x6, 0x0, 0x64)
    OP_73(0xF)
    Sleep(300)
    OP_43(0x8, 0x1, 0x0, 0x16)
    OP_43(0x9, 0x1, 0x0, 0x17)
    Sleep(1000)
    OP_43(0xA, 0x1, 0x0, 0x16)
    Sleep(1000)
    OP_43(0xB, 0x1, 0x0, 0x16)
    OP_43(0xC, 0x1, 0x0, 0x17)
    Sleep(500)
    OP_43(0xD, 0x1, 0x0, 0x16)
    Sleep(1000)
    OP_43(0xE, 0x1, 0x0, 0x17)
    Sleep(500)
    Sleep(1000)
    OP_43(0xF, 0x1, 0x0, 0x16)
    Sleep(3000)
    SetChrFlags(0x101, 0x40)
    SetChrFlags(0x15, 0x40)
    ClearChrFlags(0x101, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x15, 0x4)
    SetChrBattleFlags(0x101, 0x20)
    SetChrBattleFlags(0x15, 0x20)
    OP_48()
    OP_89(0x101, 55990, 4230, 34970, 6)
    OP_89(0x15, 55990, 4230, 34970, 6)

    def lambda_31EC():
        OP_8E(0x101, 0xD8E0, 0x1022, 0x7CEC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_31EC)
    Sleep(1000)

    def lambda_320C():
        OP_8E(0x15, 0xD9B2, 0x1022, 0x8106, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 0, lambda_320C)
    WaitChrThread(0x101, 0x0)

    def lambda_322C():
        OP_8E(0x101, 0xCD28, 0x1022, 0x78E6, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_322C)
    WaitChrThread(0x15, 0x0)

    def lambda_324C():
        OP_8E(0x15, 0xCD28, 0x1022, 0x78E6, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 0, lambda_324C)
    WaitChrThread(0x101, 0x0)

    def lambda_326C():
        OP_8E(0x101, 0xA456, 0xFA0, 0x7A4E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_326C)
    WaitChrThread(0x15, 0x0)

    def lambda_328C():
        OP_8E(0x15, 0xA9A6, 0xFA0, 0x78FA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 0, lambda_328C)
    ClearChrFlags(0x101, 0x4)
    Sleep(1000)
    ClearChrFlags(0x15, 0x4)
    Sleep(1000)
    Fade(500)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    OP_6D(42990, 4000, 31290, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3300, 0)
    OP_6C(57000, 0)
    OP_6E(200, 0)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x15, 0x0)
    OP_0D()
    Sleep(500)
    OP_8C(0x15, 225, 500)
    Sleep(500)

    ChrTalk(    #204
        0x15,
        (
            "#1061F哈～这里就是洛连特吗？\x02\x03",

            "呵呵，老实说，\x01",
            "飞船坪之外的地方简直就像是乡村啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 120, 500)

    ChrTalk(    #205
        0x101,
        (
            "#007F#3P不好意思啊，本来就是乡村城镇。\x02\x03",

            "#509F不过事先告诉你，\x01",
            "这里也是有礼拜堂的哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x15, 270, 500)

    ChrTalk(    #206
        0x15,
        (
            "#1062F那、那过一会儿我去和\x01",
            "教区长打个招呼吧。\x02\x03",

            "对了，艾丝蒂尔的家\x01",
            "在哪里？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #207
        0x101,
        (
            "#505F#3P都说了嘛……\x01",
            "没必要送我回家了。\x02\x03",

            "出城之后走一会儿就可以到。\x01",
            "而且，毕竟我也是个游击士。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #208
        0x15,
        (
            "#1061F哈哈～～不用客气啊，\x01",
            "送女士回家也是男人的义务。\x02\x03",

            "#1060F而且我也好想见见\x01",
            "你那位引以为傲的男朋友呀～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #209
        0x101,
        (
            "#503F#3P男朋友……\x01",
            "也不能说是男朋友啦…\x02\x03",

            "#008F呼！不管了！！\x01",
            "那就先到我家喝杯茶吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #210
        0x15,
        (
            "#1061FＴｈａｎｋ　ｙｏｕ！\x01",
            "那就请带路吧～\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(500)
    OP_72(0xA, 0x4)
    OP_6D(42190, 4000, 31180, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3300, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    AddParty(0x41, 0xFF, 0xFF)
    SetChrPos(0x101, 42190, 4000, 31180, 0)
    SetChrPos(0x142, 42190, 4000, 31180, 0)
    OP_A2(0x1003)
    ClearChrFlags(0x101, 0x2)
    ClearChrFlags(0x101, 0x40)
    ClearChrFlags(0x101, 0x4)
    SetChrFlags(0x15, 0x80)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_21_2F42 end

    def Function_22_363D(): pass

    label("Function_22_363D")

    SetChrFlags(0xFE, 0x40)
    ClearChrFlags(0xFE, 0x80)
    ClearChrFlags(0xFE, 0x4)
    SetChrBattleFlags(0xFE, 0x20)
    OP_89(0xFE, 55680, 3890, 35740, 0)
    OP_8E(0xFE, 0xD9C6, 0x105E, 0x795E, 0x7D0, 0x0)
    OP_8C(0xFE, 270, 0)
    OP_8F(0xFE, 0xAA0A, 0xF5A, 0x7670, 0x7D0, 0x0)
    Sleep(2000)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_22_363D end

    def Function_23_369C(): pass

    label("Function_23_369C")

    SetChrFlags(0xFE, 0x40)
    ClearChrFlags(0xFE, 0x80)
    ClearChrFlags(0xFE, 0x4)
    SetChrBattleFlags(0xFE, 0x20)
    OP_89(0xFE, 52970, 4293, 42260, 357)
    OP_8E(0xFE, 0xCEFE, 0x1022, 0x7B02, 0x7D0, 0x0)
    OP_8E(0xFE, 0xA820, 0xFA0, 0x7A76, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_23_369C end

    def Function_24_36EF(): pass

    label("Function_24_36EF")

    EventBegin(0x0)
    SetMapFlags(0x10)
    OP_11(0xE6, 0xF0, 0xFF, 0x0, 0x13880, 0x0)
    OP_6D(51650, -3070, 39040, 0)
    OP_67(0, 16810, -10000, 0)
    OP_6B(3130, 0)
    OP_6C(135000, 0)
    OP_6E(540, 0)
    SetChrFlags(0x0, 0x80)
    OP_72(0xF, 0x20)
    OP_72(0xC, 0x4)
    OP_6F(0xF, 60)
    OP_70(0xF, 0x3C)
    OP_6F(0xE, 0)
    OP_6F(0xD, 200)
    SetChrFlags(0x18, 0x4)
    SetChrFlags(0x17, 0x4)
    OP_A1(0x18, 0xF)
    SetChrPos(0x18, 55800, 15000, 35000, 0)
    OP_A1(0x17, 0xC)
    SetChrPos(0x17, 55800, 10000, 35000, 0)
    AddParty(0x2, 0xF7, 0xFF)
    AddParty(0x5, 0xF8, 0xFF)
    AddParty(0x6, 0xF9, 0xFF)
    AddParty(0x3, 0xFA, 0xFF)
    AddParty(0x4, 0xFB, 0xFF)
    AddParty(0x7, 0xFC, 0xFF)
    OP_22(0x79, 0x0, 0x64)
    OP_71(0x0, 0x20)
    OP_71(0x1, 0x20)
    OP_71(0x2, 0x20)
    OP_71(0x3, 0x20)
    OP_71(0x4, 0x20)
    OP_71(0x5, 0x20)
    OP_71(0x7, 0x20)
    OP_71(0x8, 0x20)
    OP_71(0x9, 0x20)
    OP_6F(0x0, 0)
    OP_70(0x0, 0x2D0)
    OP_6F(0x1, 0)
    OP_70(0x1, 0x2D0)
    OP_6F(0x2, 0)
    OP_70(0x2, 0x2D0)
    OP_6F(0x3, 0)
    OP_70(0x3, 0x2D0)
    OP_6F(0x4, 0)
    OP_70(0x4, 0x2D0)
    OP_6F(0x5, 0)
    OP_70(0x5, 0x2D0)
    OP_6F(0x7, 0)
    OP_70(0x7, 0x2D0)
    OP_6F(0x8, 0)
    OP_70(0x8, 0x2D0)
    OP_6F(0x9, 0)
    OP_70(0x9, 0x2D0)

    def lambda_3872():
        OP_6D(51760, -3070, 40830, 10000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3872)

    def lambda_388A():
        OP_6C(45000, 10000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_388A)

    def lambda_389A():
        OP_8F(0xFE, 0xD9F8, 0xFFFFF448, 0x88B8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_389A)

    def lambda_38B5():
        OP_8F(0xFE, 0xD9F8, 0x0, 0x88B8, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_38B5)
    OP_C8(0x200, 0x46, "C_PLAC00._CH", 0x1, 0x3E8)
    FadeToBright(1000, 0)
    OP_22(0xE2, 0x0, 0x64)
    WaitChrThread(0x18, 0x1)

    def lambda_38F8():
        OP_8F(0xFE, 0xD9F8, 0xFFFFFC18, 0x88B8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_38F8)
    WaitChrThread(0x18, 0x1)

    def lambda_3918():
        OP_8F(0xFE, 0xD9F8, 0xFFFFF448, 0x88B8, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_3918)
    WaitChrThread(0x18, 0x1)
    OP_23(0x79)
    OP_22(0xC8, 0x0, 0x64)
    OP_7C(0x0, 0xC8, 0xBB8, 0x12C)
    Sleep(1000)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x101, 0x1)
    OP_22(0x76, 0x0, 0x46)
    OP_B0(0xF, 0x3C)
    OP_6F(0xF, 60)
    OP_70(0xF, 0x1)
    OP_73(0xF)
    OP_22(0x78, 0x0, 0x64)
    OP_B0(0xD, 0x64)
    OP_6F(0xD, 200)
    OP_70(0xD, 0x0)
    OP_73(0xD)
    Sleep(1000)
    OP_23(0x79)
    Fade(1000)
    OP_6D(55840, 4200, 32009, 0)
    OP_67(0, 7250, -10000, 0)
    OP_6B(2940, 0)
    OP_6C(29000, 0)
    OP_6E(262, 0)
    OP_0D()
    OP_22(0x6, 0x0, 0x64)
    OP_6F(0xF, 411)
    OP_70(0xF, 0x1C2)
    OP_73(0xF)
    OP_43(0x101, 0x0, 0x0, 0x19)
    Sleep(500)
    OP_43(0x107, 0x0, 0x0, 0x1C)
    Sleep(300)
    OP_43(0x106, 0x0, 0x0, 0x1B)
    Sleep(500)
    OP_43(0x103, 0x0, 0x0, 0x1A)
    Sleep(500)
    OP_43(0x104, 0x0, 0x0, 0x1D)
    Sleep(500)
    OP_43(0x105, 0x0, 0x0, 0x1E)
    Sleep(500)
    OP_43(0x108, 0x0, 0x0, 0x1F)
    Sleep(500)
    WaitChrThread(0x108, 0x0)

    ChrTalk(    #211
        0x101,
        "#1020F哇……一片白啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #212
        0x107,
        (
            "#065F#6P啊……\x01",
            "什么都看不见了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #213
        0x105,
        (
            "#043F#1P雾散去之前，\x01",
            "定期船是无法出航了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #214
        0x103,
        "#026F#5P嗯……\x02",
    )

    CloseMessageWindow()
    OP_8C(0x103, 270, 400)
    Sleep(500)

    ChrTalk(    #215
        0x103,
        (
            "#020F#2P那么我们就在这里下船，\x01",
            "然后去协会一趟吧。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3B17():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_3B17)
    Sleep(50)

    def lambda_3B2A():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x108, 0, lambda_3B2A)
    Sleep(50)

    def lambda_3B3D():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_3B3D)
    Sleep(400)

    ChrTalk(    #216
        0x106,
        "#051F#2P啊啊，说的对。\x02",
    )

    CloseMessageWindow()

    def lambda_3B6C():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3B6C)
    Sleep(50)

    def lambda_3B7F():
        OP_8C(0xFE, 45, 400)
        ExitThread()

    QueueWorkItem(0x107, 0, lambda_3B7F)
    Sleep(50)

    def lambda_3B92():
        OP_8C(0xFE, 135, 400)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_3B92)
    Sleep(400)

    ChrTalk(    #217
        0x101,
        "#1004F唉……为、为什么呢？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #218
        0x108,
        (
            "#074F#2P连你们这些当地人\x01",
            "都这么惊讶的浓雾…\x02\x03",

            "#072F很可能又是『结社』\x01",
            "搞出来的勾当。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #219
        0x101,
        "#1026F啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #220
        0x104,
        (
            "#035F#2P呼……\x01",
            "剩下的地区只有柏斯和洛连特了。\x02\x03",

            "#030F看来他们下一个目标不是柏斯，\x01",
            "而是洛连特。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1500, 0, -1)
    OP_0D()
    Sleep(1000)
    OP_AD(0x2400A7, 0x0, 0x0, 0x64)
    Sleep(4000)
    OP_56(0x2)
    OP_AE(0xC8)
    Sleep(2000)
    FadeToDark(0, 0, -1)
    ClearMapFlags(0x2000000)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/T0121   ._SN", 103, 0, 0)
    IdleLoop()
    Return()

    # Function_24_36EF end

    def Function_25_3CD7(): pass

    label("Function_25_3CD7")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, 55890, 4230, 35050, 0)

    def lambda_3CFE():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3CFE)
    OP_8E(0xFE, 0xDACA, 0x1086, 0x82AA, 0x7D0, 0x0)
    OP_8E(0xFE, 0xD0E8, 0x1022, 0x7A58, 0x7D0, 0x0)
    OP_8C(0xFE, 270, 400)
    Return()

    # Function_25_3CD7 end

    def Function_26_3D3A(): pass

    label("Function_26_3D3A")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, 55890, 4230, 35050, 0)

    def lambda_3D61():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3D61)
    OP_8E(0xFE, 0xDACA, 0x1086, 0x82AA, 0x7D0, 0x0)
    OP_8E(0xFE, 0xD93A, 0x1022, 0x7BF2, 0x7D0, 0x0)
    OP_8C(0xFE, 225, 400)
    Return()

    # Function_26_3D3A end

    def Function_27_3D9D(): pass

    label("Function_27_3D9D")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, 55890, 4230, 35050, 0)

    def lambda_3DC4():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3DC4)
    OP_8E(0xFE, 0xDACA, 0x1086, 0x82AA, 0x7D0, 0x0)
    OP_8E(0xFE, 0xD9E4, 0x1022, 0x7620, 0x7D0, 0x0)
    OP_8C(0xFE, 225, 400)
    Return()

    # Function_27_3D9D end

    def Function_28_3E00(): pass

    label("Function_28_3E00")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, 55890, 4230, 35050, 0)

    def lambda_3E27():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3E27)
    OP_8E(0xFE, 0xDACA, 0x1086, 0x82AA, 0x7D0, 0x0)
    OP_8E(0xFE, 0xD3AE, 0x1022, 0x756C, 0x7D0, 0x0)
    Return()

    # Function_28_3E00 end

    def Function_29_3E5C(): pass

    label("Function_29_3E5C")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, 55890, 4230, 35050, 0)

    def lambda_3E83():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3E83)
    OP_8E(0xFE, 0xDACA, 0x1086, 0x82AA, 0x7D0, 0x0)
    OP_8E(0xFE, 0xDE76, 0x1022, 0x7878, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 400)
    Return()

    # Function_29_3E5C end

    def Function_30_3EBF(): pass

    label("Function_30_3EBF")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, 55890, 4230, 35050, 0)

    def lambda_3EE6():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3EE6)
    OP_8E(0xFE, 0xDACA, 0x1086, 0x82AA, 0x7D0, 0x0)
    OP_8E(0xFE, 0xD548, 0x1068, 0x7E7C, 0x7D0, 0x0)
    OP_8C(0xFE, 270, 400)
    Return()

    # Function_30_3EBF end

    def Function_31_3F22(): pass

    label("Function_31_3F22")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, 55890, 4230, 35050, 0)

    def lambda_3F49():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3F49)
    OP_8E(0xFE, 0xDACA, 0x1086, 0x82AA, 0x7D0, 0x0)
    OP_8E(0xFE, 0xDE80, 0x1022, 0x802A, 0x7D0, 0x0)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_31_3F22 end

    def Function_32_3F85(): pass

    label("Function_32_3F85")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3FA6")
    Call(0, 37)
    FadeToBright(0, 0)
    Sleep(100)

    label("loc_3FA6")

    Fade(1000)
    OP_6D(36120, 0, 34420, 0)
    OP_67(0, 7200, -10000, 0)
    OP_6B(3300, 0)
    OP_6C(38000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 36570, 0, 33800, 0)
    SetChrPos(0x103, 35550, 0, 33750, 0)
    SetChrPos(0xF8, 35590, 0, 32350, 0)
    SetChrPos(0xF9, 36650, 0, 32439, 0)
    TurnDirection(0x14, 0x101, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_420B")
    OP_A2(0x1A01)

    ChrTalk(    #221
        0x14,
        (
            "#5P啊，艾丝蒂尔。\x01",
            "这就要出发了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #222
        0x14,
        (
            "#5P难得回来一次，\x01",
            "为什么不多留一阵啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #223
        0x101,
        (
            "#1016F#4P嗯……还有很多事要忙啊。\x02\x03",

            "#1006F等这次的工作结束之后，\x01",
            "我会好好休息一阵的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #224
        0x14,
        "#5P嗯，那最好不过了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #225
        0x14,
        (
            "#5P好了，爱娜已经\x01",
            "付过乘船费用了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #226
        0x14,
        "#5P要马上办理乘船手续吗？\x02",
    )

    CloseMessageWindow()
    OP_8C(0x103, 90, 400)

    ChrTalk(    #227
        0x103,
        (
            "#020F#6P要办手续的话，在飞船起飞\x01",
            "之前来这里办理就可以了。\x02\x03",

            "在洛连特还有\x01",
            "其他事情要做吗？\x02",
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
            "【还有点事】\x01",          # 0
            "【办理乘船手续】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Jump("loc_427F")

    label("loc_420B")


    ChrTalk(    #228
        0x14,
        (
            "#5P噢。\x01",
            "要办理乘船手续吗？\x02",
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
            "【还有点事】\x01",          # 0
            "【办理乘船手续】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_427F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_42B6")

    ChrTalk(    #229
        0x14,
        (
            "#5P那么，有需要的时候\x01",
            "再来吧。\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x0)
    Return()

    label("loc_42B6")


    ChrTalk(    #230
        0x14,
        "#5P好。\x02",
    )

    CloseMessageWindow()
    OP_8C(0x103, 0, 400)

    ChrTalk(    #231
        0x14,
        (
            "#5P那么我就去和协会联络，\x01",
            "把其他人叫来这里。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrName("")
    SetMessageWindowPos(72, 320, 56, 3)

    AnonymousTalk(    #232
        (
            "\x07\x05艾丝蒂尔一行人办理完乘船手续之后\x01",
            "就在原地等待飞船起飞。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C0(0x15, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Call(0, 36)
    OP_6D(44610, 4000, 35220, 0)
    OP_67(0, 8220, -10000, 0)
    OP_6B(3660, 0)
    OP_6C(50000, 0)
    OP_6E(331, 0)
    SetChrPos(0x101, 40690, 4000, 36460, 180)
    SetChrPos(0x103, 41780, 4000, 37050, 180)
    SetChrPos(0xF8, 39750, 4000, 37200, 180)
    SetChrPos(0xF9, 40930, 4000, 38420, 180)
    SetChrPos(0xFA, 39260, 4000, 38230, 180)
    SetChrPos(0xFB, 40230, 4000, 39230, 180)
    SetChrPos(0xFC, 39020, 4000, 39620, 180)
    SetChrPos(0x8, 42970, 4000, 31060, 90)
    SetChrPos(0x9, 42660, 4000, 31950, 180)
    SetChrPos(0xA, 42690, 4000, 33090, 180)
    SetChrPos(0xB, 42120, 4000, 34240, 114)
    SetChrPos(0xC, 41690, 4000, 35590, 180)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    OP_71(0xA, 0x4)
    OP_71(0xA, 0x2)
    OP_72(0xF, 0x4)
    OP_72(0xC, 0x4)
    OP_72(0xD, 0x4)
    OP_6F(0xF, 450)
    OP_6F(0xC, 0)
    OP_6F(0xD, 0)
    SetChrFlags(0x1A, 0x80)
    OP_A1(0x18, 0xF)
    SetChrPos(0x18, 55000, -3040, 35000, 0)
    OP_A1(0x17, 0xC)
    SetChrPos(0x17, 55000, -3040, 35000, 0)
    OP_48()
    OP_22(0xE2, 0x0, 0x64)
    OP_22(0x75, 0x0, 0x64)
    Sleep(3000)
    OP_22(0xC8, 0x0, 0x64)
    OP_7C(0x0, 0x64, 0xBB8, 0x64)
    Sleep(1000)
    OP_22(0x76, 0x0, 0x64)
    Sleep(1000)
    OP_22(0x78, 0x0, 0x64)
    Sleep(1000)
    FadeToBright(2000, 0)
    OP_43(0x8, 0x1, 0x0, 0x21)
    Sleep(500)
    OP_43(0x9, 0x1, 0x0, 0x22)
    Sleep(580)
    OP_43(0xA, 0x1, 0x0, 0x22)
    Sleep(550)
    OP_43(0xB, 0x1, 0x0, 0x22)
    Sleep(680)
    OP_43(0xC, 0x1, 0x0, 0x22)
    Sleep(650)
    OP_43(0x101, 0x1, 0x0, 0x23)
    Sleep(500)
    OP_43(0x103, 0x1, 0x0, 0x23)
    Sleep(480)
    OP_43(0xF8, 0x1, 0x0, 0x23)
    Sleep(470)
    OP_43(0xF9, 0x1, 0x0, 0x23)
    Sleep(490)
    OP_43(0xFA, 0x1, 0x0, 0x23)
    Sleep(500)
    OP_43(0xFB, 0x1, 0x0, 0x23)
    Sleep(480)
    OP_43(0xFC, 0x1, 0x0, 0x23)
    Sleep(4800)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(500)
    OP_6D(48470, 3930, 38060, 0)
    OP_67(0, 40540, -45000, 0)
    OP_6B(740, 0)
    OP_6C(159000, 0)
    OP_6E(510, 0)
    OP_44(0x8, 0x1)
    OP_44(0x9, 0x1)
    OP_44(0xA, 0x1)
    OP_44(0xB, 0x1)
    OP_44(0xC, 0x1)
    OP_44(0x101, 0x1)
    OP_44(0x103, 0x1)
    OP_44(0xF8, 0x1)
    OP_44(0xF9, 0x1)
    OP_44(0xFA, 0x1)
    OP_44(0xFB, 0x1)
    OP_44(0xFC, 0x1)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x103, 0x80)
    SetChrFlags(0xF8, 0x80)
    SetChrFlags(0xF9, 0x80)
    SetChrFlags(0xFA, 0x80)
    SetChrFlags(0xFB, 0x80)
    SetChrFlags(0xFC, 0x80)
    OP_6F(0xF, 1)
    FadeToBright(1000, 0)
    OP_22(0xE2, 0x0, 0x64)
    Sleep(2000)
    OP_22(0x78, 0x0, 0x64)
    OP_B0(0xD, 0x64)
    OP_6F(0xD, 0)
    OP_70(0xD, 0x12C)
    Sleep(1800)
    OP_22(0x76, 0x0, 0x64)
    OP_B0(0xF, 0x32)
    OP_6F(0xF, 1)
    OP_70(0xF, 0x3C)
    OP_73(0xF)
    Sleep(1000)
    OP_23(0x75)
    OP_22(0x77, 0x1, 0x64)

    def lambda_46EC():
        OP_6D(59300, 3930, 70000, 18000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_46EC)

    def lambda_4704():
        OP_6C(215000, 20000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4704)

    def lambda_4714():
        OP_6B(850, 20000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_4714)

    def lambda_4724():
        OP_6E(580, 20000)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_4724)
    LoadEffect(0x0, "map\\\\mp028_00.eff")
    Play3DEffect(0x0, 0x0, 0xB, "Frame1_E0000_ground_Layer1", 0xFFFFE7C8, 0x8FC, 0x2567, 0x0, 0x0, 0x0, 0x5DC, 0x5DC, 0x5DC, 0x0)
    Play3DEffect(0x0, 0x1, 0xB, "Frame1_E0000_ground_Layer1", 0x1838, 0x8FC, 0x2567, 0x0, 0x0, 0x0, 0x5DC, 0x5DC, 0x5DC, 0x0)

    def lambda_47CA():
        OP_8E(0xFE, 0xD6D8, 0xFFFFF808, 0x88B8, 0x12C, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 0, lambda_47CA)
    OP_22(0x77, 0x0, 0x64)
    OP_6F(0xF, 61)
    OP_70(0xF, 0xA0)
    OP_73(0xF)
    OP_71(0xF, 0x20)
    OP_6F(0xF, 161)
    OP_70(0xF, 0x104)
    WaitChrThread(0x18, 0x0)

    def lambda_4813():
        OP_8E(0xFE, 0xD6D8, 0x7F8, 0x19A28, 0x64, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_4813)

    def lambda_482E():
        OP_8E(0xFE, 0xD6D8, 0xFFFFFFD8, 0x19A28, 0x64, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_482E)
    Sleep(200)

    def lambda_484E():
        OP_8E(0xFE, 0xD6D8, 0x7F8, 0x19A28, 0xC8, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_484E)

    def lambda_4869():
        OP_8E(0xFE, 0xD6D8, 0xFFFFFFD8, 0x19A28, 0xC8, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_4869)
    Sleep(200)

    def lambda_4889():
        OP_8E(0xFE, 0xD6D8, 0x7F8, 0x19A28, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_4889)

    def lambda_48A4():
        OP_8E(0xFE, 0xD6D8, 0xFFFFFFD8, 0x19A28, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_48A4)
    Sleep(200)

    def lambda_48C4():
        OP_8E(0xFE, 0xD6D8, 0x7F8, 0x19A28, 0x320, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_48C4)

    def lambda_48DF():
        OP_8E(0xFE, 0xD6D8, 0xFFFFFFD8, 0x19A28, 0x320, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_48DF)
    Sleep(200)

    def lambda_48FF():
        OP_8E(0xFE, 0xD6D8, 0x7F8, 0x19A28, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_48FF)

    def lambda_491A():
        OP_8E(0xFE, 0xD6D8, 0xFFFFFFD8, 0x19A28, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_491A)
    Sleep(200)

    def lambda_493A():
        OP_8E(0xFE, 0xD6D8, 0x7F8, 0x19A28, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_493A)

    def lambda_4955():
        OP_8E(0xFE, 0xD6D8, 0xFFFFFFD8, 0x19A28, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_4955)
    Sleep(200)

    def lambda_4975():
        OP_8E(0xFE, 0xD6D8, 0x7F8, 0x19A28, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_4975)

    def lambda_4990():
        OP_8E(0xFE, 0xD6D8, 0xFFFFFFD8, 0x19A28, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_4990)
    Sleep(200)

    def lambda_49B0():
        OP_8E(0xFE, 0xD6D8, 0x7F8, 0x19A28, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_49B0)

    def lambda_49CB():
        OP_8E(0xFE, 0xD6D8, 0xFFFFFFD8, 0x19A28, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_49CB)
    Sleep(200)

    def lambda_49EB():
        OP_8E(0xFE, 0xD6D8, 0x7F8, 0x19A28, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_49EB)

    def lambda_4A06():
        OP_8E(0xFE, 0xD6D8, 0xFFFFFFD8, 0x19A28, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_4A06)
    Sleep(200)

    def lambda_4A26():
        OP_8E(0xFE, 0xD6D8, 0x7F8, 0x19A28, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_4A26)

    def lambda_4A41():
        OP_8E(0xFE, 0xD6D8, 0xFFFFFFD8, 0x19A28, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_4A41)
    Sleep(200)

    def lambda_4A61():
        OP_8E(0xFE, 0xD6D8, 0x7F8, 0x19A28, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_4A61)

    def lambda_4A7C():
        OP_8E(0xFE, 0xD6D8, 0xFFFFFFD8, 0x19A28, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_4A7C)
    Sleep(200)

    def lambda_4A9C():
        OP_8E(0xFE, 0xD6D8, 0x7F8, 0x106738, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_4A9C)

    def lambda_4AB7():
        OP_8E(0xFE, 0xD6D8, 0xFFFFFFD8, 0x106738, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_4AB7)
    Sleep(200)

    def lambda_4AD7():
        OP_8E(0xFE, 0xD6D8, 0x7F8, 0x19A28, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_4AD7)

    def lambda_4AF2():
        OP_8E(0xFE, 0xD6D8, 0xFFFFFFD8, 0x19A28, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_4AF2)
    Sleep(200)

    def lambda_4B12():
        OP_8E(0xFE, 0xD6D8, 0x7F8, 0x19A28, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_4B12)

    def lambda_4B2D():
        OP_8E(0xFE, 0xD6D8, 0xFFFFFFD8, 0x19A28, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_4B2D)
    Sleep(200)

    def lambda_4B4D():
        OP_8E(0xFE, 0xD6D8, 0x7F8, 0x19A28, 0x32C8, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_4B4D)

    def lambda_4B68():
        OP_8E(0xFE, 0xD6D8, 0xFFFFFFD8, 0x19A28, 0x32C8, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_4B68)
    Sleep(2800)
    OP_24(0x77, 0x5A)
    Sleep(300)
    OP_24(0x77, 0x50)
    Sleep(300)
    OP_24(0x77, 0x46)
    Sleep(100)
    FadeToDark(2000, 0, -1)
    Sleep(200)
    OP_24(0x77, 0x3C)
    Sleep(300)
    OP_24(0x77, 0x32)
    Sleep(300)
    OP_24(0x77, 0x28)
    Sleep(300)
    OP_24(0x77, 0x1E)
    Sleep(300)
    OP_23(0x77)
    OP_0D()
    OP_71(0xB, 0x4)
    OP_71(0xC, 0x4)
    OP_71(0xD, 0x4)
    RemoveParty(0x2, 0xFF)
    RemoveParty(0x5, 0xFF)
    RemoveParty(0x6, 0xFF)
    RemoveParty(0x3, 0xFF)
    RemoveParty(0x4, 0xFF)
    RemoveParty(0x7, 0xFF)
    OP_A2(0x10F3)
    OP_A2(0x1A02)
    OP_28(0x72, 0x4, 0x40)
    OP_28(0x73, 0x4, 0x40)
    OP_28(0x74, 0x4, 0x40)
    OP_28(0x75, 0x4, 0x40)
    OP_28(0x76, 0x4, 0x40)
    OP_28(0x77, 0x4, 0x40)
    OP_28(0xAD, 0x4, 0x40)
    OP_28(0xAE, 0x4, 0x40)
    OP_28(0xAF, 0x4, 0x40)
    OP_28(0xB0, 0x4, 0x40)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/T3133   ._SN", 104, 0, 0)
    IdleLoop()
    Return()

    # Function_32_3F85 end

    def Function_33_4C3A(): pass

    label("Function_33_4C3A")

    SetChrBattleFlags(0xFE, 0x20)
    OP_8E(0xFE, 0xBC7A, 0xC3A, 0x790E, 0x7D0, 0x0)
    OP_8E(0xFE, 0xD804, 0xC3A, 0x790E, 0x7D0, 0x0)
    OP_8E(0xFE, 0xD804, 0xC3A, 0x878C, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_33_4C3A end

    def Function_34_4C81(): pass

    label("Function_34_4C81")

    SetChrBattleFlags(0xFE, 0x20)
    OP_8E(0xFE, 0xA6CC, 0xFA0, 0x78BE, 0x7D0, 0x0)
    OP_8E(0xFE, 0xBC7A, 0xC3A, 0x790E, 0x7D0, 0x0)
    OP_8E(0xFE, 0xD804, 0xF5A, 0x790E, 0x7D0, 0x0)
    OP_8E(0xFE, 0xD804, 0xC3A, 0x878C, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_34_4C81 end

    def Function_35_4CDC(): pass

    label("Function_35_4CDC")

    SetChrBattleFlags(0xFE, 0x20)
    OP_8E(0xFE, 0xA32A, 0xFA0, 0x8818, 0x7D0, 0x0)
    OP_8E(0xFE, 0xA6CC, 0xFA0, 0x78BE, 0x7D0, 0x0)
    OP_8E(0xFE, 0xBC7A, 0xC3A, 0x790E, 0x7D0, 0x0)
    OP_8E(0xFE, 0xD804, 0xC3A, 0x790E, 0x7D0, 0x0)
    OP_8E(0xFE, 0xD804, 0xC3A, 0x878C, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_35_4CDC end

    def Function_36_4D4B(): pass

    label("Function_36_4D4B")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4D84")
    AddParty(0x5, 0xFA, 0xFF)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    label("loc_4D84")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4DD1")
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4DB9")
    AddParty(0x6, 0xFA, 0xFF)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_4DD1")

    label("loc_4DB9")

    AddParty(0x6, 0xFB, 0xFF)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    label("loc_4DD1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4E46")
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4E06")
    AddParty(0x3, 0xFA, 0xFF)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_4E46")

    label("loc_4E06")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4E2E")
    AddParty(0x3, 0xFB, 0xFF)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_4E46")

    label("loc_4E2E")

    AddParty(0x3, 0xFC, 0xFF)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    label("loc_4E46")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4E93")
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4E7B")
    AddParty(0x4, 0xFB, 0xFF)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_4E93")

    label("loc_4E7B")

    AddParty(0x4, 0xFC, 0xFF)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    label("loc_4E93")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4EB8")
    AddParty(0x7, 0xFC, 0xFF)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x20), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    label("loc_4EB8")

    Return()

    # Function_36_4D4B end

    def Function_37_4EB9(): pass

    label("Function_37_4EB9")

    FadeToDark(0, 0, -1)
    OP_6D(90, 0, 24870, 0)
    Sleep(100)
    OP_A3(0x1200)
    OP_A3(0x1201)
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
        (0, "loc_4F43"),
        (1, "loc_4F49"),
        (SWITCH_DEFAULT, "loc_4F4F"),
    )


    label("loc_4F43")

    OP_A2(0x1200)
    Jump("loc_4F4F")

    label("loc_4F49")

    OP_A2(0x1201)
    Jump("loc_4F4F")

    label("loc_4F4F")

    FadeToBright(0, 0)
    OP_0D()
    OP_C9(0x0, 0x4, 0x0, 0x2, 0xFF, 0xFF, 0x5, 0x6, 0x3, 0x4, 0x7, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Return()

    # Function_37_4EB9 end

    def Function_38_4F8B(): pass

    label("Function_38_4F8B")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #233
        (
            "\x07\x05定期船飞船坪\x01",
            "≡　开往王都格兰赛尔\x01",
            "≡　开往柏斯市\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #234
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

    # Function_38_4F8B end

    def Function_39_5027(): pass

    label("Function_39_5027")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #235
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

    # Function_39_5027 end

    def Function_40_50A3(): pass

    label("Function_40_50A3")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #236
        (
            "\x07\x05　※无关人员禁止入内　　\x01",
            "   『利贝尔飞船公社』　\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_40_50A3 end

    SaveToFile()

Try(main)
