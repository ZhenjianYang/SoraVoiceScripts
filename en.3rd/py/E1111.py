from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'E1111   ._SN',
        MapName             = 'event',
        Location            = 'E1111.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60170",
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
        'Artifact',                             # 9
        'Man in Black',                         # 10
        'Man in Black',                         # 11
        'Dummy Character',                      # 12
        'Dummy Character',                      # 13
        'Dummy Character',                      # 14
        'Dummy Character',                      # 15
        'Man in Black',                         # 16
        'Man in Black',                         # 17
        'Man in Black',                         # 18
        'Dummy Character',                      # 19
        'Dummy Character',                      # 20
        'Dummy Character',                      # 21
        'Dummy Character',                      # 22
        'Dummy Character',                      # 23
        'Dummy Character',                      # 24
        'Dummy Character',                      # 25
        'Dummy Character',                      # 26
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
        'ED6_DT26/CH20612 ._CH',             # 00
        'ED6_DT27/CH03420 ._CH',             # 01
        'ED6_DT27/CH03460 ._CH',             # 02
        'ED6_DT27/CH04420 ._CH',             # 03
        'ED6_DT27/CH04421 ._CH',             # 04
        'ED6_DT27/CH04422 ._CH',             # 05
        'ED6_DT27/CH04423 ._CH',             # 06
        'ED6_DT27/CH04424 ._CH',             # 07
        'ED6_DT27/CH04460 ._CH',             # 08
        'ED6_DT27/CH04461 ._CH',             # 09
        'ED6_DT27/CH04462 ._CH',             # 0A
        'ED6_DT27/CH04463 ._CH',             # 0B
        'ED6_DT27/CH04464 ._CH',             # 0C
        'ED6_DT26/CH20613 ._CH',             # 0D
        'ED6_DT26/CH20602 ._CH',             # 0E
        'ED6_DT27/CH04080 ._CH',             # 0F
        'ED6_DT27/CH04081 ._CH',             # 10
        'ED6_DT27/CH04082 ._CH',             # 11
        'ED6_DT26/CH20604 ._CH',             # 12
        'ED6_DT26/CH20618 ._CH',             # 13
        'ED6_DT26/CH20685 ._CH',             # 14
        'ED6_DT26/CH20686 ._CH',             # 15
    )

    AddCharChipPat(
        'ED6_DT26/CH20612P._CP',             # 00
        'ED6_DT27/CH03420P._CP',             # 01
        'ED6_DT27/CH03460P._CP',             # 02
        'ED6_DT27/CH04420P._CP',             # 03
        'ED6_DT27/CH04421P._CP',             # 04
        'ED6_DT27/CH04422P._CP',             # 05
        'ED6_DT27/CH04423P._CP',             # 06
        'ED6_DT27/CH04424P._CP',             # 07
        'ED6_DT27/CH04460P._CP',             # 08
        'ED6_DT27/CH04461P._CP',             # 09
        'ED6_DT27/CH04462P._CP',             # 0A
        'ED6_DT27/CH04463P._CP',             # 0B
        'ED6_DT27/CH04464P._CP',             # 0C
        'ED6_DT26/CH20613P._CP',             # 0D
        'ED6_DT26/CH20602P._CP',             # 0E
        'ED6_DT27/CH04080P._CP',             # 0F
        'ED6_DT27/CH04081P._CP',             # 10
        'ED6_DT27/CH04082P._CP',             # 11
        'ED6_DT26/CH20604P._CP',             # 12
        'ED6_DT26/CH20618P._CP',             # 13
        'ED6_DT26/CH20685P._CP',             # 14
        'ED6_DT26/CH20686P._CP',             # 15
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -1320,
        Z                   = 0,
        Y                   = -42890,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 610,
        Z                   = 0,
        Y                   = -42950,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -1640,
        Z                   = 0,
        Y                   = -44330,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x180,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -1310,
        Z                   = 0,
        Y                   = -43190,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x180,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 900,
        Z                   = 0,
        Y                   = -43650,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x180,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 500,
        Z                   = 0,
        Y                   = -43100,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x180,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 1000,
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
        Z                   = 1000,
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
        Z                   = 1000,
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
        X                   = -80,
        Z                   = 0,
        Y                   = 11500,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x180,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 400,
        Z                   = 0,
        Y                   = 11430,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x180,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 1560,
        Z                   = 0,
        Y                   = 9860,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x180,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 1160,
        Z                   = 0,
        Y                   = 9110,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x180,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 30,
        Z                   = 0,
        Y                   = 10480,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x180,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -2330,
        Z                   = 0,
        Y                   = 9400,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x180,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -1610,
        Z                   = 0,
        Y                   = 8880,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x180,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -2140,
        Z                   = 0,
        Y                   = 8950,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x180,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclEvent(
        X                   = -3590,
        Y                   = -1000,
        Z                   = -44000,
        Range               = 3750,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0xFFFF5FD8,
        Unknown_18          = 0x0,
        Unknown_1C          = 3,
    )

    DeclEvent(
        X                   = -3500,
        Y                   = -1000,
        Z                   = -58500,
        Range               = 3500,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0xFFFF15A0,
        Unknown_18          = 0x0,
        Unknown_1C          = 22,
    )


    DeclActor(
        TriggerX            = 4500,
        TriggerZ            = 0,
        TriggerY            = 7500,
        TriggerRange        = 500,
        ActorX              = 4500,
        ActorZ              = 1000,
        ActorY              = 7500,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -8440,
        TriggerZ            = 0,
        TriggerY            = -370,
        TriggerRange        = 800,
        ActorX              = -8440,
        ActorZ              = 500,
        ActorY              = -370,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 8130,
        TriggerZ            = 0,
        TriggerY            = 3690,
        TriggerRange        = 800,
        ActorX              = 8130,
        ActorZ              = 600,
        ActorY              = 3690,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 8,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -6240,
        TriggerZ            = 0,
        TriggerY            = 10130,
        TriggerRange        = 800,
        ActorX              = -6240,
        ActorZ              = 100,
        ActorY              = 10130,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 9,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -5660,
        TriggerZ            = 0,
        TriggerY            = 5830,
        TriggerRange        = 1000,
        ActorX              = -5660,
        ActorZ              = 100,
        ActorY              = 5830,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 10,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -2260,
        TriggerZ            = 0,
        TriggerY            = 14850,
        TriggerRange        = 300,
        ActorX              = -2260,
        ActorZ              = 1700,
        ActorY              = 14850,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 13,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 12670,
        TriggerZ            = 0,
        TriggerY            = -52650,
        TriggerRange        = 500,
        ActorX              = 12670,
        ActorZ              = 1000,
        ActorY              = -52650,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 23,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_4D6",          # 00, 0
        "Function_1_6DF",          # 01, 1
        "Function_2_7EF",          # 02, 2
        "Function_3_96C",          # 03, 3
        "Function_4_E23",          # 04, 4
        "Function_5_FA6",          # 05, 5
        "Function_6_FCD",          # 06, 6
        "Function_7_10D5",         # 07, 7
        "Function_8_11E3",         # 08, 8
        "Function_9_12EF",         # 09, 9
        "Function_10_13E9",        # 0A, 10
        "Function_11_1628",        # 0B, 11
        "Function_12_1792",        # 0C, 12
        "Function_13_1A83",        # 0D, 13
        "Function_14_1D2A",        # 0E, 14
        "Function_15_1D7F",        # 0F, 15
        "Function_16_1E9C",        # 10, 16
        "Function_17_2366",        # 11, 17
        "Function_18_3665",        # 12, 18
        "Function_19_3721",        # 13, 19
        "Function_20_37B3",        # 14, 20
        "Function_21_3D45",        # 15, 21
        "Function_22_3D82",        # 16, 22
        "Function_23_3EAC",        # 17, 23
    )


    def Function_0_4D6(): pass

    label("Function_0_4D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 5)), scpexpr(EXPR_END)), "loc_4E4")
    OP_A3(0x2505)
    Event(0, 16)

    label("loc_4E4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_500")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4BC, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4BC, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_500")
    Event(0, 4)

    label("loc_500")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4BC, 5)), scpexpr(EXPR_END)), "loc_626")
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x17, 0x1)
    ClearChrFlags(0x18, 0x1)
    ClearChrFlags(0x19, 0x1)
    SetChrFlags(0x17, 0x800)
    SetChrFlags(0x18, 0x800)
    SetChrFlags(0x19, 0x800)
    SetChrPos(0x17, -180, 0, 10800, 0)
    SetChrPos(0x18, 1450, 0, 9630, 45)
    SetChrPos(0x19, -1680, 0, 9180, 315)
    OP_51(0x17, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x18, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x19, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x17, 13)
    SetChrSubChip(0x17, 0)
    SetChrChipByIndex(0x18, 19)
    SetChrSubChip(0x18, 0)
    SetChrChipByIndex(0x19, 19)
    SetChrSubChip(0x19, 0)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1F, 0x80)
    OP_9F(0x1A, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x1C, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x1F, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x20, 0x80)
    OP_9F(0x1B, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x1D, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x20, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x21, 0x80)
    OP_9F(0x1E, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x21, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    label("loc_626")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4BC, 2)), scpexpr(EXPR_END)), "loc_6D0")
    OP_51(0x11, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x11, 13)
    SetChrSubChip(0x11, 0)
    ClearChrFlags(0x11, 0x1)
    SetChrFlags(0x11, 0x800)
    SetChrPos(0x11, -1700, 0, -43900, 180)
    ClearChrFlags(0x13, 0x80)
    OP_9F(0x13, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x14, 0x80)
    OP_9F(0x14, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_51(0x12, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x12, 19)
    SetChrSubChip(0x12, 0)
    ClearChrFlags(0x12, 0x1)
    SetChrFlags(0x12, 0x800)
    SetChrPos(0x12, 900, 0, -43000, 180)
    ClearChrFlags(0x15, 0x80)
    OP_9F(0x15, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x16, 0x80)
    OP_9F(0x16, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    Jump("loc_6DE")

    label("loc_6D0")

    OP_43(0x11, 0x0, 0x0, 0x2)
    OP_43(0x12, 0x0, 0x0, 0x2)

    label("loc_6DE")

    Return()

    # Function_0_4D6 end

    def Function_1_6DF(): pass

    label("Function_1_6DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4BD, 6)), scpexpr(EXPR_END)), "loc_6EA")
    OP_64(0x0, 0x1)

    label("loc_6EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4BD, 7)), scpexpr(EXPR_END)), "loc_6F5")
    OP_64(0x1, 0x1)

    label("loc_6F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4BE, 0)), scpexpr(EXPR_END)), "loc_700")
    OP_64(0x2, 0x1)

    label("loc_700")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4BE, 1)), scpexpr(EXPR_END)), "loc_70B")
    OP_64(0x3, 0x1)

    label("loc_70B")

    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_71B")
    OP_64(0x4, 0x1)

    label("loc_71B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4BE, 2)), scpexpr(EXPR_END)), "loc_726")
    OP_64(0x4, 0x1)

    label("loc_726")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4BC, 5)), scpexpr(EXPR_END)), "loc_734")
    OP_64(0x5, 0x1)
    Jump("loc_755")

    label("loc_734")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4BC, 4)), scpexpr(EXPR_END)), "loc_751")
    OP_72(0x2001, 0x0)
    ExitThread()
    OP_72(0x801, 0x0)
    ExitThread()
    OP_6F(0x1, 60)
    Jump("loc_755")

    label("loc_751")

    OP_64(0x5, 0x1)

    label("loc_755")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4BC, 4)), scpexpr(EXPR_END)), "loc_778")
    OP_72(0x800, 0x0)
    ExitThread()
    OP_72(0x1000, 0x0)
    ExitThread()
    OP_71(0x8000, 0x0)
    ExitThread()
    OP_6F(0x0, 300)
    Jump("loc_791")

    label("loc_778")

    OP_72(0x800, 0x0)
    ExitThread()
    OP_72(0x1000, 0x0)
    ExitThread()
    OP_71(0x8000, 0x0)
    ExitThread()
    OP_6F(0x0, 0)

    label("loc_791")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4BC, 5)), scpexpr(EXPR_END)), "loc_7C0")
    OP_72(0x406, 0x0)
    ExitThread()
    OP_6F(0x6, 120)
    OP_72(0x806, 0x0)
    ExitThread()
    OP_71(0x404, 0x0)
    ExitThread()
    OP_72(0x407, 0x0)
    ExitThread()
    OP_71(0x404, 0x0)
    ExitThread()
    Jump("loc_7D9")

    label("loc_7C0")

    OP_71(0x406, 0x0)
    ExitThread()
    OP_71(0x407, 0x0)
    ExitThread()
    OP_72(0x1004, 0x0)
    ExitThread()
    OP_6F(0x4, 0)

    label("loc_7D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4BC, 5)), scpexpr(EXPR_END)), "loc_7EE")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0xAB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x2000000)

    label("loc_7EE")

    Return()

    # Function_1_6DF end

    def Function_2_7EF(): pass

    label("Function_2_7EF")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_814")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_956")

    label("loc_814")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_82D")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_956")

    label("loc_82D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_846")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_956")

    label("loc_846")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_85F")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_956")

    label("loc_85F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_878")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_956")

    label("loc_878")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_891")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_956")

    label("loc_891")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8AA")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_956")

    label("loc_8AA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8C3")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_956")

    label("loc_8C3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8DC")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_956")

    label("loc_8DC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8F5")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_956")

    label("loc_8F5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_90E")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_956")

    label("loc_90E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_927")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_956")

    label("loc_927")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_940")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_956")

    label("loc_940")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_956")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_956")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_96B")
    OP_99(0xFE, 0x0, 0x7, 0x640)
    Jump("loc_956")

    label("loc_96B")

    Return()

    # Function_2_7EF end

    def Function_3_96C(): pass

    label("Function_3_96C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4BC, 2)), scpexpr(EXPR_END)), "loc_974")
    Return()

    label("loc_974")

    EventBegin(0x0)
    Fade(500)
    OP_6D(660, 0, -42760, 0)
    OP_67(0, 5170, -10000, 0)
    OP_6B(3020, 0)
    OP_6C(45000, 0)
    OP_6E(250, 0)
    SetChrPos(0x109, -340, 0, -45080, 0)
    OP_44(0x11, 0xFF)
    OP_44(0x12, 0xFF)
    SetChrSubChip(0x11, 0)
    SetChrSubChip(0x12, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(    #0
        0x11,
        (
            "#5P...Stop right there.\x02\x03",

            "This staircase leads to Sir Conrad's private room.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x12,
        "#5PI'm afraid I am going to have to ask you to leave.\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #2
        0x109,
        "Masked Man",
        (
            "#1603F#6PI figured you'd say something like that.\x02\x03",

            "#1601FSorry, though. This isn't gonna be your\x01",
            "lucky day.\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)

    def lambda_AF4():
        OP_6B(2860, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_AF4)
    SetChrChipByIndex(0x109, 14)
    SetChrSubChip(0x109, 0)
    Sleep(500)
    OP_22(0xD8, 0x0, 0x64)
    SetChrSubChip(0x109, 1)
    Sleep(300)
    OP_62(0x11, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(100)
    OP_62(0x12, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #3
        0x11,
        "#5PWha...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x12,
        "#5PWh-What are you doing?!\x02",
    )

    CloseMessageWindow()
    LoadEffect(0x0, "scraft\\\\sc008_02.eff")
    PlayEffect(0x0, 0xFF, 0xFF, -250, 1100, -44450, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_23(0xC9)
    OP_82(0x0, 0x2)
    Sleep(500)

    def lambda_BE1():
        OP_9E(0x11, 0x14, 0x0, 0x7D0, 0xBB8)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_BE1)
    Sleep(100)

    def lambda_C00():
        OP_9E(0x12, 0x14, 0x0, 0x7D0, 0xBB8)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_C00)

    ChrTalk(    #5 op#A op#5
        0x11,
        "#5P#10AGah!\x05\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #6 op#A op#5
        0x12,
        "#5P#10AUgh!\x05\x02",
    )

    CloseMessageWindow()
    OP_9E(0x11, 0x14, 0x0, 0x12C, 0xBB8)
    OP_22(0x20C, 0x0, 0x64)
    OP_51(0x11, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x11, 13)
    SetChrSubChip(0x11, 0)
    ClearChrFlags(0x11, 0x1)
    SetChrFlags(0x11, 0x800)
    SetChrPos(0x11, -1700, 0, -43900, 180)
    Sleep(200)
    OP_9E(0x12, 0x14, 0x0, 0x12C, 0xBB8)
    OP_22(0x20C, 0x0, 0x64)
    OP_51(0x12, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x12, 19)
    SetChrSubChip(0x12, 0)
    ClearChrFlags(0x12, 0x1)
    SetChrFlags(0x12, 0x800)
    SetChrPos(0x12, 900, 0, -43000, 180)
    ClearChrFlags(0x13, 0x80)
    OP_9F(0x13, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x14, 0x80)
    OP_9F(0x14, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x15, 0x80)
    OP_9F(0x15, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x16, 0x80)
    OP_9F(0x16, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    Sleep(500)

    def lambda_D18():
        OP_6D(660, 0, -43760, 1500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_D18)
    SetChrSubChip(0x109, 0)
    Sleep(200)
    Fade(250)
    SetChrChipByIndex(0x109, 65535)
    SetChrSubChip(0x109, 0)
    OP_0D()
    Sleep(500)
    WaitChrThread(0x109, 0x0)
    Sleep(500)

    NpcTalk(    #7
        0x109,
        "Masked Man",
        (
            "#1600F#6PLooks like I'm dealing with a bunch of jaeger\x01",
            "dropouts.\x02\x03",

            "They don't seem that well trained, either.\x01",
            "This'll be cake.\x02\x03",

            "#1601FHeh. I sure wish every job I had was this easy.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_A2(0x25E2)
    EventEnd(0x0)
    Return()

    # Function_3_96C end

    def Function_4_E23(): pass

    label("Function_4_E23")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_6D(990, 450, 13390, 0)
    OP_67(0, 7520, -10000, 0)
    OP_6B(2570, 0)
    OP_6C(45000, 0)
    OP_6E(342, 0)
    SetChrPos(0x109, -190, 0, -2290, 0)
    OP_9F(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_E8E():
        OP_6D(660, 50, 2040, 6000)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_E8E)

    def lambda_EA6():
        OP_67(0, 6820, -10000, 6000)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_EA6)

    def lambda_EBE():
        OP_6B(2390, 6000)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_EBE)

    def lambda_ECE():
        OP_6E(314, 6000)
        ExitThread()

    QueueWorkItem(0x11, 3, lambda_ECE)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(2500)
    OP_22(0x6, 0x0, 0x64)
    Sleep(500)
    OP_43(0x109, 0x0, 0x0, 0x5)
    WaitChrThread(0x109, 0x0)
    Sleep(300)
    OP_8C(0x109, 270, 400)
    Sleep(500)
    OP_8C(0x109, 0, 600)
    OP_8C(0x109, 90, 600)
    Sleep(500)
    OP_8C(0x109, 0, 400)
    Sleep(500)

    NpcTalk(    #8
        0x109,
        "Masked Man",
        (
            "#1600F#5PWow. Talk about pointlessly fancy.\x02\x03",

            "All right... Now, where's he hidden it?\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_CE(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A2(0x25E3)
    EventEnd(0x0)
    Return()

    # Function_4_E23 end

    def Function_5_FA6(): pass

    label("Function_5_FA6")


    def lambda_FAC():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_FAC)
    OP_8E(0xFE, 0xFFFFFF42, 0x0, 0x352, 0x7D0, 0x0)
    Return()

    # Function_5_FA6 end

    def Function_6_FCD(): pass

    label("Function_6_FCD")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #9
        "\x07\x05There's a switch of some sort behind the desk.\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(    #10
        "\x07\x05Press the switch?\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1045")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10D1")

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Yes\x01",      # 0
            "No\x01",       # 1
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Sleep(300)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1089"),
        (1, "loc_10B4"),
        (SWITCH_DEFAULT, "loc_10C1"),
    )


    label("loc_1089")

    OP_22(0x64, 0x0, 0x64)
    Sleep(1000)
    OP_CE(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_64(0x0, 0x1)
    OP_A2(0x25EE)
    Call(0, 11)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_10CE")

    label("loc_10B4")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_10CE")

    label("loc_10C1")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_10CE")

    label("loc_10CE")

    Jump("loc_1045")

    label("loc_10D1")

    TalkEnd(0xFF)
    Return()

    # Function_6_FCD end

    def Function_7_10D5(): pass

    label("Function_7_10D5")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #11
        "\x07\x05There's a suspicious switch inside the potted plant.\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(    #12
        "\x07\x05Press the switch?\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1153")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_11DF")

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Yes\x01",      # 0
            "No\x01",       # 1
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Sleep(300)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1197"),
        (1, "loc_11C2"),
        (SWITCH_DEFAULT, "loc_11CF"),
    )


    label("loc_1197")

    OP_22(0x64, 0x0, 0x64)
    Sleep(1000)
    OP_CE(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_64(0x1, 0x1)
    OP_A2(0x25EF)
    Call(0, 11)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_11DC")

    label("loc_11C2")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_11DC")

    label("loc_11CF")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_11DC")

    label("loc_11DC")

    Jump("loc_1153")

    label("loc_11DF")

    TalkEnd(0xFF)
    Return()

    # Function_7_10D5 end

    def Function_8_11E3(): pass

    label("Function_8_11E3")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #13
        "\x07\x05There's a switch of some sort underneath the vase.\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(    #14
        "\x07\x05Press the switch?\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_125F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_12EB")

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Yes\x01",      # 0
            "No\x01",       # 1
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Sleep(300)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_12A3"),
        (1, "loc_12CE"),
        (SWITCH_DEFAULT, "loc_12DB"),
    )


    label("loc_12A3")

    OP_22(0x64, 0x0, 0x64)
    Sleep(1000)
    OP_CE(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_64(0x2, 0x1)
    OP_A2(0x25F0)
    Call(0, 11)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_12E8")

    label("loc_12CE")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_12E8")

    label("loc_12DB")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_12E8")

    label("loc_12E8")

    Jump("loc_125F")

    label("loc_12EB")

    TalkEnd(0xFF)
    Return()

    # Function_8_11E3 end

    def Function_9_12EF(): pass

    label("Function_9_12EF")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #15
        "\x07\x05This corner of the rug is oddly worn.\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(    #16
        "\x07\x05Stand on it?\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1359")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_13E5")

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Yes\x01",      # 0
            "No\x01",       # 1
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Sleep(300)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_139D"),
        (1, "loc_13C8"),
        (SWITCH_DEFAULT, "loc_13D5"),
    )


    label("loc_139D")

    OP_22(0x64, 0x0, 0x64)
    Sleep(1000)
    OP_CE(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_64(0x3, 0x1)
    OP_A2(0x25F1)
    Call(0, 11)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_13E2")

    label("loc_13C8")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_13E2")

    label("loc_13D5")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_13E2")

    label("loc_13E2")

    Jump("loc_1359")

    label("loc_13E5")

    TalkEnd(0xFF)
    Return()

    # Function_9_12EF end

    def Function_10_13E9(): pass

    label("Function_10_13E9")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #17
        "\x07\x05There's a switch in the armrest of the sofa.\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(    #18
        "\x07\x05Press the switch?\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_145F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1624")

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Yes\x01",      # 0
            "No\x01",       # 1
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Sleep(300)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_14A3"),
        (1, "loc_1607"),
        (SWITCH_DEFAULT, "loc_1614"),
    )


    label("loc_14A3")

    OP_22(0x64, 0x0, 0x64)
    Sleep(1000)
    OP_CE(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_65(0x0, 0x1)
    OP_65(0x1, 0x1)
    OP_65(0x2, 0x1)
    OP_65(0x3, 0x1)
    OP_64(0x4, 0x1)
    OP_A3(0x25EE)
    OP_A3(0x25EF)
    OP_A3(0x25F0)
    OP_A3(0x25F1)
    OP_22(0x64, 0x0, 0x64)
    Sleep(500)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #19
        "\x07\x05All of the switches were reset!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Sleep(300)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15AD")
    OP_A2(0x1)

    NpcTalk(    #20
        0x109,
        "Masked Man",
        (
            "#1602FThat one must've been a fake.\x02\x03",

            "Bah... I should've known they wouldn't make\x01",
            "it simple.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15FA")

    label("loc_15AD")


    NpcTalk(    #21
        0x109,
        "Masked Man",
        (
            "#1602FBah... I should've known they wouldn't make\x01",
            "it simple.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15FA")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1621")

    label("loc_1607")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1621")

    label("loc_1614")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1621")

    label("loc_1621")

    Jump("loc_145F")

    label("loc_1624")

    TalkEnd(0xFF)
    Return()

    # Function_10_13E9 end

    def Function_11_1628(): pass

    label("Function_11_1628")

    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_16F3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16A1")
    OP_A2(0x0)

    NpcTalk(    #22
        0x109,
        "Masked Man",
        (
            "#1600FWell, would you look at that?\x02\x03",

            "Who wants to bet that's not the only one?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_16EC")

    label("loc_16A1")


    NpcTalk(    #23
        0x109,
        "Masked Man",
        (
            "#1600FThat's probably not the only switch I need\x01",
            "to press.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16EC")

    OP_65(0x4, 0x1)
    Jump("loc_1791")

    label("loc_16F3")

    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1736")

    NpcTalk(    #24
        0x109,
        "Masked Man",
        "#1600FNow, where's the next one...?\x02",
    )

    CloseMessageWindow()
    Jump("loc_1791")

    label("loc_1736")

    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_177A")

    NpcTalk(    #25
        0x109,
        "Masked Man",
        "#1600FI doubt that's the last one...\x02",
    )

    CloseMessageWindow()
    Jump("loc_1791")

    label("loc_177A")

    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1791")
    OP_64(0x4, 0x1)
    OP_A2(0x25F2)
    Call(0, 12)

    label("loc_1791")

    Return()

    # Function_11_1628 end

    def Function_12_1792(): pass

    label("Function_12_1792")

    EventBegin(0x0)
    OP_22(0xBB, 0x0, 0x64)
    Sleep(500)
    OP_6F(0x0, 0)
    OP_70(0x0, 0x12C)
    Fade(500)

    def lambda_17B7():
        OP_6D(1280, 300, 16390, 0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_17B7)

    def lambda_17CF():
        OP_67(0, 5960, -10000, 0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_17CF)

    def lambda_17E7():
        OP_6B(2950, 0)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_17E7)

    def lambda_17F7():
        OP_6E(262, 0)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_17F7)
    WaitChrThread(0x109, 0x0)

    def lambda_180C():
        OP_6B(2850, 2000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_180C)
    WaitChrThread(0x109, 0x2)
    OP_73(0x0)
    OP_7C(0x1E, 0x1E, 0xBB8, 0x64)
    OP_22(0x12E, 0x0, 0x64)
    OP_23(0xBB)
    Sleep(300)
    OP_A2(0x25E4)
    Sleep(1000)

    def lambda_184A():
        OP_6D(1100, 0, 15350, 2000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_184A)
    SetChrPos(0x109, -330, 0, 5770, 0)

    def lambda_1873():
        OP_8E(0xFE, 0xFFFFFF7E, 0x0, 0x314C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1873)
    WaitChrThread(0x109, 0x0)
    WaitChrThread(0x109, 0x1)

    NpcTalk(    #26
        0x109,
        "Masked Man",
        (
            "#1600FHaha... And here we go.\x02\x03",

            "Everything so far's been completely in line with\x01",
            "what I expected, which means that...\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x109, 45, 400)
    Sleep(500)
    OP_8C(0x109, 315, 400)
    Sleep(500)

    def lambda_1935():
        OP_6D(-200, 0, 15800, 2000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1935)

    def lambda_194D():
        OP_8E(0xFE, 0xFFFFF736, 0x0, 0x37D2, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_194D)
    WaitChrThread(0x109, 0x0)
    OP_8C(0x109, 0, 400)
    WaitChrThread(0x109, 0x1)
    Sleep(500)
    OP_62(0x109, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x109)
    Sleep(300)
    OP_22(0x64, 0x0, 0x64)
    Sleep(500)
    OP_22(0xC0, 0x0, 0x64)
    OP_6F(0x1, 0)
    OP_70(0x1, 0x3C)
    OP_73(0x1)
    Sleep(500)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #27
        (
            "\x07\x05There's a panel with buttons that have letters written\x01",
            "on them.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #28
        "\x07\x05A password of some kind apparently must be entered.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(300)

    NpcTalk(    #29
        0x109,
        "Masked Man",
        "#1602F#6PHmm... I wonder...\x02",
    )

    CloseMessageWindow()
    Call(0, 13)
    EventEnd(0x0)
    OP_65(0x5, 0x1)
    Return()

    # Function_12_1792 end

    def Function_13_1A83(): pass

    label("Function_13_1A83")

    TalkBegin(0xFF)
    OP_8C(0x109, 0, 0)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 100, -1, -1)
    SetChrName("")

    AnonymousTalk(    #30
        "\x07\x05The Password Is...\x18\x02",
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1ACD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1D26")

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "[ORFEUS]\x01",       # 0
            "[ORPHEUS]\x01",      # 1
            "[OLPHEUS]\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_56(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToBright(300, 0)
    Sleep(300)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1B34"),
        (1, "loc_1B90"),
        (2, "loc_1CC7"),
        (SWITCH_DEFAULT, "loc_1D23"),
    )


    label("loc_1B34")

    OP_22(0x9C, 0x0, 0x64)
    Sleep(1000)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #31
        "\x07\x05Nothing happened.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Sleep(300)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1D23")

    label("loc_1B90")

    OP_22(0x9C, 0x0, 0x64)
    Sleep(1000)
    EventBegin(0x0)
    OP_6F(0x4, 0)
    OP_70(0x4, 0xF)
    OP_73(0x4)

    def lambda_1BB3():
        OP_6D(660, 550, 15930, 1500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1BB3)

    def lambda_1BCB():
        OP_67(0, 5480, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_1BCB)

    def lambda_1BE3():
        OP_6B(3000, 1500)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_1BE3)

    def lambda_1BF3():
        OP_8C(0x109, 90, 400)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1BF3)
    WaitChrThread(0x109, 0x0)
    WaitChrThread(0x109, 0x1)
    Sleep(500)

    NpcTalk(    #32
        0x109,
        "Masked Man",
        (
            "#1602F#6PI figured as much.\x02\x03",

            "Looks like my target this time is one of the toys\x01",
            "our friends decided to spread around for fun.\x02",
        )
    )

    CloseMessageWindow()
    OP_43(0x109, 0x0, 0x0, 0xE)
    Sleep(3000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x2505)
    NewScene("ED6_DT21/E1111   ._SN", 100, 0, 0)
    IdleLoop()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1D23")

    label("loc_1CC7")

    OP_22(0x9C, 0x0, 0x64)
    Sleep(1000)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #33
        "\x07\x05Nothing happened.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Sleep(300)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1D23")

    label("loc_1D23")

    Jump("loc_1ACD")

    label("loc_1D26")

    TalkEnd(0xFF)
    Return()

    # Function_13_1A83 end

    def Function_14_1D2A(): pass

    label("Function_14_1D2A")

    OP_20(0xBB8)

    def lambda_1D35():
        OP_6B(2800, 5500)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_1D35)
    OP_8C(0x109, 90, 400)
    OP_8E(0xFE, 0xFFFFFF4C, 0x0, 0x3854, 0x7D0, 0x0)
    OP_8C(0x109, 0, 400)
    OP_8E(0xFE, 0xFFFFFF9C, 0x0, 0x406A, 0x7D0, 0x0)
    Sleep(2000)
    OP_44(0x109, 0x3)
    Return()

    # Function_14_1D2A end

    def Function_15_1D7F(): pass

    label("Function_15_1D7F")

    EventBegin(0x0)
    OP_6F(0x4, 0)
    OP_70(0x4, 0xF)
    OP_73(0x4)

    def lambda_1D98():
        OP_6D(660, 550, 15930, 1500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1D98)

    def lambda_1DB0():
        OP_67(0, 5480, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_1DB0)

    def lambda_1DC8():
        OP_6B(3000, 1500)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_1DC8)

    def lambda_1DD8():
        OP_8C(0x109, 90, 400)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1DD8)
    WaitChrThread(0x109, 0x0)
    WaitChrThread(0x109, 0x1)

    NpcTalk(    #34
        0x109,
        "Masked Man",
        (
            "#1602F#6PI figured as much.\x02\x03",

            "Looks like my target this time is one of the toys\x01",
            "our friends decided to spread about for fun.\x02",
        )
    )

    CloseMessageWindow()
    OP_43(0x109, 0x0, 0x0, 0xE)
    Sleep(3000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x2505)
    NewScene("ED6_DT21/E1111   ._SN", 100, 0, 0)
    IdleLoop()
    EventEnd(0x0)
    Return()

    # Function_15_1D7F end

    def Function_16_1E9C(): pass

    label("Function_16_1E9C")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadEffect(0x0, "map\\mp259_01.eff")
    LoadEffect(0x1, "map\\mp074_00.eff")
    SetChrPos(0x109, 39760, 0, -2500, 0)
    OP_9F(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrFlags(0x10, 0x800)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x800)
    SetChrPos(0x10, 39900, 800, 4850, 0)
    PlayEffect(0x0, 0x0, 0x10, 0, 100, 0, 0, 0, 0, 800, 650, 900, 0xFF, 0, 0, 0, 0)
    OP_51(0x10, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x2BC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x2BC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x2BC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x2BC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x29, (scpexpr(EXPR_PUSH_LONG, 0x2BC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_1D(0xB7)
    Sleep(1000)
    OP_6D(44520, 2050, 4400, 0)
    OP_67(0, 4210, -10000, 0)
    OP_6B(2880, 0)
    OP_6C(51000, 0)
    OP_6E(315, 0)
    FadeToBright(2000, 0)

    def lambda_1FC9():
        OP_6D(41170, 2050, 7350, 6000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1FC9)

    def lambda_1FE1():
        OP_67(0, 4210, -10000, 6000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1FE1)

    def lambda_1FF9():
        OP_6B(2880, 6000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_1FF9)

    def lambda_2009():
        OP_6C(42000, 6000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_2009)

    def lambda_2019():
        OP_6E(315, 6000)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_2019)
    WaitChrThread(0xEE, 0x0)
    Sleep(1000)

    def lambda_2033():
        OP_6D(41290, 20, 5660, 3500)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_2033)

    def lambda_204B():
        OP_67(0, 4520, -10000, 3500)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_204B)

    def lambda_2063():
        OP_6B(3000, 3500)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_2063)

    def lambda_2073():
        OP_6E(303, 3500)
        ExitThread()

    QueueWorkItem(0x11, 3, lambda_2073)
    Sleep(2500)

    def lambda_2088():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x258)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_2088)

    def lambda_209A():
        OP_8F(0xFE, 0x9C2C, 0x0, 0xFFFFFEB6, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_209A)
    WaitChrThread(0x11, 0x0)
    WaitChrThread(0x109, 0x0)
    WaitChrThread(0x109, 0x1)
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_20E0():
        OP_6B(2730, 3000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_20E0)

    def lambda_20F0():
        OP_6E(280, 3000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_20F0)
    OP_8E(0x109, 0x9AF6, 0x14, 0xD0C, 0x3E8, 0x0)
    Sleep(300)
    OP_62(0x109, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x109)
    Sleep(500)
    WaitChrThread(0x109, 0x2)

    NpcTalk(    #35
        0x109,
        "Masked Man",
        (
            "#1602F#6PThe Fool's Locket, huh?\x02\x03",

            "A forbidden artifact that lets the bearer pass all\x01",
            "but the most obvious lies off as complete truth.\x02\x03",

            "*sigh* Really not the kind of thing a shady weapons\x01",
            "dealer should have in his possession.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(500)
    OP_22(0x8F, 0x0, 0x64)
    OP_9F(0x10, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrFlags(0x10, 0x80)
    OP_82(0x0, 0x0)
    OP_0D()
    Sleep(300)
    OP_20(0x3E8)
    OP_22(0xAC, 0x0, 0x64)
    Sleep(500)
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_1D(0xAB)
    Fade(500)
    OP_6D(41060, 0, -40020, 0)
    OP_67(0, 4310, -10000, 0)
    OP_6B(2550, 0)
    OP_6C(147000, 0)
    OP_6E(334, 0)
    SetChrPos(0x109, 39830, 20, -36180, 0)
    OP_0D()
    Sleep(300)
    OP_72(0x1005, 0x0)
    ExitThread()
    OP_6F(0x5, 15)
    OP_70(0x5, 0x0)
    OP_73(0x5)
    OP_23(0xBB)
    OP_7C(0x32, 0x32, 0xBB8, 0x64)
    OP_22(0x88, 0x0, 0x64)
    Sleep(500)
    OP_22(0x9C, 0x0, 0x64)
    OP_22(0x73, 0x0, 0x64)
    Sleep(500)
    OP_8C(0x109, 180, 600)
    Sleep(500)

    NpcTalk(    #36
        0x109,
        "Masked Man",
        "#1600F#6PHeh...\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(1000)
    Call(0, 17)
    Call(0, 20)
    EventEnd(0x0)
    Return()

    # Function_16_1E9C end

    def Function_17_2366(): pass

    label("Function_17_2366")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    SetChrPos(0x17, 40, 0, 950, 0)
    SetChrPos(0x18, 660, 0, 60, 0)
    SetChrPos(0x19, -990, 0, -570, 0)
    OP_BB(0x8, 0x1, 0x8)
    OP_BD()
    OP_C2(0x1, 0x0)
    OP_9F(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x109, 1000, 0, 18000, 180)
    SetChrFlags(0x109, 0x4)
    OP_72(0x406, 0x0)
    ExitThread()
    OP_71(0x404, 0x0)
    ExitThread()
    LoadEffect(0x0, "map\\mp279_00.eff")
    OP_6D(1270, 0, 14000, 0)
    OP_67(0, 4260, -10000, 0)
    OP_6B(2920, 0)
    OP_6C(45000, 0)
    OP_6E(288, 0)
    FadeToBright(1000, 0)
    OP_0D()
    SetChrChipByIndex(0x17, 20)

    def lambda_2451():
        OP_8E(0xFE, 0xFFFFFF6A, 0x0, 0x3200, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_2451)
    Sleep(100)
    SetChrChipByIndex(0x18, 21)

    def lambda_2476():
        OP_8E(0xFE, 0x23A, 0x0, 0x2C88, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_2476)
    Sleep(150)
    SetChrChipByIndex(0x19, 21)

    def lambda_249B():
        OP_8E(0xFE, 0xFFFFFB8C, 0x0, 0x2AEE, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_249B)
    WaitChrThread(0x17, 0x1)
    SetChrChipByIndex(0x17, 1)
    SetChrSubChip(0x17, 0)
    WaitChrThread(0x18, 0x1)
    SetChrChipByIndex(0x18, 2)
    SetChrSubChip(0x18, 0)
    WaitChrThread(0x19, 0x1)
    SetChrChipByIndex(0x19, 2)
    SetChrSubChip(0x19, 0)
    Sleep(150)

    ChrTalk(    #37
        0x19,
        (
            "#6PUgh... What's going on here?!\x02\x03",

            "What happened to the two who were\x01",
            "on guard here?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x18,
        (
            "#4PThey were both fast asleep.\x02\x03",

            "Seemed like whoever did it used a dart\x01",
            "or spray of some kind.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x17,
        (
            "#5PHmph. You think we're dealing with someone\x01",
            "in the same business as us?\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x17, 180, 400)

    ChrTalk(    #40
        0x17,
        (
            "#5PWe'd better keep him locked inside here until\x01",
            "the party's over.\x02\x03",

            "We can give our report to Master Conrad after.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x18,
        (
            "#4PWhat do you think the odds are that he's\x01",
            "not acting alone?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x17,
        (
            "#5PJudging by the security camera footage,\x01",
            "I don't think it's that high.\x02\x03",

            "That said, there's a definite chance he's\x01",
            "got some form of backup that just hasn't\x01",
            "acted yet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x19,
        (
            "#6PI'd say we're better off marking all invited\x01",
            "guests for the time being. We wouldn't want\x01",
            "to let anyone slip through our sights.\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("Man's Voice")

    AnonymousTalk(    #44
        "\x07\x05Hahaha...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_62(0x17, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(100)
    OP_62(0x18, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(100)
    OP_62(0x19, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_286E():
        OP_6D(1400, 0, 15000, 1000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_286E)
    OP_8C(0x17, 0, 600)
    WaitChrThread(0x109, 0x0)

    ChrTalk(    #45
        0x18,
        "#4PDid he just laugh at us...?\x02",
    )

    CloseMessageWindow()
    OP_8E(0x17, 0xFFFFFF9C, 0x0, 0x3778, 0x7D0, 0x0)
    Sleep(300)
    OP_8F(0x17, 0xFFFFFF9C, 0x0, 0x3AD4, 0x1388, 0x0)
    OP_22(0x228, 0x0, 0x64)
    OP_22(0x9A, 0x0, 0x64)
    OP_8F(0x17, 0xFFFFFF9C, 0x0, 0x3778, 0x1388, 0x0)

    ChrTalk(    #46
        0x17,
        "#6PSomething funny?!\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("Man's Voice")

    AnonymousTalk(    #47
        (
            "\x07\x05Oh, no... I just thought I should probably\x01",
            "apologize for underestimating you.\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("Man's Voice")

    AnonymousTalk(    #48
        (
            "\x07\x05I'd written you all off as untrained jaeger \x01",
            "dropouts, but maybe you've got more going\x01",
            "for you than I was giving you credit for.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)

    ChrTalk(    #49
        0x18,
        "#4PYou little...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x19,
        (
            "#6PHmph. You've got guts. I'll give you that.\x02\x03",

            "I've got no idea how you came to be here,\x01",
            "but you should know that Master Conrad\x01",
            "is not a merciful man.\x02\x03",

            "Don't think you're going to get out of this\x01",
            "in one piece.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x17,
        (
            "#6PHeheh...\x02\x03",

            "You're in for such a world of pain, you'll wish\x01",
            "you'd killed yourself while you had the chance.\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("Man's Voice")

    AnonymousTalk(    #52
        (
            "\x07\x05Haha... Well, doesn't that sound like a fun time?\x02\x03",

            "Sadly for you, I've already got my next date lined\x01",
            "up, so I won't be able to take you up on that.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    PlayEffect(0x0, 0x0, 0xFF, 0, 2000, 17000, 0, 270, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x392, 0x0, 0x64)
    Sleep(100)
    OP_22(0x1FE, 0x0, 0x64)

    def lambda_2C89():
        OP_7C(0x0, 0xCE4, 0xBB8, 0x64)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_2C89)
    OP_6F(0x6, 1)
    OP_70(0x6, 0x15)
    Sleep(300)
    OP_82(0x0, 0x2)
    OP_62(0x17, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_2CC9():
        OP_8F(0xFE, 0xFFFFFF9C, 0x0, 0x2FA8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 0, lambda_2CC9)
    Sleep(50)
    OP_62(0x18, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_2CFB():
        OP_8F(0xFE, 0x23A, 0x0, 0x2AF8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 0, lambda_2CFB)
    Sleep(50)
    OP_62(0x19, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_2D2D():
        OP_8F(0xFE, 0xFFFFFB8C, 0x0, 0x28FA, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 0, lambda_2D2D)
    OP_73(0x6)
    OP_82(0x0, 0x0)

    ChrTalk(    #53
        0x17,
        "#4PWhat the...?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x18,
        "#4PH-How...?\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("Man's Voice")

    AnonymousTalk(    #55
        "\x07\x05Oh, yeah. Probably should've said this earlier.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(500)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("Man's Voice")

    AnonymousTalk(    #56
        (
            "\x07\x05You REALLY might wanna step back from that door.\x01",
            "Like, a lot.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)

    def lambda_2E35():
        OP_6D(1770, 0, 15740, 2500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_2E35)

    def lambda_2E4D():
        OP_67(0, 5430, -10000, 2500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_2E4D)

    def lambda_2E65():
        OP_6B(2700, 2500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_2E65)

    def lambda_2E75():
        OP_6E(290, 2500)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_2E75)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    PlayEffect(0x0, 0x0, 0xFF, -400, 1500, 16500, 0, 270, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x392, 0x0, 0x64)
    Sleep(100)
    OP_22(0x1FE, 0x0, 0x64)
    OP_7C(0x0, 0xCE4, 0xBB8, 0x64)
    OP_6F(0x6, 21)
    OP_70(0x6, 0x29)
    Sleep(300)
    OP_82(0x0, 0x2)
    OP_73(0x6)
    Sleep(300)
    OP_43(0x17, 0x1, 0x0, 0x13)
    Sleep(300)
    PlayEffect(0x0, 0x0, 0xFF, -200, 1000, 16500, 0, 270, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x392, 0x0, 0x64)
    Sleep(100)
    OP_22(0x1FE, 0x0, 0x64)
    OP_7C(0x0, 0xCE4, 0xBB8, 0x64)
    OP_6F(0x6, 41)
    OP_70(0x6, 0x3D)
    Sleep(300)
    OP_82(0x0, 0x2)
    OP_73(0x6)
    OP_82(0x0, 0x0)
    Sleep(600)
    PlayEffect(0x0, 0x0, 0xFF, -300, 2000, 16500, 0, 270, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x392, 0x0, 0x64)
    Sleep(100)
    OP_22(0x15A, 0x0, 0x64)
    OP_22(0xF6, 0x0, 0x64)
    OP_7C(0x0, 0xCE4, 0xBB8, 0x64)
    OP_6F(0x6, 61)
    OP_70(0x6, 0x51)
    Sleep(300)
    OP_82(0x0, 0x2)
    OP_73(0x6)
    OP_82(0x0, 0x0)
    WaitChrThread(0x109, 0x0)

    def lambda_2FFE():
        OP_6D(1220, 0, 11180, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_2FFE)

    def lambda_3016():
        OP_67(0, 4830, -10000, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_3016)

    def lambda_302E():
        OP_6B(2820, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_302E)

    def lambda_303E():
        OP_6E(288, 500)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_303E)
    OP_22(0x15A, 0x0, 0x64)
    PlayEffect(0x0, 0x0, 0xFF, 0, 1500, 16500, 0, 270, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    OP_22(0x392, 0x0, 0x64)
    Sleep(100)
    OP_22(0x1FE, 0x0, 0x64)
    OP_7C(0x0, 0xCE4, 0xBB8, 0x64)
    OP_6F(0x6, 81)
    OP_70(0x6, 0x78)
    OP_43(0x17, 0x1, 0x0, 0x12)
    Sleep(300)
    OP_82(0x0, 0x2)
    OP_22(0x136, 0x0, 0x64)
    OP_22(0x13F, 0x0, 0x64)
    OP_73(0x6)
    OP_82(0x0, 0x0)
    WaitChrThread(0x17, 0x0)
    WaitChrThread(0x109, 0x0)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    ChrTalk(    #57
        0x17,
        "#4PWhat just happened?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x17,
        (
            "#4PN-No way...\x02\x03",

            "That door was designed to withstand a direct hit \x01",
            "from an orbal cannon!\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #59
        0x109,
        "Young Man's Voice",
        (
            "#4PBoy, you guys have no idea how hard it is to hold\x01",
            "back with that one.\x02\x03",

            "I'm nooot a huge fan of using it, but I mean...you\x01",
            "didn't give me much choice.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)

    def lambda_3217():
        OP_6D(1200, 0, 12480, 2500)
        ExitThread()

    QueueWorkItem(0x17, 0, lambda_3217)

    def lambda_322F():
        OP_67(0, 4830, -10000, 2500)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_322F)

    def lambda_3247():
        OP_6B(2850, 2500)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_3247)

    def lambda_3257():
        OP_6E(292, 2500)
        ExitThread()

    QueueWorkItem(0x17, 3, lambda_3257)
    SetChrPos(0x109, 250, 0, 18000, 180)
    SetChrChipByIndex(0x109, 18)
    SetChrSubChip(0x109, 0)

    def lambda_3282():
        OP_8E(0xFE, 0xFFFFFF74, 0x0, 0x35E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_3282)
    OP_9F(0x109, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
    WaitChrThread(0x109, 0x1)
    SetChrChipByIndex(0x109, 17)
    SetChrSubChip(0x109, 7)
    WaitChrThread(0x17, 0x0)
    ClearChrFlags(0x109, 0x4)
    OP_62(0x17, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(100)
    OP_62(0x18, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(100)
    OP_62(0x19, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #60
        0x18,
        "#4PTh-This is a joke, right...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x19,
        "#6PA...priest?\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #62
        0x109,
        "Father Kevin",
        (
            "#1060F#5PYep. I'm legit and everything, too.\x02\x03",

            "So if you're interested in making any confessions,\x01",
            "I'd be happy to listen to 'em. For extra cheap as a\x01",
            "limited time offer!\x02\x03",

            "And you guys would have a LOT to confess.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x18,
        "#4PUgh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x17,
        "#5PDon't lend an ear to him! Let's do this!\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x17, 3)
    SetChrSubChip(0x17, 0)
    Sleep(100)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0x18, 8)
    SetChrSubChip(0x18, 0)
    Sleep(100)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0x19, 8)
    SetChrSubChip(0x19, 0)
    OP_0D()
    Sleep(1000)

    NpcTalk(    #65
        0x109,
        "Father Kevin",
        (
            "#1068F#5PAww... I was hoping for more of a\x01",
            "'What, you CHARGE people?!' kinda\x01",
            "reaction...\x02\x03",

            "#1075FOh, well. I guess I don't mind cutting\x01",
            "to the chase this time.\x02\x03",

            "#1073FCome get some.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_3590():
        OP_6D(970, 0, 13680, 300)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_3590)

    def lambda_35A8():
        OP_67(0, 5100, -10000, 300)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_35A8)

    def lambda_35C0():
        OP_6B(2500, 300)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_35C0)

    def lambda_35D0():
        OP_6E(280, 300)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_35D0)
    SetChrChipByIndex(0x17, 4)

    def lambda_35E5():
        OP_8F(0xFE, 0xFFFFFF88, 0x0, 0x30F2, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 0, lambda_35E5)
    Sleep(10)
    SetChrChipByIndex(0x19, 9)

    def lambda_360A():
        OP_8F(0xFE, 0xFFFFFF88, 0x0, 0x30F2, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 0, lambda_360A)
    Sleep(20)
    SetChrChipByIndex(0x18, 9)

    def lambda_362F():
        OP_8F(0xFE, 0xFFFFFF88, 0x0, 0x30F2, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 0, lambda_362F)
    WaitChrThread(0x109, 0x0)
    OP_35(0x8, 0x0)
    Battle(0x75, 0x0, 0x0, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    Return()

    # Function_17_2366 end

    def Function_18_3665(): pass

    label("Function_18_3665")

    OP_62(0x17, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_367D():
        OP_8C(0xFE, 0, 600)
        ExitThread()

    QueueWorkItem(0x17, 3, lambda_367D)

    def lambda_368B():
        OP_8F(0xFE, 0x334, 0x0, 0x23F0, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 0, lambda_368B)
    Sleep(10)
    OP_62(0x18, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_36BD():
        OP_8C(0xFE, 315, 600)
        ExitThread()

    QueueWorkItem(0x18, 3, lambda_36BD)

    def lambda_36CB():
        OP_8F(0xFE, 0x898, 0x0, 0x2198, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 0, lambda_36CB)
    Sleep(20)
    OP_62(0x19, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_36FD():
        OP_8C(0xFE, 0, 600)
        ExitThread()

    QueueWorkItem(0x19, 3, lambda_36FD)

    def lambda_370B():
        OP_8F(0xFE, 0xFFFFF63C, 0x0, 0x1FFD, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 0, lambda_370B)
    Return()

    # Function_18_3665 end

    def Function_19_3721(): pass

    label("Function_19_3721")

    OP_62(0x17, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_3739():
        OP_8F(0xFE, 0xFFFFFF9C, 0x0, 0x2BC0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 0, lambda_3739)
    Sleep(50)
    OP_62(0x18, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_376B():
        OP_8F(0xFE, 0x23A, 0x0, 0x2710, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 0, lambda_376B)
    Sleep(50)
    OP_62(0x19, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_379D():
        OP_8F(0xFE, 0xFFFFFB8C, 0x0, 0x2512, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 0, lambda_379D)
    Return()

    # Function_19_3721 end

    def Function_20_37B3(): pass

    label("Function_20_37B3")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_44(0x17, 0x0)
    OP_44(0x18, 0x0)
    OP_44(0x19, 0x0)
    ClearChrFlags(0x17, 0x80)
    SetChrPos(0x17, -100, 0, 10200, 0)
    SetChrChipByIndex(0x17, 7)
    SetChrSubChip(0x17, 3)
    SetChrFlags(0x17, 0x800)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x18, 0x1)
    ClearChrFlags(0x19, 0x1)
    SetChrFlags(0x18, 0x800)
    SetChrFlags(0x19, 0x800)
    SetChrPos(0x18, 1450, 0, 9630, 45)
    SetChrPos(0x19, -1680, 0, 9180, 315)
    OP_51(0x18, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x19, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x18, 19)
    SetChrSubChip(0x18, 0)
    SetChrChipByIndex(0x19, 19)
    SetChrSubChip(0x19, 0)
    SetChrPos(0x109, 20, 0, 12970, 180)
    SetChrChipByIndex(0x109, 15)
    SetChrSubChip(0x109, 0)
    OP_72(0x406, 0x0)
    ExitThread()
    OP_6F(0x6, 120)
    OP_72(0x806, 0x0)
    ExitThread()
    OP_71(0x404, 0x0)
    ExitThread()
    OP_72(0x407, 0x0)
    ExitThread()
    OP_71(0x404, 0x0)
    ExitThread()
    OP_6D(1370, 0, 13240, 0)
    OP_67(0, 4780, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(287, 0)
    OP_1D(0xAB)
    Sleep(1000)

    def lambda_38ED():
        OP_6B(2900, 1500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_38ED)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x109, 0x0)
    OP_43(0x17, 0x1, 0x0, 0x15)

    ChrTalk(    #66
        0x17,
        (
            "#4PH-He's a Grail Knight?!\x02\x03",

            "I'd heard rumors about them, but damn...\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #67
        0x109,
        "Father Kevin",
        (
            "#1075F#5PAnd curious as I am, I'm probably better off not\x01",
            "asking about what kinda rumors you've heard.\x02\x03",

            "#1060FDon't worry, though. I'm only here for your client.\x02\x03",

            "So you go ahead and have a niiice, long nap on the\x01",
            "floor, mm'kay? You'll still live to see tomorrow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x17,
        "#4PUgh... What kind of a monster...?\x02",
    )

    CloseMessageWindow()
    OP_44(0x17, 0x1)
    OP_9E(0x17, 0x14, 0x0, 0x12C, 0xBB8)
    Fade(250)
    OP_22(0x20C, 0x0, 0x64)
    OP_51(0x17, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x17, 13)
    SetChrSubChip(0x17, 0)
    ClearChrFlags(0x17, 0x1)
    SetChrFlags(0x17, 0x800)
    SetChrPos(0x17, -180, 0, 10800, 0)
    OP_0D()
    Sleep(300)

    def lambda_3AF8():
        OP_6D(1590, 0, 14370, 2000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_3AF8)
    OP_62(0x109, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x109)
    Sleep(500)
    WaitChrThread(0x109, 0x0)
    Sleep(300)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x109, 65535)
    SetChrSubChip(0x109, 0)
    OP_0D()
    Sleep(300)

    NpcTalk(    #69
        0x109,
        "Father Kevin",
        (
            "#1060F#5P...Okay, I've got what I came for.\x02\x03",

            "Now to get back to the party and wrap this\x01",
            "job up.\x02\x03",

            "#1068FSucks I have to go without taking that lady\x01",
            "up on her offer, though...\x02\x03",

            "She was lookin' pretty darn fine, and it was\x01",
            "obvious her husband wasn't givin' her enough\x01",
            "squeeze...\x02\x03",

            "#1066FThen again, I shouldn't go playing with fire too\x01",
            "much, huh?\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x25E5)
    OP_64(0x5, 0x1)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1F, 0x80)
    OP_9F(0x1A, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x1C, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x1F, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x20, 0x80)
    OP_9F(0x1B, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x1D, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x20, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x1E, 0x80)
    OP_9F(0x1E, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x21, 0x80)
    OP_9F(0x21, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Return()

    # Function_20_37B3 end

    def Function_21_3D45(): pass

    label("Function_21_3D45")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3D81")
    OP_9E(0xFE, 0xF, 0x0, 0x12C, 0xBB8)
    Sleep(1000)
    OP_9E(0xFE, 0xF, 0x0, 0x12C, 0xBB8)
    Sleep(1500)
    Jump("Function_21_3D45")

    label("loc_3D81")

    Return()

    # Function_21_3D45 end

    def Function_22_3D82(): pass

    label("Function_22_3D82")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4BC, 5)), scpexpr(EXPR_END)), "loc_3E32")

    NpcTalk(    #70
        0x109,
        "Father Kevin",
        (
            "#1060FThis way must lead to the first-class rooms.\x02\x03",

            "#1075FNo doubt I'd find some pretty interesting stuff\x01",
            "in there, but I'd better not right now.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E8B")

    label("loc_3E32")


    NpcTalk(    #71
        0x109,
        "Masked Man",
        (
            "#1600F(I've got no business this way.)\x02\x03",

            "#1600F(Better get back to work.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3E8B")

    OP_90(0x0, 0x0, 0x0, 0x3E8, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    SetMapFlags(0x2000000)
    Return()

    # Function_22_3D82 end

    def Function_23_3EAC(): pass

    label("Function_23_3EAC")

    EventBegin(0x1)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #72
        "\x07\x05The doors are locked.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    Sleep(50)
    EventEnd(0x4)
    SetMapFlags(0x2000000)
    Return()

    # Function_23_3EAC end

    SaveToFile()

Try(main)
