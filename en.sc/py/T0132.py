from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        'Olivier',                              # 9
        'Verne',                                # 10
        'Passenger',                            # 11
        'Passenger',                            # 12
        'Passenger',                            # 13
        'Passenger',                            # 14
        'Passenger',                            # 15
        'Olivier',                              # 16
        'Anton',                                # 17
        'Ricky',                                # 18
        'Anton',                                # 19
        'Linde Passenger',                      # 20
        'Linde Passenger',                      # 21
        'Linde Passenger',                      # 22
        'Ida',                                  # 23
        'Aryll',                                # 24
        'Kitten',                               # 25
        'Kitten',                               # 26
        'Kitten',                               # 27
        'Ridge',                                # 28
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
        "Function_12_15B4",        # 0C, 12
        "Function_13_1762",        # 0D, 13
        "Function_14_1958",        # 0E, 14
        "Function_15_1B17",        # 0F, 15
        "Function_16_1C6F",        # 10, 16
        "Function_17_1E50",        # 11, 17
        "Function_18_1EC1",        # 12, 18
        "Function_19_20B5",        # 13, 19
        "Function_20_22C9",        # 14, 20
        "Function_21_27FD",        # 15, 21
        "Function_22_2819",        # 16, 22
        "Function_23_2955",        # 17, 23
        "Function_24_2B2A",        # 18, 24
        "Function_25_2DEA",        # 19, 25
        "Function_26_3638",        # 1A, 26
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

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_D89")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x414, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B10")
    OP_62(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0x9, 0x101, 0)
    Sleep(400)

    ChrTalk(    #0
        0x9,
        (
            "Oh, Estelle...\x01",
            "You're with Joshua today, I see.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x102, 400)

    ChrTalk(    #1
        0x9,
        (
            "It seems like it's been a long\x01",
            "time since I've seen Joshua.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x102,
        (
            "#1040FYeah, it really has been a while.\x02\x03",

            "So, since the orbments have stopped working,\x01",
            "how's work going?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x9,
        (
            "Well, we're managing to continue\x01",
            "business somehow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x9,
        (
            "We're currently seeing to guests from\x01",
            "the landing port.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x101,
        (
            "#1026FAh, gotcha... The people who were on\x01",
            "the airship.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_AAB")

    ChrTalk(    #6
        0x103,
        (
            "#522FSorry, but hopefully you can\x01",
            "keep on as is for a while.\x02\x03",

            "We're doing our best to improve\x01",
            "the situation on our end.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AAB")


    ChrTalk(    #7
        0x9,
        "I'm well aware of your efforts.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x9,
        (
            "I may be unable to assist you,\x01",
            "but I do support you.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x20A4)
    Jump("loc_D86")

    label("loc_B10")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 6)), scpexpr(EXPR_END)), "loc_BE9")

    ChrTalk(    #9
        0x9,
        (
            "The wedding bells from a bit\x01",
            "ago echoed all the way here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x9,
        (
            "That wedding is one of the few cheerier\x01",
            "topics of discussion we've had lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x9,
        (
            "I'm happy to celebrate a young\x01",
            "couple's new beginning.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D86")

    label("loc_BE9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CE1")

    ChrTalk(    #12
        0x9,
        (
            "Being unable to use orbal energy is quite\x01",
            "the handicap to those of us in the service\x01",
            "industry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x9,
        (
            "However, we are managing to continue\x01",
            "business somehow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x9,
        (
            "We do have customers who have\x01",
            "come from the landing port, after all.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_D86")

    label("loc_CE1")


    ChrTalk(    #15
        0x9,
        (
            "Being unable to use orbal energy is quite\x01",
            "the handicap to those of us in the service\x01",
            "industry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x9,
        (
            "I too hope for the restoration\x01",
            "of such as soon as possible.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D86")

    Jump("loc_15B0")

    label("loc_D89")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 0)), scpexpr(EXPR_END)), "loc_F44")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_E32")

    ChrTalk(    #17
        0x9,
        "The passengers who were delayed departed safely.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x9,
        (
            "I hope the next time they come to visit it'll be\x01",
            "for tourism rather than unexpected trouble.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F41")

    label("loc_E32")


    ChrTalk(    #19
        0x9,
        (
            "Finally the scheduled liners have resumed\x01",
            "service and the passengers who were delayed\x01",
            "departed safely.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x9,
        (
            "It is always pleasant to see customers\x01",
            "off after a stay.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x9,
        (
            "I hope the next time they come to visit it'll be\x01",
            "for tourism rather than unexpected trouble.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_F41")

    Jump("loc_15B0")

    label("loc_F44")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_END)), "loc_1023")

    ChrTalk(    #22
        0x9,
        "The people from the Royal Army have arrived.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x9,
        (
            "Army uniforms seem out of place\x01",
            "in peaceful Rolent...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x9,
        (
            "There isn't much choice given the circumstances,\x01",
            "though. Right now we need to prioritize security.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15B0")

    label("loc_1023")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 4)), scpexpr(EXPR_END)), "loc_11F6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 6)), scpexpr(EXPR_END)), "loc_10EC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_108D")

    ChrTalk(    #25
        0x9,
        (
            "Thank you very much for last night. I\x01",
            "look forward to your future patronage.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10E9")

    label("loc_108D")


    ChrTalk(    #26
        0x9,
        "Good work on your patrols last night.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x9,
        "I look forward to your future patronage.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_10E9")

    Jump("loc_11F3")

    label("loc_10EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1161")

    ChrTalk(    #28
        0x9,
        "Your accompaniment is in their room.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x9,
        (
            "They still appear to be resting...\x01",
            "They must be very tired.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11F3")

    label("loc_1161")


    ChrTalk(    #30
        0x9,
        "Why, everyone... Good morning.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x9,
        "Your accompaniment is in their room.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x9,
        (
            "They still appear to be resting...\x01",
            "They must be very tired.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_11F3")

    Jump("loc_15B0")

    label("loc_11F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 4)), scpexpr(EXPR_END)), "loc_13ED")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_12C6")

    ChrTalk(    #33
        0x9,
        (
            "I have no recollection of a fog this\x01",
            "thick ever descending on Rolent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x9,
        (
            "I am sure the highways must be most dangerous\x01",
            "with vision so reduced... Please, do not push\x01",
            "yourself too hard.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13EA")

    label("loc_12C6")


    ChrTalk(    #35
        0x9,
        "Why, Estelle and Scherazard...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x9,
        "Welcome to Hotel Rolent.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x9,
        "Will the four of you be staying?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x101,
        (
            "#1000FNo, we're not. We just came\x01",
            "by to see how things are.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x9,
        (
            "I am sure there is much danger on\x01",
            "the highways in these circumstances.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x9,
        "Please, do not push yourself too hard.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_13EA")

    Jump("loc_15B0")

    label("loc_13ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 3)), scpexpr(EXPR_END)), "loc_15B0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1461")

    ChrTalk(    #41
        0x9,
        "You and Joshua truly are the pride of Rolent.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x9,
        "I really do mean that. You inspire us all.\x02",
    )

    CloseMessageWindow()
    Jump("loc_15B0")

    label("loc_1461")


    ChrTalk(    #43
        0x9,
        "Oh... Why, Estelle.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x9,
        (
            "On top of everything I heard about in the news,\x01",
            "I understand you won the Martial Arts Competition\x01",
            "as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x9,
        "You and Joshua truly are the pride of Rolent.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x101,
        "#000FAwww, c'mon, Verne. Stop flattering me.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x9,
        (
            "No, no, I do mean that.\x01",
            "You inspire us all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x142,
        "#1060F(Huh... She really is something.)\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_15B0")

    TalkEnd(0x9)
    Return()

    # Function_11_81D end

    def Function_12_15B4(): pass

    label("Function_12_15B4")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 4)), scpexpr(EXPR_END)), "loc_175E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1687")

    ChrTalk(    #49
        0xFE,
        (
            "I have urgent business in Bose, so I'm planning\x01",
            "to return to the capital and take the reverse-\x01",
            "bound ship.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0xFE,
        (
            "We'll have a bracer as escort, so we\x01",
            "SHOULD be able to get there on foot.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_175E")

    label("loc_1687")


    ChrTalk(    #51
        0xFE,
        (
            "I've got a bit of urgent business in Bose,\x01",
            "you see.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0xFE,
        (
            "I'm planning to return to the capital and take\x01",
            "the reverse-bound ship.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0xFE,
        (
            "We'll have a bracer as escort, so we\x01",
            "SHOULD be able to get there on foot.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_175E")

    TalkEnd(0xA)
    Return()

    # Function_12_15B4 end

    def Function_13_1762(): pass

    label("Function_13_1762")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_END)), "loc_17C7")

    ChrTalk(    #54
        0xFE,
        "M-My purse...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0xFE,
        (
            "I-I'm really gonna have to cut back\x01",
            "on my spending for a while.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1954")

    label("loc_17C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 4)), scpexpr(EXPR_END)), "loc_1954")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_184D")

    ChrTalk(    #56
        0xFE,
        "I didn't think we'd stay at such a nice hotel.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0xFE,
        (
            "Is-is this really okay?\x01",
            "I feel like I seriously lucked out.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1954")

    label("loc_184D")


    ChrTalk(    #58
        0xFE,
        (
            "The airship company's taking care of \x01",
            "the lodging from what I understand.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0xFE,
        (
            "They said it'd be free, so I wasn't\x01",
            "expecting much, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0xFE,
        "I didn't think we'd stay at such a nice hotel.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0xFE,
        (
            "Is-is this really okay?\x01",
            "I feel like I seriously lucked out.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_1954")

    TalkEnd(0xB)
    Return()

    # Function_13_1762 end

    def Function_14_1958(): pass

    label("Function_14_1958")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_END)), "loc_1A54")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_19CC")

    ChrTalk(    #62
        0xFE,
        "That's a pretty nice shop there.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0xFE,
        (
            "I got my boyfriend to buy\x01",
            "me a lot of little things.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A51")

    label("loc_19CC")


    ChrTalk(    #64
        0xFE,
        (
            "I found an intriguing little general\x01",
            "store on the merchant street.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0xFE,
        (
            "I got my boyfriend to buy\x01",
            "me a lot of little things.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_1A51")

    Jump("loc_1B13")

    label("loc_1A54")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 4)), scpexpr(EXPR_END)), "loc_1B13")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_1ACA")

    ChrTalk(    #66
        0xFE,
        (
            "Since they're letting us stay in this room for\x01",
            "free, I guess I can forgive the airship company.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B13")

    label("loc_1ACA")


    ChrTalk(    #67
        0xFE,
        (
            "Wow, what a nice room.\x01",
            "It just chases the exhaustion right away.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_1B13")

    TalkEnd(0xC)
    Return()

    # Function_14_1958 end

    def Function_15_1B17(): pass

    label("Function_15_1B17")

    TalkBegin(0xD)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_END)), "loc_1B8E")

    ChrTalk(    #68
        0xFE,
        "Hmm, I wish I'd brought a deck of cards.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0xFE,
        (
            "Feels like this really has become\x01",
            "a parent-child trip.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C6B")

    label("loc_1B8E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 4)), scpexpr(EXPR_END)), "loc_1C6B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_1BED")

    ChrTalk(    #70
        0xFE,
        (
            "Still, how long will it be until\x01",
            "this fog clears, I wonder...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0xFE,
        "Phew!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1C6B")

    label("loc_1BED")


    ChrTalk(    #72
        0xFE,
        (
            "Phew! They got this room for us,\x01",
            "so that's a relief.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0xFE,
        (
            "As I'd expect from the company.\x01",
            "They really responded well.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)

    label("loc_1C6B")

    TalkEnd(0xD)
    Return()

    # Function_15_1B17 end

    def Function_16_1C6F(): pass

    label("Function_16_1C6F")

    TalkBegin(0xE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_END)), "loc_1D74")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_1CD6")

    ChrTalk(    #74
        0xFE,
        "Hey, Daddy. Next it's your turn.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0xFE,
        "Remember, it's 'E' from 'maple cookie.'\x02",
    )

    CloseMessageWindow()
    Jump("loc_1D71")

    label("loc_1CD6")


    ChrTalk(    #76
        0xFE,
        "Daddy, let's play the word game.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0xFE,
        "So first, I'll start with 'maple cookie.'\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0xFE,
        (
            "Come on, Daddy, it's your turn.\x01",
            "It's 'E' from 'maple cookie.'\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x6)

    label("loc_1D71")

    Jump("loc_1E4C")

    label("loc_1D74")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 4)), scpexpr(EXPR_END)), "loc_1DE5")

    ChrTalk(    #79
        0xFE,
        "Daddy went off to see how the airship place is.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0xFE,
        "I'm in charge of the room till he gets back!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1E4C")

    label("loc_1DE5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 4)), scpexpr(EXPR_END)), "loc_1E4C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_1E16")

    ChrTalk(    #81
        0xFE,
        "Heehee, I love sleepovers.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1E4C")

    label("loc_1E16")


    ChrTalk(    #82
        0xFE,
        "We're staying here tonight.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0xFE,
        "Heehee, yay.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x6)

    label("loc_1E4C")

    TalkEnd(0xE)
    Return()

    # Function_16_1C6F end

    def Function_17_1E50(): pass

    label("Function_17_1E50")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 0)), scpexpr(EXPR_END)), "loc_1EBD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_1E87")

    ChrTalk(    #84
        0xFE,
        "Uhhhhhhh, uhhhhhh, ughhhhh...\x02",
    )

    CloseMessageWindow()
    Jump("loc_1EBD")

    label("loc_1E87")


    ChrTalk(    #85
        0xFE,
        "Uuhh, uggghh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0xFE,
        "I...don...veel so goo...\x02",
    )

    CloseMessageWindow()
    OP_A2(0x7)

    label("loc_1EBD")

    TalkEnd(0xFE)
    Return()

    # Function_17_1E50 end

    def Function_18_1EC1(): pass

    label("Function_18_1EC1")

    TalkBegin(0x11)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 0)), scpexpr(EXPR_END)), "loc_20B1")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x76, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_201A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_1F86")

    ChrTalk(    #87
        0xFE,
        "Seems like Anton's still feelin' pretty bad.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0xFE,
        (
            "No big surprise there, really. The guy can barely\x01",
            "handle beer and he downed glass after glass\x01",
            "of strong liquor.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2017")

    label("loc_1F86")


    ChrTalk(    #89
        0xFE,
        "Father Divine treated him, but...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0xFE,
        "Seems like Anton's still feelin' pretty bad.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0xFE,
        "Might not be able to leave him alone for a bit.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x8)

    label("loc_2017")

    Jump("loc_20B1")

    label("loc_201A")


    ChrTalk(    #92
        0xFE,
        (
            "Anton still hasn't managed to give up on\x01",
            "his love at first sight, apparently.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0xFE,
        (
            "Well, I'll just wait here until he's finished,\x01",
            "I guess. *sigh*\x02",
        )
    )

    CloseMessageWindow()

    label("loc_20B1")

    TalkEnd(0x11)
    Return()

    # Function_18_1EC1 end

    def Function_19_20B5(): pass

    label("Function_19_20B5")

    OP_62(0xF, 0x0, 2000, 0x1C, 0x21, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0xF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_20F5")

    ChrTalk(    #94
        0xF,
        "#034FHnnn, ugnnnnnn...\x02",
    )

    CloseMessageWindow()
    Jump("loc_22C2")

    label("loc_20F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x310, 6)), scpexpr(EXPR_END)), "loc_2160")

    ChrTalk(    #95
        0xF,
        (
            "#034FUh-uhnnnnn...\x02\x03",

            "I... I can't... No, no more...\x02\x03",

            "#034FUnnnn... No more...driiiiink...\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_22C2")

    label("loc_2160")


    ChrTalk(    #96
        0xF,
        (
            "#034FUh-uhnnnnn...\x02\x03",

            "Ah... Scheraaa... Ainaaa...\x02\x03",

            "Unnnn... No more...drinky...\x02",
        )
    )

    CloseMessageWindow()
    OP_9E(0x8, 0xF, 0x0, 0x12C, 0xFA0)

    ChrTalk(    #97
        0xF,
        "#038FNo, nooo! Not a ful' bott'l...\x02",
    )

    CloseMessageWindow()
    OP_9E(0x8, 0xF, 0x0, 0x12C, 0xFA0)

    ChrTalk(    #98
        0xF,
        "#038F*guuuuuuulp*\x02",
    )

    CloseMessageWindow()
    OP_9E(0x8, 0xF, 0x0, 0x12C, 0xFA0)

    ChrTalk(    #99
        0xF,
        "#038F...○△＝`＄□￥～～!!\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #100
        0x101,
        (
            "#1019F(Well, someone's not sleeping the sleep\x01",
            "of the just. No surprise there...)\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_22C2")

    OP_A2(0x1886)
    TalkEnd(0xFF)
    Return()

    # Function_19_20B5 end

    def Function_20_22C9(): pass

    label("Function_20_22C9")

    TalkBegin(0x16)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x74, 0x1, 0x2000)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_29(0x74, 0x0, 0x8)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x74, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_23F3")

    ChrTalk(    #101
        0xFE,
        "Oh, bracers.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0xFE,
        "Look, look. My little Aryll came back as a mom.\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #103
        0x101,
        (
            "#1004FSay what?!\x02\x03",

            "Sh-She came with kids?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #104
        0xFE,
        "Yes, that's right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0xFE,
        "So, I'm thinking of names for them.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0xFE,
        "I wonder what names would be nice...\x02",
    )

    CloseMessageWindow()
    OP_28(0x74, 0x1, 0x2000)
    Jump("loc_27F9")

    label("loc_23F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_END)), "loc_2580")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x74, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_251D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_246E")

    ChrTalk(    #107
        0xFE,
        (
            "The fog doesn't seem like\x01",
            "it's letting up at all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0xFE,
        "Even this old lady's a bit worried.\x02",
    )

    CloseMessageWindow()
    Jump("loc_251A")

    label("loc_246E")


    ChrTalk(    #109
        0xFE,
        "Hello there!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0xFE,
        "It must be hard working on a day like this.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0xFE,
        (
            "The fog doesn't seem like\x01",
            "it's letting up at all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0xFE,
        "Really, what's going to happen to Rolent?\x02",
    )

    CloseMessageWindow()
    OP_A2(0x9)

    label("loc_251A")

    Jump("loc_257D")

    label("loc_251D")


    ChrTalk(    #113
        0xFE,
        (
            "The fog doesn't seem like\x01",
            "it's letting up at all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0xFE,
        "Even this old lady's a bit worried.\x02",
    )

    CloseMessageWindow()

    label("loc_257D")

    Jump("loc_27F9")

    label("loc_2580")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x74, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2746")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_265D")

    ChrTalk(    #115
        0xFE,
        (
            "The weather's awful today, too. That's why\x01",
            "this old lady's relaxing at home. Mm-hmm.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0xFE,
        (
            "I've got to work hard to think\x01",
            "up names for the kittens.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0xFE,
        (
            "This old lady's not\x01",
            "sure where to start. ㈱\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2743")

    label("loc_265D")


    ChrTalk(    #118
        0xFE,
        "Why, hello again.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0xFE,
        "I'd like to you again for your help yesterday.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0xFE,
        (
            "The weather's awful today, too. That's why\x01",
            "this old lady's relaxing at home. Mm-hmm.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0xFE,
        (
            "I've got to work hard to think\x01",
            "up names for the kittens.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x9)

    label("loc_2743")

    Jump("loc_27F9")

    label("loc_2746")


    ChrTalk(    #122
        0xFE,
        (
            "The fog seems like it's just\x01",
            "getting thicker and thicker.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0xFE,
        (
            "I guess I won't be taking a nap\x01",
            "on the terrace today for once.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0xFE,
        "Guess I'll relax at home with the kittens.\x02",
    )

    CloseMessageWindow()

    label("loc_27F9")

    TalkEnd(0x16)
    Return()

    # Function_20_22C9 end

    def Function_21_27FD(): pass

    label("Function_21_27FD")

    TalkBegin(0x17)
    OP_22(0x192, 0x0, 0x64)

    ChrTalk(    #125
        0xFE,
        "Nya～～go.\x02",
    )

    CloseMessageWindow()
    TalkEnd(0x17)
    Return()

    # Function_21_27FD end

    def Function_22_2819(): pass

    label("Function_22_2819")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 6)), scpexpr(EXPR_END)), "loc_28C1")

    ChrTalk(    #126
        0xFE,
        (
            "I thought it seemed lively, but apparently\x01",
            "there was a wedding of all things.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0xFE,
        (
            "Heh. It's a nice thing to hear.\x01",
            "Reminds you how strong people are.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2951")

    label("loc_28C1")


    ChrTalk(    #128
        0xFE,
        (
            "Rolent's very calm, but I wonder\x01",
            "how the other cities are doing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0xFE,
        (
            "It might be best, all things considered,\x01",
            "to stay here for a while...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2951")

    TalkEnd(0xFE)
    Return()

    # Function_22_2819 end

    def Function_23_2955(): pass

    label("Function_23_2955")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 5)), scpexpr(EXPR_END)), "loc_29E8")

    ChrTalk(    #130
        0xFE,
        (
            "I went out to see the city a while ago,\x01",
            "and everyone's way calmer than I'd\x01",
            "expected.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0xFE,
        "Guess the sticks really are laid back.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2B26")

    label("loc_29E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_2A53")

    ChrTalk(    #132
        0xFE,
        (
            "Pestering the airship people isn't\x01",
            "going to change anything...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0xFE,
        "I'm going to wait here.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2B26")

    label("loc_2A53")


    ChrTalk(    #134
        0xFE,
        (
            "Apparently, some people went to see\x01",
            "how things were at the landing port,\x01",
            "but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0xFE,
        "...It's probably a waste.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0xFE,
        (
            "There's no way the ships will be flying with\x01",
            "even the lights in our rooms not working.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_2B26")

    TalkEnd(0xFE)
    Return()

    # Function_23_2955 end

    def Function_24_2B2A(): pass

    label("Function_24_2B2A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 5)), scpexpr(EXPR_END)), "loc_2C61")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_2BB5")

    ChrTalk(    #137
        0xFE,
        "You can't work during an emergency like this.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0xFE,
        (
            "Best I can do is wait for the scheduled\x01",
            "liners to be restored.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C5E")

    label("loc_2BB5")


    ChrTalk(    #139
        0xFE,
        (
            "Apparently, orbments have stopped\x01",
            "working all across the kingdom.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0xFE,
        (
            "There's no way to work at a time like this.\x01",
            "I'll just relax and take it easy for a while.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)

    label("loc_2C5E")

    Jump("loc_2DE6")

    label("loc_2C61")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_2D36")

    ChrTalk(    #141
        0xFE,
        (
            "I feel like I was in this same room when\x01",
            "I got delayed by the fog last time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0xFE,
        (
            "If it can happen twice, I feel like I'm doomed to\x01",
            "get stuck here a third time... Please spare me\x01",
            "that fate, Aidios.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2DE6")

    label("loc_2D36")


    ChrTalk(    #143
        0xFE,
        (
            "I got delayed in Rolent due\x01",
            "to the fog a while back, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0xFE,
        "I feel like I stayed in the same room then.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0xFE,
        (
            "Hmm, crazy coincidence?\x01",
            "Or maybe I'm, like, cursed...\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)

    label("loc_2DE6")

    TalkEnd(0xFE)
    Return()

    # Function_24_2B2A end

    def Function_25_2DEA(): pass

    label("Function_25_2DEA")

    TalkBegin(0x1B)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_3634")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x413, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_358C")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2E34")

    ChrTalk(    #146
        0xFE,
        "Ah, Estelle, Joshua...and Schera.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2E9D")

    label("loc_2E34")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2E6B")

    ChrTalk(    #147
        0xFE,
        "Ah, Estelle, Joshua...and Agate.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2E9D")

    label("loc_2E6B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2E9D")

    ChrTalk(    #148
        0xFE,
        "Ah, Estelle, Joshua...and Zin.\x02",
    )

    CloseMessageWindow()

    label("loc_2E9D")


    ChrTalk(    #149
        0xFE,
        "Umm... Thanks for what you did at the mine.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2FE4")

    ChrTalk(    #150
        0x103,
        (
            "#524FNot at all. You fought really well.\x02\x03",

            "Really. Your estimate has gone up\x01",
            "in my mind.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x103, 400)

    ChrTalk(    #151
        0xFE,
        "Wh...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #152
        0x103,
        (
            "#020FYou bravely remained on site and\x01",
            "protected all the miners...\x02\x03",

            "Your judgment in that difficult situation\x01",
            "was flawless. No room to complain.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3165")

    label("loc_2FE4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3096")

    ChrTalk(    #153
        0x106,
        (
            "#051FDon't worry about it. You fought well.\x02\x03",

            "You made a decision under rough circumstances\x01",
            "and completed your objective.\x02\x03",

            "I think your call was a good one.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3165")

    label("loc_3096")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3165")

    ChrTalk(    #154
        0x108,
        (
            "#070FThink nothing of it. You fought well.\x02\x03",

            "You made a decision in a difficult position\x01",
            "and completed your objective really well.\x02\x03",

            "Even the best bracers would have\x01",
            "made the same decision.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3165")


    ChrTalk(    #155
        0x101,
        (
            "#1015FYeah, definitely...\x02\x03",

            "And you were alone, after all, Ridge.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #156
        0x102,
        (
            "#1040FThat's a far greater feat than anything\x01",
            "we did.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #157
        0xFE,
        "Th-Thanks...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #158
        0xFE,
        "B-But I've still got a long way to go.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_32F7")

    ChrTalk(    #159
        0x103,
        (
            "#025F*sigh* That lack of confidence is your\x01",
            "biggest failing.\x02\x03",

            "#027FYou've got the skills, so hold your head high.\x02\x03",

            "It's thanks to you being here that\x01",
            "I can be away, you know?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x103, 400)
    Jump("loc_34AD")

    label("loc_32F7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_33C1")

    ChrTalk(    #160
        0x106,
        (
            "#551FThat lack of confidence is your biggest problem...\x02\x03",

            "#050FYou've got the skills.\x01",
            "Be proud of what you did.\x02\x03",

            "It's 'cause you're here that Scherazard\x01",
            "can be away, y'know?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x106, 400)
    Jump("loc_34AD")

    label("loc_33C1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_34AD")

    ChrTalk(    #161
        0x108,
        (
            "#070FI think you should refrain from\x01",
            "spineless words like those.\x02\x03",

            "You have the abilities. You should\x01",
            "live with your head high.\x02\x03",

            "It's because you're here that Scherazard\x01",
            "can be away without worrying, after all.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x108, 400)

    label("loc_34AD")


    ChrTalk(    #162
        0xFE,
        "Y-Yes...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #163
        0xFE,
        (
            "I'll do my best and catch up to you\x01",
            "as soon as I can!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_352C")

    ChrTalk(    #164
        0x108,
        "#070FYeah! Now you're talkin'.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3586")

    label("loc_352C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_355A")

    ChrTalk(    #165
        0x106,
        "#051FThat's the spirit.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3586")

    label("loc_355A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3586")

    ChrTalk(    #166
        0x103,
        "#021FHaha. There you go.\x02",
    )

    CloseMessageWindow()

    label("loc_3586")

    OP_A2(0x209F)
    Jump("loc_3634")

    label("loc_358C")


    ChrTalk(    #167
        0xFE,
        (
            "My body still hurts, but...\x01",
            "I feel so satisfied somehow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #168
        0xFE,
        "I'm really...glad I became a bracer.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #169
        0xFE,
        (
            "Looking back over these events\x01",
            "fills me with that feeling.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3634")

    TalkEnd(0x1B)
    Return()

    # Function_25_2DEA end

    def Function_26_3638(): pass

    label("Function_26_3638")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #170
        (
            "\x07\x05Linen Room\x01",
            "※Employees Only\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_26_3638 end

    SaveToFile()

Try(main)
