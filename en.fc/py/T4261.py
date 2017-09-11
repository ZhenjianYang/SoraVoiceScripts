from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4261   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4261.x',
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
        'Factory Chief Murdock',                # 9
        'Colonel Richard',                      # 10
        'Duke Dunan',                           # 11
        'Butler Phillip',                       # 12
        'Scherazard',                           # 13
        'Revol',                                # 14
        'Nage',                                 # 15
        'Tita',                                 # 16
        'Russell',                              # 17
        'Tarot',                                # 18
        'Tarot',                                # 19
        'Tarot',                                # 20
        'Tarot',                                # 21
        'Tarot',                                # 22
        'Tarot',                                # 23
        'Tarot',                                # 24
        'Agate',                                # 25
        'Zin',                                  # 26
        'Olivier',                              # 27
        'Orbment',                              # 28
        'Bottle',                               # 29
        'Bottle',                               # 30
        'Bottle',                               # 31
        'Bottle',                               # 32
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
        'ED6_DT07/CH02623 ._CH',             # 00
        'ED6_DT07/CH02030 ._CH',             # 01
        'ED6_DT07/CH02460 ._CH',             # 02
        'ED6_DT07/CH02230 ._CH',             # 03
        'ED6_DT07/CH02240 ._CH',             # 04
        'ED6_DT07/CH02140 ._CH',             # 05
        'ED6_DT07/CH02470 ._CH',             # 06
        'ED6_DT07/CH00020 ._CH',             # 07
        'ED6_DT07/CH01570 ._CH',             # 08
        'ED6_DT07/CH01350 ._CH',             # 09
        'ED6_DT07/CH00020 ._CH',             # 0A
        'ED6_DT07/CH00060 ._CH',             # 0B
        'ED6_DT07/CH02020 ._CH',             # 0C
        'ED6_DT07/CH02033 ._CH',             # 0D
        'ED6_DT07/CH00003 ._CH',             # 0E
        'ED6_DT07/CH00013 ._CH',             # 0F
        'ED6_DT07/CH02620 ._CH',             # 10
        'ED6_DT07/CH00063 ._CH',             # 11
        'ED6_DT07/CH00023 ._CH',             # 12
        'ED6_DT06/CH20021 ._CH',             # 13
        'ED6_DT06/CH20133 ._CH',             # 14
        'ED6_DT07/CH00053 ._CH',             # 15
        'ED6_DT07/CH00073 ._CH',             # 16
        'ED6_DT07/CH00030 ._CH',             # 17
        'ED6_DT06/CH20020 ._CH',             # 18
    )

    AddCharChipPat(
        'ED6_DT07/CH02623P._CP',             # 00
        'ED6_DT07/CH02030P._CP',             # 01
        'ED6_DT07/CH02460P._CP',             # 02
        'ED6_DT07/CH02230P._CP',             # 03
        'ED6_DT07/CH02240P._CP',             # 04
        'ED6_DT07/CH02140P._CP',             # 05
        'ED6_DT07/CH02470P._CP',             # 06
        'ED6_DT07/CH00020P._CP',             # 07
        'ED6_DT07/CH01570P._CP',             # 08
        'ED6_DT07/CH01350P._CP',             # 09
        'ED6_DT07/CH00020P._CP',             # 0A
        'ED6_DT07/CH00060P._CP',             # 0B
        'ED6_DT07/CH02020P._CP',             # 0C
        'ED6_DT07/CH02033P._CP',             # 0D
        'ED6_DT07/CH00003P._CP',             # 0E
        'ED6_DT07/CH00013P._CP',             # 0F
        'ED6_DT07/CH02620P._CP',             # 10
        'ED6_DT07/CH00063P._CP',             # 11
        'ED6_DT07/CH00023P._CP',             # 12
        'ED6_DT06/CH20021P._CP',             # 13
        'ED6_DT06/CH20133P._CP',             # 14
        'ED6_DT07/CH00053P._CP',             # 15
        'ED6_DT07/CH00073P._CP',             # 16
        'ED6_DT07/CH00030P._CP',             # 17
        'ED6_DT06/CH20020P._CP',             # 18
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = 141250,
        Z                   = 0,
        Y                   = 7610,
        Direction           = 278,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = 78740,
        Z                   = 0,
        Y                   = -1880,
        Direction           = 194,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = 83700,
        Z                   = 300,
        Y                   = -52940,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 17,
        ChipIndex           = 0x11,
        NpcIndex            = 0x1D5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 90160,
        Z                   = 0,
        Y                   = -56780,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 458771,
        ChipIndex           = 0x13,
        NpcIndex            = 0x1E6,
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
        Unknown3            = 524307,
        ChipIndex           = 0x13,
        NpcIndex            = 0x1E6,
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
        Unknown3            = 589843,
        ChipIndex           = 0x13,
        NpcIndex            = 0x1E6,
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
        Unknown3            = 655379,
        ChipIndex           = 0x13,
        NpcIndex            = 0x1E6,
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
        Unknown3            = 720915,
        ChipIndex           = 0x13,
        NpcIndex            = 0x1E6,
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
        Unknown3            = 786451,
        ChipIndex           = 0x13,
        NpcIndex            = 0x1E6,
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
        Unknown3            = 262163,
        ChipIndex           = 0x13,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 86360,
        Z                   = 200,
        Y                   = -52990,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 21,
        ChipIndex           = 0x15,
        NpcIndex            = 0x1D5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 30310,
        Z                   = 200,
        Y                   = -53530,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 22,
        ChipIndex           = 0x16,
        NpcIndex            = 0x1D5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 135100,
        Z                   = 0,
        Y                   = 9440,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 23,
        ChipIndex           = 0x17,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 134700,
        Z                   = 700,
        Y                   = 10040,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 327699,
        ChipIndex           = 0x13,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 135400,
        Z                   = 700,
        Y                   = 10100,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1835032,
        ChipIndex           = 0x18,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 29400,
        Z                   = 500,
        Y                   = -53300,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1900568,
        ChipIndex           = 0x18,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 29400,
        Z                   = 500,
        Y                   = -53900,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1900568,
        ChipIndex           = 0x18,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 29000,
        Z                   = 500,
        Y                   = -53600,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1900568,
        ChipIndex           = 0x18,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclActor(
        TriggerX            = 139320,
        TriggerZ            = 0,
        TriggerY            = 7540,
        TriggerRange        = 400,
        ActorX              = 141250,
        ActorZ              = 1500,
        ActorY              = 7610,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 10,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_496",          # 00, 0
        "Function_1_6F5",          # 01, 1
        "Function_2_790",          # 02, 2
        "Function_3_90D",          # 03, 3
        "Function_4_D3E",          # 04, 4
        "Function_5_FA5",          # 05, 5
        "Function_6_12AA",         # 06, 6
        "Function_7_17A4",         # 07, 7
        "Function_8_1B3F",         # 08, 8
        "Function_9_1D93",         # 09, 9
        "Function_10_1DCF",        # 0A, 10
        "Function_11_1DD4",        # 0B, 11
        "Function_12_2025",        # 0C, 12
        "Function_13_2A4B",        # 0D, 13
        "Function_14_3FFA",        # 0E, 14
        "Function_15_4055",        # 0F, 15
        "Function_16_5B01",        # 10, 16
        "Function_17_68FF",        # 11, 17
        "Function_18_6AA1",        # 12, 18
        "Function_19_6AA8",        # 13, 19
        "Function_20_6B62",        # 14, 20
    )


    def Function_0_496(): pass

    label("Function_0_496")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCE, 0)), scpexpr(EXPR_END)), "loc_4A1")
    Event(0, 18)

    label("loc_4A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_4B8")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x54), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x3FA)
    Event(0, 13)

    label("loc_4B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 3)), scpexpr(EXPR_END)), "loc_4CF")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x54), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x3FB)
    Event(0, 16)

    label("loc_4CF")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (106, "loc_4DF"),
        (108, "loc_4F5"),
        (SWITCH_DEFAULT, "loc_508"),
    )


    label("loc_4DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4F2")
    OP_A2(0x646)
    Event(0, 15)

    label("loc_4F2")

    Jump("loc_508")

    label("loc_4F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCE, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_505")
    Event(0, 17)

    label("loc_505")

    Jump("loc_508")

    label("loc_508")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_52A")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 38190, 200, -58050, 90)

    label("loc_52A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_554")
    SetChrChipByIndex(0x0, 2)
    SetChrChipByIndex(0x1, 3)
    SetChrChipByIndex(0x138, 4)
    SetChrFlags(0x0, 0x1000)
    SetChrFlags(0x1, 0x1000)
    SetChrFlags(0x138, 0x1000)

    label("loc_554")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 7)), scpexpr(EXPR_END)), "loc_638")
    ClearChrFlags(0xC, 0x80)
    OP_44(0xC, 0xFF)
    SetChrFlags(0xC, 0x4)
    SetChrChipByIndex(0xC, 18)
    SetChrPos(0xC, 30760, 200, 53020, 270)
    SetChrPos(0x17, 29800, 500, 53440, 0)
    ClearChrFlags(0x17, 0x80)
    SetChrPos(0x12, 29750, 500, 53150, 0)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x13, 29750, 500, 52650, 0)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x14, 29300, 500, 53440, 0)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x15, 29300, 500, 52920, 0)
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0x16, 29300, 500, 52420, 0)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x1F, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x19, 0x80)
    Jump("loc_6F4")

    label("loc_638")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_65D")
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 37840, 0, -58890, 90)
    Jump("loc_6F4")

    label("loc_65D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 6)), scpexpr(EXPR_END)), "loc_66C")
    SetChrFlags(0xD, 0x80)
    Jump("loc_6F4")

    label("loc_66C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 2)), scpexpr(EXPR_END)), "loc_69D")
    SetChrFlags(0xD, 0x80)
    SetChrChipByIndex(0x8, 16)
    OP_43(0x8, 0x0, 0x0, 0x2)
    SetChrPos(0x8, 37860, 0, -59000, 90)
    ClearChrFlags(0x8, 0x80)
    Jump("loc_6F4")

    label("loc_69D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 0)), scpexpr(EXPR_END)), "loc_6C9")
    SetChrChipByIndex(0x8, 16)
    OP_43(0x8, 0x0, 0x0, 0x2)
    SetChrPos(0x8, 37860, 0, -59000, 90)
    ClearChrFlags(0x8, 0x80)
    Jump("loc_6F4")

    label("loc_6C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 1)), scpexpr(EXPR_END)), "loc_6F4")
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x4)
    SetChrFlags(0x8, 0x10)
    OP_44(0x8, 0xFF)
    SetChrPos(0x8, 30330, 250, -53540, 270)

    label("loc_6F4")

    Return()

    # Function_0_496 end

    def Function_1_6F5(): pass

    label("Function_1_6F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCE, 0)), scpexpr(EXPR_END)), "loc_711")
    SetMapFlags(0x2000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x4A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 18)
    Jump("loc_739")

    label("loc_711")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 7)), scpexpr(EXPR_END)), "loc_729")
    SetMapFlags(0x2000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x54), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_739")

    label("loc_729")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 4)), scpexpr(EXPR_END)), "loc_739")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x54), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_739")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 7)), scpexpr(EXPR_END)), "loc_745")
    OP_1B(0x0, 0x0, 0x13)

    label("loc_745")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 7)), scpexpr(EXPR_END)), "loc_74F")
    Jump("loc_786")

    label("loc_74F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_759")
    Jump("loc_786")

    label("loc_759")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 6)), scpexpr(EXPR_END)), "loc_767")
    OP_64(0x0, 0x1)
    Jump("loc_786")

    label("loc_767")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 2)), scpexpr(EXPR_END)), "loc_775")
    OP_64(0x0, 0x1)
    Jump("loc_786")

    label("loc_775")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 0)), scpexpr(EXPR_END)), "loc_77F")
    Jump("loc_786")

    label("loc_77F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 1)), scpexpr(EXPR_END)), "loc_786")

    label("loc_786")

    OP_4F(0x2B, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_1_6F5 end

    def Function_2_790(): pass

    label("Function_2_790")

    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7B5")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_8F7")

    label("loc_7B5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7CE")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_8F7")

    label("loc_7CE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7E7")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_8F7")

    label("loc_7E7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_800")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_8F7")

    label("loc_800")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_819")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_8F7")

    label("loc_819")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_832")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_8F7")

    label("loc_832")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_84B")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_8F7")

    label("loc_84B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_864")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_8F7")

    label("loc_864")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_87D")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_8F7")

    label("loc_87D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_896")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_8F7")

    label("loc_896")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8AF")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_8F7")

    label("loc_8AF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8C8")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_8F7")

    label("loc_8C8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8E1")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_8F7")

    label("loc_8E1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8F7")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_8F7")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_90C")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_8F7")

    label("loc_90C")

    Return()

    # Function_2_790 end

    def Function_3_90D(): pass

    label("Function_3_90D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CB6")
    OP_A2(0x5)

    ChrTalk(    #0
        0x10,
        (
            "#102FI've successfully recovered that\x01",
            "'Gospel' thing Colonel Richard\x01",
            "was using.\x02\x03",

            "After the investigation of the sealed area is\x01",
            "complete and I've returned to Zeiss, I'll have\x01",
            "to run a full series of experiments on it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x101,
        (
            "#007FIt is weird, I'll give you.\x02\x03",

            "#505FIt's like, nobody knows where\x01",
            "or how it was made.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x10,
        (
            "#102FIndeed.\x02\x03",

            "If we can't determine its true form, we\x01",
            "may never learn the meaning of the events\x01",
            "that occurred in the sealed area.\x02\x03",

            "#101FMy academic instincts are tingling\x01",
            "just thinking about how important\x01",
            "an artifact this truly is!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x101,
        (
            "#006FTingling is...generally good.\x02\x03",

            "Just don't get so wrapped up in it\x01",
            "that you let yourself get kidnapped\x01",
            "again, okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x10,
        (
            "#104FOf course. I'll take every precaution.\x02\x03",

            "#100FI've even made certain the Gospel\x01",
            "itself has been placed in Cassius'\x01",
            "care.\x02\x03",

            "There is no safer place for it,\x01",
            "would you not agree?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x101,
        (
            "#506FYeah, that's about the best\x01",
            "you're gonna get...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D3A")

    label("loc_CB6")


    ChrTalk(    #6
        0x10,
        (
            "#103FI must say, this harmonica's\x01",
            "pitch is incredibly clear.\x02\x03",

            "#101FI wonder if we could somehow\x01",
            "reproduce it with orbments...?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D3A")

    TalkEnd(0xFE)
    Return()

    # Function_3_90D end

    def Function_4_D3E(): pass

    label("Function_4_D3E")

    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5A), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_D63")
    SetChrSubChip(0xFE, 1)
    Jump("loc_D94")

    label("loc_D63")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xE1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_D79")
    SetChrSubChip(0xFE, 2)
    Jump("loc_D94")

    label("loc_D79")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_D8F")
    SetChrSubChip(0xFE, 0)
    Jump("loc_D94")

    label("loc_D8F")

    SetChrSubChip(0xFE, 1)

    label("loc_D94")

    OP_8C(0xFE, 90, 0)
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F59")
    OP_A2(0x4)

    ChrTalk(    #7
        0xF,
        (
            "#560FThat sound is so pretty...\x01",
            "Who's playing it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x101,
        (
            "#501FOh yeah, he's never played harmonica\x01",
            "for you before, has he?\x02\x03",

            "That's Joshua.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xF,
        (
            "#064FJoshua?!\x02\x03",

            "#061FI didn't know he could play\x01",
            "the harmonica...\x02\x03",

            "He's good!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x101,
        "#006FYeah, he's all right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xF,
        (
            "#067FI'm too clumsy to play any kind\x01",
            "of instrument, myself.\x02\x03",

            "He's lucky to have that kind of\x01",
            "talent!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x101,
        (
            "#506F(Sheesh... If Tita's clumsy,\x01",
            "what does that make me?!)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F9C")

    label("loc_F59")


    ChrTalk(    #13
        0xF,
        (
            "#061FI didn't know he could play\x01",
            "the harmonica...\x02\x03",

            "He's good!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F9C")

    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)
    Return()

    # Function_4_D3E end

    def Function_5_FA5(): pass

    label("Function_5_FA5")

    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5A), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_FCA")
    SetChrSubChip(0xFE, 2)
    Jump("loc_FFB")

    label("loc_FCA")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xE1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_FE0")
    SetChrSubChip(0xFE, 1)
    Jump("loc_FFB")

    label("loc_FE0")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_FF6")
    SetChrSubChip(0xFE, 0)
    Jump("loc_FFB")

    label("loc_FF6")

    SetChrSubChip(0xFE, 2)

    label("loc_FFB")

    OP_8C(0xFE, 270, 0)
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1235")
    OP_A2(0x8)

    ChrTalk(    #14
        0x18,
        (
            "#053FThat music...takes me back.\x02\x03",

            "I feel as if I heard it back\x01",
            "when I was a kid...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x101,
        (
            "#000FReally? But, you're originally\x01",
            "from Ravennue Village, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x18,
        "#552F...Yeah.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0xF,
        (
            "#061FHeh heh, Agate has a little\x01",
            "sister there.\x02\x03",

            "Her name's Mischa.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x18,
        "#055FHey...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x101,
        "#004FNo way! You've got a sister?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x18,
        (
            "#551FYeah, I've got a sister! So what?\x02\x03",

            "#552FI ain't brother of the year or\x01",
            "anything like that, if that's\x01",
            "what you're implying.\x02\x03",

            "#051FI pretty much never go home. But...\x01",
            "I guess maybe when I get some time\x01",
            "I can drop by for a visit.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12A1")

    label("loc_1235")


    ChrTalk(    #21
        0x18,
        (
            "#051FI pretty much never go home. But...\x01",
            "I guess maybe when I get some time\x01",
            "I can drop by for a visit.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12A1")

    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)
    Return()

    # Function_5_FA5 end

    def Function_6_12AA(): pass

    label("Function_6_12AA")

    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5A), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_12CF")
    SetChrSubChip(0xFE, 2)
    Jump("loc_1300")

    label("loc_12CF")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xE1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_12E5")
    SetChrSubChip(0xFE, 1)
    Jump("loc_1300")

    label("loc_12E5")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_12FB")
    SetChrSubChip(0xFE, 0)
    Jump("loc_1300")

    label("loc_12FB")

    SetChrSubChip(0xFE, 2)

    label("loc_1300")

    OP_8C(0xFE, 270, 0)
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1747")
    OP_A2(0x7)

    ChrTalk(    #22
        0x19,
        (
            "#070FAh, Estelle. Hello.\x02\x03",

            "It seems Master Cassius is still\x01",
            "in conference, no?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x101,
        (
            "#505FYeah, seems that way.\x02\x03",

            "2nd Lieutenant Lorence and Captain\x01",
            "Amalthea are still on the run, after\x01",
            "all...\x02\x03",

            "Re-organizing the military chain of command will\x01",
            "probably take him a good long while...and that's\x01",
            "just ONE thing he's gotta deal with.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x19,
        (
            "#073FPity. I was going to invite him\x01",
            "for a drink.\x02\x03",

            "#075FBut I'm certain the master will put every\x01",
            "effort into catching them. I have complete\x01",
            "faith in his abilities.\x02\x03",

            "Still...to think that Lorence was going\x01",
            "easy on us during the Martial Arts\x01",
            "Competition... If he hadn't been...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x101,
        (
            "#007FYeah, when he fought the second time, it was\x01",
            "like someone had flipped a switch...except\x01",
            "instead of on-off, it was strong-CRAZYstrong.\x02\x03",

            "#002FI mean, I know he used to be a\x01",
            "jaeger, but are all jaegers as\x01",
            "strong as he is?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x19,
        (
            "#072FWell, he is experienced, at least.\x01",
            "And any soldier with his experience\x01",
            "is sure to be quite powerful.\x02\x03",

            "But his power...is beyond words.\x02\x03",

            "#074FFacing him is like going off to\x01",
            "be slaughtered. It's suicide.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x101,
        "#003F...\x02",
    )

    CloseMessageWindow()
    Jump("loc_179B")

    label("loc_1747")


    ChrTalk(    #28
        0x19,
        (
            "#070FWhat a beautiful melody.\x02\x03",

            "Complements the evening's spirits\x01",
            "quite nicely.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_179B")

    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)
    Return()

    # Function_6_12AA end

    def Function_7_17A4(): pass

    label("Function_7_17A4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1AB1")
    OP_A2(0x6)

    ChrTalk(    #29
        0x1A,
        (
            "#033FOh-ho, 'tis young Joshua's\x01",
            "performance, is it not?\x02\x03",

            "#031FI heard him play by the lake, but this...this is\x01",
            "not mere playing, it's the weaving of melody; the\x01",
            "chisel of a sculptor or brush of a painter!\x02\x03",

            "He's been practicing, I surmise.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x101,
        (
            "#006FHe did play a lot when he was a kid.\x02\x03",

            "He played other songs, but this\x01",
            "was the one he'd always come\x01",
            "back to.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x1A,
        (
            "#030FWas it, now...?\x02\x03",

            "It's quite a surprise to hear\x01",
            "Joshua play such a delicately\x01",
            "beautiful yet obscure song.\x02\x03",

            "There are few enough Imperials\x01",
            "who still remember it, much less\x01",
            "Liberlians!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x101,
        "#004FWait, so it's...an Erebonian song?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x1A,
        (
            "#033FIndeed. 'The Whereabouts of Light.'\x02\x03",

            "#035FA very old Erebonian melody.\x02\x03",

            "A perennial favorite of the\x01",
            "country folk, in fact.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x101,
        "#505FWow. I had no idea...\x02",
    )

    CloseMessageWindow()
    Jump("loc_1B3B")

    label("loc_1AB1")


    ChrTalk(    #35
        0x1A,
        (
            "#037FI must hand it to that boy.\x02\x03",

            "Only he could utilize such a sad and\x01",
            "delicate melody to melt my heart...\x01",
            "instead of shattering it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B3B")

    TalkEnd(0xFE)
    Return()

    # Function_7_17A4 end

    def Function_8_1B3F(): pass

    label("Function_8_1B3F")

    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5A), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1B64")
    SetChrSubChip(0xFE, 2)
    Jump("loc_1B95")

    label("loc_1B64")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xE1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1B7A")
    SetChrSubChip(0xFE, 1)
    Jump("loc_1B95")

    label("loc_1B7A")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1B90")
    SetChrSubChip(0xFE, 0)
    Jump("loc_1B95")

    label("loc_1B90")

    SetChrSubChip(0xFE, 2)

    label("loc_1B95")

    OP_8C(0xFE, 270, 0)
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D0F")
    OP_A2(0x3)

    ChrTalk(    #36
        0xC,
        (
            "#021FHey...isn't that Joshua playing\x01",
            "the harmonica?\x02\x03",

            "If we can hear it from here...\x01",
            "then he must be playing in the\x01",
            "Garden Terrace!\x02\x03",

            "#027FNow's your chance. Better get\x01",
            "up there to him now, while the\x01",
            "situation is just right!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x101,
        (
            "#503FYeah, I'd better...\x02\x03",

            "#509F...better NOT! This is so not\x01",
            "the time for that, Schera!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xC,
        "#025FAwww, you're no fun.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1D8A")

    label("loc_1D0F")


    ChrTalk(    #39
        0xC,
        (
            "#020FGo on, get up there!\x02\x03",

            "Now's your chance to have some\x01",
            "'alone' time with him. Get to\x01",
            "'know' him a little better...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D8A")

    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)
    Return()

    # Function_8_1B3F end

    def Function_9_1D93(): pass

    label("Function_9_1D93")

    TalkBegin(0xFE)

    ChrTalk(    #40
        0xFE,
        (
            "This is Professor Russell and\x01",
            "Miss Tita's room.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_9_1D93 end

    def Function_10_1DCF(): pass

    label("Function_10_1DCF")

    Call(0, 11)
    Return()

    # Function_10_1DCF end

    def Function_11_1DD4(): pass

    label("Function_11_1DD4")

    TalkBegin(0xD)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 7)), scpexpr(EXPR_END)), "loc_1DF9")

    ChrTalk(    #41
        0xD,
        "By yourself today?\x02",
    )

    CloseMessageWindow()
    Jump("loc_2021")

    label("loc_1DF9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_1F0B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1E5D")

    ChrTalk(    #42
        0xD,
        "Colonel Richard...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xD,
        (
            "I still can't believe he'd rebel\x01",
            "against Her Majesty.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F08")

    label("loc_1E5D")

    OP_A2(0x0)

    ChrTalk(    #44
        0xD,
        (
            "Colonel Richard visited me every evening...\x01",
            "and we would talk for hours, about anything\x01",
            "and everything.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xD,
        (
            "I still can't believe he'd rebel\x01",
            "against Her Majesty.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F08")

    Jump("loc_2021")

    label("loc_1F0B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 6)), scpexpr(EXPR_END)), "loc_1F15")
    Jump("loc_2021")

    label("loc_1F15")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 2)), scpexpr(EXPR_END)), "loc_1F1F")
    Jump("loc_2021")

    label("loc_1F1F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 0)), scpexpr(EXPR_END)), "loc_1F8F")

    ChrTalk(    #46
        0xD,
        (
            "Would you like an after-dinner\x01",
            "drink?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0xD,
        (
            "We can make anything you'd \x01",
            "like, on or off the menu.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2021")

    label("loc_1F8F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 1)), scpexpr(EXPR_END)), "loc_2021")

    ChrTalk(    #48
        0xD,
        (
            "This is a place to talk. Please,\x01",
            "come right in.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0xD,
        (
            "For drinks, we have anything you\x01",
            "can think of, be it alcoholic or\x01",
            "non-alcoholic.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2021")

    TalkEnd(0xD)
    Return()

    # Function_11_1DD4 end

    def Function_12_2025(): pass

    label("Function_12_2025")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2596")
    OP_A2(0x63C)
    EventBegin(0x0)
    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x101, 29590, 0, -55060, 0)
    SetChrPos(0x102, 28580, 0, -55120, 45)
    OP_6D(29870, 0, -54070, 0)
    SetChrSubChip(0xFE, 1)
    OP_0D()

    ChrTalk(    #50
        0x8,
        "#802FEstelle! Joshua!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x101,
        (
            "#006FMr. Murdock! I thought you might\x01",
            "be here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x102,
        (
            "#6P#010FWith mayoral-class individuals on\x01",
            "the guest list, we had a feeling\x01",
            "you might also be in attendance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x8,
        (
            "#801FI must say I never expected you two to\x01",
            "win a tournament championship and end\x01",
            "up hobnobbing in Grancel Castle.\x02\x03",

            "Cassius' kids to the bone, you are!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x101,
        (
            "#008FHeh. It took more than our up-\x01",
            "bringing to get here. Lots of\x01",
            "people helped along the way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x102,
        (
            "#6P#012FSo it's been a few days... Have\x01",
            "there been any developments?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x8,
        (
            "#800FWell...right after you left for the \x01",
            "capital, Captain Amalthea from the\x01",
            "Intelligence Division came knocking.\x02\x03",

            "She forced me to come to this \x01",
            "banquet, but I kept my mouth\x01",
            "shut about Leiston Fortress.\x02\x03",

            "Professor Russell and company are\x01",
            "still on the run, too. Army hasn't\x01",
            "found 'em yet.\x02\x03",

            "#803FBut the longer we keep this up,\x01",
            "the less chance they have. It's\x01",
            "really only a matter of time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x101,
        "#003FHmmm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x8,
        (
            "#800FI asked Captain Amalthea if I could\x01",
            "see Her Majesty and wish her well,\x01",
            "but no luck. I was flat-out refused.\x02\x03",

            "So in other words, we definitely\x01",
            "aren't gonna be able to do this\x01",
            "the easy way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x101,
        (
            "#007FWe sure aren't...but don't you\x01",
            "worry, because we've totally\x01",
            "got that covered!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x102,
        (
            "#6P#012FWe WILL get the professor's message\x01",
            "to Her Majesty, one way or another.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0)
    EventEnd(0x0)
    Jump("loc_2A4A")

    label("loc_2596")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 7)), scpexpr(EXPR_END)), "loc_26B7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCE, 0)), scpexpr(EXPR_END)), "loc_2614")

    ChrTalk(    #61
        0x8,
        (
            "#800FStill seems busy out there.\x02\x03",

            "Since I'm here, I think I'll\x01",
            "go tie one on before I take\x01",
            "my leave.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_26B4")

    label("loc_2614")


    ChrTalk(    #62
        0x8,
        (
            "#800FNeither Professor Russell nor myself\x01",
            "can go for long without spending some\x01",
            "time at the factory.\x02\x03",

            "I'm going to catch the Linde\x01",
            "back to Zeiss tomorrow.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_26B4")

    Jump("loc_2A47")

    label("loc_26B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_26C1")
    Jump("loc_2A47")

    label("loc_26C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 6)), scpexpr(EXPR_END)), "loc_26CB")
    Jump("loc_2A47")

    label("loc_26CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 2)), scpexpr(EXPR_END)), "loc_292A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xDF, 1)), scpexpr(EXPR_END)), "loc_2740")

    ChrTalk(    #63
        0x8,
        (
            "#800FI'm glad to hear Her Majesty is\x01",
            "on the mend.\x02\x03",

            "That alone makes the whole trip\x01",
            "worthwhile.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2927")

    label("loc_2740")

    OP_A2(0x6F9)

    ChrTalk(    #64
        0x8,
        "#800FMadam Hilda. You look well.\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #65
        0x0,
        "Head Maid Hilda",
        (
            "#711FAs do you, Mr. Murdock.\x02\x03",

            "Though busy as ever, it seems!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x8,
        (
            "#801FYes, but it's hardly work at all when\x01",
            "the central factory is so full of\x01",
            "bright minds.\x02\x03",

            "#800FI'm glad to hear Her Majesty is\x01",
            "on the mend.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #67
        0x0,
        "Head Maid Hilda",
        (
            "#710FIndeed. I'm sure we'll all be\x01",
            "able to see her again soon.\x02\x03",

            "If there is anything you need\x01",
            "in your room, please feel free\x01",
            "to let me know.\x02\x03",

            "I'll bring it right away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x8,
        "#800FThank you, Hilda.\x02",
    )

    CloseMessageWindow()

    label("loc_2927")

    Jump("loc_2A47")

    label("loc_292A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 0)), scpexpr(EXPR_END)), "loc_2973")

    ChrTalk(    #69
        0x8,
        (
            "#800FEstelle! Joshua!\x02\x03",

            "So, have you met with Her Majesty?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A47")

    label("loc_2973")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 1)), scpexpr(EXPR_END)), "loc_2A47")
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5A), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_299C")
    SetChrSubChip(0xFE, 2)
    Jump("loc_29CD")

    label("loc_299C")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xE1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_29B2")
    SetChrSubChip(0xFE, 1)
    Jump("loc_29CD")

    label("loc_29B2")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_29C8")
    SetChrSubChip(0xFE, 0)
    Jump("loc_29CD")

    label("loc_29C8")

    SetChrSubChip(0xFE, 2)

    label("loc_29CD")

    OP_8C(0xFE, 270, 0)
    SetChrFlags(0xFE, 0x10)

    ChrTalk(    #70
        0x8,
        (
            "#800FThe Intelligence Division has\x01",
            "eyes everywhere.\x02\x03",

            "We'll have to be more subtle\x01",
            "in our movements.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0)

    label("loc_2A47")

    TalkEnd(0xFE)

    label("loc_2A4A")

    Return()

    # Function_12_2025 end

    def Function_13_2A4B(): pass

    label("Function_13_2A4B")

    EventBegin(0x0)
    OP_6D(132620, 4000, -1250, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    SetChrFlags(0x9, 0x4)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrChipByIndex(0x9, 13)
    SetChrChipByIndex(0x101, 14)
    SetChrChipByIndex(0x102, 15)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 149100, 4200, 7600, 270)
    SetChrPos(0x102, 146580, 4200, 8100, 90)
    SetChrPos(0x101, 146580, 4200, 7130, 90)
    FadeToBright(1500, 0)
    OP_6D(147760, 4000, 7560, 5000)
    Fade(1000)
    OP_6D(148910, 4000, 7610, 0)
    OP_67(0, 5740, -10000, 0)
    OP_6B(1090, 0)
    OP_6C(88000, 0)
    OP_6E(699, 0)
    OP_0D()

    ChrTalk(    #71
        0x9,
        (
            "#110F...I met Cassius shortly after I graduated\x01",
            "from the military academy.\x02\x03",

            "I was assigned to a mobile unit that was under\x01",
            "his command.\x02\x03",

            "And since that time, I have found myself in his\x01",
            "debt again and again, both personally and\x01",
            "professionally.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x101,
        (
            "#506FUh...he did...?\x02\x03",

            "#501FAnd, uh...what did you think\x01",
            "of him at the time?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x9,
        (
            "#115FTo put it simply, he was a hero.\x02\x03",

            "And a master swordsman, to boot.\x02\x03",

            "No matter the scenario, he could find\x01",
            "a way to handle any number of battle-\x01",
            "fronts in every direction...\x02\x03",

            "It wasn't just a matter of sheer\x01",
            "tactics... He understood and could\x01",
            "direct high-level strategy, as well.\x02\x03",

            "#110FQuite simply, he was a\x01",
            "man without peer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x101,
        (
            "#509FIf I didn't know better, I'd\x01",
            "say we were talking about two\x01",
            "different people.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x102,
        (
            "#010FSo you were with our father\x01",
            "during the Hundred Days War?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x9,
        (
            "#116FYes...\x01",
            "He was my C.O.\x02\x03",

            "Even now, I can still vividly remember the\x01",
            "excitement that filled me as we executed his plan\x01",
            "that turned the war's tide...\x02\x03",

            "#115FAny time I get to talking about\x01",
            "those days, time just runs away\x01",
            "with me...\x02\x03",

            "But this much I can tell you:\x02\x03",

            "#112FIf Cassius Bright had not been part\x01",
            "of the Royal Army, Liberl would now\x01",
            "be part of the Erebonian Empire.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0x101,
        (
            "#004FN-No way!\x02\x03",

            "That's kinda hard to believe...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0x9,
        (
            "#110FHa ha... Well, as a hero, he had\x01",
            "a knack for doing unbelievable\x01",
            "things.\x02\x03",

            "He left the army immediately after the war,\x01",
            "declining even a medal from the queen, so few\x01",
            "know of his achievements...\x02\x03",

            "But inside the army, many soldiers still hold\x01",
            "him up as the prime example of what a hero\x01",
            "should be.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x101,
        (
            "#009FUhh...\x02\x03",

            "#582FHe never said one word\x01",
            "about any of this to me!\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x102, 2)

    ChrTalk(    #80
        0x102,
        (
            "#010FWell, it's not really the kind of\x01",
            "thing you tell your daughter about.\x02\x03",

            "It's not fair to criticize him for that.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 1)

    ChrTalk(    #81
        0x101,
        (
            "#005FHey, whose side are you on?!\x02\x03",

            "#509FAnd besides, why doesn't any of\x01",
            "this shock you like it shocks me?\x02\x03",

            "Did you already know about all\x01",
            "of this or something?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0x102,
        (
            "#014FWell, I didn't know that he was\x01",
            "Colonel Richard's superior officer...\x02\x03",

            "#015FThe rest I knew about...vaguely.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0x101,
        (
            "#005F'Vaguely'?!\x02\x03",

            "You're an accomplice?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0x102,
        (
            "#019FH-Hey, calm down...\x02\x03",

            "It's not like he TOLD me any\x01",
            "of it. I just...figured a lot\x01",
            "of it out.\x02\x03",

            "He told me he didn't feel it was something\x01",
            "worth going out of his way to tell others about.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0x101,
        (
            "#509FGrrr... I just don't get it.\x02\x03",

            "#582FWhen he comes back,\x01",
            "he is SO in trouble!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0x9,
        "#110FHa ha...\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x102, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)
    SetChrSubChip(0x102, 0)
    SetChrSubChip(0x101, 0)

    ChrTalk(    #87
        0x101,
        "#503FErr... I...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0x102,
        (
            "#017FPlease excuse us.\x01",
            "We didn't mean to interrupt.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0x9,
        (
            "#115FNo, no. Seeing you like this\x01",
            "is actually a bit of a relief.\x02\x03",

            "When I found out that your father was intending\x01",
            "to leave the military, I desperately tried to\x01",
            "stop him...\x02\x03",

            "But it seems that by leaving, he did what was\x01",
            "best for himself, after all.\x02\x03",

            "#110FAfter losing his dear wife, maybe\x01",
            "being with you was all that could\x01",
            "help him recover.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0x101,
        "#004FColonel Richard...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0x102,
        "#012F...\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(1000)
    OP_6D(147760, 4000, 7560, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    SetChrPos(0x9, 148530, 4000, 6210, 270)
    ClearChrFlags(0x9, 0x800)
    SetChrChipByIndex(0x9, 1)
    SetChrSubChip(0x102, 2)
    OP_0D()

    ChrTalk(    #92
        0x9,
        (
            "#111F#4PNow, then... I thank you for\x01",
            "taking the time to come here.\x02\x03",

            "I really can't keep the duke\x01",
            "waiting, so I'm afraid you'll\x01",
            "have to excuse me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0x101,
        "#004FOh...all right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0x102,
        (
            "#010FOur apologies for making\x01",
            "you so late.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0x9,
        (
            "#110F#4PNot at all. You both have told\x01",
            "me the one thing I wanted most\x01",
            "to know.\x02\x03",

            "#115FAnd thus, I have no regrets.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0x101,
        "#004FHuh...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0x102,
        "#012FHow's that again?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0x9,
        (
            "#111F#4PHa ha... I'm sure we'll have a\x01",
            "chance to speak again soon.\x02\x03",

            "Cassius might even be with us\x01",
            "then, to share in the stories.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x9, 180, 400)
    OP_62(0x101, 0x0, 2300, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x102, 0x0, 2300, 0x18, 0x1B, 0xFA, 0x0)

    def lambda_3943():
        OP_6D(146770, 2000, -760, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3943)
    OP_43(0x9, 0x1, 0x0, 0xE)
    SetChrSubChip(0x101, 2)
    WaitChrThread(0x101, 0x2)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_63(0x101)
    OP_63(0x102)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0x102, 65535)
    SetChrSubChip(0x101, 0)
    SetChrSubChip(0x102, 0)
    SetChrPos(0x102, 146580, 4000, 8100, 90)
    SetChrPos(0x101, 146580, 4000, 7130, 90)

    def lambda_39B0():
        OP_8E(0xFE, 0x24068, 0xFA0, 0x14B4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_39B0)
    Sleep(300)

    def lambda_39D0():
        OP_8E(0xFE, 0x24414, 0xFA0, 0x14B4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_39D0)
    WaitChrThread(0x101, 0x1)

    def lambda_39F0():
        OP_6D(148490, 4000, 5300, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_39F0)
    OP_8C(0x101, 225, 400)
    WaitChrThread(0x102, 0x1)
    OP_8C(0x102, 225, 400)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x102, 0x4)
    WaitChrThread(0x101, 0x2)

    ChrTalk(    #99
        0x101,
        (
            "#505F#6PUmm...\x02\x03",

            "Okay, who was that man, and what\x01",
            "has he done with Colonel Richard?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #100
        0x102,
        "#017F#4PWhat are you babbling about now?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #101
        0x101,
        (
            "#003F#6PIt's just that it's weird to hear\x01",
            "him talking about Dad that way.\x02\x03",

            "I wasn't expecting him to be\x01",
            "so...well, nice.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0x102,
        (
            "#015F#4PTrue. He doesn't seem all that\x01",
            "villainous, anyway.\x02\x03",

            "#012FEven so, it's pretty much a\x01",
            "foregone conclusion that he's\x01",
            "got something up his sleeve.\x02\x03",

            "For now, we should probably put the issue of Dad\x01",
            "aside.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0x101,
        "#007F#6PYeah, I guess you're right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0x102,
        (
            "#015F#4PAnd I hate to say it...\x02\x03",

            "...but I think that he might've been\x01",
            "playing nice, just because he could\x01",
            "get something out of it.\x02\x03",

            "#012FHe's an intelligence officer, so he\x01",
            "probably thinks that fooling a couple\x01",
            "of kids is as easy as could be.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0x101,
        (
            "#009F#6PD-Don't you think that's going\x01",
            "a little too far?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0x102,
        (
            "#015F#4PYou might be right.\x02\x03",

            "Let me be the one who's mistrustful of others.\x02\x03",

            "You should just follow your instincts and\x01",
            "believe whatever you think is right.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0x101,
        "#004F#6PHuh...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0x102,
        (
            "#012F#4PBut just make sure you're prepared for anything.\x01",
            "Don't let your guard down.\x02\x03",

            "I'd say a bracer's job...is pretty\x01",
            "much that, in fact.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0x101,
        (
            "#500F#6P...\x02\x03",

            "#006FOkay, I got it.\x02\x03",

            "I'll keep it in mind.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0x102,
        "#010F#4PThank you, Estelle...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0x101,
        (
            "#506F#6P'Thank you'? What the heck\x01",
            "are you thanking me for?!\x02\x03",

            "#006FAnyway, we need to go\x01",
            "back and see Hilda.\x02\x03",

            "She's probably sick of waiting for us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0x102,
        (
            "#010F#4PYeah. She should be in the\x01",
            "maid quarters.\x02",
        )
    )

    CloseMessageWindow()
    OP_20(0x3E8)
    OP_A2(0x641)
    EventEnd(0x0)
    OP_1D(0x11)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x11), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_13_2A4B end

    def Function_14_3FFA(): pass

    label("Function_14_3FFA")

    OP_8E(0xFE, 0x241E4, 0xFA0, 0xED8, 0xBB8, 0x0)
    ClearChrFlags(0x9, 0x4)
    OP_8E(0xFE, 0x241D0, 0x7D0, 0xFFFFFA24, 0xBB8, 0x0)
    OP_8E(0xFE, 0x22632, 0x0, 0xFFFFFA24, 0xBB8, 0x0)
    OP_8E(0xFE, 0x20666, 0x0, 0x320, 0xBB8, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_14_3FFA end

    def Function_15_4055(): pass

    label("Function_15_4055")

    EventBegin(0x0)
    OP_6D(88650, 0, 6240, 0)
    OP_67(0, 5460, -10000, 0)
    OP_6B(1940, 0)
    OP_6C(46000, 0)
    OP_6E(474, 0)
    SetChrChipByIndex(0x101, 3)
    SetChrChipByIndex(0x102, 4)
    SetChrChipByIndex(0x138, 2)
    SetChrPos(0x138, 87950, 0, 4590, 0)
    SetChrPos(0x101, 87640, 0, 6230, 90)
    SetChrPos(0x102, 89210, 0, 6370, 270)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #113
        0x101,
        (
            "#327F*sigh* Well, aren't you\x01",
            "Mr. Popularity.\x02\x03",

            "It was like their eyes all changed\x01",
            "when you told them your name.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0x102,
        (
            "#337F#4PH-Hey, it was not.\x02\x03",

            "I didn't see YOU shying away from\x01",
            "joining in the conversation...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0x101,
        (
            "#473FSure, but that doesn't mean\x01",
            "I wasn't nervous.\x02\x03",

            "#327FUgh... I kind of lost all my\x01",
            "confidence there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0x102,
        "#332F#4PEh...?\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 93780, 0, 850, 90)
    SetChrPos(0xB, 93780, 0, 850, 90)
    OP_72(0x24, 0x10)
    OP_6F(0x24, 0)
    OP_70(0x24, 0x3C)
    OP_73(0x24)

    NpcTalk(    #117
        0xA,
        "Man's Voice",
        (
            "*hic*\x01",
            "What's all the noise about...?\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0xA, 0x40)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x138, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    def lambda_42FA():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_42FA)

    def lambda_4308():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4308)

    def lambda_4316():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x138, 1, lambda_4316)
    OP_6D(90380, 0, 5100, 1000)

    def lambda_4335():

        label("loc_4335")

        TurnDirection(0xFE, 0xA, 0)
        OP_48()
        Jump("loc_4335")

    QueueWorkItem2(0x101, 1, lambda_4335)

    def lambda_4346():

        label("loc_4346")

        TurnDirection(0xFE, 0xA, 0)
        OP_48()
        Jump("loc_4346")

    QueueWorkItem2(0x102, 1, lambda_4346)

    def lambda_4357():

        label("loc_4357")

        TurnDirection(0xFE, 0xA, 0)
        OP_48()
        Jump("loc_4357")

    QueueWorkItem2(0x138, 1, lambda_4357)

    def lambda_4368():
        OP_6D(89070, 0, 5570, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_4368)

    def lambda_4380():
        OP_8E(0xFE, 0x1630A, 0x0, 0x636, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_4380)
    WaitChrThread(0xA, 0x1)
    ClearChrFlags(0xB, 0x80)

    def lambda_43A5():
        OP_8E(0xFE, 0x15D06, 0x0, 0x1158, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_43A5)
    OP_8E(0xB, 0x1658A, 0x0, 0x4BA, 0x7D0, 0x0)
    OP_72(0x24, 0x800)
    OP_22(0x7, 0x0, 0x64)
    OP_6F(0x24, 60)
    OP_70(0x24, 0x0)

    def lambda_43EC():
        OP_8E(0xFE, 0x1630A, 0x0, 0x636, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_43EC)
    WaitChrThread(0xB, 0x1)

    def lambda_440C():
        OP_8E(0xFE, 0x15EA0, 0x0, 0xDAC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_440C)
    WaitChrThread(0xA, 0x1)

    def lambda_442C():
        TurnDirection(0xFE, 0x138, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_442C)

    ChrTalk(    #118
        0x138,
        "#712FOh, Duke Dunan...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0xA,
        "#227FAhh, s'a lady of the court...\x02",
    )

    CloseMessageWindow()
    OP_62(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xA, 0x101, 400)

    ChrTalk(    #120
        0xA,
        (
            "#481FHey...you maids...\x02\x03",

            "*hic*\x01",
            "You don't look familiar...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCE, 6)), scpexpr(EXPR_END)), "loc_458F")

    ChrTalk(    #121
        0x138,
        (
            "#713FThese are two of the new hires,\x01",
            "whom I'm instructing. This is\x01",
            "Lena and that's Karin.\x02\x03",

            "They're still quite inexperienced,\x01",
            "so I'm giving them some extra\x01",
            "training time.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4705")

    label("loc_458F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCE, 7)), scpexpr(EXPR_END)), "loc_464B")

    ChrTalk(    #122
        0x138,
        (
            "#713FThese are two of the new hires,\x01",
            "whom I'm instructing. This is\x01",
            "Schera and that's Karin.\x02\x03",

            "They're still quite inexperienced,\x01",
            "so I'm giving them some extra\x01",
            "training time.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4705")

    label("loc_464B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCF, 0)), scpexpr(EXPR_END)), "loc_4705")

    ChrTalk(    #123
        0x138,
        (
            "#713FThese are two of the new hires,\x01",
            "whom I'm instructing. This is\x01",
            "Dorothy and that's Karin.\x02\x03",

            "They're still quite inexperienced,\x01",
            "so I'm giving them some extra\x01",
            "training time.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4705")

    OP_62(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(    #124
        0xB,
        "#722FHmm...?\x02",
    )

    CloseMessageWindow()
    OP_8E(0xB, 0x16044, 0x0, 0x10AE, 0x7D0, 0x0)
    OP_8E(0xB, 0x15F40, 0x0, 0x14BE, 0x7D0, 0x0)
    TurnDirection(0xB, 0x102, 400)
    Sleep(500)
    TurnDirection(0xB, 0x101, 400)
    Sleep(500)

    ChrTalk(    #125
        0xB,
        "#721F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0x101,
        "#323F#3P(Did he recognize us?)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0x102,
        (
            "#335F(...Not good.)\x02\x03",

            "(Given how many times we've\x01",
            "run into him, it'd be bizarre\x01",
            "if he DIDN'T recognize us...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0xA,
        (
            "#481FCome now, Phillip.\x01",
            "Enough with the staring.\x02\x03",

            "#229FHa ha ha... It's quite unusual to\x01",
            "see coming from you. Stiff upper\x01",
            "lip and all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0xB,
        (
            "#720FPlease, pardon my rudeness.\x02\x03",

            "You look much like my niece.\x01",
            "My eyes were playing tricks\x01",
            "on me, it seems.\x02\x03",

            "I am dreadfully sorry for\x01",
            "the discourtesy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0x101,
        "#474F#3POh, it's no bother.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0x102,
        "#331FPlease, don't concern yourself.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0xA,
        (
            "#227FYou know, now that I stop and\x01",
            "look, I must say that you both\x01",
            "are quite lovely...\x02\x03",

            "You with the brown hair...you\x01",
            "have a very healthy, clean look\x01",
            "to you.\x02",
        )
    )

    CloseMessageWindow()
    OP_9E(0x101, 0xF, 0x0, 0x12C, 0xFA0)

    ChrTalk(    #133
        0x101,
        "#476F#3P(Uuggggghhh...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0xA,
        (
            "#227FAs for you, I personally think\x01",
            "you'd look best with that raven\x01",
            "hair of yours even longer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0x102,
        "#338FI... I'm honored...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0xA,
        "#483FHm... Ah, yes.\x02",
    )

    CloseMessageWindow()
    Sleep(400)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCE, 6)), scpexpr(EXPR_END)), "loc_4B57")

    ChrTalk(    #137
        0xA,
        (
            "#482F#3SLena, was it not? You shall\x01",
            "attend to me this evening!\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    Jump("loc_4C17")

    label("loc_4B57")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCE, 7)), scpexpr(EXPR_END)), "loc_4BB8")

    ChrTalk(    #138
        0xA,
        (
            "#482F#3SSchera, was it not? You shall\x01",
            "attend to me this evening!\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    Jump("loc_4C17")

    label("loc_4BB8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCF, 0)), scpexpr(EXPR_END)), "loc_4C17")

    ChrTalk(    #139
        0xA,
        (
            "#482F#3SDorothy, was it not? You shall\x01",
            "attend to me this evening!\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    label("loc_4C17")


    ChrTalk(    #140
        0x102,
        "#332F!!!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0x101,
        "#324F#3P...Uh?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0xA, 400)

    ChrTalk(    #142
        0xB,
        "#721FY-Your Grace?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0x101,
        "#473F#3P(Eww. I don't want to serve him tea!)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0x102,
        (
            "#334F(I don't think tea is what\x01",
            "he wants served...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0x138,
        (
            "#714FYour Grace... Your flirtations,\x01",
            "while flattering, are best saved for\x01",
            "another time and place.\x02\x03",

            "All of the maids in the castle\x01",
            "work directly in service to Her\x01",
            "Majesty, Queen Alicia.\x02\x03",

            "I trust you've not forgotten?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x138, 400)

    ChrTalk(    #146
        0xA,
        (
            "#480FI know, I know... Some folks\x01",
            "simply can't appreciate a joke.\x02\x03",

            "#483F*hic* The castle will be mine\x01",
            "in a week's time, anyway...\x02\x03",

            "We can set aside time\x01",
            "for some fun then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0x138,
        "#714F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0xB,
        (
            "#723FY-Your Grace!\x01",
            "Please, no more of this!\x02\x03",

            "I do not mind when you drink to\x01",
            "excess, but you know how your\x01",
            "libido gets in such instances!\x02\x03",

            "I say this, knowing full well\x01",
            "that I may be reprimanded for i--\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0xB, 400)

    ChrTalk(    #149
        0xA,
        (
            "#482FBut I SAID I was just joking!\x02\x03",

            "Enough! I'm going to bed!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #150
        0xB,
        (
            "#722FA-As you wish, Your Grace.\x02\x03",

            "#720FYour room is right over there.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4FD2():
        OP_6D(87270, 0, 5910, 4000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_4FD2)

    def lambda_4FEA():
        OP_8E(0xFE, 0x15996, 0x0, 0x1482, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_4FEA)
    Sleep(600)

    def lambda_500A():
        OP_8E(0xFE, 0x151EE, 0x0, 0x15C2, 0x514, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_500A)
    WaitChrThread(0xA, 0x1)

    def lambda_502A():
        OP_8E(0xFE, 0x14E38, 0x0, 0x15B8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_502A)
    WaitChrThread(0xA, 0x1)
    Sleep(1000)

    def lambda_504F():

        label("loc_504F")

        TurnDirection(0xFE, 0xA, 0)
        OP_48()
        Jump("loc_504F")

    QueueWorkItem2(0xB, 2, lambda_504F)

    def lambda_5060():
        TurnDirection(0xA, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_5060)
    OP_8F(0xA, 0x14E92, 0x0, 0x18EC, 0x3E8, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCE, 6)), scpexpr(EXPR_END)), "loc_5134")

    ChrTalk(    #151
        0xA,
        (
            "#227FWhoooaaa...\x01",
            "Oh, right... Lena...?\x02\x03",

            "#483FYou just let me know if you\x01",
            "have any problems...anything\x01",
            "at all.\x02\x03",

            "I'll give you the best advice\x01",
            "the future king can give...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_52A6")

    label("loc_5134")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCE, 7)), scpexpr(EXPR_END)), "loc_51EE")

    ChrTalk(    #152
        0xA,
        (
            "#227FWhoooaaa...\x01",
            "Oh, right... Schera...?\x02\x03",

            "#483FYou just let me know if you\x01",
            "have any problems...anything\x01",
            "at all.\x02\x03",

            "I'll give you the best advice\x01",
            "the future king can give...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_52A6")

    label("loc_51EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCF, 0)), scpexpr(EXPR_END)), "loc_52A6")

    ChrTalk(    #153
        0xA,
        (
            "#227FWhoooaaa...\x01",
            "Oh, right... Dorothy...?\x02\x03",

            "#483FYou just let me know if you\x01",
            "have any problems...anything\x01",
            "at all.\x02\x03",

            "I'll give you the best advice\x01",
            "the future king can give...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_52A6")


    ChrTalk(    #154
        0x101,
        (
            "#4P#476FAh...ha ha...\x01",
            "Th-Thank you very much...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #155
        0xA,
        (
            "#229FHa ha ha...\x01",
            "Aren't you cute...\x02\x03",

            "#227FYes...good, good!\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xA, 270, 400)

    def lambda_5329():
        OP_6D(83810, 0, 6600, 4000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_5329)
    OP_8E(0xA, 0x13416, 0x0, 0x1B4E, 0x5DC, 0x0)
    OP_8E(0xA, 0x13448, 0x0, 0x1CE8, 0x5DC, 0x0)
    OP_72(0x21, 0x10)
    OP_6F(0x21, 0)
    OP_70(0x21, 0x3C)
    OP_73(0x21)
    OP_8E(0xA, 0x13416, 0x0, 0x2576, 0x5DC, 0x0)
    OP_72(0x21, 0x800)
    OP_22(0x7, 0x0, 0x64)
    OP_6F(0x21, 60)
    OP_70(0x21, 0x0)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x138, 0xFF)
    OP_44(0xA, 0xFF)
    OP_44(0xB, 0xFF)

    def lambda_53BF():

        label("loc_53BF")

        TurnDirection(0xFE, 0xB, 0)
        OP_48()
        Jump("loc_53BF")

    QueueWorkItem2(0x101, 1, lambda_53BF)

    def lambda_53D0():

        label("loc_53D0")

        TurnDirection(0xFE, 0xB, 0)
        OP_48()
        Jump("loc_53D0")

    QueueWorkItem2(0x102, 1, lambda_53D0)

    def lambda_53E1():

        label("loc_53E1")

        TurnDirection(0xFE, 0xB, 0)
        OP_48()
        Jump("loc_53E1")

    QueueWorkItem2(0x138, 1, lambda_53E1)

    def lambda_53F2():
        OP_6D(88010, 0, 6080, 1500)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_53F2)
    OP_8C(0xB, 90, 400)
    WaitChrThread(0x101, 0x3)

    ChrTalk(    #156
        0xB,
        (
            "#722FI apologize unreservedly for\x01",
            "all the...fuss.\x02\x03",

            "His Grace will likely\x01",
            "remember nothing of this,\x01",
            "come the morning.\x02\x03",

            "Please, set your minds at ease.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #157
        0x138,
        "#714FI should certainly hope so.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #158
        0xB,
        (
            "#720FI am truly sorry.\x02\x03",

            "Madam and young misses, I beg\x01",
            "your pardon, but I must take\x01",
            "my leave.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xB, 270, 400)
    OP_8E(0xB, 0x13466, 0x0, 0x1694, 0xBB8, 0x0)
    OP_8E(0xB, 0x134B6, 0x0, 0x268E, 0xBB8, 0x0)
    OP_22(0x6, 0x0, 0x64)
    Sleep(1500)
    OP_22(0x7, 0x0, 0x64)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x138, 0xFF)
    OP_44(0xA, 0xFF)
    OP_44(0xB, 0xFF)
    Sleep(1000)

    ChrTalk(    #159
        0x138,
        (
            "#716F*sigh*\x01",
            "I feel so badly for him.\x02\x03",

            "He truly seems to bear the weight\x01",
            "of the world on his shoulders.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x138, 400)

    ChrTalk(    #160
        0x101,
        (
            "#324FOh, do you know Mr. Phillip\x01",
            "personally?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x138, 0x101, 400)

    ChrTalk(    #161
        0x138,
        (
            "#715FYes, ever since we were children.\x02\x03",

            "Though not nearly as well as\x01",
            "we once did, thanks to the\x01",
            "one he serves...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x138, 400)

    ChrTalk(    #162
        0x102,
        "#330FI see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #163
        0x101,
        (
            "#327FHe sure seems like he's nervous\x01",
            "all the time, doesn't he?\x02\x03",

            "#473FI'll bet that everything between\x01",
            "the duke and the colonel has him\x01",
            "completely on edge.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #164
        0x102,
        (
            "#330FProbably, yeah...\x02\x03",

            "#338FBy the way, what was that you \x01",
            "were saying earlier about me\x01",
            "being the 'popular' one?\x02\x03",

            "The duke certainly seemed\x01",
            "awfully fond of you.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #165
        0x101,
        (
            "#476FBrrr...please. I'd like to\x01",
            "keep my food in my stomach,\x01",
            "thank you.\x02\x03",

            "#471FOh, right. Back to before. I feel like\x01",
            "I'm missing something. Why would\x01",
            "the duke want tea so late?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #166
        0x102,
        "#337FUh... Well, you see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #167
        0x138,
        (
            "#713FEstelle.\x02\x03",

            "Allow me to...elucidate the matter of\x01",
            "'tea' and why gentlemen should never\x01",
            "request it in polite company.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5974():
        TurnDirection(0xFE, 0x138, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5974)
    TurnDirection(0x101, 0x138, 400)

    ChrTalk(    #168
        0x101,
        "#324FHuh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #169
        0x138,
        "#710FCome closer...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 0)
    OP_8E(0x138, 0x15626, 0x0, 0x1644, 0x7D0, 0x0)
    OP_8C(0x101, 270, 400)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #170
        "\x07\x05Hilda whispered something into Estelle's ear.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_62(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_8F(0x138, 0x1578E, 0x0, 0x11EE, 0x3E8, 0x0)

    ChrTalk(    #171
        0x101,
        "#472F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #172
        0x138,
        "#711FNow do you understand?\x02",
    )

    CloseMessageWindow()
    OP_63(0x101)
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    TurnDirection(0x101, 0x138, 400)

    ChrTalk(    #173
        0x101,
        (
            "#472FUh...\x02\x03",

            "#327F...Yes...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #174
        0x102,
        "#333F(Hopeless... Completely hopeless...)\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x3FB)
    NewScene("ED6_DT01/T4254   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_15_4055 end

    def Function_16_5B01(): pass

    label("Function_16_5B01")

    EventBegin(0x0)
    RemoveParty(0x1, 0xFF)
    ClearChrFlags(0xC, 0x80)
    OP_44(0xC, 0xFF)
    SetChrFlags(0xC, 0x4)
    SetChrChipByIndex(0xC, 18)
    SetChrPos(0xC, 30760, 200, 53020, 270)
    SetChrPos(0x17, 29800, 500, 53440, 0)
    ClearChrFlags(0x17, 0x80)
    SetChrPos(0x12, 29750, 500, 53150, 0)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x13, 29750, 500, 52650, 0)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x14, 29300, 500, 53440, 0)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x15, 29300, 500, 52920, 0)
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0x16, 29300, 500, 52420, 0)
    ClearChrFlags(0x16, 0x80)
    SetChrPos(0x101, 31390, 0, 55480, 270)
    OP_6D(29710, 0, 54720, 0)
    OP_67(0, 6900, -10000, 0)
    OP_6B(2040, 0)
    OP_6C(45000, 0)
    OP_6E(401, 0)
    FadeToBright(2000, 0)
    OP_62(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_8E(0x101, 0x7170, 0x0, 0xD6D8, 0x7D0, 0x0)
    Sleep(500)
    OP_8C(0x101, 0, 400)
    OP_8E(0x101, 0x7A9E, 0x0, 0xD6D8, 0x7D0, 0x0)
    Sleep(500)
    OP_8C(0x101, 180, 400)
    OP_8E(0x101, 0x7170, 0x0, 0xD6D8, 0x7D0, 0x0)
    Sleep(500)
    OP_63(0x101)

    ChrTalk(    #175
        0x101,
        "#505F#6PHmmm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #176
        0xC,
        (
            "#020FWhat's wrong, Estelle? You've\x01",
            "been completely on edge for a\x01",
            "while now.\x02\x03",

            "Something on your mind?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xC, 400)

    ChrTalk(    #177
        0x101,
        "#007F#6PY-Yeah...\x02",
    )

    CloseMessageWindow()

    def lambda_5D16():
        OP_6D(30840, 0, 54690, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5D16)
    OP_8E(0x101, 0x74D6, 0x0, 0xD430, 0x3E8, 0x0)
    OP_8C(0x101, 180, 400)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #178
        0x101,
        (
            "#002F#6PHey, Schera...?\x02\x03",

            "Did you think Joshua was acting\x01",
            "weird at dinner?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #179
        0xC,
        (
            "#023F#4P???\x02\x03",

            "If anyone was acting weird,\x01",
            "I'd say it was you.\x02\x03",

            "He was as calm as he ever is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #180
        0x101,
        "#003F#6PWell, yeah, but...\x02",
    )

    CloseMessageWindow()
    OP_62(0xC, 0x0, 1700, 0xA, 0xB, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #181
        0xC,
        (
            "#027F#4PAh-ha...\x02\x03",

            "I see. I get it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #182
        0x101,
        "#004F#6PUh...get what?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #183
        0xC,
        (
            "#021F#4PYou can't keep secrets from me.♪\x02\x03",

            "I had a feeling about it, but\x01",
            "I was wondering if you'd ever\x01",
            "admit it to yourself.\x02\x03",

            "#027FYou're kinda falling for Joshua,\x01",
            "aren't you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #184
        0x101,
        (
            "#503F#6P...\x02\x03",

            "#503FY-You can tell...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #185
        0xC,
        (
            "#027F#4PIt's pretty obvious. Sorry, hon.\x02\x03",

            "But I'm guessing you haven't\x01",
            "told him anything about this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #186
        0x101,
        (
            "#503F#6PN-No...\x02\x03",

            "Joshua's always picking on me,\x01",
            "telling me what a dope I am...\x02\x03",

            "#506FNot that I should be criticizing\x01",
            "anyone, I guess.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #187
        0xC,
        (
            "#520F#4P*sigh*\x01",
            "You're so naive.\x02\x03",

            "It's a wonder how you've lasted\x01",
            "this long. You need to learn to\x01",
            "look a little deeper.\x02\x03",

            "Big sister is ready to begin your\x01",
            "education in love, Estelle!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #188
        0x101,
        (
            "#509F#6PI'm never asking you for\x01",
            "advice again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #189
        0xC,
        (
            "#020F#4PI'm just kidding. I'm sorry;\x01",
            "I don't mean to tease.\x02\x03",

            "#026FBut...\x02\x03",

            "You guys set out just when\x01",
            "puberty was about to hit.\x02\x03",

            "It's only logical that you'd\x01",
            "start picking up on feelings\x01",
            "for each other...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #190
        0x101,
        (
            "#008F#6PO-Oh... You think so...?\x02\x03",

            "#503FTraveling together just seems\x01",
            "like such a petty reason for\x01",
            "that kind of thing...\x02\x03",

            "I-I guess I've gotten a little\x01",
            "more self-aware since we started\x01",
            "all this...\x02\x03",

            "#504FArgh! This isn't like me at all!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #191
        0xC,
        (
            "#027F#4PHa ha... You're the proverbial\x01",
            "flower that refuses to blossom.\x02\x03",

            "Every girl feels that way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #192
        0x101,
        "#008F#6PSchera...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #193
        0xC,
        (
            "#020F#4PI don't want to lecture you, or\x01",
            "talk about this with you if you're\x01",
            "not ready...\x02\x03",

            "...but if you are, then what say\x01",
            "we have ourselves some girl talk,\x01",
            "hmm?\x02\x03",

            "Would it help if I told your fortune?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #194
        0x101,
        (
            "#503F#6PUmm...\x01",
            "Yeah, okay...\x02\x03",

            "I promise I'll listen to whatever\x01",
            "you have to say.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #195
        0xC,
        (
            "#020F#4POkay...\x02\x03",

            "#520FAll right! Time for your\x01",
            "lesson, my protege!\x02\x03",

            "Oh, Estelle, big sister is\x01",
            "moved to tears!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #196
        0x101,
        (
            "#509F#6POn second thought...never mind.\x02\x03",

            "#501FBut thank you...\x01",
            "I do feel a little better.\x02\x03",

            "I'm gonna go see Joshua\x01",
            "for a little bit.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xC, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_62(0xC, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(    #197
        0xC,
        (
            "#023F#4POh...?!\x02\x03",

            "You're going to tell him?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #198
        0x101,
        (
            "#006F#6PNot about that.\x02\x03",

            "There really does seem to be\x01",
            "something weird going on with\x01",
            "him.\x02\x03",

            "I want to see what that's\x01",
            "about first.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #199
        0xC,
        (
            "#025F#4PAwww...\x02\x03",

            "#020FWell, you do seem to know him\x01",
            "better than anyone else.\x02\x03",

            "#021FI'm sure that everything will turn\x01",
            "out just fine between you two.\x02\x03",

            "Maybe you can even just have a nice,\x01",
            "calm discussion with him and be open\x01",
            "about what's on your mind.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #200
        0x101,
        (
            "#007F#6PI... I don't think I'm quite\x01",
            "THAT ready yet.\x02\x03",

            "#006FOkay, I'll see you later!\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 90, 800)

    def lambda_67EA():
        OP_6D(31870, 0, 54140, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_67EA)
    OP_8E(0x101, 0x816A, 0x0, 0xD430, 0x1388, 0x0)
    SetChrSubChip(0xC, 1)
    OP_8E(0x101, 0x88B8, 0x0, 0xC490, 0x1388, 0x0)
    OP_22(0x6, 0x0, 0x64)

    def lambda_6834():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_6834)
    OP_8E(0x101, 0x88B8, 0x0, 0xBF54, 0x1388, 0x0)
    Sleep(1500)

    def lambda_685F():
        OP_6D(30840, 0, 54690, 1500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_685F)
    WaitChrThread(0x101, 0x1)
    Fade(500)
    SetChrChipByIndex(0xC, 20)
    SetChrFlags(0xC, 0x2)
    SetChrSubChip(0xC, 0)
    OP_0D()
    Sleep(400)
    SetChrSubChip(0xC, 1)
    Sleep(400)
    OP_99(0xC, 0x1, 0x3, 0x320)
    Sleep(400)

    ChrTalk(    #201
        0xC,
        (
            "#026F#6PYoung love...\x02\x03",

            "#027FAhh, they'll probably be fine...\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(1000)
    Call(0, 17)
    Return()

    # Function_16_5B01 end

    def Function_17_68FF(): pass

    label("Function_17_68FF")

    EventBegin(0x0)
    OP_6D(89230, 0, 60740, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 79820, 0, 50600, 0)

    def lambda_6955():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_6955)
    FadeToBright(1000, 0)
    OP_22(0x6, 0x0, 0x64)

    def lambda_6975():
        OP_8E(0xFE, 0x13754, 0x0, 0xD7B4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6975)
    OP_6D(81310, 0, 56390, 4000)
    WaitChrThread(0x101, 0x1)
    OP_8C(0x101, 90, 400)

    ChrTalk(    #202
        0x101,
        (
            "#004F#5PHuh... They're not here.\x02\x03",

            "#505FOh, yeah... Dad's still in\x01",
            "some meeting, I think.\x02\x03",

            "But where's Joshua?\x02",
        )
    )

    CloseMessageWindow()
    OP_20(0x5DC)
    OP_21()
    OP_1D(0x4A)
    OP_1F(0x50, 0xC8)
    Sleep(2000)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x101, 0, 400)

    ChrTalk(    #203
        0x101,
        (
            "#501F#5PJoshua...?\x02\x03",

            "Ah... He's out playing\x01",
            "somewhere, then.\x02",
        )
    )

    CloseMessageWindow()
    OP_1B(0x0, 0x0, 0xFFFF)
    OP_1B(0x6, 0x0, 0xFFFF)
    OP_A2(0x670)
    EventEnd(0x0)
    Return()

    # Function_17_68FF end

    def Function_18_6AA1(): pass

    label("Function_18_6AA1")

    OP_1F(0x50, 0xC8)
    Return()

    # Function_18_6AA1 end

    def Function_19_6AA8(): pass

    label("Function_19_6AA8")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6B1D")
    OP_A2(0x9)

    ChrTalk(    #204
        0x101,
        (
            "#505FThe harmonica sounds like\x01",
            "it's coming from outside.\x02\x03",

            "Maybe Joshua's at the Garden Terrace?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6B4B")

    label("loc_6B1D")


    ChrTalk(    #205
        0x101,
        "#006FI need to check the Garden Terrace.\x02",
    )

    CloseMessageWindow()

    label("loc_6B4B")

    OP_90(0x0, 0x5DC, 0x0, 0x0, 0xBB8, 0x0)
    EventEnd(0x1)
    Return()

    # Function_19_6AA8 end

    def Function_20_6B62(): pass

    label("Function_20_6B62")

    EventBegin(0x1)

    ChrTalk(    #206
        0x101,
        (
            "#007FUgh... What is wrong with me?\x02\x03",

            "#000FI need to go to Joshua's room.\x02",
        )
    )

    CloseMessageWindow()
    OP_90(0x0, 0x0, 0x0, 0xFFFFFA24, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_20_6B62 end

    SaveToFile()

Try(main)
