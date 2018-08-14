from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

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
        '古代遗物',                             # 9
        '黑衣人',                               # 10
        '黑衣人',                               # 11
        '障碍用临时角色',                       # 12
        '障碍用临时角色',                       # 13
        '障碍用临时角色',                       # 14
        '障碍用临时角色',                       # 15
        '黑衣人',                               # 16
        '黑衣人',                               # 17
        '黑衣人',                               # 18
        '障碍用临时角色',                       # 19
        '障碍用临时角色',                       # 20
        '障碍用临时角色',                       # 21
        '障碍用临时角色',                       # 22
        '障碍用临时角色',                       # 23
        '障碍用临时角色',                       # 24
        '障碍用临时角色',                       # 25
        '障碍用临时角色',                       # 26
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
        "Function_4_E07",          # 04, 4
        "Function_5_F88",          # 05, 5
        "Function_6_FAF",          # 06, 6
        "Function_7_10C7",         # 07, 7
        "Function_8_11DB",         # 08, 8
        "Function_9_12F5",         # 09, 9
        "Function_10_140F",        # 0A, 10
        "Function_11_1627",        # 0B, 11
        "Function_12_1774",        # 0C, 12
        "Function_13_1A0F",        # 0D, 13
        "Function_14_1CE7",        # 0E, 14
        "Function_15_1D3C",        # 0F, 15
        "Function_16_1E43",        # 10, 16
        "Function_17_22DB",        # 11, 17
        "Function_18_3365",        # 12, 18
        "Function_19_3421",        # 13, 19
        "Function_20_34B3",        # 14, 20
        "Function_21_39A8",        # 15, 21
        "Function_22_39E5",        # 16, 22
        "Function_23_3AEB",        # 17, 23
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
            "#5P……这位客人，请您留步。\x02\x03",

            "这前面就是主人\x01",
            "康莱特先生的私人房间了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x12,
        "#5P请回去吧。\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #2
        0x109,
        "戴面具的绅士",
        (
            "#1603F#6P啊啊，你们工作辛苦了。\x02\x03",

            "#1601F不过……\x01",
            "你们的运气实在是太差了。\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)

    def lambda_AC4():
        OP_6B(2860, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_AC4)
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
        "#5P哎……\x02",
    )

    Jump("loc_B41")

    label("loc_B41")

    CloseMessageWindow()

    ChrTalk(    #4
        0x12,
        "#5P想、想干什么……\x02",
    )

    CloseMessageWindow()
    LoadEffect(0x0, "scraft\\\\sc008_02.eff")
    PlayEffect(0x0, 0xFF, 0xFF, -250, 1100, -44450, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_23(0xC9)
    OP_82(0x0, 0x2)
    Sleep(500)

    def lambda_BBE():
        OP_9E(0x11, 0x14, 0x0, 0x7D0, 0xBB8)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_BBE)
    Sleep(100)

    def lambda_BDD():
        OP_9E(0x12, 0x14, 0x0, 0x7D0, 0xBB8)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_BDD)

    ChrTalk(    #5 op#A op#5
        0x11,
        "#5P#10A啊……！\x05\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #6 op#A op#5
        0x12,
        "#5P#10A……呜……！\x05\x02",
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

    def lambda_D0D():
        OP_6D(660, 0, -43760, 1500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_D0D)
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
        "戴面具的绅士",
        (
            "#1600F#6P唔……\x01",
            "猎兵也堕落了吗……？\x02\x03",

            "就这种程度的本事，\x01",
            "看来这次用不着花什么功夫就能完事。\x02\x03",

            "#1601F呵呵，比以往的工作都要轻松，\x01",
            "真是太好了。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_A2(0x25E2)
    EventEnd(0x0)
    Return()

    # Function_3_96C end

    def Function_4_E07(): pass

    label("Function_4_E07")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_6D(990, 450, 13390, 0)
    OP_67(0, 7520, -10000, 0)
    OP_6B(2570, 0)
    OP_6C(45000, 0)
    OP_6E(342, 0)
    SetChrPos(0x109, -190, 0, -2290, 0)
    OP_9F(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_E72():
        OP_6D(660, 50, 2040, 6000)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_E72)

    def lambda_E8A():
        OP_67(0, 6820, -10000, 6000)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_E8A)

    def lambda_EA2():
        OP_6B(2390, 6000)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_EA2)

    def lambda_EB2():
        OP_6E(314, 6000)
        ExitThread()

    QueueWorkItem(0x11, 3, lambda_EB2)
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
        "戴面具的绅士",
        (
            "#1600F#5P呵呵……\x01",
            "这奢华的房间真是浪费啊。\x02\x03",

            "好了，到底藏在哪里呢？\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_CE(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A2(0x25E3)
    EventEnd(0x0)
    Return()

    # Function_4_E07 end

    def Function_5_F88(): pass

    label("Function_5_F88")


    def lambda_F8E():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_F8E)
    OP_8E(0xFE, 0xFFFFFF42, 0x0, 0x352, 0x7D0, 0x0)
    Return()

    # Function_5_F88 end

    def Function_6_FAF(): pass

    label("Function_6_FAF")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #9
        "\x07\x05桌子下面，有一个类似开关的东西。\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(    #10
        "\x07\x05要不要按一下试试？\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_101E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10C3")

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "【是】\x01",      # 0
            "【否】\x01",      # 1
        )
    )

    Jump("loc_1054")

    label("loc_1054")

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Sleep(300)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_107B"),
        (1, "loc_10A6"),
        (SWITCH_DEFAULT, "loc_10B3"),
    )


    label("loc_107B")

    OP_22(0x64, 0x0, 0x64)
    Sleep(1000)
    OP_CE(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_64(0x0, 0x1)
    OP_A2(0x25EE)
    Call(0, 11)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_10C0")

    label("loc_10A6")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_10C0")

    label("loc_10B3")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_10C0")

    label("loc_10C0")

    Jump("loc_101E")

    label("loc_10C3")

    TalkEnd(0xFF)
    Return()

    # Function_6_FAF end

    def Function_7_10C7(): pass

    label("Function_7_10C7")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #11
        "\x07\x05盆栽里面，有一个奇怪的开关。\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(    #12
        "\x07\x05要不要按一下试试？\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1132")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_11D7")

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "【是】\x01",      # 0
            "【否】\x01",      # 1
        )
    )

    Jump("loc_1168")

    label("loc_1168")

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Sleep(300)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_118F"),
        (1, "loc_11BA"),
        (SWITCH_DEFAULT, "loc_11C7"),
    )


    label("loc_118F")

    OP_22(0x64, 0x0, 0x64)
    Sleep(1000)
    OP_CE(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_64(0x1, 0x1)
    OP_A2(0x25EF)
    Call(0, 11)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_11D4")

    label("loc_11BA")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_11D4")

    label("loc_11C7")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_11D4")

    label("loc_11D4")

    Jump("loc_1132")

    label("loc_11D7")

    TalkEnd(0xFF)
    Return()

    # Function_7_10C7 end

    def Function_8_11DB(): pass

    label("Function_8_11DB")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #13
        "\x07\x05花瓶的下面，有一个类似开关的东西。\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(    #14
        "\x07\x05要不要按一下试试？\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_124C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_12F1")

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "【是】\x01",      # 0
            "【否】\x01",      # 1
        )
    )

    Jump("loc_1282")

    label("loc_1282")

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Sleep(300)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_12A9"),
        (1, "loc_12D4"),
        (SWITCH_DEFAULT, "loc_12E1"),
    )


    label("loc_12A9")

    OP_22(0x64, 0x0, 0x64)
    Sleep(1000)
    OP_CE(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_64(0x2, 0x1)
    OP_A2(0x25F0)
    Call(0, 11)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_12EE")

    label("loc_12D4")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_12EE")

    label("loc_12E1")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_12EE")

    label("loc_12EE")

    Jump("loc_124C")

    label("loc_12F1")

    TalkEnd(0xFF)
    Return()

    # Function_8_11DB end

    def Function_9_12F5(): pass

    label("Function_9_12F5")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #15
        "\x07\x05这附近的地毯，好像已经被踩得非常旧了。\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(    #16
        "\x07\x05要不要踩踩看？\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1366")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_140B")

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "【是】\x01",      # 0
            "【否】\x01",      # 1
        )
    )

    Jump("loc_139C")

    label("loc_139C")

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Sleep(300)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_13C3"),
        (1, "loc_13EE"),
        (SWITCH_DEFAULT, "loc_13FB"),
    )


    label("loc_13C3")

    OP_22(0x64, 0x0, 0x64)
    Sleep(1000)
    OP_CE(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_64(0x3, 0x1)
    OP_A2(0x25F1)
    Call(0, 11)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1408")

    label("loc_13EE")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1408")

    label("loc_13FB")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1408")

    label("loc_1408")

    Jump("loc_1366")

    label("loc_140B")

    TalkEnd(0xFF)
    Return()

    # Function_9_12F5 end

    def Function_10_140F(): pass

    label("Function_10_140F")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #17
        "\x07\x05沙发的扶手上，有一个类似开关的东西。\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(    #18
        "\x07\x05要不要按一下试试？\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1482")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1623")

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "【是】\x01",      # 0
            "【否】\x01",      # 1
        )
    )

    Jump("loc_14B8")

    label("loc_14B8")

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Sleep(300)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_14DF"),
        (1, "loc_1606"),
        (SWITCH_DEFAULT, "loc_1613"),
    )


    label("loc_14DF")

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
        "\x07\x05所有的开关都恢复到初始状态了！\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Sleep(300)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15C4")
    OP_A2(0x1)

    NpcTalk(    #20
        0x109,
        "戴面具的绅士",
        (
            "#1602F假的吗？\x02\x03",

            "哎呀哎呀。\x01",
            "真是麻烦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15F9")

    label("loc_15C4")


    NpcTalk(    #21
        0x109,
        "戴面具的绅士",
        (
            "#1602F哎呀哎呀。\x01",
            "真是麻烦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15F9")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1620")

    label("loc_1606")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1620")

    label("loc_1613")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1620")

    label("loc_1620")

    Jump("loc_1482")

    label("loc_1623")

    TalkEnd(0xFF)
    Return()

    # Function_10_140F end

    def Function_11_1627(): pass

    label("Function_11_1627")

    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_16E2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_169C")
    OP_A2(0x0)

    NpcTalk(    #22
        0x109,
        "戴面具的绅士",
        (
            "#1600F开关……？\x02\x03",

            "看来，\x01",
            "这样的机关应该不止一个。\x02",
        )
    )

    Jump("loc_1698")

    label("loc_1698")

    CloseMessageWindow()
    Jump("loc_16DB")

    label("loc_169C")


    NpcTalk(    #23
        0x109,
        "戴面具的绅士",
        (
            "#1600F看来，\x01",
            "这样的机关应该不止一个。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16DB")

    OP_65(0x4, 0x1)
    Jump("loc_1773")

    label("loc_16E2")

    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1723")

    NpcTalk(    #24
        0x109,
        "戴面具的绅士",
        "#1600F好了，下一个是……\x02",
    )

    CloseMessageWindow()
    Jump("loc_1773")

    label("loc_1723")

    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_175C")

    NpcTalk(    #25
        0x109,
        "戴面具的绅士",
        "#1600F还有啊……\x02",
    )

    CloseMessageWindow()
    Jump("loc_1773")

    label("loc_175C")

    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1773")
    OP_64(0x4, 0x1)
    OP_A2(0x25F2)
    Call(0, 12)

    label("loc_1773")

    Return()

    # Function_11_1627 end

    def Function_12_1774(): pass

    label("Function_12_1774")

    EventBegin(0x0)
    OP_22(0xBB, 0x0, 0x64)
    Sleep(500)
    OP_6F(0x0, 0)
    OP_70(0x0, 0x12C)
    Fade(500)

    def lambda_1799():
        OP_6D(1280, 300, 16390, 0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1799)

    def lambda_17B1():
        OP_67(0, 5960, -10000, 0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_17B1)

    def lambda_17C9():
        OP_6B(2950, 0)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_17C9)

    def lambda_17D9():
        OP_6E(262, 0)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_17D9)
    WaitChrThread(0x109, 0x0)

    def lambda_17EE():
        OP_6B(2850, 2000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_17EE)
    WaitChrThread(0x109, 0x2)
    OP_73(0x0)
    OP_7C(0x1E, 0x1E, 0xBB8, 0x64)
    OP_22(0x12E, 0x0, 0x64)
    OP_23(0xBB)
    Sleep(300)
    OP_A2(0x25E4)
    Sleep(1000)

    def lambda_182C():
        OP_6D(1100, 0, 15350, 2000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_182C)
    SetChrPos(0x109, -330, 0, 5770, 0)

    def lambda_1855():
        OP_8E(0xFE, 0xFFFFFF7E, 0x0, 0x314C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1855)
    WaitChrThread(0x109, 0x0)
    WaitChrThread(0x109, 0x1)

    NpcTalk(    #26
        0x109,
        "戴面具的绅士",
        (
            "#1600F呵呵……\x01",
            "真是老套的剧情。\x02\x03",

            "如果我没有猜错的话，\x01",
            "接下来大概就是…… \x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x109, 45, 400)
    Sleep(500)
    OP_8C(0x109, 315, 400)
    Sleep(500)

    def lambda_18FC():
        OP_6D(-200, 0, 15800, 2000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_18FC)

    def lambda_1914():
        OP_8E(0xFE, 0xFFFFF736, 0x0, 0x37D2, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1914)
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
        "\x07\x05有块刻有文字的提示板。\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(    #28
        "\x07\x05看来必须要输入密码。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(300)

    NpcTalk(    #29
        0x109,
        "戴面具的绅士",
        "#1602F#6P唔，有可能的是……\x02",
    )

    CloseMessageWindow()
    Call(0, 13)
    EventEnd(0x0)
    OP_65(0x5, 0x1)
    Return()

    # Function_12_1774 end

    def Function_13_1A0F(): pass

    label("Function_13_1A0F")

    TalkBegin(0xFF)
    OP_8C(0x109, 0, 0)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 100, -1, -1)
    SetChrName("")

    AnonymousTalk(    #30
        "\x07\x05隐秘之门的密码是？\x18\x02",
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1A5B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1CE3")

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【Ｏ·Ｒ·Ｆ·Ｅ·Ｕ·Ｈ·Ｓ】\x01",      # 0
            "【Ｏ·Ｒ·Ｐ·Ｈ·Ｅ·Ｕ·Ｓ】\x01",      # 1
            "【Ｏ·Ｌ·Ｐ·Ｈ·Ｅ·Ｕ·Ｓ】\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_56(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToBright(300, 0)
    Sleep(300)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1B02"),
        (1, "loc_1B61"),
        (2, "loc_1C81"),
        (SWITCH_DEFAULT, "loc_1CE0"),
    )


    label("loc_1B02")

    OP_22(0x9C, 0x0, 0x64)
    Sleep(1000)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #31
        "\x07\x05好像没有什么反应。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Sleep(300)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1CE0")

    label("loc_1B61")

    OP_22(0x9C, 0x0, 0x64)
    Sleep(1000)
    EventBegin(0x0)
    OP_6F(0x4, 0)
    OP_70(0x4, 0xF)
    OP_73(0x4)

    def lambda_1B84():
        OP_6D(660, 550, 15930, 1500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1B84)

    def lambda_1B9C():
        OP_67(0, 5480, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_1B9C)

    def lambda_1BB4():
        OP_6B(3000, 1500)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_1BB4)

    def lambda_1BC4():
        OP_8C(0x109, 90, 400)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1BC4)
    WaitChrThread(0x109, 0x0)
    WaitChrThread(0x109, 0x1)
    Sleep(500)

    NpcTalk(    #32
        0x109,
        "戴面具的绅士",
        (
            "#1602F#6P哼……果不其然。\x02\x03",

            "这次的目标——\x01",
            "是『那伙人』故意散播的\x01",
            "玩具的可能性相当高。\x02",
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
    Jump("loc_1CE0")

    label("loc_1C81")

    OP_22(0x9C, 0x0, 0x64)
    Sleep(1000)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #33
        "\x07\x05好像没有什么反应。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Sleep(300)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1CE0")

    label("loc_1CE0")

    Jump("loc_1A5B")

    label("loc_1CE3")

    TalkEnd(0xFF)
    Return()

    # Function_13_1A0F end

    def Function_14_1CE7(): pass

    label("Function_14_1CE7")

    OP_20(0xBB8)

    def lambda_1CF2():
        OP_6B(2800, 5500)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_1CF2)
    OP_8C(0x109, 90, 400)
    OP_8E(0xFE, 0xFFFFFF4C, 0x0, 0x3854, 0x7D0, 0x0)
    OP_8C(0x109, 0, 400)
    OP_8E(0xFE, 0xFFFFFF9C, 0x0, 0x406A, 0x7D0, 0x0)
    Sleep(2000)
    OP_44(0x109, 0x3)
    Return()

    # Function_14_1CE7 end

    def Function_15_1D3C(): pass

    label("Function_15_1D3C")

    EventBegin(0x0)
    OP_6F(0x4, 0)
    OP_70(0x4, 0xF)
    OP_73(0x4)

    def lambda_1D55():
        OP_6D(660, 550, 15930, 1500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1D55)

    def lambda_1D6D():
        OP_67(0, 5480, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_1D6D)

    def lambda_1D85():
        OP_6B(3000, 1500)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_1D85)

    def lambda_1D95():
        OP_8C(0x109, 90, 400)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1D95)
    WaitChrThread(0x109, 0x0)
    WaitChrThread(0x109, 0x1)

    NpcTalk(    #34
        0x109,
        "戴面具的绅士",
        (
            "#1602F#6P哼……果不其然。\x02\x03",

            "这次的目标——\x01",
            "是『那伙人』故意散播的\x01",
            "玩具的可能性相当高。\x02",
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

    # Function_15_1D3C end

    def Function_16_1E43(): pass

    label("Function_16_1E43")

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

    def lambda_1F70():
        OP_6D(41170, 2050, 7350, 6000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1F70)

    def lambda_1F88():
        OP_67(0, 4210, -10000, 6000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1F88)

    def lambda_1FA0():
        OP_6B(2880, 6000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_1FA0)

    def lambda_1FB0():
        OP_6C(42000, 6000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_1FB0)

    def lambda_1FC0():
        OP_6E(315, 6000)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_1FC0)
    WaitChrThread(0xEE, 0x0)
    Sleep(1000)

    def lambda_1FDA():
        OP_6D(41290, 20, 5660, 3500)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_1FDA)

    def lambda_1FF2():
        OP_67(0, 4520, -10000, 3500)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_1FF2)

    def lambda_200A():
        OP_6B(3000, 3500)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_200A)

    def lambda_201A():
        OP_6E(303, 3500)
        ExitThread()

    QueueWorkItem(0x11, 3, lambda_201A)
    Sleep(2500)

    def lambda_202F():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x258)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_202F)

    def lambda_2041():
        OP_8F(0xFE, 0x9C2C, 0x0, 0xFFFFFEB6, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_2041)
    WaitChrThread(0x11, 0x0)
    WaitChrThread(0x109, 0x0)
    WaitChrThread(0x109, 0x1)
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_2087():
        OP_6B(2730, 3000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_2087)

    def lambda_2097():
        OP_6E(280, 3000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_2097)
    OP_8E(0x109, 0x9AF6, 0x14, 0xD0C, 0x3E8, 0x0)
    Sleep(300)
    OP_62(0x109, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x109)
    Sleep(500)
    WaitChrThread(0x109, 0x2)

    NpcTalk(    #35
        0x109,
        "戴面具的绅士",
        (
            "#1602F#6P『愚者挂坠』——\x02\x03",

            "戴在身上的话，\x01",
            "会使人相信其大部分的谎言，\x01",
            "是禁忌的古代遗物之一……\x02\x03",

            "真是……一个小小的武器商人，\x01",
            "居然如此无法无天。\x02",
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
        "戴面具的绅士",
        "#1600F#6P哼……\x02",
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

    # Function_16_1E43 end

    def Function_17_22DB(): pass

    label("Function_17_22DB")

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

    def lambda_23C6():
        OP_8E(0xFE, 0xFFFFFF6A, 0x0, 0x3200, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_23C6)
    Sleep(100)
    SetChrChipByIndex(0x18, 21)

    def lambda_23EB():
        OP_8E(0xFE, 0x23A, 0x0, 0x2C88, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_23EB)
    Sleep(150)
    SetChrChipByIndex(0x19, 21)

    def lambda_2410():
        OP_8E(0xFE, 0xFFFFFB8C, 0x0, 0x2AEE, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_2410)
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
            "#6P喂，到底怎么回事！\x02\x03",

            "放哨的这些家伙\x01",
            "到底在干什么！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x18,
        (
            "#4P……那两个人\x01",
            "似乎同时被麻醉了。\x02\x03",

            "应该是用了针或者喷射器之类的东西。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x17,
        (
            "#5P哼……\x01",
            "说不定是我们的同行干的。\x02",
        )
    )

    Jump("loc_252D")

    label("loc_252D")

    CloseMessageWindow()
    OP_8C(0x17, 180, 400)

    ChrTalk(    #40
        0x17,
        (
            "#5P在宴会结束之前\x01",
            "就把这家伙关在里面吧。\x02\x03",

            "在那之后\x01",
            "再去向康莱特大人报告。\x02",
        )
    )

    Jump("loc_259B")

    label("loc_259B")

    CloseMessageWindow()

    ChrTalk(    #41
        0x18,
        "#4P会不会有其他同伙？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x17,
        (
            "#5P从监视器的记录来看，\x01",
            "应该只有这家伙一个人。\x02\x03",

            "但是，不排除有\x01",
            "其他同伙暗中支援的可能性。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x19,
        (
            "#6P趁现在还没引起骚动，\x01",
            "先对全部客人进行一下确认比较好。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("绅士的声音")

    AnonymousTalk(    #44
        "\x07\x05呵呵呵……\x02",
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

    def lambda_26FD():
        OP_6D(1400, 0, 15000, 1000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_26FD)
    OP_8C(0x17, 0, 600)
    WaitChrThread(0x109, 0x0)

    ChrTalk(    #45
        0x18,
        "#4P刚才的是……\x02",
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
        (
            "#6P喂，你这家伙！\x01",
            "有什么好笑的！\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("绅士的声音")

    AnonymousTalk(    #47
        (
            "\x07\x05不，没什么……\x01",
            "只是为刚才小看你们的行为，\x01",
            "感到有些抱歉。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("绅士的声音")

    AnonymousTalk(    #48
        (
            "\x07\x05本以为你们只是堕落的小混混，\x01",
            "但是看来猎兵毕竟还是受过不少的训练啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)

    ChrTalk(    #49
        0x18,
        "#4P这家伙……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x19,
        (
            "#6P哼……\x01",
            "你也不简单，真是好大的胆子。\x02\x03",

            "虽然不清楚你的底细，\x01",
            "但是，康莱特大人可不是好惹的。\x02\x03",

            "别以为这样就能全身而退。\x02",
        )
    )

    Jump("loc_2925")

    label("loc_2925")

    CloseMessageWindow()

    ChrTalk(    #51
        0x17,
        (
            "#6P哈哈哈……\x02\x03",

            "我们会让你品尝一下\x01",
            "比舌头被割掉还要美味的痛苦。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("绅士的声音")

    AnonymousTalk(    #52
        (
            "\x07\x05呵呵……\x01",
            "那可真是充满魅力的邀请啊。\x02\x03",

            "不过，真不巧，\x01",
            "我已经事先有约了。 \x02",
        )
    )

    Jump("loc_29F1")

    label("loc_29F1")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    PlayEffect(0x0, 0x0, 0xFF, 0, 2000, 17000, 0, 270, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x392, 0x0, 0x64)
    Sleep(100)
    OP_22(0x1FE, 0x0, 0x64)

    def lambda_2A47():
        OP_7C(0x0, 0xCE4, 0xBB8, 0x64)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_2A47)
    OP_6F(0x6, 1)
    OP_70(0x6, 0x15)
    Sleep(300)
    OP_82(0x0, 0x2)
    OP_62(0x17, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_2A87():
        OP_8F(0xFE, 0xFFFFFF9C, 0x0, 0x2FA8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 0, lambda_2A87)
    Sleep(50)
    OP_62(0x18, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_2AB9():
        OP_8F(0xFE, 0x23A, 0x0, 0x2AF8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 0, lambda_2AB9)
    Sleep(50)
    OP_62(0x19, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_2AEB():
        OP_8F(0xFE, 0xFFFFFB8C, 0x0, 0x28FA, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 0, lambda_2AEB)
    OP_73(0x6)
    OP_82(0x0, 0x0)

    ChrTalk(    #53
        0x17,
        "#4P什……！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x18,
        "#4P什、什么……？\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("绅士的声音")

    AnonymousTalk(    #55
        "\x07\x05对了，有句话忘了告诉你们。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(500)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("绅士的声音")

    AnonymousTalk(    #56
        (
            "\x07\x05——你们啊，\x01",
            "还是早点离开那里比较好哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)

    def lambda_2BE2():
        OP_6D(1770, 0, 15740, 2500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_2BE2)

    def lambda_2BFA():
        OP_67(0, 5430, -10000, 2500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_2BFA)

    def lambda_2C12():
        OP_6B(2700, 2500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_2C12)

    def lambda_2C22():
        OP_6E(290, 2500)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_2C22)
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

    def lambda_2DAB():
        OP_6D(1220, 0, 11180, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_2DAB)

    def lambda_2DC3():
        OP_67(0, 4830, -10000, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_2DC3)

    def lambda_2DDB():
        OP_6B(2820, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_2DDB)

    def lambda_2DEB():
        OP_6E(288, 500)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_2DEB)
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
        "#4P什……！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x17,
        (
            "#4P怎、怎么可能……\x02\x03",

            "这可是……\x01",
            "连导力炮的轰击都能承受的大门啊！\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #59
        0x109,
        "青年的声音",
        (
            "#4P哎呀哎呀，\x01",
            "这战技好难控制轻重啊。\x02\x03",

            "呵呵，\x01",
            "可不要让我花多余的功夫。\x02",
        )
    )

    Jump("loc_2F66")

    label("loc_2F66")

    CloseMessageWindow()
    Sleep(300)

    def lambda_2F72():
        OP_6D(1200, 0, 12480, 2500)
        ExitThread()

    QueueWorkItem(0x17, 0, lambda_2F72)

    def lambda_2F8A():
        OP_67(0, 4830, -10000, 2500)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_2F8A)

    def lambda_2FA2():
        OP_6B(2850, 2500)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_2FA2)

    def lambda_2FB2():
        OP_6E(292, 2500)
        ExitThread()

    QueueWorkItem(0x17, 3, lambda_2FB2)
    SetChrPos(0x109, 250, 0, 18000, 180)
    SetChrChipByIndex(0x109, 18)
    SetChrSubChip(0x109, 0)

    def lambda_2FDD():
        OP_8E(0xFE, 0xFFFFFF74, 0x0, 0x35E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_2FDD)
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
        "#4P什、什么……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x19,
        "#6P教会的……神父？\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #62
        0x109,
        "凯文·格拉汉姆",
        (
            "#1060F#5P没错，是货真价实的神父。\x02\x03",

            "要忏悔的话，\x01",
            "我可以给你们算便宜一点哦。\x02\x03",

            "这几位小哥看起来\x01",
            "似乎都有着黑暗的过去嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x18,
        "#4P哼……\x02",
    )

    Jump("loc_3160")

    label("loc_3160")

    CloseMessageWindow()

    ChrTalk(    #64
        0x17,
        (
            "#5P别听他花言巧语！\x01",
            "一起上！\x02",
        )
    )

    Jump("loc_3194")

    label("loc_3194")

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
        "凯文·格拉汉姆",
        (
            "#1068F#5P唉……\x01",
            "我本来还想听到你们抱怨\x01",
            "『忏悔也要收钱吗！』。\x02\x03",

            "#1075F……也罢。\x01",
            "反正也没什么时间了。\x02\x03",

            "#1073F一起来吧。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_3290():
        OP_6D(970, 0, 13680, 300)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_3290)

    def lambda_32A8():
        OP_67(0, 5100, -10000, 300)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_32A8)

    def lambda_32C0():
        OP_6B(2500, 300)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_32C0)

    def lambda_32D0():
        OP_6E(280, 300)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_32D0)
    SetChrChipByIndex(0x17, 4)

    def lambda_32E5():
        OP_8F(0xFE, 0xFFFFFF88, 0x0, 0x30F2, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 0, lambda_32E5)
    Sleep(10)
    SetChrChipByIndex(0x19, 9)

    def lambda_330A():
        OP_8F(0xFE, 0xFFFFFF88, 0x0, 0x30F2, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 0, lambda_330A)
    Sleep(20)
    SetChrChipByIndex(0x18, 9)

    def lambda_332F():
        OP_8F(0xFE, 0xFFFFFF88, 0x0, 0x30F2, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 0, lambda_332F)
    WaitChrThread(0x109, 0x0)
    OP_35(0x8, 0x0)
    Battle(0x75, 0x0, 0x0, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    Return()

    # Function_17_22DB end

    def Function_18_3365(): pass

    label("Function_18_3365")

    OP_62(0x17, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_337D():
        OP_8C(0xFE, 0, 600)
        ExitThread()

    QueueWorkItem(0x17, 3, lambda_337D)

    def lambda_338B():
        OP_8F(0xFE, 0x334, 0x0, 0x23F0, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 0, lambda_338B)
    Sleep(10)
    OP_62(0x18, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_33BD():
        OP_8C(0xFE, 315, 600)
        ExitThread()

    QueueWorkItem(0x18, 3, lambda_33BD)

    def lambda_33CB():
        OP_8F(0xFE, 0x898, 0x0, 0x2198, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 0, lambda_33CB)
    Sleep(20)
    OP_62(0x19, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_33FD():
        OP_8C(0xFE, 0, 600)
        ExitThread()

    QueueWorkItem(0x19, 3, lambda_33FD)

    def lambda_340B():
        OP_8F(0xFE, 0xFFFFF63C, 0x0, 0x1FFD, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 0, lambda_340B)
    Return()

    # Function_18_3365 end

    def Function_19_3421(): pass

    label("Function_19_3421")

    OP_62(0x17, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_3439():
        OP_8F(0xFE, 0xFFFFFF9C, 0x0, 0x2BC0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 0, lambda_3439)
    Sleep(50)
    OP_62(0x18, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_346B():
        OP_8F(0xFE, 0x23A, 0x0, 0x2710, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 0, lambda_346B)
    Sleep(50)
    OP_62(0x19, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_349D():
        OP_8F(0xFE, 0xFFFFFB8C, 0x0, 0x2512, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 0, lambda_349D)
    Return()

    # Function_19_3421 end

    def Function_20_34B3(): pass

    label("Function_20_34B3")

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

    def lambda_35ED():
        OP_6B(2900, 1500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_35ED)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x109, 0x0)
    OP_43(0x17, 0x1, 0x0, 0x15)

    ChrTalk(    #66
        0x17,
        (
            "#4P教、教会的精英……\x01",
            "被称为『星杯骑士』的家伙吗……\x02\x03",

            "我以前只是听过传闻而已……\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #67
        0x109,
        "凯文·格拉汉姆",
        (
            "#1075F#5P到底是什么样的传闻，\x01",
            "我这次就不追问到底了。\x02\x03",

            "#1060F不用担心，\x01",
            "我的目标只有你们的雇主。\x02\x03",

            "你们就放心地睡一会儿吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x17,
        (
            "#4P呜……\x01",
            "………怪物…………\x02",
        )
    )

    Jump("loc_3742")

    label("loc_3742")

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

    def lambda_37A0():
        OP_6D(1590, 0, 14370, 2000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_37A0)
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
        "凯文·格拉汉姆",
        (
            "#1060F#5P……好了，\x01",
            "目标物品已经回收完毕。\x02\x03",

            "尽快回舞会现场，\x01",
            "把余下的工作干完吧。\x02\x03",

            "#1068F唉，话说回来，\x01",
            "错过那位女士的邀请可真浪费啊。\x02\x03",

            "身材挺不错的，\x01",
            "而且看起来似乎\x01",
            "无法从自己丈夫那里得到满足……\x02\x03",

            "#1066F咳……算了，开玩笑也要有个限度。\x02",
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

    # Function_20_34B3 end

    def Function_21_39A8(): pass

    label("Function_21_39A8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_39E4")
    OP_9E(0xFE, 0xF, 0x0, 0x12C, 0xBB8)
    Sleep(1000)
    OP_9E(0xFE, 0xF, 0x0, 0x12C, 0xBB8)
    Sleep(1500)
    Jump("Function_21_39A8")

    label("loc_39E4")

    Return()

    # Function_21_39A8 end

    def Function_22_39E5(): pass

    label("Function_22_39E5")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4BC, 5)), scpexpr(EXPR_END)), "loc_3A6B")

    NpcTalk(    #70
        0x109,
        "凯文·格拉汉姆",
        (
            "#1060F这里是头等客房吗……\x02\x03",

            "#1075F把这里扫荡一番虽然也很有意思，\x01",
            "但这次还是放过他们吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3ACA")

    label("loc_3A6B")


    NpcTalk(    #71
        0x109,
        "戴面具的绅士",
        (
            "#1600F（呵呵，不需要往这边走。）\x02\x03",

            "#1600F（赶快把事情搞定吧。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3ACA")

    OP_90(0x0, 0x0, 0x0, 0x3E8, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    SetMapFlags(0x2000000)
    Return()

    # Function_22_39E5 end

    def Function_23_3AEB(): pass

    label("Function_23_3AEB")

    EventBegin(0x1)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #72
        "\x07\x05门牢牢地锁着。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    Sleep(50)
    EventEnd(0x4)
    SetMapFlags(0x2000000)
    Return()

    # Function_23_3AEB end

    SaveToFile()

Try(main)
