from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'T0132   ._SN',
        MapName             = 'Rolent',
        Location            = 'T0132.x',
        MapIndex            = 8,
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
            'ED6_DT21/SUB000  ._SN',
            ''
        ],
    )

    BuildStringList(
        '@FileName',                            # 8
        '奥利维尔',                             # 9
        '威诺',                                 # 10
        '乘客',                                 # 11
        '乘客',                                 # 12
        '乘客',                                 # 13
        '乘客',                                 # 14
        '乘客',                                 # 15
        '奥利维尔',                             # 16
        '安敦',                                 # 17
        '利库斯',                               # 18
        '安敦',                                 # 19
        '林德号的乘客',                         # 20
        '林德号的乘客',                         # 21
        '林德号的乘客',                         # 22
        '伊娜',                                 # 23
        '安莉尔',                               # 24
        '小猫',                                 # 25
        '小猫',                                 # 26
        '小猫',                                 # 27
        '利吉',                                 # 28
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
        'ED6_DT26/CH20244 ._CH',             # 00
        'ED6_DT07/CH01560 ._CH',             # 01
        'ED6_DT07/CH01020 ._CH',             # 02
        'ED6_DT07/CH01140 ._CH',             # 03
        'ED6_DT07/CH01150 ._CH',             # 04
        'ED6_DT07/CH01460 ._CH',             # 05
        'ED6_DT07/CH01470 ._CH',             # 06
        'ED6_DT26/CH20255 ._CH',             # 07
        'ED6_DT07/CH01044 ._CH',             # 08
        'ED6_DT07/CH01180 ._CH',             # 09
        'ED6_DT07/CH01030 ._CH',             # 0A
        'ED6_DT07/CH01700 ._CH',             # 0B
        'ED6_DT27/CH03880 ._CH',             # 0C
        'ED6_DT27/CH03881 ._CH',             # 0D
        'ED6_DT27/CH03882 ._CH',             # 0E
        'ED6_DT07/CH01760 ._CH',             # 0F
    )

    AddCharChipPat(
        'ED6_DT26/CH20244P._CP',             # 00
        'ED6_DT07/CH01560P._CP',             # 01
        'ED6_DT07/CH01020P._CP',             # 02
        'ED6_DT07/CH01140P._CP',             # 03
        'ED6_DT07/CH01150P._CP',             # 04
        'ED6_DT07/CH01460P._CP',             # 05
        'ED6_DT07/CH01470P._CP',             # 06
        'ED6_DT26/CH20255P._CP',             # 07
        'ED6_DT07/CH01044P._CP',             # 08
        'ED6_DT07/CH01180P._CP',             # 09
        'ED6_DT07/CH01030P._CP',             # 0A
        'ED6_DT07/CH01700P._CP',             # 0B
        'ED6_DT27/CH03880P._CP',             # 0C
        'ED6_DT27/CH03881P._CP',             # 0D
        'ED6_DT27/CH03882P._CP',             # 0E
        'ED6_DT07/CH01760P._CP',             # 0F
    )

    DeclNpc(
        X                   = -83400,
        Z                   = 600,
        Y                   = 150180,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x187,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 4500,
        Z                   = 0,
        Y                   = 190660,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = -86920,
        Z                   = 0,
        Y                   = 152460,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = -87040,
        Z                   = 0,
        Y                   = 122170,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = -87150,
        Z                   = 0,
        Y                   = 118770,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 14,
    )

    DeclNpc(
        X                   = -45350,
        Z                   = 0,
        Y                   = 152520,
        Direction           = 45,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 15,
    )

    DeclNpc(
        X                   = -44610,
        Z                   = 0,
        Y                   = 153260,
        Direction           = 225,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = -83780,
        Z                   = 0,
        Y                   = 149780,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x105,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -82000,
        Z                   = 200,
        Y                   = 158050,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x195,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -83650,
        Z                   = 0,
        Y                   = 151440,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 18,
    )

    DeclNpc(
        X                   = -82000,
        Z                   = -600,
        Y                   = 158050,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x195,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 17,
    )

    DeclNpc(
        X                   = 5170,
        Z                   = 0,
        Y                   = 181750,
        Direction           = 167,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 5,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 22,
    )

    DeclNpc(
        X                   = -83940,
        Z                   = 0,
        Y                   = 152750,
        Direction           = 256,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 23,
    )

    DeclNpc(
        X                   = -48500,
        Z                   = 0,
        Y                   = 156140,
        Direction           = 271,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 24,
    )

    DeclNpc(
        X                   = -86540,
        Z                   = 0,
        Y                   = 119250,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 20,
    )

    DeclNpc(
        X                   = -85700,
        Z                   = 0,
        Y                   = 120430,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 21,
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
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
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
        NpcIndex            = 0x195,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
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
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -87080,
        Z                   = 0,
        Y                   = 119580,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 15,
        ChipIndex           = 0xF,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 25,
    )


    DeclActor(
        TriggerX            = -83780,
        TriggerZ            = 0,
        TriggerY            = 150460,
        TriggerRange        = 1000,
        ActorX              = -84380,
        ActorZ              = 1000,
        ActorY              = 150260,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 19,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 6598,
        TriggerZ            = 0,
        TriggerY            = 190158,
        TriggerRange        = 1000,
        ActorX              = 4500,
        ActorZ              = 1500,
        ActorY              = 190662,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 10,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 3130,
        TriggerZ            = 0,
        TriggerY            = 192000,
        TriggerRange        = 800,
        ActorX              = 3130,
        ActorZ              = 1000,
        ActorY              = 192000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 26,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_416",          # 00, 0
        "Function_1_65B",          # 01, 1
        "Function_2_6A3",          # 02, 2
        "Function_3_6C7",          # 03, 3
        "Function_4_704",          # 04, 4
        "Function_5_728",          # 05, 5
        "Function_6_74C",          # 06, 6
        "Function_7_770",          # 07, 7
        "Function_8_794",          # 08, 8
        "Function_9_7B8",          # 09, 9
        "Function_10_818",         # 0A, 10
        "Function_11_81D",         # 0B, 11
        "Function_12_1096",        # 0C, 12
        "Function_13_1195",        # 0D, 13
        "Function_14_12D7",        # 0E, 14
        "Function_15_13EC",        # 0F, 15
        "Function_16_14E0",        # 10, 16
        "Function_17_1638",        # 11, 17
        "Function_18_1689",        # 12, 18
        "Function_19_17BF",        # 13, 19
        "Function_20_1A32",        # 14, 20
        "Function_21_1DCC",        # 15, 21
        "Function_22_1DE4",        # 16, 22
        "Function_23_1EA3",        # 17, 23
        "Function_24_1FD2",        # 18, 24
        "Function_25_2148",        # 19, 25
        "Function_26_27CF",        # 1A, 26
    )


    def Function_0_416(): pass

    label("Function_0_416")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_43B")
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 5)), scpexpr(EXPR_END)), "loc_438")
    ClearChrFlags(0x1B, 0x80)

    label("loc_438")

    Jump("loc_4FF")

    label("loc_43B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 0)), scpexpr(EXPR_END)), "loc_46F")
    ClearChrFlags(0x11, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x76, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_46C")
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x11, -83460, 0, 153000, 0)

    label("loc_46C")

    Jump("loc_4FF")

    label("loc_46F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_END)), "loc_4B4")
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, -88460, 0, 155910, 268)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, -84470, 0, 151460, 182)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x10)
    Jump("loc_4FF")

    label("loc_4B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 4)), scpexpr(EXPR_END)), "loc_4D7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4C8")
    ClearChrFlags(0x8, 0x80)

    label("loc_4C8")

    ClearChrFlags(0xE, 0x80)
    OP_43(0xE, 0x0, 0x0, 0x2)
    Jump("loc_4FF")

    label("loc_4D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 4)), scpexpr(EXPR_END)), "loc_4FF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4EB")
    ClearChrFlags(0xA, 0x80)

    label("loc_4EB")

    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)

    label("loc_4FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_509")
    Jump("loc_65A")

    label("loc_509")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 0)), scpexpr(EXPR_END)), "loc_513")
    Jump("loc_65A")

    label("loc_513")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 4)), scpexpr(EXPR_END)), "loc_653")
    ClearChrFlags(0x16, 0x80)
    OP_51(0x18, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x258), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x18, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x258), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x18, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x258), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x18, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x258), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x18, 0x29, (scpexpr(EXPR_PUSH_LONG, 0x258), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x19, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x258), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x19, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x258), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x19, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x258), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x19, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x258), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x19, 0x29, (scpexpr(EXPR_PUSH_LONG, 0x258), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x19, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1A, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x258), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1A, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x258), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1A, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x258), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1A, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x258), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1A, 0x29, (scpexpr(EXPR_PUSH_LONG, 0x258), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    SetChrFlags(0x18, 0x4)
    SetChrFlags(0x19, 0x4)
    SetChrFlags(0x18, 0x40)
    SetChrFlags(0x19, 0x40)
    SetChrPos(0x16, -85600, 0, 119540, 0)
    SetChrPos(0x1A, -84190, 0, 123070, 330)
    SetChrPos(0x19, -83500, 580, 117300, 270)
    SetChrPos(0x18, -83030, 580, 116830, 315)
    OP_43(0x1A, 0x1, 0x0, 0x6)
    OP_43(0x19, 0x1, 0x0, 0x7)
    OP_43(0x18, 0x1, 0x0, 0x8)
    Jump("loc_65A")

    label("loc_653")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 4)), scpexpr(EXPR_END)), "loc_65A")

    label("loc_65A")

    Return()

    # Function_0_416 end

    def Function_1_65B(): pass

    label("Function_1_65B")

    OP_82(0x80, 0x0)
    OP_82(0x82, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x76, 0x0, 0x10)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_68F")
    SoundDistance(0x1CB, 0xFFFEBFB0, 0x4B0, 0x26962, 0x7D0, 0x2710, 0x64, 0x0)
    Jump("loc_692")

    label("loc_68F")

    OP_82(0x81, 0x0)

    label("loc_692")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_6A2")
    OP_64(0x0, 0x1)

    label("loc_6A2")

    Return()

    # Function_1_65B end

    def Function_2_6A3(): pass

    label("Function_2_6A3")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6C6")
    OP_8D(0xFE, -46050, 153320, -43570, 152040, 2000)
    Jump("Function_2_6A3")

    label("loc_6C6")

    Return()

    # Function_2_6A3 end

    def Function_3_6C7(): pass

    label("Function_3_6C7")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_703")
    OP_9E(0x10, 0x19, 0x0, 0x12C, 0xFA0)
    Sleep(400)
    OP_9E(0x10, 0x19, 0x0, 0x12C, 0xFA0)
    Sleep(2500)
    Jump("Function_3_6C7")

    label("loc_703")

    Return()

    # Function_3_6C7 end

    def Function_4_704(): pass

    label("Function_4_704")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_727")
    OP_8D(0xFE, -83510, 153450, -85710, 152080, 2000)
    Jump("Function_4_704")

    label("loc_727")

    Return()

    # Function_4_704 end

    def Function_5_728(): pass

    label("Function_5_728")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_74B")
    OP_8D(0xFE, 4880, 177010, 6450, 182780, 2000)
    Jump("Function_5_728")

    label("loc_74B")

    Return()

    # Function_5_728 end

    def Function_6_74C(): pass

    label("Function_6_74C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_76F")
    OP_8D(0xFE, -85500, 124240, -83590, 123040, 1000)
    Jump("Function_6_74C")

    label("loc_76F")

    Return()

    # Function_6_74C end

    def Function_7_770(): pass

    label("Function_7_770")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_793")
    OP_8D(0xFE, -83000, 117760, -83510, 116930, 1000)
    Jump("Function_7_770")

    label("loc_793")

    Return()

    # Function_7_770 end

    def Function_8_794(): pass

    label("Function_8_794")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7B7")
    OP_8D(0xFE, -84200, 117760, -83500, 116930, 1000)
    Jump("Function_8_794")

    label("loc_7B7")

    Return()

    # Function_8_794 end

    def Function_9_7B8(): pass

    label("Function_9_7B8")

    ClearChrFlags(0xFE, 0x1)

    label("loc_7BD")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_817")
    OP_8C(0xFE, 270, 400)
    OP_8E(0xFE, 0xFFFEB754, 0xFB3, 0x1DDB2, 0x3E8, 0x0)
    OP_8C(0xFE, 180, 400)
    Sleep(1000)
    OP_8C(0xFE, 90, 400)
    OP_8E(0xFE, 0xFFFEC1D6, 0xFB3, 0x1DDB2, 0x3E8, 0x0)
    OP_8C(0xFE, 180, 400)
    Sleep(1000)
    Jump("loc_7BD")

    label("loc_817")

    Return()

    # Function_9_7B8 end

    def Function_10_818(): pass

    label("Function_10_818")

    Call(0, 11)
    Return()

    # Function_10_818 end

    def Function_11_81D(): pass

    label("Function_11_81D")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_857")
    Call(6, 6)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_846")
    OP_A9(0x5)
    TalkEnd(0x9)
    Return()

    label("loc_846")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_857")
    TalkEnd(0x9)
    Return()

    label("loc_857")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_B84")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x414, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A2B")
    OP_62(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0x9, 0x101, 0)
    Sleep(400)

    ChrTalk(    #0
        0x9,
        (
            "啊，是艾丝蒂尔……\x01",
            "今天约修亚也一起来了吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x102, 400)

    ChrTalk(    #1
        0x9,
        (
            "真是好久都没看见\x01",
            "约修亚了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x102,
        (
            "#1040F嗯，确实啊……\x02\x03",

            "导力器已经不能用了，\x01",
            "旅馆营业没问题吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x9,
        (
            "是，无论如何也要\x01",
            "继续营业。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x9,
        (
            "因为滞留在飞船坪\x01",
            "的人都要住在这里。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x101,
        (
            "#1026F是吗……\x01",
            "坐定期船来的那些人啊。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9EE")

    ChrTalk(    #6
        0x103,
        (
            "#522F抱歉，还要请您\x01",
            "再坚持一阵。\x02\x03",

            "我们会尽全力去\x01",
            "改善现在的状况的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9EE")


    ChrTalk(    #7
        0x9,
        (
            "嗯，我知道大家\x01",
            "很努力。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x9,
        "我会继续支持你们的。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x20A4)
    Jump("loc_B81")

    label("loc_A2B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 6)), scpexpr(EXPR_END)), "loc_A96")

    ChrTalk(    #9
        0x9,
        (
            "刚才听到结婚\x01",
            "礼乐了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x9,
        (
            "结婚仪式算是最近\x01",
            "少有的开心话题了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x9,
        (
            "祝福那对年轻\x01",
            "的新人吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B81")

    label("loc_A96")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B2C")

    ChrTalk(    #12
        0x9,
        (
            "导力器不能使用\x01",
            "对我们的营业\x01",
            "有很大影响呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x9,
        (
            "不过我们还是努力\x01",
            "维持着营业。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x9,
        (
            "滞留在飞船坪的那些人倒也算是\x01",
            "提供了足够的客源。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_B81")

    label("loc_B2C")


    ChrTalk(    #15
        0x9,
        (
            "导力器不能使用\x01",
            "对我们的营业……\x01",
            "总之状况很不好。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x9,
        (
            "希望可以早点\x01",
            "恢复正常吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B81")

    Jump("loc_1092")

    label("loc_B84")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 0)), scpexpr(EXPR_END)), "loc_C5F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_BDB")

    ChrTalk(    #17
        0x9,
        (
            "被限制行动的客人们\x01",
            "也平安出发了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x9,
        (
            "希望他们下次\x01",
            "旅行顺利啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C5C")

    label("loc_BDB")


    ChrTalk(    #19
        0x9,
        (
            "定期船终于恢复了，\x01",
            "被限制行动的客人们\x01",
            "也平安出发了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x9,
        (
            "客人都平安的离开了，\x01",
            "心情真好。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x9,
        (
            "希望他们下次\x01",
            "旅行顺利啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_C5C")

    Jump("loc_1092")

    label("loc_C5F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_END)), "loc_CE8")

    ChrTalk(    #22
        0x9,
        (
            "王国军的人\x01",
            "好像也到了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x9,
        (
            "洛连特这里来了\x01",
            "很多穿军服的人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x9,
        (
            "这种状况下，这也是没办法的事。\x01",
            "现在要以警备工作为优先。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1092")

    label("loc_CE8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 4)), scpexpr(EXPR_END)), "loc_E10")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 6)), scpexpr(EXPR_END)), "loc_D5F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_D21")

    ChrTalk(    #25
        0x9,
        (
            "昨天谢谢了，\x01",
            "欢迎下次光临。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D5C")

    label("loc_D21")


    ChrTalk(    #26
        0x9,
        (
            "巡逻到深夜还\x01",
            "真是辛苦啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x9,
        (
            "希望你们下次\x01",
            "再来。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_D5C")

    Jump("loc_E0D")

    label("loc_D5F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_DAD")

    ChrTalk(    #28
        0x9,
        (
            "你们的伙伴正在房间\x01",
            "中休息。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x9,
        (
            "好像还在睡，\x01",
            "看样子很累了吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E0D")

    label("loc_DAD")


    ChrTalk(    #30
        0x9,
        (
            "啊，各位，\x01",
            "早上好。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x9,
        (
            "你们的伙伴正在房间\x01",
            "中休息。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x9,
        (
            "好像还在睡，\x01",
            "看样子很累了吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_E0D")

    Jump("loc_1092")

    label("loc_E10")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 4)), scpexpr(EXPR_END)), "loc_F44")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_E78")

    ChrTalk(    #33
        0x9,
        (
            "浓雾的事\x01",
            "我也记不清楚了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x9,
        (
            "街道视线很差，\x01",
            "可能会有危险哟。\x01",
            "请不要贸然行动啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F41")

    label("loc_E78")


    ChrTalk(    #35
        0x9,
        (
            "艾丝蒂尔，\x01",
            "还有雪拉扎德…\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x9,
        (
            "欢迎光临浓雾中的\x01",
            "洛连特旅馆。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x9,
        "…４位都要住宿吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x101,
        (
            "#1000F呜…不是呢，\x01",
            "只是来看看而已。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x9,
        (
            "这样状况不明，\x01",
            "街道上就很危险了吧…\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x9,
        "无论如何请大家小心。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_F41")

    Jump("loc_1092")

    label("loc_F44")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 3)), scpexpr(EXPR_END)), "loc_1092")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_FA0")

    ChrTalk(    #41
        0x9,
        (
            "艾丝蒂尔和\x01",
            "约修亚是我们洛连特的骄傲。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x9,
        "没开玩笑，我真是那么想的。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1092")

    label("loc_FA0")


    ChrTalk(    #43
        0x9,
        (
            "啊……\x01",
            "这不是艾丝蒂尔吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x9,
        (
            "听说你在各地十分活跃，\x01",
            "还取得了武术大会的优胜啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x9,
        (
            "艾丝蒂尔和约修亚\x01",
            "已经是洛连特的骄傲了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x101,
        (
            "#000F啊啊～\x01",
            "不要太夸赞我啦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x9,
        (
            "这不是夸赞，\x01",
            "而是真心的想法。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x142,
        (
            "#1060F（嘿……\x01",
            "　真了不起呢……）\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_1092")

    TalkEnd(0x9)
    Return()

    # Function_11_81D end

    def Function_12_1096(): pass

    label("Function_12_1096")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 4)), scpexpr(EXPR_END)), "loc_1191")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1115")

    ChrTalk(    #49
        0xFE,
        (
            "先去柏斯有急事，\x01",
            "然后还要返回王都，\x01",
            "都要用到飞船啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0xFE,
        (
            "不过有游击士的护送，\x01",
            "算了，步行应该也可以。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1191")

    label("loc_1115")


    ChrTalk(    #51
        0xFE,
        (
            "我有些急事必须\x01",
            "要去柏斯。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0xFE,
        (
            "然后还要返回王都，\x01",
            "都要用到飞船啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0xFE,
        (
            "不过有游击士的护送，\x01",
            "算了，步行应该也可以。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_1191")

    TalkEnd(0xA)
    Return()

    # Function_12_1096 end

    def Function_13_1195(): pass

    label("Function_13_1195")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_END)), "loc_11D9")

    ChrTalk(    #54
        0xFE,
        "钱、钱包已经…\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0xFE,
        (
            "接、接下来一定\x01",
            "要节约一点了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12D3")

    label("loc_11D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 4)), scpexpr(EXPR_END)), "loc_12D3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_1234")

    ChrTalk(    #56
        0xFE,
        (
            "真没想到要在这么豪华\x01",
            "的旅馆住宿。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0xFE,
        (
            "可、可以吗？\x01",
            "真是没心理准备，\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12D3")

    label("loc_1234")


    ChrTalk(    #58
        0xFE,
        (
            "本来想着在飞船公社\x01",
            "住宿就可以了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0xFE,
        (
            "他们说是普通的住处，\x01",
            "都没抱过什么期待。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0xFE,
        (
            "真没想到要在这么豪华\x01",
            "的旅馆住宿。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0xFE,
        (
            "可、可以吗？\x01",
            "还没心理准备。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_12D3")

    TalkEnd(0xB)
    Return()

    # Function_13_1195 end

    def Function_14_12D7(): pass

    label("Function_14_12D7")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_END)), "loc_136E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_1324")

    ChrTalk(    #62
        0xFE,
        "真是很不错的店呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0xFE,
        (
            "他给我买了好多\x01",
            "的小礼物呢㈱\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_136B")

    label("loc_1324")


    ChrTalk(    #64
        0xFE,
        (
            "商店街中有个\x01",
            "不错的杂货店呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0xFE,
        (
            "他给我买了好多\x01",
            "的小礼物呢㈱\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_136B")

    Jump("loc_13E8")

    label("loc_136E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 4)), scpexpr(EXPR_END)), "loc_13E8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_13BA")

    ChrTalk(    #66
        0xFE,
        (
            "要是能免费住在这个房间的话，\x01",
            "我就愿意原谅公社的过失。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13E8")

    label("loc_13BA")


    ChrTalk(    #67
        0xFE,
        (
            "哇～好棒的房间啊。\x01",
            "疲劳马上就没有了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_13E8")

    TalkEnd(0xC)
    Return()

    # Function_14_12D7 end

    def Function_15_13EC(): pass

    label("Function_15_13EC")

    TalkBegin(0xD)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_END)), "loc_1437")

    ChrTalk(    #68
        0xFE,
        (
            "嗯～要是带着\x01",
            "扑克来就好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0xFE,
        (
            "真是不错的\x01",
            "亲子旅行啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14DC")

    label("loc_1437")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 4)), scpexpr(EXPR_END)), "loc_14DC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_1487")

    ChrTalk(    #70
        0xFE,
        (
            "不过，在雾散去之前\x01",
            "要做什么好呢～？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0xFE,
        "呼，真是烦恼呢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_14DC")

    label("loc_1487")


    ChrTalk(    #72
        0xFE,
        (
            "呼，替我们准备好了住处，\x01",
            "总算是放心了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0xFE,
        (
            "不愧是公社啊。\x01",
            "应对措施很完善。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)

    label("loc_14DC")

    TalkEnd(0xD)
    Return()

    # Function_15_13EC end

    def Function_16_14E0(): pass

    label("Function_16_14E0")

    TalkBegin(0xE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_END)), "loc_159A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_1532")

    ChrTalk(    #74
        0xFE,
        (
            "看啊，爸爸。\x01",
            "该轮到爸爸了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0xFE,
        (
            "特制的饼干中\x01",
            "的干字哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1597")

    label("loc_1532")


    ChrTalk(    #76
        0xFE,
        "爸爸～要玩接龙吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0xFE,
        (
            "嗯，第一个词是\x01",
            "特制的饼干。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0xFE,
        (
            "啊，该轮到爸爸了。\x01",
            "是饼干的干字哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x6)

    label("loc_1597")

    Jump("loc_1634")

    label("loc_159A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 4)), scpexpr(EXPR_END)), "loc_15DA")

    ChrTalk(    #79
        0xFE,
        (
            "爸爸去飞船坪\x01",
            "查看情况了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0xFE,
        (
            "所以我\x01",
            "留在这里。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1634")

    label("loc_15DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 4)), scpexpr(EXPR_END)), "loc_1634")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_1607")

    ChrTalk(    #81
        0xFE,
        "嘿嘿，我最喜欢外宿了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1634")

    label("loc_1607")


    ChrTalk(    #82
        0xFE,
        "今天就住在这里。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0xFE,
        "嘿嘿，太好啦。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x6)

    label("loc_1634")

    TalkEnd(0xE)
    Return()

    # Function_16_14E0 end

    def Function_17_1638(): pass

    label("Function_17_1638")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 0)), scpexpr(EXPR_END)), "loc_1685")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_165E")

    ChrTalk(    #84
        0xFE,
        "呜——呜——\x02",
    )

    CloseMessageWindow()
    Jump("loc_1685")

    label("loc_165E")


    ChrTalk(    #85
        0xFE,
        "呜——呜——\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0xFE,
        "心情真不好。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x7)

    label("loc_1685")

    TalkEnd(0xFE)
    Return()

    # Function_17_1638 end

    def Function_18_1689(): pass

    label("Function_18_1689")

    TalkBegin(0x11)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 0)), scpexpr(EXPR_END)), "loc_17BB")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x76, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_175A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_16E9")

    ChrTalk(    #87
        0xFE,
        (
            "安敦那家伙\x01",
            "好像很痛苦的样子。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0xFE,
        (
            "明明不会喝酒\x01",
            "却喝那么多。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1757")

    label("loc_16E9")


    ChrTalk(    #89
        0xFE,
        (
            "虽然有教区长\x01",
            "在照顾他，\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0xFE,
        (
            "但安敦那家伙\x01",
            "好像很痛苦的样子。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0xFE,
        (
            "不过也许只能暂时\x01",
            "把他扔在一边了吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x8)

    label("loc_1757")

    Jump("loc_17BB")

    label("loc_175A")


    ChrTalk(    #92
        0xFE,
        (
            "安敦那家伙\x01",
            "明明是没结果的单相思，\x01",
            "却还是不死心。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0xFE,
        (
            "算了，在他明白之前，\x01",
            "我一直在这里等。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17BB")

    TalkEnd(0x11)
    Return()

    # Function_18_1689 end

    def Function_19_17BF(): pass

    label("Function_19_17BF")

    OP_62(0xF, 0x0, 2000, 0x1C, 0x21, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0xF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1815")

    ChrTalk(    #94
        0xF,
        (
            "#034F呜～呜……………\x01",
            "……………………………\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A2B")

    label("loc_1815")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x310, 6)), scpexpr(EXPR_END)), "loc_18B5")

    ChrTalk(    #95
        0xF,
        (
            "#034F呜……呜……………\x01",
            "……………………………\x02\x03",

            "已……已经不能……………\x01",
            "…………再、再喝了……\x02\x03",

            "#034F呜～呜……………\x01",
            "……………………………\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_1A2B")

    label("loc_18B5")


    ChrTalk(    #96
        0xF,
        (
            "#034F呜……呜……………\x01",
            "……………………………\x02\x03",

            "啊啊……雪拉小姐………\x01",
            "……爱、爱娜……\x02\x03",

            "已……已经不能……………\x01",
            "…………再、再喝了……\x02",
        )
    )

    CloseMessageWindow()
    OP_9E(0x8, 0xF, 0x0, 0x12C, 0xFA0)

    ChrTalk(    #97
        0xF,
        (
            "#038F哇…………………\x01",
            "……那个瓶子……！\x02",
        )
    )

    CloseMessageWindow()
    OP_9E(0x8, 0xF, 0x0, 0x12C, 0xFA0)

    ChrTalk(    #98
        0xF,
        "#038F啊啊………………！！\x02",
    )

    CloseMessageWindow()
    OP_9E(0x8, 0xF, 0x0, 0x12C, 0xFA0)

    ChrTalk(    #99
        0xF,
        "#038F……○△×＄□￥～～！！\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #100
        0x101,
        "#1019F（似乎做恶梦了啊。）\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_1A2B")

    OP_A2(0x1886)
    TalkEnd(0xFF)
    Return()

    # Function_19_17BF end

    def Function_20_1A32(): pass

    label("Function_20_1A32")

    TalkBegin(0x16)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x74, 0x1, 0x2000)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_29(0x74, 0x0, 0x8)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x74, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1B3B")

    ChrTalk(    #101
        0xFE,
        "啊～各位游击士。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0xFE,
        (
            "你们看～～安莉尔\x01",
            "当了妈妈回来了哦～\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #103
        0x101,
        (
            "#1004F咦咦！？\x02\x03",

            "带、带着自己的宝宝们回来的？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #104
        0xFE,
        "嗯～是啊～～\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0xFE,
        (
            "所以，现在\x01",
            "正在想名字哦～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0xFE,
        (
            "嗯～怎样的名字\x01",
            "才好呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x74, 0x1, 0x2000)
    Jump("loc_1DC8")

    label("loc_1B3B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_END)), "loc_1C6A")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x74, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1C23")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_1B9A")

    ChrTalk(    #107
        0xFE,
        (
            "雾好像\x01",
            "一点要散去的迹象都没有啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0xFE,
        (
            "连阿姨都\x01",
            "有点担心了呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C20")

    label("loc_1B9A")


    ChrTalk(    #109
        0xFE,
        "啊～各位游击士。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0xFE,
        (
            "真是辛苦，在这种天气\x01",
            "也要工作。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0xFE,
        (
            "雾好像\x01",
            "一点要散去的迹象都没有啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0xFE,
        (
            "啊啊～洛连特究竟\x01",
            "怎么了啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x9)

    label("loc_1C20")

    Jump("loc_1C67")

    label("loc_1C23")


    ChrTalk(    #113
        0xFE,
        (
            "雾好像\x01",
            "一点要散去的迹象都没有啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0xFE,
        (
            "连阿姨都\x01",
            "有点担心了呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C67")

    Jump("loc_1DC8")

    label("loc_1C6A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x74, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1D69")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_1CE2")

    ChrTalk(    #115
        0xFE,
        (
            "今天又是这种鬼天气，\x01",
            "阿姨在家休息了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0xFE,
        (
            "要好好想想小猫们\x01",
            "的名字啊～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0xFE,
        "呼呼～阿姨好烦恼㈱\x02",
    )

    CloseMessageWindow()
    Jump("loc_1D66")

    label("loc_1CE2")


    ChrTalk(    #118
        0xFE,
        "啊～各位游击士。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0xFE,
        (
            "呼呼～～昨天\x01",
            "真是多谢了㈱\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0xFE,
        (
            "今天又是这种鬼天气，\x01",
            "阿姨在家休息了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0xFE,
        (
            "要好好想想小猫们\x01",
            "的名字啊～\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x9)

    label("loc_1D66")

    Jump("loc_1DC8")

    label("loc_1D69")


    ChrTalk(    #122
        0xFE,
        (
            "雾好像\x01",
            "越来越浓了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0xFE,
        (
            "今天好像不能\x01",
            "在阳台午睡了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0xFE,
        (
            "和小猫们一起在家\x01",
            "好好休息吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1DC8")

    TalkEnd(0x16)
    Return()

    # Function_20_1A32 end

    def Function_21_1DCC(): pass

    label("Function_21_1DCC")

    TalkBegin(0x17)
    OP_22(0x192, 0x0, 0x64)

    ChrTalk(    #125
        0xFE,
        "喵～～\x02",
    )

    CloseMessageWindow()
    TalkEnd(0x17)
    Return()

    # Function_21_1DCC end

    def Function_22_1DE4(): pass

    label("Function_22_1DE4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 6)), scpexpr(EXPR_END)), "loc_1E4B")

    ChrTalk(    #126
        0xFE,
        (
            "还在想为什么这么热闹，\x01",
            "原来是结婚仪式啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0xFE,
        (
            "呵呵，真不错啊。\x01",
            "让人感到人性的坚强。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E9F")

    label("loc_1E4B")


    ChrTalk(    #128
        0xFE,
        (
            "洛连特暂时是没事了，\x01",
            "但不知道别的城市怎么样。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0xFE,
        (
            "也许暂时待在\x01",
            "这里比较好吧…\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E9F")

    TalkEnd(0xFE)
    Return()

    # Function_22_1DE4 end

    def Function_23_1EA3(): pass

    label("Function_23_1EA3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 5)), scpexpr(EXPR_END)), "loc_1F06")

    ChrTalk(    #130
        0xFE,
        (
            "刚才在城里转了转，\x01",
            "大家比我想象的要冷静啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0xFE,
        (
            "呼～乡村城市\x01",
            "还真是名不虚传啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1FCE")

    label("loc_1F06")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_1F53")

    ChrTalk(    #132
        0xFE,
        (
            "四处去看了看，\x01",
            "哪里都没什么变化。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0xFE,
        "……我就在这里等着了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1FCE")

    label("loc_1F53")


    ChrTalk(    #134
        0xFE,
        (
            "看了看飞船坪的情况，\x01",
            "那里也有一些人，\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0xFE,
        "不过似乎都是被迫待在那里的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0xFE,
        (
            "虽然指示灯还亮着，\x01",
            "但飞船无法起飞了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_1FCE")

    TalkEnd(0xFE)
    Return()

    # Function_23_1EA3 end

    def Function_24_1FD2(): pass

    label("Function_24_1FD2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 5)), scpexpr(EXPR_END)), "loc_2079")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_2025")

    ChrTalk(    #137
        0xFE,
        "这种时候也没有工作了，\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0xFE,
        (
            "好好休息吧。\x01",
            "等着定期船恢复。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2076")

    label("loc_2025")


    ChrTalk(    #139
        0xFE,
        (
            "王国中的导力器\x01",
            "好像都瘫痪了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0xFE,
        (
            "这种时候也不会有工作，\x01",
            "稍微歇一歇吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)

    label("loc_2076")

    Jump("loc_2144")

    label("loc_2079")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_20D7")

    ChrTalk(    #141
        0xFE,
        (
            "雾散去之前\x01",
            "就可以随意使用这房间哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0xFE,
        (
            "虽说是第二次说……\x01",
            "不过拜托饶了我吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2144")

    label("loc_20D7")


    ChrTalk(    #143
        0xFE,
        (
            "之前在洛连特\x01",
            "也是因为大雾停留在这…\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0xFE,
        (
            "啊，那时候好像\x01",
            "也是住在这房间哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0xFE,
        "嗯，好厉害的巧合啊。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x5)

    label("loc_2144")

    TalkEnd(0xFE)
    Return()

    # Function_24_1FD2 end

    def Function_25_2148(): pass

    label("Function_25_2148")

    TalkBegin(0x1B)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_27CB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x413, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_274E")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_219A")

    ChrTalk(    #146
        0xFE,
        (
            "啊，艾丝蒂尔和约修亚～\x01",
            "……还有雪拉前辈。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2213")

    label("loc_219A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_21DA")

    ChrTalk(    #147
        0xFE,
        (
            "啊，艾丝蒂尔和约修亚～\x01",
            "还有阿加特先生……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2213")

    label("loc_21DA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2213")

    ChrTalk(    #148
        0xFE,
        (
            "啊，艾丝蒂尔和约修亚～\x01",
            "还有金先生……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2213")


    ChrTalk(    #149
        0xFE,
        (
            "那个……在矿山\x01",
            "麻烦你们了，真是感谢。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2302")

    ChrTalk(    #150
        0x103,
        (
            "#524F不用在意，\x01",
            "你做很出色。\x02\x03",

            "真的…\x01",
            "说老实话，要对你刮目相看了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x103, 400)

    ChrTalk(    #151
        0xFE,
        "啊…？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #152
        0x103,
        (
            "#020F勇气十足地留在现场，\x01",
            "保护了全体矿工。\x02\x03",

            "多余的话就不说了，\x01",
            "总之，你做得很出色。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2433")

    label("loc_2302")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2393")

    ChrTalk(    #153
        0x106,
        (
            "#051F不要介意，\x01",
            "你干得已经很棒了。\x02\x03",

            "在那种艰难的情形下做出最佳判断，\x01",
            "真的很了不起。\x02\x03",

            "多余的话就不多说了，\x01",
            "总之你做得很好。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2433")

    label("loc_2393")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2433")

    ChrTalk(    #154
        0x108,
        (
            "#070F不用介意啊。\x01",
            "我认为你做得很出色。\x02\x03",

            "在那种艰难的情形下做出最佳判断，\x01",
            "而且也达到了目的。\x02\x03",

            "任何一个优秀的游击士\x01",
            "也都会做出和你一样的判断。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2433")


    ChrTalk(    #155
        0x101,
        (
            "#1015F嗯，确实……\x02\x03",

            "毕竟利吉先生是\x01",
            "一个人在奋战啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #156
        0x102,
        (
            "#1040F我们只是来增援的，\x01",
            "功劳可远不如你呢。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #157
        0xFE,
        "啊，谢谢……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #158
        0xFE,
        (
            "可、可是…\x01",
            "我还差得很远呢。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2572")

    ChrTalk(    #159
        0x103,
        (
            "#025F哈哈，没自信\x01",
            "就是你最大的缺点了。\x02\x03",

            "#027F你的实力很不错，\x01",
            "所以应该拿出自信。\x02\x03",

            "只要有你在的话，\x01",
            "我们即使离开也不会担心的。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x103, 400)
    Jump("loc_268C")

    label("loc_2572")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2608")

    ChrTalk(    #160
        0x106,
        (
            "#551F缺乏自信\x01",
            "就是你最大的弱点啦！\x02\x03",

            "#050F既然自己有实力，\x01",
            "就应该拿出信心来！\x02\x03",

            "正因为有你在，\x01",
            "所以雪拉扎德\x01",
            "可以放心离开。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x106, 400)
    Jump("loc_268C")

    label("loc_2608")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_268C")

    ChrTalk(    #161
        0x108,
        (
            "#070F不要说那种\x01",
            "话啊！\x02\x03",

            "你的实力很不错，\x01",
            "所以应该拿出自信来！\x02\x03",

            "正因为有你在，\x01",
            "所以雪拉扎德\x01",
            "可以放心离开。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x108, 400)

    label("loc_268C")


    ChrTalk(    #162
        0xFE,
        "是、是的！！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #163
        0xFE,
        (
            "我今后也会继续努力，\x01",
            "争取追上前辈们的！\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_26F5")

    ChrTalk(    #164
        0x108,
        "#070F嗯！这样才对。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2748")

    label("loc_26F5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_271D")

    ChrTalk(    #165
        0x106,
        "#051F嗯，努力吧！\x02",
    )

    CloseMessageWindow()
    Jump("loc_2748")

    label("loc_271D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2748")

    ChrTalk(    #166
        0x103,
        "#021F呵呵，就是要这样。\x02",
    )

    CloseMessageWindow()

    label("loc_2748")

    OP_A2(0x209F)
    Jump("loc_27CB")

    label("loc_274E")


    ChrTalk(    #167
        0xFE,
        (
            "虽然身体还疼得很……\x01",
            "但总觉得很充实呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #168
        0xFE,
        (
            "真的……\x01",
            "能当游击士真是太好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #169
        0xFE,
        (
            "通过这次的事件，\x01",
            "这种想法更加坚定了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_27CB")

    TalkEnd(0x1B)
    Return()

    # Function_25_2148 end

    def Function_26_27CF(): pass

    label("Function_26_27CF")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #170
        (
            "\x07\x05　　　　　　　工作人员室　　　　　　　\x01",
            "          ※无关人员请勿入内\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_26_27CF end

    SaveToFile()

Try(main)
