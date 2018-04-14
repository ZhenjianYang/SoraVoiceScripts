from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 卢安

    CreateScenaFile(
        FileName            = 'T2131   ._SN',
        MapName             = 'Ruan',
        Location            = 'T2131.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60012",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            'ED6_DT21/T2131   ._SN',
            'ED6_DT21/T2131_1 ._SN',
            'ED6_DT21/T2131_2 ._SN',
            '',
            '',
            '',
            'ED6_DT21/SUB000  ._SN',
            ''
        ],
    )

    BuildStringList(
        '@FileName',                            # 8
        '普莱米奥',                             # 9
        '修比拉老板',                           # 10
        '洛特丽亚',                             # 11
        '费高',                                 # 12
        '阿伦特',                               # 13
        '菲利奥',                               # 14
        '拉科舒',                               # 15
        '迪恩',                                 # 16
        '斯库阿洛',                             # 17
        '哈尔德',                               # 18
        '兰切',                                 # 19
        '茶',                                   # 20
        '波尔多斯',                             # 21
        '波尔',                                 # 22
        '贝斯卡',                               # 23
        '塞卡鲁特',                             # 24
        '君特',                                 # 25
        '目标用照相机',                         # 26
        '目标用照相机２',                       # 27
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
        'ED6_DT07/CH01270 ._CH',             # 00
        'ED6_DT07/CH01560 ._CH',             # 01
        'ED6_DT27/CH03930 ._CH',             # 02
        'ED6_DT07/CH01570 ._CH',             # 03
        'ED6_DT07/CH01120 ._CH',             # 04
        'ED6_DT07/CH01040 ._CH',             # 05
        'ED6_DT07/CH01030 ._CH',             # 06
        'ED6_DT07/CH01123 ._CH',             # 07
        'ED6_DT06/CH20020 ._CH',             # 08
        'ED6_DT07/CH01680 ._CH',             # 09
        'ED6_DT07/CH01120 ._CH',             # 0A
        'ED6_DT07/CH01463 ._CH',             # 0B
        'ED6_DT07/CH02510 ._CH',             # 0C
        'ED6_DT07/CH01460 ._CH',             # 0D
        'ED6_DT07/CH01443 ._CH',             # 0E
    )

    AddCharChipPat(
        'ED6_DT07/CH01270P._CP',             # 00
        'ED6_DT07/CH01560P._CP',             # 01
        'ED6_DT27/CH03930P._CP',             # 02
        'ED6_DT07/CH01570P._CP',             # 03
        'ED6_DT07/CH01120P._CP',             # 04
        'ED6_DT07/CH01040P._CP',             # 05
        'ED6_DT07/CH01030P._CP',             # 06
        'ED6_DT07/CH01123P._CP',             # 07
        'ED6_DT06/CH20020P._CP',             # 08
        'ED6_DT07/CH01680P._CP',             # 09
        'ED6_DT07/CH01120P._CP',             # 0A
        'ED6_DT07/CH01463P._CP',             # 0B
        'ED6_DT07/CH02510P._CP',             # 0C
        'ED6_DT07/CH01460P._CP',             # 0D
        'ED6_DT07/CH01443P._CP',             # 0E
    )

    DeclNpc(
        X                   = -5500,
        Z                   = 300,
        Y                   = 33800,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 22,
    )

    DeclNpc(
        X                   = 26000,
        Z                   = 0,
        Y                   = 27230,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 18,
    )

    DeclNpc(
        X                   = 33420,
        Z                   = 0,
        Y                   = 35300,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 14,
    )

    DeclNpc(
        X                   = 35010,
        Z                   = 0,
        Y                   = 30340,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = 24900,
        Z                   = 250,
        Y                   = 35290,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = 24900,
        Z                   = 250,
        Y                   = 35290,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 24900,
        Z                   = 250,
        Y                   = 35290,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 0,
    )

    DeclNpc(
        X                   = -3510,
        Z                   = 250,
        Y                   = 31610,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 23,
    )

    DeclNpc(
        X                   = -2940,
        Z                   = 0,
        Y                   = 5590,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 20,
    )

    DeclNpc(
        X                   = -1860,
        Z                   = 200,
        Y                   = 305,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x195,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = -2860,
        Z                   = 750,
        Y                   = 300,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 655368,
        ChipIndex           = 0x8,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -2920,
        Z                   = 750,
        Y                   = -220,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1638408,
        ChipIndex           = 0x8,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -17250,
        Z                   = 0,
        Y                   = 1960,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = -22080,
        Z                   = 0,
        Y                   = 2720,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = -300,
        Z                   = 200,
        Y                   = 2126,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x115,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = -17650,
        Z                   = 200,
        Y                   = 3320,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x1D5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 24,
    )

    DeclNpc(
        X                   = 35040,
        Z                   = 0,
        Y                   = 27960,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
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
        TriggerX            = -4000,
        TriggerZ            = 250,
        TriggerY            = 33700,
        TriggerRange        = 400,
        ActorX              = -5500,
        ActorZ              = 1800,
        ActorY              = 33800,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 21,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 33310,
        TriggerZ            = 0,
        TriggerY            = 33689,
        TriggerRange        = 400,
        ActorX              = 33420,
        ActorZ              = 1700,
        ActorY              = 35300,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 14,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 33190,
        TriggerZ            = 0,
        TriggerY            = 30422,
        TriggerRange        = 1000,
        ActorX              = 35010,
        ActorZ              = 1700,
        ActorY              = 30340,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 10,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 33190,
        TriggerZ            = 0,
        TriggerY            = 27980,
        TriggerRange        = 1000,
        ActorX              = 35040,
        ActorZ              = 1700,
        ActorY              = 27960,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 12,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 25610,
        TriggerZ            = 0,
        TriggerY            = 28960,
        TriggerRange        = 1700,
        ActorX              = 26000,
        ActorZ              = 1700,
        ActorY              = 27230,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 18,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 27820,
        TriggerZ            = 0,
        TriggerY            = 28620,
        TriggerRange        = 1700,
        ActorX              = 26000,
        ActorZ              = 1700,
        ActorY              = 27230,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 18,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 25000,
        TriggerZ            = 250,
        TriggerY            = 36880,
        TriggerRange        = 700,
        ActorX              = 25150,
        ActorZ              = 1500,
        ActorY              = 37640,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 17,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 27030,
        TriggerZ            = 250,
        TriggerY            = 36880,
        TriggerRange        = 700,
        ActorX              = 27030,
        ActorZ              = 1500,
        ActorY              = 37640,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 16,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 28730,
        TriggerZ            = 0,
        TriggerY            = 37220,
        TriggerRange        = 800,
        ActorX              = 28730,
        ActorZ              = 1800,
        ActorY              = 37220,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 25,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_4C6",          # 00, 0
        "Function_1_647",          # 01, 1
        "Function_2_725",          # 02, 2
        "Function_3_72C",          # 03, 3
        "Function_4_AE6",          # 04, 4
        "Function_5_F4A",          # 05, 5
        "Function_6_13D9",         # 06, 6
        "Function_7_1460",         # 07, 7
        "Function_8_16A4",         # 08, 8
        "Function_9_1987",         # 09, 9
        "Function_10_1CCB",        # 0A, 10
        "Function_11_1D8E",        # 0B, 11
        "Function_12_2176",        # 0C, 12
        "Function_13_223B",        # 0D, 13
        "Function_14_255B",        # 0E, 14
        "Function_15_25FA",        # 0F, 15
        "Function_16_2AD9",        # 10, 16
        "Function_17_2B85",        # 11, 17
        "Function_18_2C33",        # 12, 18
        "Function_19_2CF4",        # 13, 19
        "Function_20_335D",        # 14, 20
        "Function_21_3A87",        # 15, 21
        "Function_22_3A8C",        # 16, 22
        "Function_23_3FE5",        # 17, 23
        "Function_24_40A2",        # 18, 24
        "Function_25_4233",        # 19, 25
    )


    def Function_0_4C6(): pass

    label("Function_0_4C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_523")
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrPos(0x16, -1030, 0, 2240, 0)
    SetChrChipByIndex(0x16, 13)
    ClearChrFlags(0x16, 0x10)
    ClearChrFlags(0x16, 0x4)
    OP_43(0x16, 0x0, 0x6, 0x2)
    ClearChrFlags(0x17, 0x80)
    OP_8C(0x15, 180, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_520")
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0xC, 0x80)

    label("loc_520")

    Jump("loc_646")

    label("loc_523")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_580")
    SetChrPos(0xC, -6569, 0, 32668, 270)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x68, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x68, 0x0, 0x40)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_54F")
    Jump("loc_565")

    label("loc_54F")

    SetChrPos(0xD, 32520, 0, 29800, 90)
    SetChrFlags(0xD, 0x10)

    label("loc_565")

    SetChrPos(0xE, 5386, 250, 34285, 180)
    OP_8C(0x9, 90, 0)
    Jump("loc_646")

    label("loc_580")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_5AF")
    SetChrFlags(0xC, 0x80)
    SetChrPos(0xE, 4570, 250, 30488, 90)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    Jump("loc_646")

    label("loc_5AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 4)), scpexpr(EXPR_END)), "loc_5FB")
    SetChrFlags(0x8, 0x80)
    SetChrPos(0xC, 32603, 0, 29644, 67)
    SetChrPos(0xD, 33180, 0, 31996, 135)
    SetChrFlags(0xD, 0x10)
    SetChrFlags(0xC, 0x10)
    SetChrPos(0xE, -2350, 250, 33680, 270)
    Jump("loc_646")

    label("loc_5FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_635")
    SetChrPos(0xC, 32603, 0, 29644, 67)
    SetChrPos(0xD, 33180, 0, 31996, 135)
    SetChrFlags(0xD, 0x10)
    SetChrFlags(0xC, 0x10)
    Jump("loc_646")

    label("loc_635")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_END)), "loc_646")
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)

    label("loc_646")

    Return()

    # Function_0_4C6 end

    def Function_1_647(): pass

    label("Function_1_647")

    OP_71(0x3, 0x8)
    OP_71(0x3, 0x20)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_661")
    OP_64(0x0, 0x1)

    label("loc_661")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_695")
    OP_72(0x0, 0x20)
    OP_72(0x0, 0x8)
    OP_72(0x1, 0x20)
    OP_72(0x1, 0x8)
    OP_72(0x2, 0x20)
    OP_72(0x2, 0x8)
    OP_72(0x3, 0x20)
    OP_72(0x3, 0x8)

    label("loc_695")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6E4")
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (105, "loc_6B5"),
        (106, "loc_6C5"),
        (107, "loc_6C5"),
        (SWITCH_DEFAULT, "loc_6D5"),
    )


    label("loc_6B5")

    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 2)
    Jump("loc_6E1")

    label("loc_6C5")

    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x19), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 2)
    Jump("loc_6E1")

    label("loc_6D5")

    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6E1")

    label("loc_6E1")

    Jump("loc_724")

    label("loc_6E4")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (105, "loc_6F8"),
        (106, "loc_708"),
        (107, "loc_708"),
        (SWITCH_DEFAULT, "loc_718"),
    )


    label("loc_6F8")

    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 2)
    Jump("loc_724")

    label("loc_708")

    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x19), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 2)
    Jump("loc_724")

    label("loc_718")

    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_724")

    label("loc_724")

    Return()

    # Function_1_647 end

    def Function_2_725(): pass

    label("Function_2_725")

    OP_20(0x3E8)
    OP_21()
    Return()

    # Function_2_725 end

    def Function_3_72C(): pass

    label("Function_3_72C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_7F7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7A0")

    ChrTalk(    #0
        0xFE,
        (
            "啊……啊，导力引擎\x01",
            "不能早点动起来吗～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "只要出动我自豪的船，\x01",
            "一定能捕到百倍的鱼啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xC)
    Jump("loc_7F0")

    label("loc_7A0")


    ChrTalk(    #2
        0xFE,
        (
            "啊……啊，导力引擎\x01",
            "不能早点动起来吗～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        (
            "在那天到来之前\x01",
            "只能省着点了……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7F0")

    TalkEnd(0xFE)
    Return()

    label("loc_7F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_8E5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_88D")

    ChrTalk(    #4
        0xFE,
        (
            "平时的船不能动了，\x01",
            "现在只能乘小船去打鱼啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        (
            "只能捕到很少的一些鱼，\x01",
            "生活真困苦啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xFE,
        (
            "努力了一天，\x01",
            "才终于能赚个酒钱。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xC)
    Jump("loc_8E1")

    label("loc_88D")


    ChrTalk(    #7
        0xFE,
        (
            "不能出船，\x01",
            "我这个当渔夫的也要失业喽……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xFE,
        (
            "用小船努力一天\x01",
            "才终于能赚个酒钱。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8E1")

    TalkEnd(0xFE)
    Return()

    label("loc_8E5")

    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1E), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x96), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_912")
    SetChrSubChip(0xFE, 2)
    Jump("loc_938")

    label("loc_912")

    Jc((scpexpr(EXPR_PUSH_LONG, 0xD2), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x14A), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_933")
    SetChrSubChip(0xFE, 1)
    Jump("loc_938")

    label("loc_933")

    SetChrSubChip(0xFE, 0)

    label("loc_938")

    OP_8C(0xFE, 0, 0)
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_9A4")

    ChrTalk(    #9
        0xFE,
        (
            "聚在仓库里的家伙\x01",
            "对选举漠不关心啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xFE,
        (
            "如果诺曼成了市长\x01",
            "一定会把他们赶出去的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_ADD")

    label("loc_9A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_9E3")

    ChrTalk(    #11
        0xFE,
        (
            "感觉大家\x01",
            "好像都很焦躁。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xFE,
        "虽说吵架是不好的。\x02",
    )

    CloseMessageWindow()
    Jump("loc_ADD")

    label("loc_9E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A58")

    ChrTalk(    #13
        0xFE,
        (
            "我是不太明白\x01",
            "复杂的东西啦……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        (
            "确实戴尔蒙市长\x01",
            "什么也没为我们做过。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xFE,
        (
            "连起重机\x01",
            "都没修理过。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_ADD")

    label("loc_A58")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_END)), "loc_ADD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_A8E")

    ChrTalk(    #16
        0xFE,
        (
            "我有空的时候\x01",
            "也去帮忙发传单吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_ADD")

    label("loc_A8E")

    OP_A2(0xC)

    ChrTalk(    #17
        0xFE,
        (
            "因为我是渔夫嘛。\x01",
            "没有港口就麻烦了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xFE,
        (
            "希望波尔多斯主任\x01",
            "多多努力啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_ADD")

    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)
    Return()

    # Function_3_72C end

    def Function_4_AE6(): pass

    label("Function_4_AE6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_B9E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B52")

    ChrTalk(    #19
        0xFE,
        (
            "导力引擎不能动，\x01",
            "我们船员就没事可做。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xFE,
        (
            "飞船的乘务员们，\x01",
            "一定也感到无聊吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xB)
    Jump("loc_B9B")

    label("loc_B52")


    ChrTalk(    #21
        0xFE,
        (
            "导力引擎不能动，\x01",
            "我们船员就没事可做。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xFE,
        "就像是被捞起来的鱼一样。\x02",
    )

    CloseMessageWindow()

    label("loc_B9B")

    Jump("loc_F46")

    label("loc_B9E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_C7F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C3A")

    ChrTalk(    #23
        0xFE,
        (
            "虽然好多了，\x01",
            "但城市还很混乱呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0xFE,
        (
            "但是，关键的诺曼市长\x01",
            "自己却一直躲在市长官邸……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0xFE,
        (
            "真是的，所以说波尔多斯\x01",
            "当市长不就好了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xB)
    Jump("loc_C7C")

    label("loc_C3A")


    ChrTalk(    #26
        0xFE,
        (
            "让诺曼来当\x01",
            "结果就是这样。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xFE,
        (
            "真是的，卢安市民\x01",
            "真是没眼光。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C7C")

    Jump("loc_F46")

    label("loc_C7F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_CDB")

    ChrTalk(    #28
        0xFE,
        (
            "也得告诉桥对面的人\x01",
            "港口的问题才行。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xFE,
        (
            "不能只当成是\x01",
            "在港口工作的人的问题。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F46")

    label("loc_CDB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_D4A")

    ChrTalk(    #30
        0xFE,
        (
            "总之没人受伤\x01",
            "就是万幸了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xFE,
        (
            "波尔多斯\x01",
            "在这种时候也很冷静。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xFE,
        (
            "关键时刻\x01",
            "果然是可靠的男人啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F46")

    label("loc_D4A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_E3F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_DA2")

    ChrTalk(    #33
        0xFE,
        (
            "港口问题\x01",
            "并不仅是钱的多少问题。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xFE,
        "是这个城市的灵魂问题哦。\x02",
    )

    CloseMessageWindow()
    Jump("loc_E3C")

    label("loc_DA2")

    OP_A2(0xB)

    ChrTalk(    #35
        0xFE,
        (
            "呀，欢迎。\x01",
            "欢迎来到波尔多斯阵营事务所。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0xFE,
        (
            "因为我也是船员。\x01",
            "此次的选举确实是一件大事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xFE,
        (
            "让诺曼什么的当市长看看啊。\x01",
            "港口只会比现在更萧条的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E3C")

    Jump("loc_F46")

    label("loc_E3F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_END)), "loc_F46")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_EB2")

    ChrTalk(    #38
        0xFE,
        (
            "波尔多斯虽然有软弱的一面，\x01",
            "但他是真正的海之男儿。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xFE,
        (
            "不管怎样这次的市长选举\x01",
            "都要支持他啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F46")

    label("loc_EB2")

    OP_A2(0xB)

    ChrTalk(    #40
        0xFE,
        (
            "呀，欢迎。\x01",
            "欢迎来到波尔多斯阵营事务所。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0xFE,
        (
            "波尔多斯虽然也有软弱的一面，\x01",
            "但他是真正的海之男儿。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0xFE,
        (
            "不管怎样这次的市长选举\x01",
            "都要支持他啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F46")

    TalkEnd(0xFE)
    Return()

    # Function_4_AE6 end

    def Function_5_F4A(): pass

    label("Function_5_F4A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_10BA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_FC2")

    ChrTalk(    #43
        0xFE,
        (
            "从现在起要在北街区的运动中\x01",
            "投入更多力量。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0xFE,
        (
            "还是希望经营旅游业的人们\x01",
            "也能理解我们的主张啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10B7")

    label("loc_FC2")

    OP_A2(0xA)

    ChrTalk(    #45
        0xFE,
        (
            "从现在起要在北街区的运动中\x01",
            "投入更多力量。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0xFE,
        (
            "还是希望经营旅游业的人们\x01",
            "也能理解我们的主张啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0xFE,
        (
            "我们也认为旅游业\x01",
            "是重要的产业。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0xFE,
        (
            "只是，要把前市长时期\x01",
            "所走的极端\x01",
            "重新恢复平衡。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0xFE,
        (
            "虽然是简单的道理……\x01",
            "却很难得到大家正确的理解。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10B7")

    Jump("loc_13D5")

    label("loc_10BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_1195")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_1115")

    ChrTalk(    #50
        0xFE,
        (
            "港口的家伙真是\x01",
            "性情暴躁得不行啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0xFE,
        (
            "但也说明了\x01",
            "老实的人也很多呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1192")

    label("loc_1115")

    OP_A2(0xA)

    ChrTalk(    #52
        0xFE,
        (
            "呼，总之\x01",
            "还好没闹成大事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0xFE,
        (
            "引起这次骚乱的人\x01",
            "打算去找诺曼候选人\x01",
            "道歉呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0xFE,
        (
            "支持者之间的对立\x01",
            "可不能遗留下来啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1192")

    Jump("loc_13D5")

    label("loc_1195")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_12CD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_1218")

    ChrTalk(    #55
        0xFE,
        (
            "卢安经济的中心是旅游业，\x01",
            "但也不能为此牺牲港口。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0xFE,
        (
            "如果对老旧化的设施置之不理，\x01",
            "就会有发生事故的危险。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12CA")

    label("loc_1218")

    OP_A2(0xA)

    ChrTalk(    #57
        0xFE,
        (
            "诺曼候选人说得对，\x01",
            "卢安经济的中心是旅游业。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0xFE,
        (
            "但是，也不能因此\x01",
            "就对港口置之不理。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0xFE,
        (
            "如果对老旧化的设施置之不理，\x01",
            "就会有发生事故的危险。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0xFE,
        "变成那样就为时已晚了。\x02",
    )

    CloseMessageWindow()

    label("loc_12CA")

    Jump("loc_13D5")

    label("loc_12CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_END)), "loc_13D5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_133B")

    ChrTalk(    #61
        0xFE,
        (
            "身为港湾地区的代表，\x01",
            "想想我自己都觉得不适合了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0xFE,
        "哎呀哎呀，这次的市长候选人吗～？\x02",
    )

    CloseMessageWindow()
    Jump("loc_13D5")

    label("loc_133B")

    OP_A2(0xA)

    ChrTalk(    #63
        0xFE,
        (
            "哎呀哎呀，市长候选人\x01",
            "真不是我能胜任的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0xFE,
        (
            "我是被大家硬推上来的。\x01",
            "实在没办法才来当候选人的啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0xFE,
        (
            "但既然站出来了，\x01",
            "就要以当选为目标而努力。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13D5")

    TalkEnd(0xFE)
    Return()

    # Function_5_F4A end

    def Function_6_13D9(): pass

    label("Function_6_13D9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_1417")

    ChrTalk(    #66
        0x11,
        (
            "对了，外边\x01",
            "好像很吵闹……\x02\x03",

            "……有什么事吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_145C")

    label("loc_1417")

    OP_A2(0x8)

    ChrTalk(    #67
        0x11,
        (
            "嗯，价格合适，\x01",
            "味道也可以说合格。\x02\x03",

            "这样游客\x01",
            "应该也会喜欢的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_145C")

    TalkEnd(0xFE)
    Return()

    # Function_6_13D9 end

    def Function_7_1460(): pass

    label("Function_7_1460")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_1582")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x68, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_14C7")

    ChrTalk(    #68
        0xFE,
        (
            "哈、哈哈哈，\x01",
            "只不过是输了一场，没什么啦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0xFE,
        (
            "好了～连赢几盘\x01",
            "马上赢回来！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_157F")

    label("loc_14C7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x68, 0x0, 0x40)"), scpexpr(EXPR_END)), "loc_1533")

    ChrTalk(    #70
        0xFE,
        (
            "哈哈哈～～\x01",
            "你们也很努力了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0xFE,
        (
            "不过，今天是\x01",
            "找错了对手。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0xFE,
        (
            "那么，暂且\x01",
            "在此赚点钱吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_157F")

    label("loc_1533")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_1578")

    ChrTalk(    #73
        0xD,
        (
            "呀～你也很努力战斗了。\x01",
            "就是找错了对手。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0xD,
        "哈哈哈。\x02",
    )

    CloseMessageWindow()
    Jump("loc_157F")

    label("loc_1578")

    OP_A2(0x6)
    Call(0, 9)

    label("loc_157F")

    Jump("loc_16A0")

    label("loc_1582")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_164C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_15DB")

    ChrTalk(    #75
        0xFE,
        (
            "大家都怕我，\x01",
            "不跟我比牌啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0xFE,
        (
            "没办法只好暂时\x01",
            "玩玩吃角子游戏了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1649")

    label("loc_15DB")

    OP_A2(0x6)

    ChrTalk(    #77
        0xFE,
        (
            "呀～吃角子游戏\x01",
            "也中大奖了哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0xFE,
        (
            "这是要我辞掉工作\x01",
            "专门干这个吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0xFE,
        (
            "嗯，空之女神一定\x01",
            "是这样说的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1649")

    Jump("loc_16A0")

    label("loc_164C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_16A0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_1699")

    ChrTalk(    #80
        0xFE,
        (
            "呜哦哦哦，\x01",
            "又赢了哦！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0xFE,
        (
            "难不成我\x01",
            "是游戏天才！？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_16A0")

    label("loc_1699")

    OP_A2(0x6)
    Call(0, 9)

    label("loc_16A0")

    TalkEnd(0xFE)
    Return()

    # Function_7_1460 end

    def Function_8_16A4(): pass

    label("Function_8_16A4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_17C7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_176A")

    ChrTalk(    #82
        0xFE,
        (
            "在１楼的店里\x01",
            "洗盘子的打工费到手了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0xFE,
        (
            "于是就这样\x01",
            "来一决胜负了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0xFE,
        (
            "定期船恢复原状之前\x01",
            "需要赚交通费嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0xFE,
        (
            "嗯，虽然以前运气超级不好，\x01",
            "只要状态回来了那是小事一桩。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)
    Jump("loc_17C4")

    label("loc_176A")


    ChrTalk(    #86
        0xFE,
        (
            "定期船恢复原状之前\x01",
            "预定先赚够回去的交通费。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0xFE,
        (
            "呼，首先从吃角子游戏开始\x01",
            "赚回来吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17C4")

    Jump("loc_1983")

    label("loc_17C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_1842")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_1805")

    ChrTalk(    #88
        0xFE,
        (
            "嗯～活动身体来工作\x01",
            "总觉得很有充实感啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_183F")

    label("loc_1805")

    OP_A2(0x5)

    ChrTalk(    #89
        0xFE,
        (
            "把回家的钱\x01",
            "都输光了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0xFE,
        "所以就留在这里打工。\x02",
    )

    CloseMessageWindow()

    label("loc_183F")

    Jump("loc_1983")

    label("loc_1842")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_184C")
    Jump("loc_1983")

    label("loc_184C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_18C1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_18B7")

    ChrTalk(    #91
        0xFE,
        (
            "呼哦哦哦哦哦～\x01",
            "又是我输了！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0xFE,
        (
            "不、不，一定是搞错了。\x01",
            "怎么可能输给这种外行？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18BE")

    label("loc_18B7")

    OP_A2(0x5)
    Call(0, 9)

    label("loc_18BE")

    Jump("loc_1983")

    label("loc_18C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_END)), "loc_1983")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_1920")

    ChrTalk(    #93
        0xFE,
        (
            "好像玩吃角子游戏\x01",
            "的感觉老回不来啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0xFE,
        (
            "没办法，去找些肥鸭\x01",
            "用牌榨干吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1983")

    label("loc_1920")

    OP_A2(0x5)

    ChrTalk(    #95
        0xFE,
        (
            "嗯～到底是\x01",
            "古董的吃角子游戏机。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0xFE,
        "和普通的触感就是不同。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0xFE,
        (
            "……嗯，就是因此\x01",
            "才输了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1983")

    TalkEnd(0xFE)
    Return()

    # Function_8_16A4 end

    def Function_9_1987(): pass

    label("Function_9_1987")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_1ADE")
    OP_A2(0x3)
    OP_A2(0x6)
    OP_4A(0xD, 255)
    OP_4A(0xB, 255)

    ChrTalk(    #98
        0xD,
        "……好，来吧～～\x02",
    )

    CloseMessageWindow()
    OP_62(0xD, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0xD)
    OP_62(0xD, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(400)
    RunExpression(0x5, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A1A")

    ChrTalk(    #99
        0xD,
        "看吧来了！是Ｊ！\x02",
    )

    CloseMessageWindow()
    Jump("loc_1A5E")

    label("loc_1A1A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A48")

    ChrTalk(    #100
        0xD,
        "看吧来了！是Ｊｏｋｅｒ！\x02",
    )

    CloseMessageWindow()
    Jump("loc_1A5E")

    label("loc_1A48")


    ChrTalk(    #101
        0xD,
        "来了来了！是Ａ！\x02",
    )

    CloseMessageWindow()

    label("loc_1A5E")


    ChrTalk(    #102
        0xB,
        "………………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0xB,
        "……客人您赢了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0xD,
        (
            "呀～你也很努力战斗了。\x01",
            "就是找错了对手。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0xD,
        "哈哈哈。\x02",
    )

    CloseMessageWindow()
    OP_4B(0xD, 255)
    OP_4B(0xB, 255)
    Jump("loc_1CCA")

    label("loc_1ADE")

    OP_A2(0x5)
    OP_A2(0x3)
    OP_A2(0x6)
    OP_4A(0xD, 255)
    OP_4A(0xB, 255)
    OP_4A(0xC, 255)

    ChrTalk(    #106
        0xB,
        "轮到客人您了哦？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0xC,
        "唔唔～…………\x02",
    )

    CloseMessageWindow()
    RunExpression(0x5, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B4F")

    ChrTalk(    #108
        0xC,
        "好、好！比牌吧！\x02",
    )

    CloseMessageWindow()
    Jump("loc_1BC0")

    label("loc_1B4F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B73")

    ChrTalk(    #109
        0xC,
        "当然！比牌吧！\x02",
    )

    CloseMessageWindow()
    Jump("loc_1BC0")

    label("loc_1B73")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1BA8")

    ChrTalk(    #110
        0xC,
        (
            "这、这次一定赢！\x01",
            "当然，比牌吧！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BC0")

    label("loc_1BA8")


    ChrTalk(    #111
        0xC,
        "一决胜负！比牌吧！\x02",
    )

    CloseMessageWindow()

    label("loc_1BC0")


    ChrTalk(    #112
        0xD,
        "哼哼，这样好吗。\x02",
    )

    CloseMessageWindow()
    RunExpression(0x5, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1C0A")

    ChrTalk(    #113
        0xD,
        "这边可是三张Ａ哦。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1C9B")

    label("loc_1C0A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1C3B")

    ChrTalk(    #114
        0xD,
        (
            "这边可是绰绰有余的\x01",
            "葫芦哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C9B")

    label("loc_1C3B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1C62")

    ChrTalk(    #115
        0xD,
        (
            "这边可是\x01",
            "四条哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C9B")

    label("loc_1C62")


    ChrTalk(    #116
        0xD,
        (
            "这边可是\x01",
            "同花哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0xD,
        (
            "咦？ 仔细一看\x01",
            "原来还带顺呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C9B")


    ChrTalk(    #118
        0xC,
        (
            "呼哦哦哦哦哦～\x01",
            "又是我输了！？\x02",
        )
    )

    CloseMessageWindow()
    OP_4B(0xD, 255)
    OP_4B(0xB, 255)
    OP_4B(0xC, 255)

    label("loc_1CCA")

    Return()

    # Function_9_1987 end

    def Function_10_1CCB(): pass

    label("Function_10_1CCB")

    TalkBegin(0xB)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "对话\x01",          # 0
            "玩同花顺\x01",      # 1
            "离开\x01",          # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1D73")
    FadeToDark(300, 0, -1)
    OP_0D()
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_C0(0xF, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)
    FadeToBright(300, 0)
    TalkEnd(0xB)
    Return()

    label("loc_1D73")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1D86")
    OP_56(0x0)
    TalkEnd(0xB)
    Return()

    label("loc_1D86")

    Call(0, 11)
    TalkEnd(0xB)
    Return()

    # Function_10_1CCB end

    def Function_11_1D8E(): pass

    label("Function_11_1D8E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1FC6")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x68, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x68, 0x0, 0x80)"), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x416, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1E97")

    ChrTalk(    #119
        0xB,
        (
            "啊……\x01",
            "好久不见。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0xB,
        (
            "当时让我见识了\x01",
            "精彩的比赛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0x101,
        (
            "#1016F啊哈哈……\x01",
            "还有那样的委托啊。\x02\x03",

            "嗯，虽然我\x01",
            "没派上什么用场……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x101, 400)

    ChrTalk(    #122
        0xB,
        "这真是谦虚了……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0xB,
        (
            "可以的话\x01",
            "我随时都能奉陪哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0xB,
        (
            "那么，请慢慢\x01",
            "享受胜负的乐趣吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)
    OP_A2(0x20B6)
    Jump("loc_1FC3")

    label("loc_1E97")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_1EE7")

    ChrTalk(    #125
        0xB,
        (
            "可以的话\x01",
            "我随时都能奉陪哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0xB,
        (
            "那么，请慢慢\x01",
            "享受胜负的乐趣吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1FC3")

    label("loc_1EE7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_1F9A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F5B")

    ChrTalk(    #127
        0xB,
        (
            "这种情况下\x01",
            "客人也少。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0xB,
        (
            "南区的船员们\x01",
            "几乎都不来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0xB,
        (
            "果然桥不能通行的\x01",
            "影响很大啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)
    Jump("loc_1F97")

    label("loc_1F5B")


    ChrTalk(    #130
        0xB,
        (
            "这种情况下\x01",
            "客人也少。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0xB,
        (
            "南区的船员们\x01",
            "几乎都不来了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F97")

    Jump("loc_1FC3")

    label("loc_1F9A")


    ChrTalk(    #132
        0xB,
        "欢迎光临。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0xB,
        (
            "可以的话\x01",
            "我奉陪哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1FC3")

    Jump("loc_2175")

    label("loc_1FC6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_20BE")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x68, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_201E")

    ChrTalk(    #134
        0xB,
        (
            "哟，刚才辛苦了。\x01",
            "之后交给我们吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0xB,
        (
            "那位客人\x01",
            "我们会照顾的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_20BB")

    label("loc_201E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x68, 0x0, 0x40)"), scpexpr(EXPR_END)), "loc_2077")

    ChrTalk(    #136
        0xB,
        (
            "游击士们\x01",
            "会输也是没办法的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0xB,
        (
            "差不多该是最终武器\x01",
            "出场的时候了吧……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_20BB")

    label("loc_2077")


    ChrTalk(    #138
        0xB,
        (
            "这位客人……\x01",
            "似乎非常幸运呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0xB,
        (
            "如何？\x01",
            "能和客人比试一场吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_20BB")

    Jump("loc_2175")

    label("loc_20BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_2114")

    ChrTalk(    #140
        0xB,
        (
            "支持者们\x01",
            "为什么那么热衷于选举呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0xB,
        (
            "难道在选举结果上\x01",
            "也压了米拉吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2175")

    label("loc_2114")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2139")

    ChrTalk(    #142
        0xB,
        (
            "客人也来\x01",
            "玩牌吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2175")

    label("loc_2139")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_END)), "loc_2175")

    ChrTalk(    #143
        0xB,
        (
            "欢迎来到\x01",
            "用牌开拓命运的世界……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0xB,
        "我奉陪哦。\x02",
    )

    CloseMessageWindow()

    label("loc_2175")

    Return()

    # Function_11_1D8E end

    def Function_12_2176(): pass

    label("Function_12_2176")

    TalkBegin(0x18)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "对话\x01",            # 0
            "玩二十一点\x01",      # 1
            "离开\x01",            # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2220")
    FadeToDark(300, 0, -1)
    OP_0D()
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_C0(0xD, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)
    FadeToBright(300, 0)
    TalkEnd(0x18)
    Return()

    label("loc_2220")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2233")
    OP_56(0x0)
    TalkEnd(0x18)
    Return()

    label("loc_2233")

    Call(0, 13)
    TalkEnd(0x18)
    Return()

    # Function_12_2176 end

    def Function_13_223B(): pass

    label("Function_13_223B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_22CA")

    ChrTalk(    #145
        0x18,
        (
            "引入非导力式的机器\x01",
            "是老板的爱好……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #146
        0x18,
        (
            "因此我们的吃角子游戏机\x01",
            "现在还能用。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0x18,
        (
            "说不定是老板的直觉，\x01",
            "感到会变成这样也不一定。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_255A")

    label("loc_22CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_2328")

    ChrTalk(    #148
        0x18,
        (
            "哟，虽然时世危急，\x01",
            "不来比试一盘吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0x18,
        (
            "正是这种时候\x01",
            "才需要享受人生的悠闲啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_255A")

    label("loc_2328")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_2392")

    ChrTalk(    #150
        0x18,
        (
            "虽然乘胜追击是很重要，\x01",
            "但太得意忘形可是会吃苦头的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #151
        0x18,
        (
            "看穿这个节奏，\x01",
            "这正是人生的奥秘。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_255A")

    label("loc_2392")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_2452")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_END)), "loc_23E8")

    ChrTalk(    #152
        0x18,
        (
            "我一辈子\x01",
            "也不想和政治扯上关系。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0x18,
        "啊啊，当然投票也不会去的。\x02",
    )

    CloseMessageWindow()
    Jump("loc_244F")

    label("loc_23E8")

    OP_A2(0xE)

    ChrTalk(    #154
        0x18,
        (
            "桥那边支持者们\x01",
            "好像有纠纷。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #155
        0x18,
        (
            "跟政治有关的人，\x01",
            "脱了皮都一样。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #156
        0x18,
        "我一辈子都不想扯上关系。\x02",
    )

    CloseMessageWindow()

    label("loc_244F")

    Jump("loc_255A")

    label("loc_2452")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_249B")

    ChrTalk(    #157
        0x18,
        "重要的是时机。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #158
        0x18,
        (
            "只要不搞错这点，\x01",
            "它就能丰富人生。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_255A")

    label("loc_249B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_END)), "loc_255A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_END)), "loc_24E3")

    ChrTalk(    #159
        0x18,
        (
            "二十一点\x01",
            "是客人也有胜算的游戏。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #160
        0x18,
        "请务必试试。\x02",
    )

    CloseMessageWindow()
    Jump("loc_255A")

    label("loc_24E3")

    OP_A2(0xE)

    ChrTalk(    #161
        0x18,
        "呀，欢迎。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #162
        0x18,
        (
            "这个台子上可以玩\x01",
            "二十一点。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #163
        0x18,
        (
            "是根据玩法确实能赚到钱的\x01",
            "少数卡牌游戏之一。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #164
        0x18,
        "请随意享受。\x02",
    )

    CloseMessageWindow()

    label("loc_255A")

    Return()

    # Function_13_223B end

    def Function_14_255B(): pass

    label("Function_14_255B")

    TalkBegin(0xA)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "对话\x01",          # 0
            "兑换代币\x01",      # 1
            "离开\x01",          # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_25DF")
    OP_0D()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_25C4")
    OP_A9(0x6C)
    Jump("loc_25C6")

    label("loc_25C4")

    OP_A9(0x69)

    label("loc_25C6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x23B, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_25D8")
    OP_A2(0x10B6)

    label("loc_25D8")

    TalkEnd(0xA)
    Return()

    label("loc_25DF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_25F2")
    OP_56(0x0)
    TalkEnd(0xA)
    Return()

    label("loc_25F2")

    Call(0, 15)
    TalkEnd(0xA)
    Return()

    # Function_14_255B end

    def Function_15_25FA(): pass

    label("Function_15_25FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_269A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2653")

    ChrTalk(    #165
        0xA,
        (
            "客人太少，\x01",
            "感觉店也很寂寞。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #166
        0xA,
        (
            "真希望导力器\x01",
            "尽快恢复原状啊～\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_2697")

    label("loc_2653")


    ChrTalk(    #167
        0xA,
        (
            "客人太少\x01",
            "感觉店也很寂寞。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #168
        0xA,
        (
            "老板对于这些\x01",
            "似乎完全不在乎……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2697")

    Jump("loc_2AD8")

    label("loc_269A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_2725")

    ChrTalk(    #169
        0xA,
        (
            "导力器停了的时候\x01",
            "老板也很平静。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #170
        0xA,
        (
            "真是，任何时候都是那张\x01",
            "扑克脸啊～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #171
        0xA,
        (
            "如果内心其实是在心惊胆战的话，\x01",
            "那就很有趣了哟。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2AD8")

    label("loc_2725")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_2889")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x68, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_27B0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_2774")

    ChrTalk(    #172
        0xA,
        (
            "下次请丢开工作\x01",
            "再来玩哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #173
        0xA,
        (
            "我也会\x01",
            "奉陪的㈱\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_27AD")

    label("loc_2774")

    OP_A2(0x2)

    ChrTalk(    #174
        0xA,
        (
            "大家好厉害！\x01",
            "我太感动了！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #175
        0xA,
        (
            "游击士\x01",
            "这么强啊！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_27AD")

    Jump("loc_2886")

    label("loc_27B0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x68, 0x0, 0x40)"), scpexpr(EXPR_END)), "loc_2838")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_27F5")

    ChrTalk(    #176
        0xA,
        (
            "呜呼呼，好久没有\x01",
            "这么认真玩了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #177
        0xA,
        "嗯嗯⊙\x02",
    )

    CloseMessageWindow()
    Jump("loc_2835")

    label("loc_27F5")

    OP_A2(0x2)

    ChrTalk(    #178
        0xA,
        "各位真是遗憾啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #179
        0xA,
        (
            "但是没关系哦。\x01",
            "我会帮你们报仇的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2835")

    Jump("loc_2886")

    label("loc_2838")


    ChrTalk(    #180
        0xA,
        (
            "刚才开始费高先生\x01",
            "就和老板用眼神交流着。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #181
        0xA,
        (
            "难道…\x01",
            "是轮到我出场了吗！？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2886")

    Jump("loc_2AD8")

    label("loc_2889")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_2911")

    ChrTalk(    #182
        0xA,
        (
            "老板他无论\x01",
            "客人怎么赢\x01",
            "都完全不动摇哦～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #183
        0xA,
        (
            "还能若无其事地\x01",
            "和那人聊天气呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #184
        0xA,
        (
            "摆出那种扑克脸，\x01",
            "到底是深谙此道之人啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2AD8")

    label("loc_2911")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2A5D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_29F5")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_29A7")

    ChrTalk(    #185
        0xA,
        (
            "真是的～客人\x01",
            "还真是固执呢～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #186
        0xA,
        (
            "明白了。\x01",
            "那么稍微给点提示㈱\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #187
        0xA,
        "……头发长的一方获胜哦。\x02",
    )

    CloseMessageWindow()
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_29F2")

    label("loc_29A7")


    ChrTalk(    #188
        0xA,
        (
            "所以说，其实我知道哦。\x01",
            "选举哪一方会胜……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #189
        0xA,
        "当然不会跟任何人说的。\x02",
    )

    CloseMessageWindow()

    label("loc_29F2")

    Jump("loc_2A5A")

    label("loc_29F5")

    OP_A2(0x2)

    ChrTalk(    #190
        0xA,
        (
            "别看我这样\x01",
            "可是很擅长这个的哦～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #191
        0xA,
        (
            "不知为何就是知道。\x01",
            "一看就知道会来什么牌或者骰子是多少。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A5A")

    Jump("loc_2AD8")

    label("loc_2A5D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_END)), "loc_2AD8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_2A95")

    ChrTalk(    #192
        0xA,
        (
            "不明白怎么玩的时候\x01",
            "就尽管问我哦㈱\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2AD8")

    label("loc_2A95")

    OP_A2(0x2)

    ChrTalk(    #193
        0xA,
        (
            "我最近刚刚\x01",
            "加入这家店哦～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #194
        0xA,
        (
            "在很热闹的地方\x01",
            "快乐地工作！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2AD8")

    Return()

    # Function_15_25FA end

    def Function_16_2AD9(): pass

    label("Function_16_2AD9")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        1,
        (
            "玩１代币\x01",      # 0
            "离开\x01",          # 1
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B81")
    FadeToDark(300, 0, -1)
    OP_0D()
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_C0(0xC, 0x1, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_2B81")

    TalkEnd(0xFF)
    Return()

    # Function_16_2AD9 end

    def Function_17_2B85(): pass

    label("Function_17_2B85")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        1,
        (
            "玩１０代币\x01",      # 0
            "离开\x01",            # 1
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2C2F")
    FadeToDark(300, 0, -1)
    OP_0D()
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_C0(0xC, 0xA, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_2C2F")

    TalkEnd(0xFF)
    Return()

    # Function_17_2B85 end

    def Function_18_2C33(): pass

    label("Function_18_2C33")

    TalkBegin(0x9)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "对话\x01",        # 0
            "玩轮盘\x01",      # 1
            "离开\x01",        # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2CD9")
    FadeToDark(300, 0, -1)
    OP_0D()
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_C0(0xB, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)
    FadeToBright(300, 0)
    TalkEnd(0x9)
    Return()

    label("loc_2CD9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2CEC")
    OP_56(0x0)
    TalkEnd(0x9)
    Return()

    label("loc_2CEC")

    Call(0, 19)
    TalkEnd(0x9)
    Return()

    # Function_18_2C33 end

    def Function_19_2CF4(): pass

    label("Function_19_2CF4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_2E1A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2DAD")

    ChrTalk(    #195
        0x9,
        (
            "刚才到屋顶上\x01",
            "透了口气……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #196
        0x9,
        (
            "那个浮在天上的物体\x01",
            "总是散发着金色的光芒啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #197
        0x9,
        (
            "明明是那么异样的存在，\x01",
            "但最近却好像已经习惯了似的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #198
        0x9,
        (
            "唔，习惯还\x01",
            "真是可怕。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_2E17")

    label("loc_2DAD")


    ChrTalk(    #199
        0x9,
        (
            "那种东西的存在本身\x01",
            "实在应该令人觉得奇怪……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #200
        0x9,
        (
            "但看着看着就习惯了，\x01",
            "这正是人这种生物可怕的地方啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E17")

    Jump("loc_335C")

    label("loc_2E1A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_2F25")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2EB8")

    ChrTalk(    #201
        0x9,
        (
            "欢迎来到\x01",
            "『拉旺塔尔』游戏吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #202
        0x9,
        (
            "虽然现在是这样的非常时期，\x01",
            "但还请和平常一样的享受。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #203
        0x9,
        (
            "因为本店的娱乐机器是\x01",
            "非导力驱动的古董。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_2F22")

    label("loc_2EB8")


    ChrTalk(    #204
        0x9,
        (
            "虽然现在是这样的非常时期，\x01",
            "本店还是和平时一样正在营业。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #205
        0x9,
        (
            "正是在事态严峻的时候\x01",
            "世间才更需要娱乐。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F22")

    Jump("loc_335C")

    label("loc_2F25")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_3051")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x68, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2F91")

    ChrTalk(    #206
        0x9,
        (
            "如果胜运偏离了\x01",
            "以后就很难再回来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #207
        0x9,
        (
            "那位客人，马上就会把\x01",
            "赢走的份都输回去吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_304E")

    label("loc_2F91")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x68, 0x0, 0x40)"), scpexpr(EXPR_END)), "loc_2FD0")

    ChrTalk(    #208
        0x9,
        "唔，没办法啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #209
        0x9,
        "差不多该轮到她出场了吗。\x02",
    )

    CloseMessageWindow()
    Jump("loc_304E")

    label("loc_2FD0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_300B")

    ChrTalk(    #210
        0x9,
        (
            "乘着气势得来的胜利\x01",
            "要崩溃起来也是很快的呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_304E")

    label("loc_300B")

    OP_A2(0x1)

    ChrTalk(    #211
        0x9,
        (
            "唔，那位客人似乎\x01",
            "乘上胜运了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #212
        0x9,
        (
            "只有祈祷他\x01",
            "不要失足了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_304E")

    Jump("loc_335C")

    label("loc_3051")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_3112")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_3087")

    ChrTalk(    #213
        0x9,
        (
            "希望新市长也能继续\x01",
            "援助旅游业。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_310F")

    label("loc_3087")

    OP_A2(0x1)

    ChrTalk(    #214
        0x9,
        (
            "虽然前市长很不幸的\x01",
            "发生那样的事……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #215
        0x9,
        (
            "但前市长重视旅游的政策\x01",
            "对我们的店也有很大帮助。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #216
        0x9,
        (
            "希望新市长也能继续\x01",
            "援助旅游业啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_310F")

    Jump("loc_335C")

    label("loc_3112")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_31F4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_3177")

    ChrTalk(    #217
        0x9,
        (
            "本店引以自豪的吃角子游戏机\x01",
            "已经试过了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #218
        0x9,
        (
            "全部是非导力驱动\x01",
            "的古董哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_31F1")

    label("loc_3177")

    OP_A2(0x1)

    ChrTalk(    #219
        0x9,
        (
            "本店引以自豪的吃角子游戏机\x01",
            "已经试过了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #220
        0x9,
        (
            "全部是非导力驱动\x01",
            "的古董。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #221
        0x9,
        (
            "应该能体会到\x01",
            "拉杆所具有的厚重感哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_31F1")

    Jump("loc_335C")

    label("loc_31F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_END)), "loc_335C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_324F")

    ChrTalk(    #222
        0x9,
        (
            "欢迎来到\x01",
            "『拉旺塔尔』。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #223
        0x9,
        (
            "虽然让大家久等了，\x01",
            "总算重新装修开张了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_335C")

    label("loc_324F")

    OP_A2(0x1)

    ChrTalk(    #224
        0x9,
        (
            "欢迎来到\x01",
            "『拉旺塔尔』游戏吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #225
        0x9,
        (
            "世上有无法进行合理判断\x01",
            "而被迫进行选择的时候。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #226
        0x9,
        (
            "可是，女神传授给了我们\x01",
            "解决那种状况的方法。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #227
        0x9,
        "……对，那就是第六感。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #228
        0x9,
        (
            "和人生的选择一样，\x01",
            "它的胜负\x01",
            "也是找不到合理的理由的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #229
        0x9,
        (
            "是否能用直觉感知危机，\x01",
            "那就是它的真髓。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_335C")

    Return()

    # Function_19_2CF4 end

    def Function_20_335D(): pass

    label("Function_20_335D")

    TalkBegin(0x10)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "对话\x01",                                 # 0
            "买东西\x01",                               # 1
            "招牌菜『海风通心汤粉』　400米拉\x01",      # 2
            "离开\x01",                                 # 3
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_33DE")
    OP_0D()
    OP_A9(0x6A)
    OP_56(0x0)
    TalkEnd(0x10)
    Return()

    label("loc_33DE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_34EF")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x12), scpexpr(EXPR_PUSH_LONG, 0x190), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_34B7")
    SubMira(400)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMessageWindowPos(-1, -1, -1, -1)
    OP_22(0xB, 0x0, 0x64)

    AnonymousTalk(    #230
        "\x06\x07\x02海风通心汤粉\x07\x00已经品尝过了。\x02",
    )

    CloseMessageWindow()
    OP_31(0x0, 0xFD, 0x320)
    OP_31(0x1, 0xFD, 0x320)
    OP_31(0x2, 0xFD, 0x320)
    OP_31(0x3, 0xFD, 0x320)
    OP_31(0x4, 0xFD, 0x320)
    OP_31(0x5, 0xFD, 0x320)
    OP_31(0x6, 0xFD, 0x320)
    OP_31(0x7, 0xFD, 0x320)
    OP_31(0x8, 0xFD, 0x320)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x20D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_34A9")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_AC(0x3)"), scpexpr(EXPR_END)), "loc_347D")
    Jump("loc_34A9")

    label("loc_347D")

    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #231
        "\x06\x07\x02海风通心汤粉\x07\x00的做法已经学会了。\x02",
    )

    CloseMessageWindow()

    label("loc_34A9")

    OP_56(0x0)
    FadeToBright(1000, 0)
    Jump("loc_34DD")

    label("loc_34B7")

    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #232
        "没有足够的米拉。\x02",
    )

    CloseMessageWindow()
    FadeToBright(300, 0)

    label("loc_34DD")

    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x10)
    Return()

    label("loc_34EF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3500")
    TalkEnd(0x10)
    Return()

    label("loc_3500")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_35F8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_35B0")

    ChrTalk(    #233
        0xFE,
        "渔夫们也很困苦哦。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #234
        0xFE,
        (
            "满载导力引擎的船全部不能动了，\x01",
            "只能出动小型船。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #235
        0xFE,
        (
            "不过，有工作做\x01",
            "就算不错了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #236
        0xFE,
        (
            "看看船员们吧。\x01",
            "全都沉没在里面的二楼了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x9)
    Jump("loc_35F5")

    label("loc_35B0")


    ChrTalk(    #237
        0xFE,
        "渔夫们也很困苦哦。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #238
        0xFE,
        (
            "不过，还算有工作做，\x01",
            "比起船员还好点吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_35F5")

    Jump("loc_3A83")

    label("loc_35F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_36C8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3667")

    ChrTalk(    #239
        0xFE,
        "欢迎光临。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #240
        0xFE,
        (
            "把柴火放进暖炉后\x01",
            "总算能营业了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #241
        0xFE,
        (
            "暂时还是按照平日的\x01",
            "菜单来做的。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x9)
    Jump("loc_36C5")

    label("loc_3667")


    ChrTalk(    #242
        0xFE,
        (
            "把柴火放进暖炉后\x01",
            "总算能营业了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #243
        0xFE,
        (
            "厨房也快变成桑拿浴室了，\x01",
            "现在只能靠气势渡过难关啦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_36C5")

    Jump("loc_3A83")

    label("loc_36C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_37C1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_3722")

    ChrTalk(    #244
        0xFE,
        (
            "都参加过武术大会了，\x01",
            "却又回到仓库生活。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #245
        0xFE,
        "真是没有上进心的家伙。\x02",
    )

    CloseMessageWindow()
    Jump("loc_37BE")

    label("loc_3722")

    OP_A2(0x9)

    ChrTalk(    #246
        0xFE,
        (
            "这么说来渡鸦帮的家伙\x01",
            "参加了王都的武术大会吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #247
        0xFE,
        (
            "在利贝尔通讯上看到照片\x01",
            "的时候真是大吃一惊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #248
        0xFE,
        (
            "话虽如此，结果还是和以前一样\x01",
            "又回到了仓库生活。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_37BE")

    Jump("loc_3A83")

    label("loc_37C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_38A8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_3822")

    ChrTalk(    #249
        0xFE,
        (
            "在有选举权的人眼前引起骚动\x01",
            "可不妙啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #250
        0xFE,
        (
            "要是打起来的话\x01",
            "超级破坏形象啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_38A5")

    label("loc_3822")

    OP_A2(0x9)

    ChrTalk(    #251
        0xFE,
        "骚动的事我听说了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #252
        0xFE,
        (
            "确实对方也有错的地方，\x01",
            "但出言挑衅的人也不对。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #253
        0xFE,
        (
            "有选举权的人都在看着呢，\x01",
            "以后做事希望能三思啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_38A5")

    Jump("loc_3A83")

    label("loc_38A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_39B0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_391B")

    ChrTalk(    #254
        0xFE,
        (
            "与海共同生活的人\x01",
            "拥有对这个城市港口的留恋。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #255
        0xFE,
        (
            "波尔多斯就是代表这个心情\x01",
            "的市长候选人。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_39AD")

    label("loc_391B")

    OP_A2(0x9)

    ChrTalk(    #256
        0xFE,
        (
            "我原来也是渔夫，\x01",
            "有着对这个城市港口的留恋。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #257
        0xFE,
        (
            "波尔多斯就是代表这个心情\x01",
            "的市长候选人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #258
        0xFE,
        (
            "就算再怎么糊涂也不会\x01",
            "投票给诺曼那暴发户的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_39AD")

    Jump("loc_3A83")

    label("loc_39B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_END)), "loc_3A83")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_39E6")

    ChrTalk(    #259
        0xFE,
        (
            "哟！欢迎光临。\x01",
            "欢迎来亚克罗萨。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A83")

    label("loc_39E6")

    OP_A2(0x9)

    ChrTalk(    #260
        0xFE,
        (
            "哟！欢迎光临。\x01",
            "欢迎来亚克罗萨。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #261
        0xFE,
        (
            "二楼成为波尔多斯\x01",
            "先生的选举事务所了，\x01",
            "不过店里还是和平时一样在营业啦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #262
        0xFE,
        (
            "请尽情享受\x01",
            "我们这儿自豪的新鲜海鲜。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3A83")

    TalkEnd(0x10)
    Return()

    # Function_20_335D end

    def Function_21_3A87(): pass

    label("Function_21_3A87")

    Call(0, 22)
    Return()

    # Function_21_3A87 end

    def Function_22_3A8C(): pass

    label("Function_22_3A8C")

    TalkBegin(0x8)
    Call(6, 4)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3AA9")
    OP_A9(0x68)
    TalkEnd(0x8)
    Return()

    label("loc_3AA9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3ABA")
    TalkEnd(0x8)
    Return()

    label("loc_3ABA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_3BA6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B59")

    ChrTalk(    #263
        0x8,
        (
            "弟弟上次来店里\x01",
            "到底是多久以前的事了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #264
        0x8,
        (
            "嗯，要改变心情\x01",
            "就得开始努力了，\x01",
            "我也要开始支持啦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #265
        0x8,
        (
            "无论怎么说\x01",
            "他是我唯一的弟弟嘛。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_3BA3")

    label("loc_3B59")


    ChrTalk(    #266
        0x8,
        (
            "弟弟上次来店里\x01",
            "到底是多久以前的事了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #267
        0x8,
        (
            "为此勉强开店\x01",
            "也值得了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3BA3")

    Jump("loc_3FE1")

    label("loc_3BA6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_3C95")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3C38")

    ChrTalk(    #268
        0x8,
        (
            "桥还是吊在上面，\x01",
            "炉子也不能用，真头痛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #269
        0x8,
        (
            "尽管如此\x01",
            "还是勉强开店营业……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #270
        0x8,
        (
            "不过说实话，真不知道\x01",
            "要持续到什么时候。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_3C92")

    label("loc_3C38")


    ChrTalk(    #271
        0x8,
        (
            "桥还是吊在上面，\x01",
            "炉子也不能用，真头痛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #272
        0x8,
        (
            "军队或者游击士谁都行，\x01",
            "赶快想点办法吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3C92")

    Jump("loc_3FE1")

    label("loc_3C95")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_3D3E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_3CE8")

    ChrTalk(    #273
        0x8,
        (
            "不过，连路费\x01",
            "都输光了真是难以置信。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #274
        0x8,
        (
            "想必是\x01",
            "冲昏了头吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3D3B")

    label("loc_3CE8")

    OP_A2(0x0)

    ChrTalk(    #275
        0x8,
        (
            "在娱乐场输光了的客人\x01",
            "我就雇他们打零工。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #276
        0x8,
        (
            "嗯，有他们在\x01",
            "就不会有麻烦了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3D3B")

    Jump("loc_3FE1")

    label("loc_3D3E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_3DB5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D61")

    ChrTalk(    #277
        0x8,
        "哟，游击士们。\x02",
    )

    CloseMessageWindow()

    label("loc_3D61")

    OP_A2(0x0)

    ChrTalk(    #278
        0x8,
        (
            "刚才真是危险，\x01",
            "还好没事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #279
        0x8,
        (
            "双方都很热心是没错，\x01",
            "但希望能再成熟点啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3FE1")

    label("loc_3DB5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3E89")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_3E2F")

    ChrTalk(    #280
        0x8,
        (
            "那边很近的酒店\x01",
            "是诺曼阵营的事务所。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #281
        0x8,
        (
            "经常为众多的宣传员\x01",
            "叫外卖，\x01",
            "对我们来说也是不错的客人。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E86")

    label("loc_3E2F")

    OP_A2(0x0)

    ChrTalk(    #282
        0x8,
        (
            "在这附近做买卖的人\x01",
            "全都支持诺曼先生哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #283
        0x8,
        (
            "要是没有游客\x01",
            "买卖就做不下去了嘛。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3E86")

    Jump("loc_3FE1")

    label("loc_3E89")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_END)), "loc_3FE1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_3F25")

    ChrTalk(    #284
        0x8,
        (
            "我弟弟迪恩好像\x01",
            "参加了最近的武术大会呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #285
        0x8,
        (
            "但是，才刚刚有点改观，\x01",
            "现在却又在仓库里偷懒了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #286
        0x8,
        (
            "那些家伙真是，\x01",
            "到底有没有干劲啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3FE1")

    label("loc_3F25")

    OP_A2(0x0)

    ChrTalk(    #287
        0x8,
        (
            "我弟弟迪恩\x01",
            "在港口的渡鸦帮\x01",
            "当小混混……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #288
        0x8,
        (
            "那些家伙们似乎\x01",
            "参加了最近的武术大会呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #289
        0x8,
        (
            "但是，才刚刚有点改观，\x01",
            "现在却又在仓库里偷懒了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #290
        0x8,
        (
            "那些家伙真是的…\x01",
            "到底有没有干劲啊……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3FE1")

    TalkEnd(0x8)
    Return()

    # Function_22_3A8C end

    def Function_23_3FE5(): pass

    label("Function_23_3FE5")

    TalkBegin(0xF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_409E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_405A")

    ChrTalk(    #291
        0xFE,
        (
            "嘿嘿，来大哥的店\x01",
            "吃午饭呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #292
        0xFE,
        (
            "真是好久没有\x01",
            "在外边碰到了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #293
        0xFE,
        (
            "以后经常\x01",
            "来露个脸吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xD)
    Jump("loc_409E")

    label("loc_405A")


    ChrTalk(    #294
        0xFE,
        (
            "大哥做的饭菜\x01",
            "果然是最美味的啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #295
        0xFE,
        (
            "嘿，令人想起\x01",
            "妈妈的事啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_409E")

    TalkEnd(0xF)
    Return()

    # Function_23_3FE5 end

    def Function_24_40A2(): pass

    label("Function_24_40A2")

    TalkBegin(0x17)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_417E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4129")

    ChrTalk(    #296
        0xFE,
        (
            "呼，出航的时候\x01",
            "总是怀念陆地……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #297
        0xFE,
        (
            "不能出航的时候，\x01",
            "反而怀念起大海来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #298
        0xFE,
        (
            "哎呀，人总是\x01",
            "不能满足啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xF)
    Jump("loc_417B")

    label("loc_4129")


    ChrTalk(    #299
        0xFE,
        (
            "不能出航的时候，\x01",
            "就怀念起大海来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #300
        0xFE,
        (
            "船员这种生物\x01",
            "果然不能在陆上久留啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_417B")

    Jump("loc_422F")

    label("loc_417E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_422F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_41DF")

    ChrTalk(    #301
        0xFE,
        (
            "航海归来是好，\x01",
            "却又不能出航了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #302
        0xFE,
        (
            "就当是休息的机会\x01",
            "老实地喝喝酒吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xF)
    Jump("loc_422F")

    label("loc_41DF")


    ChrTalk(    #303
        0xFE,
        (
            "航海归来是好，\x01",
            "却又不能出航了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #304
        0xFE,
        (
            "导力器竟然动不了，\x01",
            "到底是什么原因呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_422F")

    TalkEnd(0x17)
    Return()

    # Function_24_40A2 end

    def Function_25_4233(): pass

    label("Function_25_4233")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_4296")
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #305
        (
            "\x07\x05心里一直想着去赚钱。\x01",
            "『拉旺塔尔』游戏吧\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Jump("loc_4304")

    label("loc_4296")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #306
        (
            "\x07\x05祝．新拉旺塔尔开张！\x01",
            "为你带来惊险和兴奋。\x01",
            "『拉旺塔尔』游戏吧\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)

    label("loc_4304")

    Return()

    # Function_25_4233 end

    SaveToFile()

Try(main)
