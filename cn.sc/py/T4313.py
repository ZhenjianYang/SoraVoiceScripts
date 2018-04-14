from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4313   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4313.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60017",
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
        '管家雷蒙德',                           # 9
        '杜南公爵',                             # 10
        '玲',                                   # 11
        '希德中校',                             # 12
        '凯诺娜',                               # 13
        '卡西乌斯',                             # 14
        '理查德',                               # 15
        '沃尔特议员',                           # 16
        '莉卡妲夫人',                           # 17
        '爱尔莎大使',                           # 18
        '贝尔克副队长',                         # 19
        '西莫鲁',                               # 20
        '妮娜',                                 # 21
        '图书管理员皮埃多罗',                   # 22
        '约克姆老人',                           # 23
        '游客',                                 # 24
        '游客',                                 # 25
        '管家菲利普',                           # 26
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
        'ED6_DT07/CH01570 ._CH',             # 00
        'ED6_DT07/CH02140 ._CH',             # 01
        'ED6_DT27/CH03004 ._CH',             # 02
        'ED6_DT27/CH03510 ._CH',             # 03
        'ED6_DT27/CH03590 ._CH',             # 04
        'ED6_DT27/CH03123 ._CH',             # 05
        'ED6_DT27/CH03670 ._CH',             # 06
        'ED6_DT27/CH03690 ._CH',             # 07
        'ED6_DT07/CH01200 ._CH',             # 08
        'ED6_DT07/CH01230 ._CH',             # 09
        'ED6_DT27/CH03720 ._CH',             # 0A
        'ED6_DT07/CH01310 ._CH',             # 0B
        'ED6_DT07/CH01350 ._CH',             # 0C
        'ED6_DT07/CH01770 ._CH',             # 0D
        'ED6_DT07/CH01100 ._CH',             # 0E
        'ED6_DT07/CH01490 ._CH',             # 0F
        'ED6_DT07/CH01050 ._CH',             # 10
        'ED6_DT07/CH01160 ._CH',             # 11
        'ED6_DT07/CH02470 ._CH',             # 12
    )

    AddCharChipPat(
        'ED6_DT07/CH01570P._CP',             # 00
        'ED6_DT07/CH02140P._CP',             # 01
        'ED6_DT27/CH03004P._CP',             # 02
        'ED6_DT27/CH03510P._CP',             # 03
        'ED6_DT27/CH03590P._CP',             # 04
        'ED6_DT27/CH03123P._CP',             # 05
        'ED6_DT27/CH03670P._CP',             # 06
        'ED6_DT27/CH03690P._CP',             # 07
        'ED6_DT07/CH01200P._CP',             # 08
        'ED6_DT07/CH01230P._CP',             # 09
        'ED6_DT27/CH03720P._CP',             # 0A
        'ED6_DT07/CH01310P._CP',             # 0B
        'ED6_DT07/CH01350P._CP',             # 0C
        'ED6_DT07/CH01770P._CP',             # 0D
        'ED6_DT07/CH01100P._CP',             # 0E
        'ED6_DT07/CH01490P._CP',             # 0F
        'ED6_DT07/CH01050P._CP',             # 10
        'ED6_DT07/CH01160P._CP',             # 11
        'ED6_DT07/CH02470P._CP',             # 12
    )

    DeclNpc(
        X                   = -11850,
        Z                   = 0,
        Y                   = 20220,
        Direction           = 225,
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
        X                   = -16000,
        Z                   = 0,
        Y                   = -38500,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
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
        Direction           = 0,
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
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
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
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -14110,
        Z                   = 0,
        Y                   = -8710,
        Direction           = 0,
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
        X                   = -10410,
        Z                   = 0,
        Y                   = -15620,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = -14830,
        Z                   = 0,
        Y                   = -14420,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = 11910,
        Z                   = 0,
        Y                   = 18100,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = -19030,
        Z                   = 0,
        Y                   = 20590,
        Direction           = 315,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = -12710,
        Z                   = 0,
        Y                   = 48170,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 13,
        ChipIndex           = 0xD,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = 20140,
        Z                   = 0,
        Y                   = -42620,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = 10340,
        Z                   = 0,
        Y                   = -41560,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 15,
        ChipIndex           = 0xF,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = 14120,
        Z                   = 0,
        Y                   = 50600,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 16,
        ChipIndex           = 0x10,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 14,
    )

    DeclNpc(
        X                   = 15980,
        Z                   = 0,
        Y                   = 50600,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 17,
        ChipIndex           = 0x11,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 15,
    )

    DeclNpc(
        X                   = -12960,
        Z                   = 0,
        Y                   = -44100,
        Direction           = 87,
        Unknown2            = 0,
        Unknown3            = 18,
        ChipIndex           = 0x12,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )


    DeclActor(
        TriggerX            = -13210,
        TriggerZ            = 0,
        TriggerY            = 18820,
        TriggerRange        = 800,
        ActorX              = -11850,
        ActorZ              = 1500,
        ActorY              = 20220,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -14700,
        TriggerZ            = 0,
        TriggerY            = 47000,
        TriggerRange        = 2000,
        ActorX              = -18500,
        ActorZ              = 1500,
        ActorY              = 46500,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 17,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -17800,
        TriggerZ            = 0,
        TriggerY            = 47000,
        TriggerRange        = 2000,
        ActorX              = -18500,
        ActorZ              = 1500,
        ActorY              = 46500,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 17,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -21000,
        TriggerZ            = 0,
        TriggerY            = 47000,
        TriggerRange        = 2000,
        ActorX              = -18500,
        ActorZ              = 1500,
        ActorY              = 46500,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 17,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 25980,
        TriggerZ            = 0,
        TriggerY            = 50580,
        TriggerRange        = 800,
        ActorX              = 25690,
        ActorZ              = 1500,
        ActorY              = 51500,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 19,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -10300,
        TriggerZ            = 0,
        TriggerY            = 19220,
        TriggerRange        = 500,
        ActorX              = -10900,
        ActorZ              = 1500,
        ActorY              = 19110,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 28,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 22140,
        TriggerZ            = 0,
        TriggerY            = 50600,
        TriggerRange        = 800,
        ActorX              = 21830,
        ActorZ              = 890,
        ActorY              = 51760,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 34,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 18200,
        TriggerZ            = 0,
        TriggerY            = 51350,
        TriggerRange        = 800,
        ActorX              = 18200,
        ActorZ              = 1800,
        ActorY              = 51350,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 35,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 14200,
        TriggerZ            = 0,
        TriggerY            = 51310,
        TriggerRange        = 800,
        ActorX              = 14200,
        ActorZ              = 2000,
        ActorY              = 51310,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 36,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 10220,
        TriggerZ            = 0,
        TriggerY            = 51150,
        TriggerRange        = 800,
        ActorX              = 10220,
        ActorZ              = 1200,
        ActorY              = 51150,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 37,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 24340,
        TriggerZ            = 0,
        TriggerY            = 45480,
        TriggerRange        = 800,
        ActorX              = 24340,
        ActorZ              = 500,
        ActorY              = 45480,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 38,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_50E",          # 00, 0
        "Function_1_67E",          # 01, 1
        "Function_2_6B7",          # 02, 2
        "Function_3_834",          # 03, 3
        "Function_4_839",          # 04, 4
        "Function_5_E39",          # 05, 5
        "Function_6_F5A",          # 06, 6
        "Function_7_1357",         # 07, 7
        "Function_8_1566",         # 08, 8
        "Function_9_1AA5",         # 09, 9
        "Function_10_1BF0",        # 0A, 10
        "Function_11_1CE2",        # 0B, 11
        "Function_12_1EFF",        # 0C, 12
        "Function_13_213C",        # 0D, 13
        "Function_14_21B0",        # 0E, 14
        "Function_15_227D",        # 0F, 15
        "Function_16_2348",        # 10, 16
        "Function_17_23BA",        # 11, 17
        "Function_18_2426",        # 12, 18
        "Function_19_2A67",        # 13, 19
        "Function_20_2C0F",        # 14, 20
        "Function_21_41CE",        # 15, 21
        "Function_22_421D",        # 16, 22
        "Function_23_4279",        # 17, 23
        "Function_24_42DA",        # 18, 24
        "Function_25_433B",        # 19, 25
        "Function_26_4388",        # 1A, 26
        "Function_27_45C0",        # 1B, 27
        "Function_28_4ED7",        # 1C, 28
        "Function_29_5343",        # 1D, 29
        "Function_30_60C8",        # 1E, 30
        "Function_31_70FE",        # 1F, 31
        "Function_32_7121",        # 20, 32
        "Function_33_71BA",        # 21, 33
        "Function_34_723B",        # 22, 34
        "Function_35_7282",        # 23, 35
        "Function_36_72C9",        # 24, 36
        "Function_37_7310",        # 25, 37
        "Function_38_7355",        # 26, 38
    )


    def Function_0_50E(): pass

    label("Function_0_50E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_561")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_55E")
    SetChrPos(0x8, -15170, 0, 17070, 225)
    SetChrPos(0x13, -16940, 0, 16460, 90)
    SetChrPos(0x14, -15820, 0, 15350, 0)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x10, 0x80)

    label("loc_55E")

    Jump("loc_63E")

    label("loc_561")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_63E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_5A8")
    SetChrPos(0xF, -14830, 0, -13010, 180)
    SetChrPos(0x14, 18250, 0, 44450, 0)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x16, 0x80)
    Jump("loc_63E")

    label("loc_5A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 3)), scpexpr(EXPR_END)), "loc_5B2")
    Jump("loc_63E")

    label("loc_5B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C2, 7)), scpexpr(EXPR_END)), "loc_625")
    SetChrPos(0xF, -11700, 0, -14320, 274)
    SetChrPos(0x10, -13610, 0, -14320, 93)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x17, 23640, 0, 44900, 0)
    SetChrPos(0x18, 25640, 0, 44900, 270)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 0)), scpexpr(EXPR_END)), "loc_622")
    ClearChrFlags(0x19, 0x80)

    label("loc_622")

    Jump("loc_63E")

    label("loc_625")

    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)

    label("loc_63E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_65D")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10F0)
    SetMapFlags(0x10000000)
    Event(0, 30)
    Jump("loc_67D")

    label("loc_65D")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_669"),
        (SWITCH_DEFAULT, "loc_67D"),
    )


    label("loc_669")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_67A")
    SetMapFlags(0x10000000)
    Event(0, 20)

    label("loc_67A")

    Jump("loc_67D")

    label("loc_67D")

    Return()

    # Function_0_50E end

    def Function_1_67E(): pass

    label("Function_1_67E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_68E")
    OP_64(0x0, 0x1)

    label("loc_68E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C2, 7)), scpexpr(EXPR_END)), "loc_6A5")
    OP_64(0x1, 0x1)
    OP_64(0x2, 0x1)
    OP_64(0x3, 0x1)
    OP_64(0x5, 0x1)

    label("loc_6A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6B6")
    OP_72(0x7, 0x4)

    label("loc_6B6")

    Return()

    # Function_1_67E end

    def Function_2_6B7(): pass

    label("Function_2_6B7")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6DC")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_81E")

    label("loc_6DC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6F5")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_81E")

    label("loc_6F5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_70E")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_81E")

    label("loc_70E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_727")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_81E")

    label("loc_727")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_740")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_81E")

    label("loc_740")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_759")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_81E")

    label("loc_759")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_772")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_81E")

    label("loc_772")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_78B")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_81E")

    label("loc_78B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7A4")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_81E")

    label("loc_7A4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7BD")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_81E")

    label("loc_7BD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7D6")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_81E")

    label("loc_7D6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7EF")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_81E")

    label("loc_7EF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_808")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_81E")

    label("loc_808")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_81E")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_81E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_833")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_81E")

    label("loc_833")

    Return()

    # Function_2_6B7 end

    def Function_3_834(): pass

    label("Function_3_834")

    Call(0, 4)
    Return()

    # Function_3_834 end

    def Function_4_839(): pass

    label("Function_4_839")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_93D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_93A")
    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_8B1")

    ChrTalk(    #0
        0x8,
        (
            "什么也不做令人心神不宁，\x01",
            "就决定开始大扫除了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x8,
        (
            "之后只有等待\x01",
            "女王陛下的指示了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_937")

    label("loc_8B1")


    ChrTalk(    #2
        0x8,
        (
            "总之，到底\x01",
            "会变成怎样……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x8,
        (
            "什么也不做令人心神不宁，\x01",
            "就决定开始离宫的大扫除了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x8,
        (
            "如果有事情做\x01",
            "就用不着考虑多余的事了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_937")

    TalkEnd(0x8)

    label("loc_93A")

    Jump("loc_E38")

    label("loc_93D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E38")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_B1D")
    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2CC, 2)), scpexpr(EXPR_END)), "loc_9AF")

    ChrTalk(    #5
        0x8,
        (
            "似乎发生了很多事，\x01",
            "不过能解决就好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x8,
        (
            "总是给你们添麻烦\x01",
            "真是不好意思呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B17")

    label("loc_9AF")


    ChrTalk(    #7
        0x8,
        "啊，你们是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x8,
        (
            "今天玲\x01",
            "没有一起来吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x101,
        (
            "#1003F玲她……\x01",
            "回到父母身边了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x8,
        (
            "咦咦！？\x01",
            "找到她父母了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x8,
        (
            "听说在王都\x01",
            "发生了不得了的事情\x01",
            "正在担心呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x8,
        (
            "是吗，\x01",
            "那就好……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x101,
        "#1005F一点都不好！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x8,
        "咦！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x101,
        (
            "#1009F我一定要抓住她，\x01",
            "把她给带回来！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x8,
        (
            "带、带回来，\x01",
            "她父母有什么问题吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x8,
        (
            "嗯～最近由于父母的情况\x01",
            "孩子的环境真是复杂啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1662)

    label("loc_B17")

    TalkEnd(0x8)
    Jump("loc_E38")

    label("loc_B1D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 3)), scpexpr(EXPR_END)), "loc_CE6")
    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2CC, 1)), scpexpr(EXPR_END)), "loc_B74")

    ChrTalk(    #18
        0x8,
        (
            "玲似乎和大家\x01",
            "相处融洽，我就放心了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x8,
        "早点找到父母就好了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_CE0")

    label("loc_B74")

    TurnDirection(0x8, 0x12F, 0)

    ChrTalk(    #20
        0x8,
        "呀，这不是玲吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x12F,
        (
            "#261F啊，管家大哥哥！\x02\x03",

            "#265F哈哈哈，今天\x01",
            "也和玲躲猫猫吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x8,
        "啊、啊哈哈……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x8,
        (
            "抱歉，今天\x01",
            "还有工作，就算了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x12F,
        (
            "#268F男人真没意思。\x02\x03",

            "#266F总是说工作、工作的\x01",
            "结果又不陪我玩。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #25
        0x8,
        "呜……真是一针见血……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x0, 400)

    ChrTalk(    #26
        0x8,
        (
            "但是，她和大家\x01",
            "看上去好像很融洽，我可以放心了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x101,
        "#1016F啊、啊哈哈，托你的福。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1661)

    label("loc_CE0")

    TalkEnd(0x8)
    Jump("loc_E38")

    label("loc_CE6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C2, 7)), scpexpr(EXPR_END)), "loc_D43")
    TalkBegin(0x8)

    ChrTalk(    #28
        0x8,
        "说实话，我真是不知如何是好了……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x8,
        (
            "交给游击士协会的话，\x01",
            "就能放心了。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x8)
    Jump("loc_E38")

    label("loc_D43")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C2, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C2, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C2, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D61")
    Call(0, 27)
    Jump("loc_E38")

    label("loc_D61")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_DAD")

    ChrTalk(    #30
        0x8,
        (
            "呼～话说回来\x01",
            "到底藏在哪儿呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x8,
        "这个离宫也很大啊～……\x02",
    )

    CloseMessageWindow()
    Jump("loc_E35")

    label("loc_DAD")


    ChrTalk(    #32
        0x8,
        (
            "呀，怎样，\x01",
            "能找到那女孩吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x101,
        (
            "#1007F嗯～现在\x01",
            "还不好说……\x02\x03",

            "#1006F不过，再到一些想到的地方\x01",
            "找找看吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x8,
        "嗯，拜托你们了哦。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_E35")

    TalkEnd(0x8)

    label("loc_E38")

    Return()

    # Function_4_839 end

    def Function_5_E39(): pass

    label("Function_5_E39")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 0)), scpexpr(EXPR_END)), "loc_EBB")
    TalkBegin(0x9)

    ChrTalk(    #35
        0x9,
        (
            "#222F你们啊，是不是向菲利普\x01",
            "灌输了什么？\x02\x03",

            "最近只要看到他\x01",
            "总是挑三拣四诸多要求……\x02\x03",

            "#224F到底当我是什么人啊！\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x9)
    Jump("loc_F59")

    label("loc_EBB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C2, 7)), scpexpr(EXPR_END)), "loc_F0A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C2, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_ED1")
    Call(0, 26)
    Jump("loc_F07")

    label("loc_ED1")

    TalkBegin(0x9)

    ChrTalk(    #36
        0x9,
        (
            "#224F哎，带着这小丫头\x01",
            "赶快从这房间里出去！\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x9)

    label("loc_F07")

    Jump("loc_F59")

    label("loc_F0A")

    TalkBegin(0x9)

    ChrTalk(    #37
        0x9,
        (
            "#222F穿白裙子的女孩？\x02\x03",

            "#224F不认识那种小丫头！\x01",
            "赶快从这房间里出去！\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x9)

    label("loc_F59")

    Return()

    # Function_5_E39 end

    def Function_6_F5A(): pass

    label("Function_6_F5A")

    TalkBegin(0xF)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1353")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_FBC")

    ChrTalk(    #38
        0xFE,
        "第一次见到爱尔莎大使……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xFE,
        (
            "哎呀……\x01",
            "还真是相当伶牙俐齿的女性啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1353")

    label("loc_FBC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 3)), scpexpr(EXPR_END)), "loc_1128")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_100F")

    ChrTalk(    #40
        0xFE,
        (
            "哈哈，我妻子的话\x01",
            "请别放在心上。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0xFE,
        (
            "她是因为\x01",
            "不太了解政治。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1125")

    label("loc_100F")


    ChrTalk(    #42
        0xFE,
        (
            "互不侵犯条约……共和国议会也是\x01",
            "各种各样的意见交织混杂啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xFE,
        (
            "厌恶帝国的民和党等从当初开始\x01",
            "就表现出反对的态度。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0xFE,
        (
            "要封住过激的在野党\x01",
            "每次都让总统伤透脑筋……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xFE,
        (
            "由于新型引擎的事\x01",
            "这次很容易获得了过半数的赞成。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0xFE,
        (
            "靠艾莉茜雅女王的手腕共和国的\x01",
            "总统似乎也能成事了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_1125")

    Jump("loc_1353")

    label("loc_1128")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C2, 7)), scpexpr(EXPR_END)), "loc_1245")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_1197")

    ChrTalk(    #47
        0xFE,
        (
            "哈哈，看来她的心思\x01",
            "都在王都旅游上呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0xFE,
        (
            "唉，因为是各种各样的主义主张\x01",
            "共存的共和国嘛。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1242")

    label("loc_1197")


    ChrTalk(    #49
        0xFE,
        (
            "我的妻子对政治\x01",
            "缺乏根本的理解。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0xFE,
        (
            "这次打算纠正这个\x01",
            "才带她同行……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0xFE,
        (
            "哈哈，看来她的心思\x01",
            "都在王都旅游上呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0xFE,
        (
            "唉，因为是各种各样的主义主张\x01",
            "共存的共和国嘛。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_1242")

    Jump("loc_1353")

    label("loc_1245")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_1353")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_12AC")

    ChrTalk(    #53
        0xFE,
        (
            "我是共和国议会的议员，\x01",
            "我叫沃尔特。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0xFE,
        (
            "顺便视察和准备签字仪式\x01",
            "就提前到现场了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1353")

    label("loc_12AC")


    ChrTalk(    #55
        0xFE,
        (
            "我是共和国议会的议员，\x01",
            "我叫沃尔特。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0xFE,
        (
            "顺便视察和准备签字仪式\x01",
            "就提前到现场了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0xFE,
        (
            "唔，相当\x01",
            "出色的离宫不是吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0xFE,
        (
            "确实可以说是进行签字仪式\x01",
            "最适合的地方。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_1353")

    TalkEnd(0xF)
    Return()

    # Function_6_F5A end

    def Function_7_1357(): pass

    label("Function_7_1357")

    TalkBegin(0x10)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1562")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_13BE")

    ChrTalk(    #59
        0xFE,
        (
            "因此，我多次\x01",
            "对丈夫说……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0xFE,
        (
            "在对政治高谈阔论之前\x01",
            "应该先学习与人交往。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1562")

    label("loc_13BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 3)), scpexpr(EXPR_END)), "loc_1464")

    ChrTalk(    #61
        0xFE,
        (
            "像丈夫一样的小人物和总统啊\x01",
            "艾莉茜雅女王等人谈话，\x01",
            "实在太奇怪了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0xFE,
        (
            "在成为大人物之前应该\x01",
            "以谦虚的姿态行事啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0xFE,
        (
            "为公事而来\x01",
            "却还没和大使打过招呼。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1562")

    label("loc_1464")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C2, 7)), scpexpr(EXPR_END)), "loc_1505")

    ChrTalk(    #64
        0xFE,
        (
            "像丈夫这样，\x01",
            "一介议员为了签字仪式而出差,\x01",
            "本来就没有必要嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0xFE,
        (
            "好不容易当了议员\x01",
            "就随便来看看而已。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0xFE,
        (
            "比起那个，早点去格兰赛尔\x01",
            "旅游多好啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1562")

    label("loc_1505")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_1562")

    ChrTalk(    #67
        0xFE,
        (
            "利贝尔王国\x01",
            "虽然在地图上是小国家……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0xFE,
        (
            "但人们都很亲切，\x01",
            "并有着非常美丽的土地。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1562")

    TalkEnd(0x10)
    Return()

    # Function_7_1357 end

    def Function_8_1566(): pass

    label("Function_8_1566")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2CC, 3)), scpexpr(EXPR_END)), "loc_1572")
    SetChrFlags(0xFE, 0x10)

    label("loc_1572")

    TalkBegin(0x11)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1AA1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_1AA1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2CC, 3)), scpexpr(EXPR_END)), "loc_1686")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_15EF")

    ChrTalk(    #69
        0x11,
        (
            "#1113F如果是官方的视察，\x01",
            "应该先通过大使馆才对。\x02\x03",

            "还是说称为视察的\x01",
            "公费旅游来的？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1683")

    label("loc_15EF")


    ChrTalk(    #70
        0x11,
        (
            "#1113F好了，沃尔特议员。\x02\x03",

            "远道而来辛苦了\x01",
            "虽然想这么说……\x02\x03",

            "#1112F如果是官方的视察，\x01",
            "应该先通过大使馆才对。\x02\x03",

            "还是说称为视察的\x01",
            "公费旅游来的？\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_1683")

    Jump("loc_1AA1")

    label("loc_1686")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_16F4")

    ChrTalk(    #71
        0x11,
        (
            "#1110F哎呀，这不是金先生吗。\x02\x03",

            "居然能在这里\x01",
            "见面真是意外。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x108,
        (
            "#070F哈哈，正好\x01",
            "路过嘛。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1729")

    label("loc_16F4")


    ChrTalk(    #73
        0x11,
        (
            "#1110F哎呀，你们。\x02\x03",

            "居然能在这里\x01",
            "见面真是意外。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1729")


    ChrTalk(    #74
        0x101,
        "#1000F你好，爱尔莎大使。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x11,
        (
            "#1110F对了对了，恐吓信事件的始末，\x01",
            "我听了利贝尔方面的报告哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x101,
        "#1011F啊，是吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0x11,
        (
            "#1113F嗯嗯，情报部的余党，\x01",
            "特务兵们的秘密工作……\x02\x03",

            "#1110F不过，对于艾莉茜雅女王来说\x01",
            "应该料到了吧？\x02\x03",

            "不过，我感到\x01",
            "没这么简单……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0x101,
        (
            "#1016F啊、啊哈哈……\x02\x03",

            "(和、和外国人这样\x01",
            " 说话真是紧张啊。)\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_18E2")

    ChrTalk(    #79
        0x106,
        (
            "#050F（嗯，这种时候关键看胆量。）\x02\x03",

            "(要是游击士无论对方是谁\x01",
            "　最低限度的策略和谈判\x01",
            "　还是要能上得了台面才行。)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_195B")

    label("loc_18E2")


    ChrTalk(    #80
        0x103,
        (
            "#020F（不过，还是要看经验和适应能力。）\x02\x03",

            "(要是游击士无论对方是谁\x01",
            "　最低限度的策略和谈判\x01",
            "　还是要能上得了台面才行。)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_195B")


    ChrTalk(    #81
        0x11,
        (
            "#1110F……艾莉茜雅女王看起来，\x01",
            "似乎也相当辛苦啊。\x02\x03",

            "但是，政变的处理，\x01",
            "不是相当顺利吗。\x02\x03",

            "你们也相当活跃\x01",
            "大使馆都在谈论呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0x101,
        (
            "#1016F不，哪里……身为游击士\x01",
            "这是应该做的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0x11,
        (
            "#1111F呵呵，虽然想再详细问问，\x01",
            "但现在开始似乎很忙呢。\x02\x03",

            "#1110F下次有机会再聊吧，\x01",
            "艾丝蒂尔·布莱特。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0x101,
        (
            "#1000F好，好的，那么，\x01",
            "今天就失陪了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1663)

    label("loc_1AA1")

    TalkEnd(0x11)
    Return()

    # Function_8_1566 end

    def Function_9_1AA5(): pass

    label("Function_9_1AA5")

    TalkBegin(0x12)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1BEC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_1BEC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_1B29")

    ChrTalk(    #85
        0xFE,
        (
            "话说回来，没能追上\x01",
            "那个巨大人偶真是懊悔啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0xFE,
        (
            "今后，被那种东西袭击时，\x01",
            "我们怎样应该应对……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BEC")

    label("loc_1B29")


    ChrTalk(    #87
        0xFE,
        (
            "虽说有亲卫队的帮助，\x01",
            "但要破坏那怪物战车……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0xFE,
        (
            "真是的，你们\x01",
            "游击士的力量真不得了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0xFE,
        (
            "话说回来，没能追上\x01",
            "那个巨大人偶真是懊悔啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0xFE,
        (
            "今后，被那种东西袭击时，\x01",
            "我们应该怎样应对……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)

    label("loc_1BEC")

    TalkEnd(0x12)
    Return()

    # Function_9_1AA5 end

    def Function_10_1BF0(): pass

    label("Function_10_1BF0")

    TalkBegin(0x13)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1C3C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1C39")

    ChrTalk(    #91
        0xFE,
        "这可是不能输的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0xFE,
        (
            "谁打扫的房间多\x01",
            "就赢了～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C39")

    Jump("loc_1CDE")

    label("loc_1C3C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1CDE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_1C9E")

    ChrTalk(    #93
        0xFE,
        (
            "希德中校他们\x01",
            "好像一直没睡。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0xFE,
        (
            "军人也真是辛苦。\x01",
            "别搞坏身体就好了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1CDE")

    label("loc_1C9E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 3)), scpexpr(EXPR_END)), "loc_1CDE")
    TurnDirection(0xFE, 0x12F, 0)

    ChrTalk(    #95
        0xFE,
        "哎呀，玲……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0xFE,
        "呵呵，今天和朋友在一起呢。\x02",
    )

    CloseMessageWindow()

    label("loc_1CDE")

    TalkEnd(0x13)
    Return()

    # Function_10_1BF0 end

    def Function_11_1CE2(): pass

    label("Function_11_1CE2")

    TalkBegin(0x14)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1D57")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1D54")

    ChrTalk(    #97
        0xFE,
        (
            "西莫鲁真是的，完全\x01",
            "中了雷蒙德先生的招……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0xFE,
        (
            "但是，对于名为决斗的事\x01",
            "我是不能插手的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D54")

    Jump("loc_1EE3")

    label("loc_1D57")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1EE3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_1E37")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_1DB2")

    ChrTalk(    #99
        0xFE,
        (
            "啦啦啦～⊙\x01",
            "啦啦噜噜啦啦⊙\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0xFE,
        (
            "竖着擦，\x01",
            "横着擦，斜着擦⊙\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E34")

    label("loc_1DB2")


    ChrTalk(    #101
        0xFE,
        (
            "这里展示物多，\x01",
            "打扫可辛苦了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0xFE,
        "不过，也是看本事的地方。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0xFE,
        (
            "啦啦啦～⊙\x01",
            "啦啦噜噜啦啦⊙\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0xFE,
        (
            "竖着擦，\x01",
            "横着擦，斜着擦⊙\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x6)

    label("loc_1E34")

    Jump("loc_1EE3")

    label("loc_1E37")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 3)), scpexpr(EXPR_END)), "loc_1EE3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_1E8A")

    ChrTalk(    #105
        0xFE,
        (
            "噜噜噜-噜噜-⊙\x01",
            "啦啦啦啦啦⊙\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0xFE,
        (
            "打扫起来～⊙\x01",
            "心也亮晶晶～⊙\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1EE3")

    label("loc_1E8A")


    ChrTalk(    #107
        0xFE,
        (
            "怎么说这个房间\x01",
            "似乎是用作作战会议室呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0xFE,
        (
            "……啊不好，\x01",
            "必须早点扫除完毕才行。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x6)

    label("loc_1EE3")

    TalkEnd(0x14)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1EFE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_1EFE")
    SetChrFlags(0xFE, 0x10)

    label("loc_1EFE")

    Return()

    # Function_11_1CE2 end

    def Function_12_1EFF(): pass

    label("Function_12_1EFF")

    TalkBegin(0x15)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1F68")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1F65")

    ChrTalk(    #109
        0xFE,
        (
            "原来这里\x01",
            "来访的人就少……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0xFE,
        (
            "没有导力的时代也活过，\x01",
            "并不觉得特别困难啦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F65")

    Jump("loc_2138")

    label("loc_1F68")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2138")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_1FD4")

    ChrTalk(    #111
        0xFE,
        (
            "士兵们把瓦雷利亚湖的\x01",
            "周边地图拿走了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0xFE,
        (
            "说要在湖里找人偶\x01",
            "嘿，到底说什么呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2138")

    label("loc_1FD4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 3)), scpexpr(EXPR_END)), "loc_205D")

    ChrTalk(    #113
        0xFE,
        (
            "到签字仪式结束之前\x01",
            "据说市民禁止进出。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0xFE,
        (
            "呼，这下\x01",
            "这个房间要变得更加安静了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0xFE,
        (
            "这样的话是不是劝劝\x01",
            "士兵们也看看书呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2138")

    label("loc_205D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C2, 7)), scpexpr(EXPR_END)), "loc_20FC")

    ChrTalk(    #116
        0xFE,
        (
            "读书就是要\x01",
            "安静的环境。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0xFE,
        (
            "在这一点上，这里可说\x01",
            "是无可挑剔的地方……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0xFE,
        (
            "不过访问的市民大半\x01",
            "都是来看庭园或者展览室的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0xFE,
        "真是有点寂寞啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2138")

    label("loc_20FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_2138")

    ChrTalk(    #120
        0xFE,
        "在找什么书吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0xFE,
        (
            "……女孩子？\x01",
            "哦，没看到啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2138")

    TalkEnd(0x15)
    Return()

    # Function_12_1EFF end

    def Function_13_213C(): pass

    label("Function_13_213C")

    TalkBegin(0x16)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_21AC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_21AC")

    ChrTalk(    #122
        0xFE,
        (
            "今天是作为爱尔莎大使的陪同\x01",
            "来到这个离宫了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0xFE,
        (
            "爱尔莎大使的话\x01",
            "在访问议员的房间呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_21AC")

    TalkEnd(0x16)
    Return()

    # Function_13_213C end

    def Function_14_21B0(): pass

    label("Function_14_21B0")

    TalkBegin(0x17)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2279")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C2, 7)), scpexpr(EXPR_END)), "loc_2226")

    ChrTalk(    #124
        0xFE,
        (
            "哦～这是利贝尔的先王\x01",
            "埃德加Ⅲ世\x01",
            "生前最爱用的椅子啊～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0xFE,
        (
            "原来如此～\x01",
            "确实有高贵的感觉。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2279")

    label("loc_2226")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_2279")

    ChrTalk(    #126
        0xFE,
        (
            "这个共和国大使\x01",
            "赠呈的壶真漂亮啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0xFE,
        (
            "果然壶\x01",
            "还是要共和国的东西好啊～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2279")

    TalkEnd(0x17)
    Return()

    # Function_14_21B0 end

    def Function_15_227D(): pass

    label("Function_15_227D")

    TalkBegin(0x18)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2344")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C2, 7)), scpexpr(EXPR_END)), "loc_22E5")

    ChrTalk(    #128
        0xFE,
        (
            "姐姐，在看说明之前，\x01",
            "可是说了椅子不少坏话啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0xFE,
        "……真是的，够起劲的。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2344")

    label("loc_22E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_2344")

    ChrTalk(    #130
        0xFE,
        (
            "姐姐看的\x01",
            "是帝国制作的壶啦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0xFE,
        (
            "稍微往下看，\x01",
            "就写着说明嘛……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0xFE,
        "真是受不了了。\x02",
    )

    CloseMessageWindow()

    label("loc_2344")

    TalkEnd(0x18)
    Return()

    # Function_15_227D end

    def Function_16_2348(): pass

    label("Function_16_2348")

    TalkBegin(0x19)

    ChrTalk(    #133
        0x19,
        (
            "#720F我相信……\x02\x03",

            "总有一天阁下\x01",
            "会察觉到自己的使命。\x02\x03",

            "到那天为止我菲利普，粉身碎骨\x01",
            "也要诚心诚意服侍他。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x19)
    Return()

    # Function_16_2348 end

    def Function_17_23BA(): pass

    label("Function_17_23BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_23C9")
    Call(0, 18)
    Jump("loc_2425")

    label("loc_23C9")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #134
        "\x07\x05有聚餐用的大桌子。\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(    #135
        "\x07\x05桌子下没有任何人。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    TalkEnd(0xFF)

    label("loc_2425")

    Return()

    # Function_17_23BA end

    def Function_18_2426(): pass

    label("Function_18_2426")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2444")
    Call(0, 32)
    Call(0, 33)
    FadeToBright(0, 0)

    label("loc_2444")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #136
        "\x07\x05有聚餐用的大桌子。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_277B")
    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x101, -17710, 0, 44750, 360)
    SetChrPos(0x104, -17930, 0, 43630, 360)
    SetChrPos(0xF7, -19230, 0, 43930, 45)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_24F5")
    SetChrPos(0x105, -16800, 0, 43480, 360)
    Jump("loc_2536")

    label("loc_24F5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2517")
    SetChrPos(0x107, -16800, 0, 43480, 360)
    Jump("loc_2536")

    label("loc_2517")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2536")
    SetChrPos(0x108, -16800, 0, 43480, 360)

    label("loc_2536")

    OP_6D(-17730, 0, 44700, 0)
    OP_67(0, 6660, -10000, 0)
    OP_6B(1380, 0)
    OP_6C(40000, 0)
    OP_6E(504, 0)
    Sleep(500)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #137
        0x101,
        (
            "#1004F难不成，藏在\x01",
            "这下面……\x02",
        )
    )

    CloseMessageWindow()
    Fade(250)
    SetChrChipByIndex(0x101, 2)
    OP_0D()
    Sleep(500)

    ChrTalk(    #138
        0x101,
        (
            "#1015F……………………………\x02\x03",

            "#1016F哈哈……\x01",
            "果然不在呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0x104,
        (
            "#032F咳咳，这个且不说……\x02\x03",

            "现在你的服装\x01",
            "还是不要随便蹲下比较好。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0x101,
        "#1004F哎？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0x104,
        "#031F怎么说呢……快看到了。\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_95(0x101, 0x0, 0x0, 0x0, 0x320, 0x2EE0)
    SetChrChipByIndex(0x101, 65535)
    Sleep(500)
    TurnDirection(0x101, 0x104, 600)

    ChrTalk(    #142
        0x101,
        "#1019F～～～呜～～～～\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2726")

    ChrTalk(    #143
        0x106,
        (
            "#552F刚才是你不对。\x02\x03",

            "穿的不是紧身裤\x01",
            "稍微注意点吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_275A")

    label("loc_2726")


    ChrTalk(    #144
        0x103,
        (
            "#524F刚才是你不对。\x02\x03",

            "穿的是裙子\x01",
            "请稍微当心点。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_275A")


    ChrTalk(    #145
        0x101,
        "#1013F呜呜……知道了啦。\x02",
    )

    CloseMessageWindow()
    Jump("loc_29C1")

    label("loc_277B")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x101, -17710, 0, 44750, 360)
    SetChrPos(0xF7, -17930, 0, 43630, 360)
    SetChrPos(0xF8, -19230, 0, 43930, 45)
    SetChrPos(0xF9, -16800, 0, 43480, 360)
    OP_6D(-17730, 0, 44700, 0)
    OP_67(0, 6660, -10000, 0)
    OP_6B(1380, 0)
    OP_6C(40000, 0)
    OP_6E(504, 0)
    Sleep(500)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #146
        0x101,
        (
            "#1004F难不成，藏在\x01",
            "这下面……\x02",
        )
    )

    CloseMessageWindow()
    Fade(250)
    SetChrChipByIndex(0x101, 2)
    OP_0D()
    Sleep(500)

    ChrTalk(    #147
        0x101,
        (
            "#1015F……………………………\x02\x03",

            "#1016F哈哈……\x01",
            "果然不在呢。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_28DA")

    ChrTalk(    #148
        0x106,
        (
            "#551F喂喂，艾丝蒂尔。\x02\x03",

            "穿的不是紧身裤,\x01",
            "别那么随便就蹲下。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_291A")

    label("loc_28DA")


    ChrTalk(    #149
        0x103,
        (
            "#025F我说艾丝蒂尔……\x02\x03",

            "穿的不是紧身裤\x01",
            "别那么随便就蹲下啦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_291A")


    ChrTalk(    #150
        0x101,
        "#1013F啊……\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_95(0x101, 0x0, 0x0, 0x0, 0x320, 0x2EE0)
    SetChrChipByIndex(0x101, 65535)
    Sleep(500)
    TurnDirection(0x101, 0xF7, 400)

    ChrTalk(    #151
        0x101,
        "#1008F嘿嘿，不好意思。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_29A8")

    ChrTalk(    #152
        0x106,
        "#552F真是的……\x02",
    )

    CloseMessageWindow()
    Jump("loc_29C1")

    label("loc_29A8")


    ChrTalk(    #153
        0x103,
        "#524F唉，真是的……\x02",
    )

    CloseMessageWindow()

    label("loc_29C1")

    OP_A2(0x160E)
    OP_28(0x89, 0x1, 0x8)
    FadeToDark(500, 0, -1)
    OP_0D()
    OP_6D(-17930, 0, 43830, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, -17930, 0, 43830, 180)
    SetChrPos(0x1, -17930, 0, 43830, 180)
    SetChrPos(0x2, -17930, 0, 43830, 180)
    SetChrPos(0x3, -17930, 0, 43830, 180)
    Sleep(500)
    FadeToBright(500, 0)
    EventEnd(0x0)
    Return()

    # Function_18_2426 end

    def Function_19_2A67(): pass

    label("Function_19_2A67")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C2, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2BC8")
    EventBegin(0x1)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #154
        "\x07\x05有大个的绯红色的壶。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #155
        0x101,
        (
            "#1006F解放离宫的时候，这个下面\x01",
            "贴着备用钥匙吧。\x02\x03",

            "这壶相当大\x01",
            "说不定藏在里面……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2B61")

    ChrTalk(    #156
        0x106,
        (
            "#053F到底是不可能啊。\x02\x03",

            "#555F最主要是，那么小的口\x01",
            "怎么进去嘛。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B9E")

    label("loc_2B61")


    ChrTalk(    #157
        0x103,
        (
            "#025F怎么可能嘛……\x02\x03",

            "#524F首先，那么小的口\x01",
            "怎么进得去？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B9E")


    ChrTalk(    #158
        0x101,
        "#1008F嘿嘿，这倒也是。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x160F)
    OP_28(0x89, 0x1, 0x10)
    EventEnd(0x1)
    Jump("loc_2C0E")

    label("loc_2BC8")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #159
        "\x07\x05有大个的绯红色的壶。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    TalkEnd(0xFF)

    label("loc_2C0E")

    Return()

    # Function_19_2A67 end

    def Function_20_2C0F(): pass

    label("Function_20_2C0F")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2C26")
    Call(0, 32)
    Call(0, 33)

    label("loc_2C26")

    SetChrFlags(0x101, 0x80)
    SetChrFlags(0xF7, 0x80)
    SetChrFlags(0xF8, 0x80)
    SetChrFlags(0xF9, 0x80)
    SetChrPos(0x9, -15000, 0, -43330, 180)
    OP_4A(0x9, 255)
    OP_67(0, 6640, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    OP_69(0x9, 0x0)
    FadeToBright(2000, 0)
    OP_A2(0x0)
    OP_43(0x9, 0x1, 0x0, 0x15)
    OP_0D()
    Sleep(1000)
    OP_4A(0x9, 1)

    ChrTalk(    #160
        0x9,
        (
            "#222F好慢！太慢了！\x02\x03",

            "菲利普这家伙……\x01",
            "买杂志和炸面圈\x01",
            "得花多少时间啊！\x02",
        )
    )

    CloseMessageWindow()
    OP_4B(0x9, 1)
    OP_A3(0x0)
    OP_A6(0x1)
    OP_62(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_36FD")

    def lambda_2D1E():
        OP_6D(-14340, 0, -44170, 1000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_2D1E)
    OP_43(0x101, 0x1, 0x0, 0x16)
    OP_43(0xF7, 0x1, 0x0, 0x17)
    OP_43(0xF8, 0x1, 0x0, 0x18)
    OP_43(0xF9, 0x1, 0x0, 0x19)
    OP_8C(0x9, 180, 400)
    Sleep(500)

    ChrTalk(    #161
        0x9,
        (
            "#224F#5P喂，菲利普！\x01",
            "要我等多久才……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #162
        0x101,
        "#1004F#6P啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #163
        0x9,
        "#223F#5P你、你、你……\x02",
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #164
        0x9,
        "#226F#3S#5P你们是～！？\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2E3E")

    ChrTalk(    #165
        0x106,
        (
            "#555F#2P怎么？\x01",
            "这个奇怪的大叔。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E75")

    label("loc_2E3E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2E75")

    ChrTalk(    #166
        0x103,
        (
            "#023F#2P哎呀……\x01",
            "记得那时在城里……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E75")


    ChrTalk(    #167
        0x101,
        (
            "#1025F#6P杜南公爵……\x01",
            "在这种地方啊。\x02\x03",

            "#1016F嗯，还好吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #168
        0x9,
        (
            "#222F#5P哎，装模作样！\x02\x03",

            "都是因为你们,\x01",
            "都是因为你们……\x02\x03",

            "#224F我要被迫在这里\x01",
            "过软禁生活！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #169
        0x101,
        (
            "#1007F#6P嗯～就算你说\x01",
            "是因为我们……\x02\x03",

            "但上了理查德上校的套,\x01",
            "算是公爵先生自作自受吧。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2FEB")

    ChrTalk(    #170
        0x108,
        (
            "#070F不过，只被软禁\x01",
            "应该算好运了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #171
        0x104,
        (
            "#035F呼，这要是在埃雷波尼亚\x01",
            "就算是皇族也要处以极刑啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_30CC")

    label("loc_2FEB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3058")

    ChrTalk(    #172
        0x108,
        (
            "#074F不过，只被软禁\x01",
            "应该算好运了。\x02\x03",

            "#070F要是在其他国家，就算是王族\x01",
            "也免不了要服刑吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_30CC")

    label("loc_3058")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_30CC")

    ChrTalk(    #173
        0x104,
        (
            "#035F呼，身为利贝尔王族\x01",
            "你应该谢天谢地才是。\x02\x03",

            "#030F这要是在埃雷波尼亚\x01",
            "就算是皇族也要处以极刑啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_30CC")


    ChrTalk(    #174
        0x9,
        (
            "#226F#5P呜……\x02\x03",

            "#222F哼、哼……\x01",
            "的确幽禁陛下\x01",
            "是过分了点，这我承认。\x02\x03",

            "虽然是被理查德教唆,\x01",
            "但这个还是不应该的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #175
        0x101,
        "#1006F#6P咦，相当微妙的台词嘛？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #176
        0x9,
        (
            "#225F#5P哼，别误会。\x01",
            "我也很敬爱陛下。\x02\x03",

            "无论作为君主还是姑母大人\x01",
            "都是无可挑剔的人物。\x02\x03",

            "#224F但是，要指明科洛蒂娅那小丫头\x01",
            "当下任国王\x01",
            "我无论如何也不能接受！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #177
        0x101,
        (
            "#1009F#6P喂……\x01",
            "我可听不下去了。\x02\x03",

            "科洛丝头脑好又肯用功\x01",
            "也有服众的气量。\x02\x03",

            "被公爵先生称做小丫头\x01",
            "这太没道理了吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #178
        0x9,
        (
            "#220F#5P哼，我说的\x01",
            "可不是这些。\x02\x03",

            "诚然，确实像陛下说的那样\x01",
            "那女孩是有才能。\x02\x03",

            "但是，到底科洛蒂娅\x01",
            "真的有成为女王的精神准备吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #179
        0x101,
        "#1026F#6P啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #180
        0x9,
        (
            "#220F#5P一直以来都是这样，\x01",
            "她不太愿意在公务场合出面。\x02\x03",

            "如果以知名度来说，我\x01",
            "更加为国民所知吧。\x02\x03",

            "也就是说，那女孩是没有\x01",
            "立于人上的觉悟不是吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #181
        0x101,
        "#1003F#6P这，这个……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #182
        0x9,
        (
            "#222F#5P听说那女孩，隐藏身份\x01",
            "过着学生生活。\x02\x03",

            "还在孤儿院什么的\x01",
            "长期逗留不是吗。\x02\x03",

            "#225F比起那些，出席公共事务\x01",
            "广为人知……\x02\x03",

            "#224F这才是王族的义务吧！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #183
        0x101,
        (
            "#1002F#6P…………………………\x02\x03",

            "#1007F我对王族的义务什么的\x01",
            "完全不清楚……\x02\x03",

            "说不定公爵先生的话\x01",
            "也有一番道理。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #184
        0x9,
        "#221F#5P哇哈哈，当然了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #185
        0x101,
        (
            "#1002F#6P但是，我只对你这么说。\x02\x03",

            "科洛丝现在，虽然烦恼\x01",
            "却也在努力寻找答案。\x02\x03",

            "#1005F至少，比以软禁为借口\x01",
            "什么都不做的公爵先生强！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #186
        0x9,
        "#226F#5P什、什么！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #187
        0x101,
        (
            "#1006F#6P科洛丝有没有女王的资格\x01",
            "要做判断\x01",
            "也等看了那个答案之后吧。\x02\x03",

            "大概，公爵先生\x01",
            "也能理解吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #188
        0x9,
        (
            "#226F#5P唔……\x02\x03",

            "#222F哼、哼，白痴一样。\x02\x03",

            "#224F哎，真不爽！\x01",
            "赶快从房间出去！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #189
        0x101,
        (
            "#1005F#6P还用你说！\x02\x03",

            "#1007F……啊，在这之前。\x02\x03",

            "#1015F这里有没有个穿白衣服的\x01",
            "女孩子来过？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #190
        0x9,
        (
            "#222F#5P那是什么……\x02\x03",

            "#224F我一直待在这里！\x01",
            "没看到那样的小丫头！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #191
        0x101,
        "#1019F#6P啊是吗，打扰了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_41AC")

    label("loc_36FD")


    def lambda_3703():
        OP_6D(-14340, 0, -44170, 1000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_3703)
    OP_43(0x101, 0x1, 0x0, 0x16)
    OP_43(0x105, 0x1, 0x0, 0x17)
    OP_43(0xF7, 0x1, 0x0, 0x18)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3742")
    OP_43(0x104, 0x1, 0x0, 0x19)
    Jump("loc_376F")

    label("loc_3742")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_375A")
    OP_43(0x107, 0x1, 0x0, 0x19)
    Jump("loc_376F")

    label("loc_375A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_376F")
    OP_43(0x108, 0x1, 0x0, 0x19)

    label("loc_376F")

    OP_8C(0x9, 180, 400)
    Sleep(500)

    ChrTalk(    #192
        0x9,
        (
            "#224F#5P喂，菲利普！\x01",
            "要我等多久才……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #193
        0x101,
        "#1004F#6P啊……\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x105, 0x1)

    ChrTalk(    #194
        0x105,
        "#043F#2P啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #195
        0x9,
        "#223F#5P你、你、你……\x02",
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #196
        0x9,
        "#226F#3S#5P你们是～！？\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_387A")

    ChrTalk(    #197
        0x106,
        (
            "#555F#6P怎么？\x01",
            "这个奇怪的大叔。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_38B3")

    label("loc_387A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_38B3")

    ChrTalk(    #198
        0x103,
        (
            "#023F#6P哎呀……\x01",
            "记得那时在城里来着。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_38B3")


    ChrTalk(    #199
        0x101,
        (
            "#1019F#6P杜南公爵……\x01",
            "在这种地方啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #200
        0x105,
        (
            "#542F#2P王叔……\x01",
            "那个，还好吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #201
        0x9,
        (
            "#222F#5P哎，装模作样！\x02\x03",

            "都是因为你们,\x01",
            "都是因为你们……\x02\x03",

            "#224F我要被迫在这里\x01",
            "过软禁生活！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #202
        0x101,
        (
            "#1007F#6P嗯～就算你说\x01",
            "是因为我们……\x02\x03",

            "但上了理查德上校的套\x01",
            "是公爵先生自作自受吧。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3A27")

    ChrTalk(    #203
        0x108,
        (
            "#074F#2P不过，只被软禁\x01",
            "应该算好运了。\x02\x03",

            "#070F要是在其他国家，就算是王族\x01",
            "也免不了要服刑吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A9E")

    label("loc_3A27")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3A9E")

    ChrTalk(    #204
        0x104,
        (
            "#035F#2P呼，身为利贝尔王族\x01",
            "你应该谢天谢地才是。\x02\x03",

            "#030F这要是在埃雷波尼亚\x01",
            "就算是皇族也要处以极刑啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3A9E")


    ChrTalk(    #205
        0x9,
        (
            "#226F#5P呜……\x02\x03",

            "#222F哼、哼……\x01",
            "的确幽禁陛下\x01",
            "是过分了点，这我承认。\x02\x03",

            "虽然是被理查德教唆,\x01",
            "但这个还是不应该的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #206
        0x101,
        "#1006F#6P咦，相当微妙的台词嘛？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #207
        0x9,
        (
            "#225F#5P哼，别误会。\x01",
            "我也很敬爱陛下。\x02\x03",

            "无论作为君主还是姑母大人\x01",
            "都是无可挑剔的人物。\x02\x03",

            "#224F但是，科洛蒂娅！\x02\x03",

            "像你这种小丫头\x01",
            "当下任国王\x01",
            "我无论如何也不能接受！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #208
        0x105,
        "#049F#2P………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #209
        0x101,
        (
            "#1005F#6P慢、慢着！\x01",
            "我可听不下去了！\x02\x03",

            "科洛丝头脑好又肯用功\x01",
            "也有服众的气量！\x02\x03",

            "被公爵先生称做小丫头\x01",
            "有什么理由……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #210
        0x105,
        (
            "#047F#2P……艾丝蒂尔，不必说了。\x02\x03",

            "#043F以前也说过，我……\x01",
            "还没有继承王位的精神准备。\x02\x03",

            "会让王叔感到不快\x01",
            "也是理所当然的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #211
        0x101,
        "#1026F#6P科洛丝……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #212
        0x9,
        (
            "#220F#5P嗯，说得真微妙。\x02\x03",

            "一直以来都是这样，\x01",
            "不太愿意在公务场合出面。\x02\x03",

            "如果以知名度来说，我\x01",
            "更加为国民所知吧。\x02\x03",

            "这也就是，你没有立于人上\x01",
            "的精神准备。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #213
        0x105,
        "#043F#2P…………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #214
        0x9,
        (
            "#222F#5P听说你隐藏身份\x01",
            "过着学生生活。\x02\x03",

            "还在孤儿院什么的\x01",
            "长期逗留不是吗。\x02\x03",

            "#225F比起那些，出席公共事务\x01",
            "并广为人知……\x02\x03",

            "#224F这才是王族的义务吧！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #215
        0x105,
        "#049F#2P……那是………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #216
        0x101,
        (
            "#1002F#6P…………………………\x02\x03",

            "#1007F我对王族的义务什么的\x01",
            "完全不清楚……\x02\x03",

            "说不定公爵先生的话\x01",
            "也有一番道理。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #217
        0x9,
        "#221F#5P哇哈哈，当然了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #218
        0x101,
        (
            "#1002F#6P但是，我只对你这么说。\x02\x03",

            "科洛丝现在，虽然烦恼\x01",
            "却也在努力寻找答案。\x02\x03",

            "#1005F至少，比以软禁为借口\x01",
            "什么都不做的公爵先生强！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #219
        0x9,
        "#226F#5P什、什么！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #220
        0x105,
        (
            "#049F#2P艾丝蒂尔……\x02\x03",

            "#043F……那个，杜南王叔。\x02\x03",

            "我现在，正借助\x01",
            "艾丝蒂尔的力量\x01",
            "在寻找自己的道路。\x02\x03",

            "#047F我当女王的资格\x01",
            "到底有还是没有……\x02\x03",

            "不久的将来，希望也能\x01",
            "让王叔看到答案。\x02\x03",

            "#042F所以在这之前……\x01",
            "能请您耐心等待吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #221
        0x9,
        (
            "#226F#5P唔……\x02\x03",

            "#222F哼、哼，白痴一样。\x02\x03",

            "#224F哎，真不爽！\x01",
            "赶快从房间出去！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #222
        0x101,
        (
            "#1005F#6P还用你说！\x02\x03",

            "#1007F……啊，在这之前。\x02\x03",

            "#1015F这里有没有个穿白衣服的\x01",
            "女孩子来过？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #223
        0x9,
        (
            "#222F#5P那是什么……\x02\x03",

            "#224F我一直待在这里！\x01",
            "没看到那样的小丫头！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #224
        0x101,
        "#1019F#6P啊是吗，打扰了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #225
        0x105,
        "#047F……失陪了。\x02",
    )

    CloseMessageWindow()

    label("loc_41AC")

    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(500)
    OP_A2(0x10F1)
    OP_A2(0x1612)
    NewScene("ED6_DT21/T4303   ._SN", 100, 0, 0)
    IdleLoop()
    EventEnd(0x0)
    Return()

    # Function_20_2C0F end

    def Function_21_41CE(): pass

    label("Function_21_41CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_4200")
    OP_8E(0xFE, 0xFFFFC950, 0x0, 0xFFFF56BE, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFC180, 0x0, 0xFFFF56BE, 0x7D0, 0x0)
    Jump("Function_21_41CE")

    label("loc_4200")

    OP_22(0x6, 0x0, 0x64)
    OP_8E(0xFE, 0xFFFFC568, 0x0, 0xFFFF56BE, 0x7D0, 0x0)
    OP_A2(0x1)
    Return()

    # Function_21_41CE end

    def Function_22_421D(): pass

    label("Function_22_421D")

    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, -14130, 0, -49500, 180)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_4244():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4244)
    OP_8E(0xFE, 0xFFFFC8EC, 0x0, 0xFFFF4278, 0x9C4, 0x0)
    OP_8F(0xFE, 0xFFFFC73E, 0x0, 0xFFFF4DFE, 0x9C4, 0x0)
    Return()

    # Function_22_421D end

    def Function_23_4279(): pass

    label("Function_23_4279")

    Sleep(500)
    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, -14130, 0, -49500, 180)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_42A5():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_42A5)
    OP_8E(0xFE, 0xFFFFC8EC, 0x0, 0xFFFF4278, 0x9C4, 0x0)
    OP_8F(0xFE, 0xFFFFCA86, 0x0, 0xFFFF4BEC, 0x9C4, 0x0)
    Return()

    # Function_23_4279 end

    def Function_24_42DA(): pass

    label("Function_24_42DA")

    Sleep(1000)
    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, -14130, 0, -49500, 180)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_4306():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4306)
    OP_8E(0xFE, 0xFFFFC8EC, 0x0, 0xFFFF4278, 0x9C4, 0x0)
    OP_8F(0xFE, 0xFFFFC45A, 0x0, 0xFFFF4908, 0x9C4, 0x0)
    Return()

    # Function_24_42DA end

    def Function_25_433B(): pass

    label("Function_25_433B")

    Sleep(1500)
    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, -14130, 0, -49500, 180)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_4367():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4367)
    OP_8E(0xFE, 0xFFFFC84C, 0x0, 0xFFFF46CE, 0x9C4, 0x0)
    Return()

    # Function_25_433B end

    def Function_26_4388(): pass

    label("Function_26_4388")

    EventBegin(0x0)
    Fade(1000)
    OP_4A(0x9, 255)
    OP_8C(0x9, 180, 0)
    SetChrPos(0x12F, -16400, 0, -39920, 0)
    SetChrPos(0x101, -15400, 0, -39750, 0)
    SetChrPos(0xF7, -15710, 0, -41000, 0)
    SetChrPos(0xF8, -16850, 0, -41250, 0)
    SetChrPos(0xF9, -14720, 0, -41100, 0)
    OP_6D(-15710, 0, -39150, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()

    ChrTalk(    #226
        0x9,
        "#222F#5P……怎么，还在啊？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #227
        0x12F,
        "#264F（盯……）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #228
        0x9,
        "#223F#5P怎、怎么了你？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #229
        0x12F,
        (
            "#260F对了，姐姐。\x02\x03",

            "这位大叔\x01",
            "怎么梳个这么有趣的发型？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #230
        0x9,
        "#226F#5P你、你说什么～！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #231
        0x101,
        (
            "#1016F#4P哎，算了算了。\x01",
            "小孩子嘛……\x02\x03",

            "#1006F顺带一提，这位大叔\x01",
            "搞笑的不只是发型。\x02\x03",

            "服装和性格也很有趣哦～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #232
        0x12F,
        "#261F哈哈哈，这样啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #233
        0x9,
        (
            "#226F#5P这算是\x01",
            "帮我吗～！！\x02\x03",

            "#224F哎，带着这小丫头\x01",
            "赶快从这房间里出去！\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x9, 0, 400)
    OP_4B(0x9, 255)
    OP_A2(0x1613)
    EventEnd(0x0)
    Return()

    # Function_26_4388 end

    def Function_27_45C0(): pass

    label("Function_27_45C0")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_45E0")
    Call(0, 32)
    Call(0, 33)
    FadeToBright(0, 0)

    label("loc_45E0")

    Fade(1000)
    OP_4A(0x8, 255)
    SetChrPos(0x101, -13290, 0, 18890, 45)
    SetChrPos(0xF7, -12530, 0, 18230, 0)
    SetChrPos(0xF8, -13740, 0, 17710, 45)
    SetChrPos(0xF9, -14560, 0, 18430, 45)
    OP_6D(-12740, 0, 19290, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2D0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_487F")

    ChrTalk(    #234
        0x8,
        "怎样，找到了吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #235
        0x101,
        (
            "#1007F没有，很遗憾。\x02\x03",

            "看起来可疑的地方\x01",
            "都调查了一遍倒是。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #236
        0x8,
        "难、难道说……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #237
        0x8,
        (
            "出去艾尔贝离宫外边\x01",
            "的可能性……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4736")

    ChrTalk(    #238
        0x106,
        (
            "#552F可恶……\x01",
            "那可就麻烦了呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_475E")

    label("loc_4736")


    ChrTalk(    #239
        0x103,
        (
            "#522F嗯……\x01",
            "如果是那样就麻烦了呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_475E")


    ChrTalk(    #240
        0x101,
        (
            "#1015F嗯～只不过是躲猫猫\x01",
            "我想不会的……\x02\x03",

            "藏在一般能去的地方\x01",
            "是规则嘛。\x02\x03",

            "#1006F大概，藏在意想不到的地方\x01",
            "的可能性会比较高。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_482E")

    ChrTalk(    #241
        0x106,
        (
            "#051F原来如此，偶尔\x01",
            "你也会说点敏锐的话嘛。\x02\x03",

            "再稍微找找看？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4879")

    label("loc_482E")


    ChrTalk(    #242
        0x103,
        (
            "#021F呵呵，不愧是艾丝蒂尔。\x01",
            "对玩耍的事很敏锐呢。\x02\x03",

            "#020F再稍微找找看？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4879")

    OP_A2(0x1682)
    Jump("loc_48F8")

    label("loc_487F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_48C3")

    ChrTalk(    #243
        0x106,
        (
            "#052F怎么办，艾丝蒂尔。\x02\x03",

            "还是在离宫里找找看？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_48F8")

    label("loc_48C3")


    ChrTalk(    #244
        0x103,
        (
            "#023F怎么办呢，艾丝蒂尔。\x02\x03",

            "还是在离宫里找找看？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_48F8")

    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【再稍微找找】\x01",            # 0
            "【死心考虑别的办法】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_4963"),
        (1, "loc_498D"),
        (SWITCH_DEFAULT, "loc_4ED0"),
    )


    label("loc_4963")


    ChrTalk(    #245
        0x101,
        (
            "#1006F嗯，稍微改变想法\x01",
            "找找看吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4ED0")

    label("loc_498D")


    ChrTalk(    #246
        0x101,
        (
            "#1007F嗯～既然陷入瓶颈\x01",
            "最好是坦率地投降吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #247
        0x8,
        "投降就是说？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #248
        0x101,
        (
            "#1015F嗯，躲猫猫时\x01",
            "要是鬼投降了……\x02\x03",

            "#1006F鬼哭着输～了！\x01",
            "躲猫猫完～了！这样\x01",
            "一边说一边到处转转就行了。\x02\x03",

            "要是那样的话，那个女孩子也\x01",
            "一定会出来的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #249
        0x8,
        "原，原来如此……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4ACA")

    ChrTalk(    #250
        0x107,
        (
            "#067F嘿嘿，有点\x01",
            "难为情啊……\x02\x03",

            "为了请她出来\x01",
            "没办法了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4B5D")

    label("loc_4ACA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4B16")

    ChrTalk(    #251
        0x105,
        (
            "#045F呵呵，有点\x01",
            "难为情啊……\x02\x03",

            "为了请她出来\x01",
            "没办法了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4B5D")

    label("loc_4B16")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4B5D")

    ChrTalk(    #252
        0x104,
        (
            "#035F呼，稍微有点\x01",
            "难为情啊。\x02\x03",

            "#037F我就开心地说吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4B5D")


    ChrTalk(    #253
        0x101,
        (
            "#1006F那么各位，\x01",
            "练习说一次看看吧。\x02\x03",

            "#1018F鬼哭着输～了！\x01",
            "躲猫猫完～了！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    SetMessageWindowPos(-1, 160, -1, -1)
    SetChrName("全员")

    AnonymousTalk(    #254
        (
            "\x07\x00#3S鬼哭着输～了！\x01",
            "躲猫猫完～了！\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrFlags(0xA, 0x4)
    SetChrPos(0xA, -10290, -500, 19160, 0)

    NpcTalk(    #255
        0xA,
        "声音",
        "#5P喵呜⊙\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0xF7, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4C71")
    OP_62(0xF8, 0x0, 2300, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_4CA5")

    label("loc_4C71")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4C93")
    OP_62(0xF8, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_4CA5")

    label("loc_4C93")

    OP_62(0xF8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)

    label("loc_4CA5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4CC7")
    OP_62(0xF9, 0x0, 2300, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_4CFB")

    label("loc_4CC7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4CE9")
    OP_62(0xF9, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_4CFB")

    label("loc_4CE9")

    OP_62(0xF9, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)

    label("loc_4CFB")

    OP_62(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_63(0x101)
    OP_63(0xF7)
    OP_63(0xF8)
    OP_63(0xF9)
    OP_63(0x8)

    def lambda_4D27():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4D27)
    Sleep(50)

    def lambda_4D3A():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_4D3A)
    Sleep(50)

    def lambda_4D4D():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_4D4D)
    Sleep(50)

    def lambda_4D60():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_4D60)
    Sleep(50)

    def lambda_4D73():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_4D73)
    Sleep(500)

    ChrTalk(    #256
        0x101,
        "#1008F刚，刚才的声音是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #257
        0x8,
        "难道…\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #258
        0xA,
        "声音",
        "#5P嘻嘻，玲赢了哦。\x02",
    )

    CloseMessageWindow()

    def lambda_4DD0():

        label("loc_4DD0")

        TurnDirection(0xFE, 0xA, 400)
        OP_48()
        Jump("loc_4DD0")

    QueueWorkItem2(0x8, 1, lambda_4DD0)

    def lambda_4DE1():
        OP_6D(-11020, 0, 19860, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4DE1)
    ClearChrFlags(0xA, 0x80)
    OP_8E(0xA, 0xFFFFD95E, 0x0, 0x4F9C, 0x3E8, 0x0)
    OP_44(0x8, 0x1)
    OP_8C(0xA, 225, 400)
    WaitChrThread(0x101, 0x2)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #259
        0x101,
        (
            "#1004F#6P啊～！？\x01",
            "在艾尔·雷登遇见的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #260
        0xA,
        (
            "#5P#261F哈哈哈……\x01",
            "姐姐，好久不见呢。\x02\x03",

            "还记得玲的事\x01",
            "玲好高兴。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrFlags(0xA, 0x80)
    OP_A2(0x1615)
    OP_28(0x89, 0x1, 0x800)
    OP_28(0x89, 0x1, 0x1000)
    Call(0, 29)
    Jump("loc_4ED0")

    label("loc_4ED0")

    OP_4B(0x8, 255)
    EventEnd(0x0)
    Return()

    # Function_27_45C0 end

    def Function_28_4ED7(): pass

    label("Function_28_4ED7")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4EF7")
    Call(0, 32)
    Call(0, 33)
    FadeToBright(0, 0)

    label("loc_4EF7")

    Fade(1000)
    SetChrPos(0x101, -9950, 0, 20590, 180)
    SetChrPos(0xF7, -12280, 0, 18190, 45)
    SetChrPos(0xF8, -10910, 0, 18200, 0)
    SetChrPos(0xF9, -9550, 0, 18200, 0)
    OP_6D(-10150, 0, 20240, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()
    Sleep(500)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #261
        (
            "\x07\x05艾丝蒂尔为慎重起见\x01",
            "查看了一下柜台底下。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Fade(250)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 2)
    SetChrSubChip(0x101, 5)
    OP_0D()
    Sleep(500)
    OP_62(0x101, 0xC8, 1400, 0x2, 0x7, 0x50, 0x1)
    Sleep(1000)

    ChrTalk(    #262
        0x101,
        "#1004F咦……\x02",
    )

    CloseMessageWindow()
    OP_4A(0x8, 255)
    TurnDirection(0x8, 0x101, 400)
    Sleep(500)

    ChrTalk(    #263
        0x8,
        "？？？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #264
        0x8,
        "怎么了？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #265
        0x101,
        (
            "#1016F啊哈哈……\x02\x03",

            "没什么怎么了……\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0xA, 0x4)
    SetChrPos(0xA, -10290, -500, 19160, 0)

    NpcTalk(    #266
        0xA,
        "声音",
        "#5P呜喵～……\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #267
        0xA,
        "声音",
        "#5P啊～啊，玲输了啊。\x02",
    )

    CloseMessageWindow()
    OP_62(0xF7, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_50FA")
    OP_62(0xF8, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_5138")

    label("loc_50FA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5121")
    OP_62(0xF8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_5138")

    label("loc_5121")

    OP_62(0xF8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_5138")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_515F")
    OP_62(0xF9, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_519D")

    label("loc_515F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5186")
    OP_62(0xF9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_519D")

    label("loc_5186")

    OP_62(0xF9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_519D")

    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    Fade(250)
    ClearChrFlags(0x101, 0x2)
    SetChrSubChip(0x101, 0)
    SetChrChipByIndex(0x101, 65535)
    OP_0D()
    Sleep(250)

    def lambda_51D9():
        OP_6D(-10460, 0, 20440, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_51D9)
    OP_8F(0x101, 0xFFFFD882, 0x0, 0x5352, 0x3E8, 0x0)
    ClearChrFlags(0xA, 0x80)
    OP_8E(0xA, 0xFFFFD95E, 0x0, 0x4F9C, 0x3E8, 0x0)
    OP_44(0x8, 0x1)
    OP_8C(0xA, 225, 400)
    WaitChrThread(0x101, 0x2)

    ChrTalk(    #268
        0x8,
        "咦咦！？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_527A")

    ChrTalk(    #269
        0x106,
        (
            "#052F#6P难不成……\x01",
            "是在艾尔·雷登遇见的……？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_52AD")

    label("loc_527A")


    ChrTalk(    #270
        0x103,
        (
            "#023F#6P难不成……\x01",
            "是在艾尔·雷登遇见的孩子？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_52AD")


    ChrTalk(    #271
        0x101,
        (
            "#1017F#5P呵呵，果然\x01",
            "是玲啊。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x101, 400)
    Sleep(500)

    ChrTalk(    #272
        0xA,
        (
            "#261F#4P哈哈哈……\x01",
            "姐姐，好久不见呢。\x02\x03",

            "还记得玲的事\x01",
            "玲好高兴。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrFlags(0xA, 0x80)
    OP_A2(0x1616)
    OP_28(0x89, 0x1, 0x80)
    OP_28(0x89, 0x1, 0x100)
    Call(0, 29)
    Return()

    # Function_28_4ED7 end

    def Function_29_5343(): pass

    label("Function_29_5343")

    EventBegin(0x0)
    AddParty(0x2E, 0xFF, 0xFF)
    SetChrPos(0x101, -13340, 0, 18690, 90)
    SetChrPos(0xF7, -13560, 0, 17570, 90)
    SetChrPos(0xF8, -14890, 0, 17470, 90)
    SetChrPos(0xF9, -14630, 0, 18640, 90)
    SetChrPos(0x12F, -11980, 0, 18170, 270)
    TurnDirection(0x8, 0x101, 0)
    OP_6D(-12300, 0, 19340, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    Sleep(500)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #273
        0x8,
        (
            "#5P呀～没想到\x01",
            "你们认识啊。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x12F, 400)
    Sleep(500)

    ChrTalk(    #274
        0x8,
        (
            "#5P嗯，你……\x01",
            "叫玲对吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x12F, 0, 400)

    ChrTalk(    #275
        0x12F,
        (
            "#260F嗯嗯，是啊。\x01",
            "玲就是叫玲。\x02\x03",

            "#261F对不起，请保密。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #276
        0x8,
        "#5P哈哈，我不介意。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #277
        0x8,
        (
            "#5P但是为什么突然\x01",
            "玩起躲猫猫来了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #278
        0x12F,
        (
            "#263F因为，听说\x01",
            "姐姐来了……\x02\x03",

            "我想跟你一起玩,\x01",
            "就努力藏起来了哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #279
        0x101,
        (
            "#1016F啊哈哈，这样啊。\x02\x03",

            "#1006F不过，你居然\x01",
            "知道我们会来呢？\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x12F, 270, 400)

    ChrTalk(    #280
        0x12F,
        (
            "#264F#2P因为姐姐\x01",
            "是游击士吧？\x02\x03",

            "玲听说\x01",
            "游击士来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #281
        0x101,
        (
            "#1025F嗯，话是没错……\x02\x03",

            "但是游击士又不只我一个，\x01",
            "说不定是其他的人来了哦？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #282
        0x12F,
        (
            "#260F#2P但是，玲相信的。\x01",
            "来的是姐姐。\x02\x03",

            "#261F作为证据，你看，\x01",
            "是来了吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #283
        0x101,
        "#1016F唔，嗯……确实。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_57D1")

    ChrTalk(    #284
        0x106,
        (
            "#053F#6P嗯，这个暂且不提……\x02\x03",

            "#050F你爸爸妈妈\x01",
            "到底去哪里了？\x02\x03",

            "怎么在这种地方\x01",
            "一个人玩？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #285
        0x12F,
        "#262F#2P（盯……）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #286
        0x106,
        "#055F#6P什、什么啊？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #287
        0x12F,
        (
            "#268F#2P大哥哥，你不行啊。\x02\x03",

            "好像完全不懂得\x01",
            "怎么跟淑女说话嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #288
        0x106,
        "#057F#6P我怒……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_576B")

    ChrTalk(    #289
        0x107,
        (
            "#067F#6P阿、阿加特哥哥。\x01",
            "你先忍忍……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_576B")


    ChrTalk(    #290
        0x12F,
        (
            "#263F#2P不过，玲是淑女\x01",
            "就以宽大之心原谅你吧。\x02\x03",

            "#260F那，爸爸妈妈\x01",
            "去了哪里……\x02\x03",

            "玲也不太清楚。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_59CF")

    label("loc_57D1")


    ChrTalk(    #291
        0x103,
        (
            "#020F#6P嗯，这个暂且不提……\x02\x03",

            "你的爸爸和妈妈\x01",
            "到底去了哪里呢？\x02\x03",

            "怎么在这种地方\x01",
            "让玲一个人玩？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #292
        0x12F,
        (
            "#264F#2P哇，仔细一看姐姐\x01",
            "的衣服真有趣呢。\x02\x03",

            "那样露出肚脐\x01",
            "不会感冒吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #293
        0x103,
        (
            "#021F#6P嗯，习惯了嘛。\x02\x03",

            "#023F唔，不说这个了,\x01",
            "玲的爸爸和妈妈……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #294
        0x12F,
        (
            "#265F#2P不过，看那肤色\x01",
            "是南国出身吧？\x02\x03",

            "这样不怕冷吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #295
        0x103,
        (
            "#021F#6P从小就跟着旅行艺人剧团\x01",
            "到处走过了。\x02\x03",

            "热的地方冷的地方都没问题哦。\x02\x03",

            "#022F话·说·回·来。\x02\x03",

            "#027F玲的爸爸妈妈\x01",
            "到底去了哪里呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #296
        0x12F,
        (
            "#266F#2P呼，没办法了。\x02\x03",

            "#260F爸爸妈妈\x01",
            "去了哪里……\x02\x03",

            "玲也不太清楚。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_59CF")


    ChrTalk(    #297
        0x101,
        "#1004F不知道？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #298
        0x12F,
        (
            "#263F#2P玲和爸爸妈妈一起\x01",
            "来这里玩的……\x02\x03",

            "但是吃了午饭以后，爸爸他们\x01",
            "一脸认真地对玲说。\x02\x03",

            "#262F爸爸妈妈有很重要的事情\x01",
            "不得不和玲分别了。\x02\x03",

            "不过没关系，事情办完了\x01",
            "一定来接玲的。\x02\x03",

            "在爸爸妈妈回来之前\x01",
            "乖乖地等着好吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0xF7, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5B10")
    OP_62(0xF8, 0x0, 2300, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_5B4E")

    label("loc_5B10")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5B37")
    OP_62(0xF8, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_5B4E")

    label("loc_5B37")

    OP_62(0xF8, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)

    label("loc_5B4E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5B75")
    OP_62(0xF9, 0x0, 2300, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_5BB3")

    label("loc_5B75")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5B9C")
    OP_62(0xF9, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_5BB3")

    label("loc_5B9C")

    OP_62(0xF9, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)

    label("loc_5BB3")

    OP_62(0x8, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1500)

    ChrTalk(    #299
        0x101,
        "#1019F这，这是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #300
        0x12F,
        (
            "#261F#2P呵呵，玲已经１１岁了\x01",
            "就回答当然好了。\x02\x03",

            "然后，爸爸妈妈\x01",
            "就走了。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5C64")

    ChrTalk(    #301
        0x106,
        "#551F#6P喂喂，开玩笑吧……\x02",
    )

    CloseMessageWindow()
    Jump("loc_5C82")

    label("loc_5C64")


    ChrTalk(    #302
        0x103,
        "#025F#6P这可头痛了啊……\x02",
    )

    CloseMessageWindow()

    label("loc_5C82")


    ChrTalk(    #303
        0x8,
        (
            "#5P嗯……\x01",
            "没想到事情是这样。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 400)
    Sleep(500)

    ChrTalk(    #304
        0x8,
        (
            "#5P怎么办？\x01",
            "感觉没动力\x01",
            "去找监护人了。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5D41")

    ChrTalk(    #305
        0x101,
        (
            "#1007F嗯……\x02\x03",

            "#1015F阿加特，明白吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #306
        0x106,
        (
            "#552F#6P没办法……\x01",
            "这也是协会的工作。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5D94")

    label("loc_5D41")


    ChrTalk(    #307
        0x101,
        (
            "#1007F嗯……\x02\x03",

            "#1015F雪拉姐，明白吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #308
        0x103,
        (
            "#524F#6P当然了。\x01",
            "这也是协会的工作。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5D94")

    TurnDirection(0x101, 0x8, 400)
    Sleep(500)

    ChrTalk(    #309
        0x101,
        (
            "#1006F管家先生，别担心。\x02\x03",

            "这孩子我们\x01",
            "会负责照顾的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #310
        0x8,
        "#5P咦……？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x12F, 400)
    Sleep(500)

    ChrTalk(    #311
        0x101,
        (
            "#1006F对了，玲。\x02\x03",

            "和姐姐们一起\x01",
            "去王都的协会好吗？\x02\x03",

            "一定会马上\x01",
            "找到爸爸妈妈的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #312
        0x12F,
        (
            "#264F#2P是吗？\x02\x03",

            "但是爸爸妈妈，说\x01",
            "有很重要的事情哦？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #313
        0x101,
        (
            "#1006F没问题没问题。\x01",
            "绝对会找到的。\x02\x03",

            "#1018F相信姐姐啦！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #314
        0x12F,
        (
            "#267F#2P嗯……\x02\x03",

            "#265F那玲\x01",
            "跟姐姐一起去。\x02\x03",

            "就交给你照顾了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #315
        0x101,
        (
            "#1006F嗯！\x01",
            "也请你多关照哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #316
        0x8,
        "#5P呼……真是抱歉。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #317
        0x8,
        "#5P那孩子的事，就拜托了。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5FA8")

    ChrTalk(    #318
        0x106,
        (
            "#053F#6P啊啊，交给我们吧。\x02\x03",

            "#051F好……\x01",
            "赶快返回协会吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5FE4")

    label("loc_5FA8")


    ChrTalk(    #319
        0x103,
        (
            "#021F#6P嗯嗯，交给我们吧。\x02\x03",

            "#020F那么……\x01",
            "就回协会吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5FE4")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6D(-16620, 0, 16070, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, -16620, 0, 16070, 180)
    SetChrPos(0x1, -16620, 0, 16070, 180)
    SetChrPos(0x2, -16620, 0, 16070, 180)
    SetChrPos(0x3, -16620, 0, 16070, 180)
    SetChrPos(0x12F, -16620, 0, 16070, 180)
    OP_64(0x5, 0x1)
    OP_8C(0x8, 225, 0)
    OP_4B(0x8, 255)
    OP_A2(0x1617)
    Sleep(500)
    FadeToBright(1000, 0)
    OP_28(0x89, 0x1, 0x2000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C2, 5)), scpexpr(EXPR_END)), "loc_60B1")
    Jump("loc_60C5")

    label("loc_60B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2D0, 2)), scpexpr(EXPR_END)), "loc_60C0")
    OP_2B(0x89, 0x1)
    Jump("loc_60C5")

    label("loc_60C0")

    OP_2B(0x89, 0x3)

    label("loc_60C5")

    EventEnd(0x0)
    Return()

    # Function_29_5343 end

    def Function_30_60C8(): pass

    label("Function_30_60C8")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #320
        (
            "\x07\x05此后，王国军的警备艇\x01",
            "进行了彻夜的搜索……\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #321
        (
            "\x07\x05结果，依然没能抓住少女所乘的\x01",
            "巨大人形兵器的去向。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #322
        "\x07\x05翌日──\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(500)
    OP_6D(-11130, 0, -43550, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(1980, 0)
    OP_6C(33000, 0)
    OP_6E(386, 0)
    SetChrPos(0xC, -11940, 200, -43100, 180)
    SetChrPos(0x10F, -11940, 0, -45090, 0)
    SetChrPos(0xB, -10710, 0, -43660, 270)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x4)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x109, 0x80)
    SetChrFlags(0xF7, 0x80)
    OP_1D(0x53)
    Sleep(100)
    FadeToBright(3000, 0)
    OP_6B(1780, 3000)
    OP_0D()
    Sleep(500)

    ChrTalk(    #323
        0xB,
        (
            "#700F──凯诺娜。\x01",
            "求求你了说出来吧？\x02\x03",

            "那少女，是以怎样的形式\x01",
            "接触你们的？\x02\x03",

            "还有你们了解\x01",
            "『结社』的存在到什么程度？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #324
        0xC,
        "#1238F#5P……………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #325
        0x10F,
        (
            "#176F凯诺娜……\x01",
            "别耍性子了吧。\x02\x03",

            "#178F这样下去不仅是你，\x01",
            "连你部下们的罪也会加重。\x02\x03",

            "这不是你的本意吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #326
        0xC,
        (
            "#1231F#5P哼，他们和我\x01",
            "都早已有死的觉悟。\x02\x03",

            "岂会屈服于这种程度的威胁。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #327
        0x10F,
        (
            "#177F不要轻易言死！\x02\x03",

            "#177F你也看到了吧！\x01",
            "那个巨大的人形兵器！\x02\x03",

            "使用那种东西的家伙\x01",
            "潜入了王国啊！？\x02\x03",

            "事态严重\x01",
            "你不可能不明白吧！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #328
        0xC,
        "#1238F#5P……………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #329
        0xB,
        (
            "#703F凯诺娜……\x02\x03",

            "#700F在某种意义上来说\x01",
            "理查德上校是高洁的爱国者。\x02\x03",

            "比任何人都希望利贝尔自主独立\x01",
            "不受任何威胁。\x02\x03",

            "这点我认为是真心的。\x02\x03",

            "#703F而现在，利贝尔中\x01",
            "新的乌云正在悄悄临近……\x02\x03",

            "如果他知道了\x01",
            "会怎么想？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #330
        0xC,
        "#1238F#5P……啰嗦……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #331
        0xB,
        "#702F什么？\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xC, 1)
    Sleep(500)

    ChrTalk(    #332
        0xC,
        "#1236F#6P#3S……啰嗦，闭嘴！\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    Sleep(300)

    ChrTalk(    #333
        0xC,
        (
            "#1235F#6P别那么冠冕堂皇地\x01",
            "谈论理查德阁下的心情！\x02\x03",

            "赶走阁下，\x01",
            "抢走其地位之辈！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #334
        0xB,
        "#700F……………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #335
        0x10F,
        "#177F凯诺娜，你这家伙！\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xC, 0)
    Sleep(300)

    ChrTalk(    #336
        0xC,
        (
            "#1230F#5P你也一样，尤莉亚！\x02\x03",

            "看着过去的竞争对手\x01",
            "落魄至此，\x01",
            "想必很愉快吧！？\x02\x03",

            "#1234F那你就笑啊！\x02\x03",

            "不管是来自内心的笑还是嘲笑都无所谓！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #337
        0x10F,
        "#175F……凯诺娜…………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #338
        0xC,
        (
            "#1236F#5P我在泥泞中苟延残喘至今，\x01",
            "都是为了帮助阁下！\x02\x03",

            "现在既然无法实现，\x01",
            "我也没有生存的意义了！\x02\x03",

            "赶快枪毙我就是了！\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x6, 0x0, 0x64)
    Sleep(500)
    SetChrPos(0xD, -14860, 0, -49890, 90)

    NpcTalk(    #339
        0xD,
        "男性的声音",
        (
            "#5P喂喂……\x01",
            "真是蠢话啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xC, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x10F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0xB, 0xD, 400)
    SetChrSubChip(0xC, 0)
    Sleep(50)
    SetChrSubChip(0xC, 2)
    TurnDirection(0x10F, 0xD, 400)
    OP_9F(0xD, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xD, -13940, 0, -49200, 360)
    ClearChrFlags(0xD, 0x80)

    def lambda_67E0():

        label("loc_67E0")

        TurnDirection(0xFE, 0xD, 0)
        OP_48()
        Jump("loc_67E0")

    QueueWorkItem2(0xB, 1, lambda_67E0)

    def lambda_67F1():

        label("loc_67F1")

        TurnDirection(0xFE, 0xD, 0)
        OP_48()
        Jump("loc_67F1")

    QueueWorkItem2(0x10F, 1, lambda_67F1)

    def lambda_6802():
        OP_6D(-11520, 0, -44030, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6802)

    def lambda_681A():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_681A)
    OP_8E(0xD, 0xFFFFC9F0, 0x0, 0xFFFF4DC2, 0x7D0, 0x0)
    OP_8C(0xD, 90, 400)
    Sleep(500)
    OP_44(0xB, 0x1)
    OP_44(0x10F, 0x1)

    ChrTalk(    #340
        0xD,
        "#1120F#6P让我来阻止你吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #341
        0xB,
        "#702F#2P准将……！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #342
        0x10F,
        "#173F#2P为、为什么在这里……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #343
        0xD,
        (
            "#1125F#6P关于这次的事件，\x01",
            "有些事想和陛下商量。\x02\x03",

            "#1120F另外还有些事，\x01",
            "所以刚到王都。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #344
        0xB,
        "#701F#2P原来如此……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #345
        0x10F,
        "#171F#2P百忙之中，辛苦您了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #346
        0xC,
        (
            "#1231F#5P卡西乌斯·布莱特……\x01",
            "万恶的根源出现了……\x02\x03",

            "你也是来……\x01",
            "嘲笑我的吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0xC, 400)
    Sleep(500)

    ChrTalk(    #347
        0xD,
        (
            "#1123F#6P哎呀哎呀，被讨厌了呢。\x02\x03",

            "别看我这样，\x01",
            "也是以不输给理查德的\x01",
            "男人风度而自满啊。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #348
        0xC,
        "#1234F#5P#3S开、开什么玩笑！\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #349
        0xC,
        (
            "#1235F#5P要是没有你……\x01",
            "阁下……理查德阁下……\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0xE, -14860, 0, -49890, 90)

    NpcTalk(    #350
        0xE,
        "男性的声音",
        "#5P咳咳，准将……\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #351
        0xE,
        "男性的声音",
        (
            "#5P能不能不要\x01",
            "戏弄她啊？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xC, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x10F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0xB, 0xE, 400)
    TurnDirection(0x10F, 0xE, 400)
    TurnDirection(0xD, 0xE, 400)

    ChrTalk(    #352
        0xC,
        "#1232F#5P咦……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #353
        0xB,
        "#702F#5P刚才那是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #354
        0x10F,
        "#173F#2P难、难道是……\x02",
    )

    CloseMessageWindow()

    def lambda_6B75():
        OP_6D(-12930, 0, -43070, 3500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6B75)

    def lambda_6B8D():
        OP_67(0, 7500, -10000, 3500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_6B8D)

    def lambda_6BA5():
        OP_6B(1700, 3500)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_6BA5)

    def lambda_6BB5():
        OP_6C(0, 3500)
        ExitThread()

    QueueWorkItem(0x10F, 2, lambda_6BB5)

    def lambda_6BC5():
        OP_6E(400, 3500)
        ExitThread()

    QueueWorkItem(0x10F, 3, lambda_6BC5)
    OP_43(0xD, 0x0, 0x0, 0x1F)
    Sleep(500)
    OP_9F(0xE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xE, -13940, 0, -49200, 360)
    ClearChrFlags(0xE, 0x80)

    def lambda_6C02():

        label("loc_6C02")

        TurnDirection(0xFE, 0xE, 0)
        OP_48()
        Jump("loc_6C02")

    QueueWorkItem2(0xB, 1, lambda_6C02)

    def lambda_6C13():

        label("loc_6C13")

        TurnDirection(0xFE, 0xE, 0)
        OP_48()
        Jump("loc_6C13")

    QueueWorkItem2(0x10F, 1, lambda_6C13)

    def lambda_6C24():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_6C24)
    OP_8E(0xE, 0xFFFFCA2C, 0x0, 0xFFFF4F0C, 0x5DC, 0x0)
    OP_8C(0xE, 45, 400)
    OP_44(0xB, 0x1)
    OP_44(0x10F, 0x1)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #355
        0xC,
        "#1239F#2P…………啊………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #356
        0x10F,
        "#173F#2P理、理查德上校！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #357
        0xB,
        "#701F#2P……好久不见。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #358
        0xE,
        (
            "#1170F#6P好久不见了。\x01",
            "希德中校，舒华兹上尉。\x02\x03",

            "#1171F还有……凯诺娜。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #359
        0xC,
        "#1239F#2P啊……啊啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #360
        0xE,
        (
            "#1170F#6P虽还是服役之身，\x01",
            "但准将还是强人所难\x01",
            "带我来这里了。\x02\x03",

            "无论如何也想和你，\x01",
            "直接见面谈谈。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #361
        0xC,
        "#1239F#2P……和……我？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #362
        0xE,
        (
            "#1170F#6P啊啊……\x02\x03",

            "#1173F──抱歉，凯诺娜。\x02\x03",

            "我的傲慢和目光短浅\x01",
            "让你们也卷进来了。\x02\x03",

            "让前途有望的年轻才干们\x01",
            "承担了犯罪行为。\x02\x03",

            "#1174F我一直想为此道歉。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #363
        0xC,
        (
            "#1233F#2P请别这样，阁下！\x01",
            "我们是因自己的意志……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #364
        0xE,
        (
            "#1172F#6P不，这是我的责任。\x02\x03",

            "你们只不过是按照我的方针，\x01",
            "来行动而已。\x02\x03",

            "在这个意义上，这次事件\x01",
            "也可以算是我的责任吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #365
        0xC,
        "#1237F#2P怎、怎么会……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #366
        0xE,
        (
            "#1173F#6P所以……\x01",
            "我在此重新宣言。\x02\x03",

            "#1172F──由现在开始，\x01",
            "王国军情报部解散。\x02\x03",

            "以后，其任务会由军司令部\x01",
            "全权接手吧。\x02\x03",

            "#1171F凯诺娜……\x01",
            "以前真是辛苦你了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #367
        0xC,
        "#1232F#2P………啊……………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #368
        0xE,
        (
            "#1170F#6P这下……\x01",
            "你就不需要再勉强了。\x02\x03",

            "不需要再为了帮助我\x01",
            "而押上性命了。\x02\x03",

            "#1174F所以去死之类……\x01",
            "悲哀的事不要说了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #369
        0xC,
        (
            "#1245F#2P理查德……阁下……\x02\x03",

            "#1237F……呜呜……啊啊啊……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    FadeToDark(1500, 0, -1)

    def lambda_70A7():
        OP_6B(1980, 1500)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_70A7)

    ChrTalk(    #370 op#A op#5
        0xC,
        "#1246F#4S#2P#16A呜啊啊啊啊啊啊啊……！\x05\x02",
    )

    OP_0D()
    OP_20(0xBB8)
    OP_21()
    Sleep(2000)
    RemoveParty(0xE, 0xFF)
    OP_A2(0x10F1)
    ClearMapFlags(0x2000000)
    NewScene("ED6_DT21/T4121   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_30_60C8 end

    def Function_31_70FE(): pass

    label("Function_31_70FE")

    OP_8C(0xFE, 0, 400)
    OP_8E(0xFE, 0xFFFFC824, 0x0, 0xFFFF536C, 0x5DC, 0x0)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_31_70FE end

    def Function_32_7121(): pass

    label("Function_32_7121")

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
        (0, "loc_719B"),
        (1, "loc_71A1"),
        (SWITCH_DEFAULT, "loc_71A7"),
    )


    label("loc_719B")

    OP_A2(0x1200)
    Jump("loc_71A7")

    label("loc_71A1")

    OP_A2(0x1201)
    Jump("loc_71A7")

    label("loc_71A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_71B5")
    AddParty(0x2, 0xF7, 0xFF)
    Jump("loc_71B9")

    label("loc_71B5")

    AddParty(0x5, 0xF7, 0xFF)

    label("loc_71B9")

    Return()

    # Function_32_7121 end

    def Function_33_71BA(): pass

    label("Function_33_71BA")

    ClearMapFlags(0x1)
    OP_6D(-3960, 0, -27940, 0)
    Sleep(100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_71FD")
    FadeToBright(0, 0)
    OP_C9(0x0, 0x4, 0x0, 0x2, 0xFF, 0xFF, 0x3, 0x4, 0x6, 0x7, 0xFFFF)
    Jump("loc_721B")

    label("loc_71FD")

    FadeToBright(0, 0)
    OP_C9(0x0, 0x4, 0x0, 0x5, 0xFF, 0xFF, 0x3, 0x4, 0x6, 0x7, 0xFFFF)

    label("loc_721B")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Sleep(1000)
    Return()

    # Function_33_71BA end

    def Function_34_723B(): pass

    label("Function_34_723B")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #371
        "\x07\x05有着漂亮装饰的碟子。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_34_723B end

    def Function_35_7282(): pass

    label("Function_35_7282")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #372
        "\x07\x05放置着东方风格的壶。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_35_7282 end

    def Function_36_72C9(): pass

    label("Function_36_72C9")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #373
        "\x07\x05放置着帝国风格的壶。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_36_72C9 end

    def Function_37_7310(): pass

    label("Function_37_7310")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #374
        "\x07\x05罗列着美术品目录。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_37_7310 end

    def Function_38_7355(): pass

    label("Function_38_7355")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #375
        (
            "\x07\x05『先王的宝席』\x01",
            "　先王埃德加Ⅲ世\x01",
            "　在艾尔贝离宫逗留时\x01",
            "　常用的椅子。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_38_7355 end

    SaveToFile()

Try(main)
