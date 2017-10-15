from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'T0310   ._SN',
        MapName             = 'Rolent',
        Location            = 'T0310.x',
        MapIndex            = 15,
        MapDefaultBGM       = "ed60015",
        Flags               = 0,
        EntryFunctionIndex  = 18,
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
        'Cassius',                              # 9
        'Scherazard',                           # 10
        'Kevin',                                # 11
        'Target Camera',                        # 12
        'Pot',                                  # 13
        'Tea',                                  # 14
        'Tea',                                  # 15
        'Tea',                                  # 16
        'Tea',                                  # 17
        'Kettle',                               # 18
        'Lena',                                 # 19
        'Dish',                                 # 20
        'Dish',                                 # 21
        'Dish',                                 # 22
        'Salad',                                # 23
        'Bread',                                # 24
        'Fork',                                 # 25
        'Fork',                                 # 26
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
        'ED6_DT27/CH03670 ._CH',             # 00
        'ED6_DT07/CH00020 ._CH',             # 01
        'ED6_DT07/CH02003 ._CH',             # 02
        'ED6_DT07/CH00023 ._CH',             # 03
        'ED6_DT07/CH00003 ._CH',             # 04
        'ED6_DT06/CH20020 ._CH',             # 05
        'ED6_DT27/CH03003 ._CH',             # 06
        'ED6_DT07/CH00053 ._CH',             # 07
        'ED6_DT07/CH00033 ._CH',             # 08
        'ED6_DT07/CH00043 ._CH',             # 09
        'ED6_DT07/CH00063 ._CH',             # 0A
        'ED6_DT07/CH00073 ._CH',             # 0B
        'ED6_DT26/CH20320 ._CH',             # 0C
        'ED6_DT07/CH02003 ._CH',             # 0D
        'ED6_DT27/CH03740 ._CH',             # 0E
        'ED6_DT26/CH20332 ._CH',             # 0F
        'ED6_DT27/CH03743 ._CH',             # 10
        'ED6_DT06/CH20008 ._CH',             # 11
        'ED6_DT27/CH03740 ._CH',             # 12
        'ED6_DT26/CH20239 ._CH',             # 13
        'ED6_DT27/CH03740 ._CH',             # 14
        'ED6_DT27/CH03080 ._CH',             # 15
        'ED6_DT26/CH20232 ._CH',             # 16
        'ED6_DT27/CH03673 ._CH',             # 17
        'ED6_DT26/CH20263 ._CH',             # 18
        'ED6_DT26/CH20278 ._CH',             # 19
    )

    AddCharChipPat(
        'ED6_DT27/CH03670P._CP',             # 00
        'ED6_DT07/CH00020P._CP',             # 01
        'ED6_DT07/CH02003P._CP',             # 02
        'ED6_DT07/CH00023P._CP',             # 03
        'ED6_DT07/CH00003P._CP',             # 04
        'ED6_DT06/CH20020P._CP',             # 05
        'ED6_DT27/CH03003P._CP',             # 06
        'ED6_DT07/CH00053P._CP',             # 07
        'ED6_DT07/CH00033P._CP',             # 08
        'ED6_DT07/CH00043P._CP',             # 09
        'ED6_DT07/CH00063P._CP',             # 0A
        'ED6_DT07/CH00073P._CP',             # 0B
        'ED6_DT26/CH20320P._CP',             # 0C
        'ED6_DT07/CH02003P._CP',             # 0D
        'ED6_DT27/CH03740P._CP',             # 0E
        'ED6_DT26/CH20332P._CP',             # 0F
        'ED6_DT27/CH03743P._CP',             # 10
        'ED6_DT06/CH20008P._CP',             # 11
        'ED6_DT27/CH03740P._CP',             # 12
        'ED6_DT26/CH20239P._CP',             # 13
        'ED6_DT27/CH03740P._CP',             # 14
        'ED6_DT27/CH03080P._CP',             # 15
        'ED6_DT26/CH20232P._CP',             # 16
        'ED6_DT27/CH03673P._CP',             # 17
        'ED6_DT26/CH20263P._CP',             # 18
        'ED6_DT26/CH20278P._CP',             # 19
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
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
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
        Unknown3            = 1703941,
        ChipIndex           = 0x5,
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
        Unknown3            = 1638405,
        ChipIndex           = 0x5,
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
        Unknown3            = 1638405,
        ChipIndex           = 0x5,
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
        Unknown3            = 1638405,
        ChipIndex           = 0x5,
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
        Unknown3            = 1638405,
        ChipIndex           = 0x5,
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
        Unknown3            = 1703941,
        ChipIndex           = 0x5,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 655365,
        ChipIndex           = 0x5,
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
        Unknown3            = 655365,
        ChipIndex           = 0x5,
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
        Unknown3            = 655365,
        ChipIndex           = 0x5,
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
        Unknown3            = 458757,
        ChipIndex           = 0x5,
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
        Unknown3            = 1769477,
        ChipIndex           = 0x5,
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
        Unknown3            = 1376261,
        ChipIndex           = 0x5,
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
        Unknown3            = 1376261,
        ChipIndex           = 0x5,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclActor(
        TriggerX            = 72990,
        TriggerZ            = 0,
        TriggerY            = -460,
        TriggerRange        = 800,
        ActorX              = 72990,
        ActorZ              = 1000,
        ActorY              = -460,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 10,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 9360,
        TriggerZ            = 0,
        TriggerY            = 68590,
        TriggerRange        = 800,
        ActorX              = 9260,
        ActorZ              = 800,
        ActorY              = 68720,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 14,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 70420,
        TriggerZ            = 0,
        TriggerY            = 148490,
        TriggerRange        = 500,
        ActorX              = 70420,
        ActorZ              = 500,
        ActorY              = 148490,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 17,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 146290,
        TriggerZ            = 0,
        TriggerY            = 144760,
        TriggerRange        = 800,
        ActorX              = 147910,
        ActorZ              = 1500,
        ActorY              = 144780,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 21,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 72010,
        TriggerZ            = 0,
        TriggerY            = 71390,
        TriggerRange        = 800,
        ActorX              = 72570,
        ActorZ              = 1500,
        ActorY              = 72600,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 21,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_46E",          # 00, 0
        "Function_1_4FB",          # 01, 1
        "Function_2_9BC",          # 02, 2
        "Function_3_B39",          # 03, 3
        "Function_4_B6B",          # 04, 4
        "Function_5_B70",          # 05, 5
        "Function_6_2BBB",         # 06, 6
        "Function_7_35CE",         # 07, 7
        "Function_8_3808",         # 08, 8
        "Function_9_6185",         # 09, 9
        "Function_10_6535",        # 0A, 10
        "Function_11_6549",        # 0B, 11
        "Function_12_6702",        # 0C, 12
        "Function_13_73B8",        # 0D, 13
        "Function_14_799D",        # 0E, 14
        "Function_15_7AA0",        # 0F, 15
        "Function_16_7BC3",        # 10, 16
        "Function_17_7D48",        # 11, 17
        "Function_18_7EDB",        # 12, 18
        "Function_19_8046",        # 13, 19
        "Function_20_80E1",        # 14, 20
        "Function_21_8133",        # 15, 21
    )


    def Function_0_46E(): pass

    label("Function_0_46E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_488")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x58), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10F0)
    Event(0, 5)
    Jump("loc_4FA")

    label("loc_488")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 1)), scpexpr(EXPR_END)), "loc_4A2")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x19), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10F1)
    Event(0, 6)
    Jump("loc_4FA")

    label("loc_4A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 2)), scpexpr(EXPR_END)), "loc_4B3")
    OP_A3(0x10F2)
    Event(0, 7)
    Jump("loc_4FA")

    label("loc_4B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 3)), scpexpr(EXPR_END)), "loc_4C4")
    OP_A3(0x10F3)
    Event(0, 8)
    Jump("loc_4FA")

    label("loc_4C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 4)), scpexpr(EXPR_END)), "loc_4DE")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x75), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10F4)
    Event(0, 9)
    Jump("loc_4FA")

    label("loc_4DE")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6F), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4FA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x307, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x307, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4FA")
    Event(0, 16)

    label("loc_4FA")

    Return()

    # Function_0_46E end

    def Function_1_4FB(): pass

    label("Function_1_4FB")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x306, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_530")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x75), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x2000000)
    OP_10(0x8, 0x0)
    OP_10(0x9, 0x0)
    OP_10(0xA, 0x1)
    OP_10(0xB, 0x1)
    OP_64(0x3, 0x1)
    OP_64(0x3, 0x1)
    Jump("loc_53C")

    label("loc_530")

    OP_10(0x8, 0x1)
    OP_10(0x9, 0x1)
    OP_10(0xA, 0x0)
    OP_10(0xB, 0x0)

    label("loc_53C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x306, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x307, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_554")
    OP_72(0x4, 0x10)
    OP_65(0x0, 0x1)
    Jump("loc_55D")

    label("loc_554")

    OP_71(0x4, 0x10)
    OP_64(0x0, 0x1)

    label("loc_55D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x306, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x307, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_570")
    OP_65(0x1, 0x1)
    Jump("loc_574")

    label("loc_570")

    OP_64(0x1, 0x1)

    label("loc_574")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x306, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x307, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_587")
    OP_65(0x2, 0x1)
    Jump("loc_58B")

    label("loc_587")

    OP_64(0x2, 0x1)

    label("loc_58B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_99F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x306, 4)), scpexpr(EXPR_END)), "loc_5C8")
    SetChrFlags(0x8, 0x20)
    SetChrFlags(0x8, 0x10)
    SetChrFlags(0x8, 0x4)
    SetChrPos(0x8, 3070, 200, 71390, 180)
    SetChrChipByIndex(0x8, 13)
    ClearChrFlags(0x8, 0x80)

    label("loc_5C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x306, 4)), scpexpr(EXPR_END)), "loc_99F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x306, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5F7")
    SetChrPos(0x12, -1400, 0, 3140, 90)
    ClearChrFlags(0x12, 0x80)
    OP_43(0x12, 0x0, 0x0, 0x2)
    Jump("loc_99F")

    label("loc_5F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x306, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_742")
    SetChrPos(0x12, -1400, 0, 3140, 90)
    SetChrFlags(0x12, 0x10)
    ClearChrFlags(0x12, 0x80)
    OP_43(0x12, 0x0, 0x0, 0x2)
    SetChrPos(0x11, -630, 800, 2940, 0)
    SetChrSubChip(0x11, 31)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x13, -8290, 800, 1250, 0)
    SetChrPos(0x14, -9800, 800, 1250, 0)
    SetChrPos(0x15, -8290, 800, 290, 0)
    SetChrPos(0x17, -7870, 800, 270, 0)
    SetChrPos(0x18, -8000, 800, 1300, 0)
    SetChrPos(0x19, -10450, 800, 1290, 0)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    SetChrSubChip(0x13, 1)
    SetChrSubChip(0x14, 1)
    SetChrSubChip(0x15, 1)
    SetChrSubChip(0x17, 12)
    LoadEffect(0x1, "map\\\\mp068_00.eff")
    PlayEffect(0x1, 0x1, 0xFF, -630, 0, 2940, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_731"),
        (101, "loc_731"),
        (104, "loc_731"),
        (SWITCH_DEFAULT, "loc_739"),
    )


    label("loc_731")

    OP_22(0x119, 0x1, 0x5A)
    Jump("loc_73F")

    label("loc_739")

    OP_23(0x119)
    Jump("loc_73F")

    label("loc_73F")

    Jump("loc_99F")

    label("loc_742")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x307, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7E5")
    SetChrPos(0x13, -8290, 800, 1250, 0)
    SetChrPos(0x14, -9800, 800, 1250, 0)
    SetChrPos(0x15, -8290, 800, 290, 0)
    SetChrPos(0x17, -7870, 800, 270, 0)
    SetChrPos(0x18, -8000, 800, 1300, 0)
    SetChrPos(0x19, -10450, 800, 1290, 0)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    SetChrSubChip(0x13, 0)
    SetChrSubChip(0x14, 0)
    SetChrSubChip(0x15, 0)
    SetChrSubChip(0x17, 12)
    Jump("loc_99F")

    label("loc_7E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x307, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x307, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8C6")
    SetChrPos(0x12, -1560, 0, 3990, 90)
    ClearChrFlags(0x12, 0x80)
    OP_43(0x12, 0x0, 0x0, 0x2)
    SetChrPos(0x13, -8290, 800, 1250, 0)
    SetChrPos(0x14, -9800, 800, 1250, 0)
    SetChrPos(0x15, -8290, 800, 290, 0)
    SetChrPos(0x16, -640, 600, 4330, 0)
    SetChrPos(0x17, -7870, 800, 270, 0)
    SetChrPos(0x18, -8000, 800, 1300, 0)
    SetChrPos(0x19, -10450, 800, 1290, 0)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    SetChrSubChip(0x13, 0)
    SetChrSubChip(0x14, 0)
    SetChrSubChip(0x15, 0)
    SetChrSubChip(0x17, 12)
    OP_6F(0x8, 0)
    Jump("loc_99F")

    label("loc_8C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x307, 3)), scpexpr(EXPR_END)), "loc_99F")
    SetChrPos(0x12, -7000, 0, 1420, 270)
    ClearChrFlags(0x12, 0x80)
    OP_43(0x12, 0x0, 0x0, 0x2)
    SetChrPos(0x13, -8290, 800, 1250, 0)
    SetChrPos(0x14, -9800, 800, 1250, 0)
    SetChrPos(0x15, -8290, 800, 290, 0)
    SetChrPos(0x16, -9200, 800, 800, 0)
    SetChrPos(0x17, -7870, 800, 270, 0)
    SetChrPos(0x18, -8000, 800, 1300, 0)
    SetChrPos(0x19, -10450, 800, 1290, 0)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    SetChrSubChip(0x13, 0)
    SetChrSubChip(0x14, 0)
    SetChrSubChip(0x15, 0)
    SetChrSubChip(0x17, 12)
    OP_6F(0x8, 15)

    label("loc_99F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x305, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9AE")
    Jump("loc_9B8")

    label("loc_9AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 5)), scpexpr(EXPR_END)), "loc_9B8")
    OP_82(0x81, 0x0)

    label("loc_9B8")

    OP_82(0x80, 0x0)
    Return()

    # Function_1_4FB end

    def Function_2_9BC(): pass

    label("Function_2_9BC")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9E1")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_B23")

    label("loc_9E1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9FA")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_B23")

    label("loc_9FA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A13")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_B23")

    label("loc_A13")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A2C")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_B23")

    label("loc_A2C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A45")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_B23")

    label("loc_A45")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A5E")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_B23")

    label("loc_A5E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A77")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_B23")

    label("loc_A77")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A90")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_B23")

    label("loc_A90")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AA9")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_B23")

    label("loc_AA9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AC2")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_B23")

    label("loc_AC2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_ADB")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_B23")

    label("loc_ADB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AF4")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_B23")

    label("loc_AF4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B0D")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_B23")

    label("loc_B0D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B23")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_B23")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_B38")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_B23")

    label("loc_B38")

    Return()

    # Function_2_9BC end

    def Function_3_B39(): pass

    label("Function_3_B39")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x306, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B50")
    Call(0, 12)
    Jump("loc_B6A")

    label("loc_B50")

    TalkBegin(0x8)

    ChrTalk(    #0
        0x8,
        "◆セリフ無し。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0x8)

    label("loc_B6A")

    Return()

    # Function_3_B39 end

    def Function_4_B6B(): pass

    label("Function_4_B6B")

    Call(0, 13)
    Return()

    # Function_4_B6B end

    def Function_5_B70(): pass

    label("Function_5_B70")

    EventBegin(0x0)
    OP_6D(-900, 0, -2790, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(50000, 0)
    OP_6E(280, 0)
    SetChrFlags(0x142, 0x80)
    SetChrPos(0x101, -1210, 0, -5810, 0)

    def lambda_BCB():
        OP_8E(0x101, 0xFFFFFC7C, 0x0, 0xFFFFF51A, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_BCB)
    WaitChrThread(0x101, 0x0)
    OP_8C(0x101, 270, 400)
    Sleep(300)
    OP_8C(0x101, 0, 400)
    OP_8C(0x101, 90, 400)
    Sleep(300)

    ChrTalk(    #1
        0x101,
        (
            "#001FJoshuaaaa! I'm hooooome!\x02\x03",

            "You're back, right?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x101)
    Sleep(500)

    ChrTalk(    #2
        0x101,
        (
            "#505FThat's weird.\x02\x03",

            "I'm sure he must be here...\x02\x03",

            "#004FAh! Maybe he's in Dad's study.\x02",
        )
    )

    CloseMessageWindow()
    OP_6A(0x101)
    OP_8E(0x101, 0x128E, 0x0, 0xFFFFFBC8, 0x1388, 0x0)
    OP_8C(0x101, 0, 400)
    OP_72(0x1, 0x10)
    OP_6F(0x1, 0)
    OP_70(0x1, 0x13)
    OP_73(0x1)
    FadeToDark(1000, 0, -1)
    OP_8E(0x101, 0x155E, 0x0, 0x8B6, 0x1388, 0x0)
    OP_0D()
    SetChrPos(0x101, 2910, 0, 65200, 0)
    OP_69(0x101, 0x0)
    FadeToBright(1000, 0)
    OP_8E(0x101, 0xD2A, 0x0, 0x10982, 0x1388, 0x0)
    OP_0D()
    OP_20(0x1388)
    OP_62(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x101)
    Sleep(500)

    ChrTalk(    #3
        0x101,
        "#586FJ-Joshua...?\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x142, 0x80)
    OP_8C(0x101, 180, 400)
    Sleep(500)
    FadeToDark(1000, 0, -1)

    def lambda_D9A():
        OP_8E(0xFE, 0xB0E, 0x0, 0xFB4A, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_D9A)
    Sleep(500)
    OP_9F(0x101, 0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_0D()
    SetChrPos(0x142, -1200, 0, -5160, 0)
    OP_9F(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    SetChrPos(0x101, 5470, 0, 2230, 180)
    OP_69(0x101, 0x0)
    FadeToBright(1000, 0)

    def lambda_E03():
        OP_8E(0x142, 0xFFFFFDD0, 0x0, 0xFFFFF4CA, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_E03)

    def lambda_E1E():
        OP_8E(0x101, 0x12C0, 0x0, 0xFFFFF4FC, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x142, 0, lambda_E1E)
    Sleep(1000)
    WaitChrThread(0x142, 0x0)
    OP_44(0x101, 0x0)

    def lambda_E47():
        TurnDirection(0x142, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_E47)

    def lambda_E55():
        OP_8E(0x101, 0x2A3A, 0x7D0, 0xFFFFF330, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x142, 0, lambda_E55)
    WaitChrThread(0x142, 0x0)
    FadeToDark(1000, 0, -1)

    def lambda_E7F():
        OP_8E(0x101, 0x2ABC, 0x7D0, 0xFFFFFA38, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x142, 0, lambda_E7F)
    WaitChrThread(0x142, 0x0)

    def lambda_E9F():
        OP_8E(0x101, 0x21F2, 0xFA0, 0xFFFFFAE2, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x142, 0, lambda_E9F)
    OP_0D()
    SetChrPos(0x101, 81350, 0, -1130, 270)
    OP_69(0x101, 0x0)
    FadeToBright(1000, 0)
    OP_8E(0x101, 0x125B6, 0x0, 0xFFFFFC4A, 0x1388, 0x0)
    OP_0D()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #4
        0x101,
        "#004FOh, wait, duh.\x02",
    )

    CloseMessageWindow()
    OP_8C(0x101, 90, 500)
    Sleep(500)

    ChrTalk(    #5
        0x101,
        (
            "#586FIt's possible he's in my room\x01",
            "looking for something, right?\x02\x03",

            "#503F...Did I leave some underwear\x01",
            "or something laying around?\x02",
        )
    )

    CloseMessageWindow()
    OP_8E(0x101, 0x13394, 0x0, 0xFFFFFDD0, 0x1388, 0x0)
    OP_8C(0x101, 0, 400)
    OP_72(0x3, 0x10)
    OP_6F(0x3, 0)
    OP_70(0x3, 0x13)
    OP_73(0x3)
    FadeToDark(1000, 0, -1)
    OP_8E(0x101, 0x13344, 0x0, 0x5BE, 0x1388, 0x0)
    OP_0D()
    SetChrPos(0x101, 143760, 0, 139970, 0)
    OP_69(0x101, 0x0)
    FadeToBright(1000, 0)
    OP_8E(0x101, 0x235FA, 0x0, 0x231B8, 0x1388, 0x0)
    OP_0D()
    OP_62(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x101)
    Sleep(500)

    ChrTalk(    #6
        0x101,
        (
            "#587F...\x02\x03",

            "#506FUh... My room's clean, at least!\x02\x03",

            "Though Joshua probably wouldn't care\x01",
            "about a few panties here and there...\x02\x03",

            "#586FSo...\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 180, 400)
    Sleep(500)

    def lambda_10F6():
        OP_8E(0x101, 0x23190, 0x0, 0x222C2, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_10F6)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_44(0x101, 0x1)
    SetChrPos(0x101, 78660, 0, 1470, 180)
    OP_69(0x101, 0x0)
    FadeToBright(1000, 0)
    OP_8E(0x101, 0x13434, 0x0, 0xFFFFFA24, 0x7D0, 0x0)
    OP_0D()
    OP_8E(0x101, 0x11C6A, 0x0, 0xFFFFFA24, 0x7D0, 0x0)
    OP_8E(0x101, 0x11C6A, 0x0, 0xFFFFFE0C, 0x7D0, 0x0)
    OP_62(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x101)
    Sleep(500)
    OP_22(0x71, 0x0, 0x64)
    Sleep(300)
    Sleep(1000)

    ChrTalk(    #7
        0x101,
        "#586FJoshua...I'm coming in, okay?\x02",
    )

    CloseMessageWindow()
    OP_72(0x4, 0x10)
    OP_6F(0x4, 0)
    OP_70(0x4, 0x13)
    OP_73(0x4)
    Sleep(500)
    FadeToDark(2000, 0, -1)
    ClearMapFlags(0x1)
    OP_8E(0x101, 0x11DF0, 0x0, 0x6D6, 0x3E8, 0x0)
    OP_0D()
    OP_6D(70660, 0, 64780, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(50000, 0)
    OP_6E(280, 0)
    SetChrPos(0x101, 70820, 0, 64790, 0)
    Sleep(500)
    OP_C4(0x0, 0x2)
    OP_1D(0x50)
    FadeToBright(1500, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #8
        0x101,
        "#587F...Oh.\x02",
    )

    CloseMessageWindow()

    def lambda_1293():
        OP_6D(70630, 0, 71190, 5000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1293)

    def lambda_12AB():
        OP_67(0, 6000, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_12AB)
    Sleep(1000)

    def lambda_12C8():
        OP_8E(0x101, 0x113D2, 0x0, 0x1163E, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_12C8)
    Sleep(3000)

    def lambda_12E8():
        OP_8E(0x101, 0x113D2, 0x0, 0x1163E, 0x3B6, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_12E8)
    Sleep(2000)

    def lambda_1308():
        OP_8E(0x101, 0x113D2, 0x0, 0x1163E, 0x384, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1308)
    Sleep(1000)

    def lambda_1328():
        OP_8E(0x101, 0x113D2, 0x0, 0x1163E, 0x352, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1328)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x101, 0x2)
    Sleep(500)

    ChrTalk(    #9
        0x101,
        "#586FOf course... Makes sense...\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    Fade(250)
    SetChrChipByIndex(0x101, 22)
    SetChrSubChip(0x101, 0)
    OP_22(0xD1, 0x0, 0x50)
    OP_0D()
    Sleep(1000)

    ChrTalk(    #10
        0x101,
        "#588FI'm such an idiot...\x02",
    )

    CloseMessageWindow()
    OP_9F(0x142, 0x0, 0x0, 0x0, 0x0, 0x0)
    SetChrPos(0x142, 70840, 0, 64450, 50)

    def lambda_13D7():
        OP_9F(0x142, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x142, 0, lambda_13D7)
    OP_8E(0x142, 0x113AA, 0x0, 0x109A0, 0x5DC, 0x0)
    Sleep(500)

    ChrTalk(    #11
        0x142,
        "#1067F#4PSo your boyfriend's not here, huh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x101,
        "#003F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x142,
        (
            "#4P#1060FOr, hey, maybe we missed him?\x02\x03",

            "He came back, then headed out\x01",
            "to town for a bit, and we passed by\x01",
            "each other without realizing?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x101,
        "#588F...No.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x142,
        (
            "#4P#1065F*sigh*\x02\x03",

            "#1063FYou've accepted it, then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x101,
        (
            "#003FI...\x02\x03",

            "#586FReally...\x01",
            "I knew, somewhere, deep down.\x02\x03",

            "I knew he'd really left.\x02\x03",

            "There was no way he'd come\x01",
            "back home for any longer than\x01",
            "a few moments.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x142,
        "#4P#1067FRight...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x101,
        (
            "#588FBut this room was it.\x01",
            "It was my last hope.\x02\x03",

            "I have no idea where else\x01",
            "he could be. At all.\x02\x03",

            "So...this is the end.\x02\x03",

            "I'll never see Joshua again. Ever...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x142,
        (
            "#4P#1063F...\x02\x03",

            "#1065FAin't it a bit early to be\x01",
            "giving up THAT easily?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x101,
        "#587FHuh?\x02",
    )

    CloseMessageWindow()

    def lambda_16C8():
        OP_6D(71130, 0, 71690, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_16C8)
    OP_8E(0x142, 0x117EC, 0x0, 0x115DA, 0x7D0, 0x0)
    OP_8C(0x142, 270, 400)
    WaitChrThread(0x101, 0x3)
    Sleep(500)

    ChrTalk(    #21
        0x142,
        (
            "#4P#1060FIn the end, the only one who knows\x01",
            "whether we're destined to meet someone\x01",
            "again, here or beyond, is Aidios Herself.\x02\x03",

            "Just because YOU think fate's against\x01",
            "you is no reason to give up.\x02\x03",

            "The question then, Estelle, is this:\x01",
            "what do you think you can do about it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x101,
        (
            "#003F#6PBut, but...\x02\x03",

            "I don't even have any leads to follow...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x142,
        (
            "#4P#1060FNo leads at all? You sure?\x02\x03",

            "I don't know your boyfriend,\x01",
            "of course, but...\x02\x03",

            "Nobody I know would disappear\x01",
            "without SOME reason.\x02",
        )
    )

    CloseMessageWindow()
    OP_51(0x101, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(150)
    Sleep(500)

    ChrTalk(    #24
        0x101,
        "#587F#6PWhat do you...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x142,
        (
            "#4P#1063FWas there anything weird in how he\x01",
            "talked or acted towards you recently?\x02\x03",

            "Or maybe something strange had\x01",
            "been happening with him lately?\x02\x03",

            "Something only you, who've been\x01",
            "with him so long, would pick up on?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x101,
        "#580F#6PHey!\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    OP_20(0x5DC)
    OP_AD(0x2400B8, 0x0, 0x0, 0x3E8)
    Sleep(1200)
    OP_77(0x0, 0x0, 0x0, 0x0, 0x0)
    OP_AD(0x2400B9, 0x0, 0x0, 0x3E8)
    Sleep(1200)
    OP_AD(0x2400BA, 0x0, 0x0, 0x3E8)
    Sleep(1200)
    OP_AD(0x2400BB, 0x0, 0x0, 0x3E8)
    Sleep(1200)
    OP_AD(0x2400BC, 0x0, 0x0, 0x3E8)
    Sleep(1200)
    OP_AD(0x2400BD, 0x0, 0x0, 0x3E8)
    Sleep(1200)
    OP_AD(0x2400BE, 0x0, 0x0, 0x3E8)
    Sleep(1200)
    OP_AE(0x3E8)
    Sleep(1000)
    SetChrName("Estelle")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #27
        "\x07\x00#580F#3SOh, yeah, of course!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_69(0x101, 0x0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrSubChip(0x101, 0)
    OP_77(0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
    Sleep(1500)

    ChrTalk(    #28
        0x101,
        (
            "#580F#6PJoshua started acting weird RIGHT\x01",
            "after I got back to that spot where we\x01",
            "were resting!\x02\x03",

            "What the...? Why is my head fuzzy...?\x02\x03",

            "Why can't I remember who I met\x01",
            "along the way? I DID meet someone!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x142,
        (
            "#4P#1063FHey, you okay?\x01",
            "You went white as a sheet there.\x02",
        )
    )

    CloseMessageWindow()
    OP_51(0x101, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(150)
    Sleep(500)

    ChrTalk(    #30
        0x101,
        "#587F#6PYeah... I think so...\x02",
    )

    CloseMessageWindow()
    OP_51(0x101, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(200)
    Sleep(500)
    Fade(500)
    SetChrChipByIndex(0x101, 65535)
    ClearChrFlags(0x101, 0x2)
    SetChrSubChip(0x101, 0)
    OP_8C(0x101, 0, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #31
        0x101,
        (
            "#002F#6PNow I get it.\x02\x03",

            "Joshua went off to stop the 'foul magician.'\x02\x03",

            "#003FIf the person I met then was that 'magician'...\x02\x03",

            "...and that person was the one actually behind\x01",
            "the coup and Colonel Richard's memory trouble...\x02\x03",

            "...then that magician must still be planning\x01",
            "something else in Liberl!\x02\x03",

            "#586FBut that means, if I can stop him, as a bracer...\x02\x03",

            "Maybe... Just maybe...\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x6, 0x0, 0x64)
    Sleep(500)
    SetChrPos(0x8, 70740, 0, 64890, 0)

    NpcTalk(    #32
        0x8,
        "Man's Voice",
        "#1PSo, you've realized what's going on.\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_1D(0x76)
    Sleep(500)

    def lambda_1E77():
        TurnDirection(0x142, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x142, 0, lambda_1E77)

    def lambda_1E85():
        OP_8C(0x101, 180, 400)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_1E85)

    def lambda_1E93():
        OP_6D(70790, 0, 70530, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1E93)

    def lambda_1EAB():
        OP_67(0, 6000, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1EAB)
    Sleep(500)
    ClearChrFlags(0x8, 0x80)
    OP_9F(0x8, 0x0, 0x0, 0x0, 0x0, 0x0)

    def lambda_1ED8():
        OP_8E(0x8, 0x112A6, 0x0, 0x10DBA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_1ED8)

    def lambda_1EF3():
        OP_9F(0x8, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1EF3)
    Sleep(500)

    def lambda_1F0A():
        OP_8E(0x142, 0x119C2, 0x0, 0x11260, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x142, 1, lambda_1F0A)
    WaitChrThread(0x142, 0x1)

    def lambda_1F2A():
        OP_8C(0x142, 225, 400)
        ExitThread()

    QueueWorkItem(0x142, 2, lambda_1F2A)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 70740, 0, 64890, 0)
    OP_9F(0x9, 0x0, 0x0, 0x0, 0x0, 0x0)

    def lambda_1F59():
        OP_8E(0x9, 0x115EE, 0x0, 0x10A72, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1F59)

    def lambda_1F74():
        OP_9F(0x9, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1F74)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #33
        0x101,
        (
            "#580F#3PDad?! Schera?!\x02\x03",

            "Why are you here?\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x142, 250, 400)
    Sleep(500)

    ChrTalk(    #34
        0x142,
        (
            "#1060F#4PSorry, Estelle.\x02\x03",

            "When we touched down, I took\x01",
            "the liberty of contacting the guild's\x01",
            "Grancel branch on the sly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x101,
        "#004F#3POh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x9,
        (
            "#025FEstelle, honey, you scared the pants\x01",
            "off of us, running away like that!\x02\x03",

            "We were at the Grancel guildhouse\x01",
            "trying to find you when the call came in.\x02\x03",

            "#524FWe barely managed to catch a\x01",
            "departing freightliner out here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x101,
        "#586F#3PAh... I'm sorry.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x8,
        (
            "#1125F#6PJust as Scherazard said.\x01",
            "I'm glad you're safe, Estelle.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x8, 55, 400)
    Sleep(500)

    ChrTalk(    #39
        0x8,
        (
            "#1120F#6PNow then, Father Kevin, was it?\x01",
            "I appreciate your contacting us.\x02\x03",

            "You have my deepest thanks for\x01",
            "letting us know where Estelle was.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x142, 225, 400)
    Sleep(300)

    ChrTalk(    #40
        0x142,
        (
            "#1061F#4PNaaah, don't worry about it.\x02\x03",

            "My fault for butting into family\x01",
            "matters, really.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x101,
        (
            "#003F#3PU-Umm...\x02\x03",

            "Dad, I...\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x8, 6, 400)
    Sleep(200)
    OP_8C(0x142, 250, 400)
    Sleep(200)

    ChrTalk(    #42
        0x8,
        (
            "#6P#1122FNo, Estelle. The one who needs\x01",
            "to apologize is me.\x02\x03",

            "#1125FIt was nothing more than my ego\x01",
            "talking when I told you to stay away\x01",
            "from Ouroboros.\x02\x03",

            "I was simply forcing my opinion, as\x01",
            "a man and as your father, onto you.\x02\x03",

            "#1120FScherazard made the point, ah...\x01",
            "quite clear on our trip over.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x101,
        "#586F#3PSchera...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x9,
        (
            "#021FI sure did! Don't worry, Estelle.\x01",
            "I'm completely behind you on this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x8,
        (
            "#6P#1125FIn all honesty, I thought I'd prepared for\x01",
            "this day for a long while, but...losing him\x01",
            "is worse than I could have even imagined.\x02\x03",

            "Thus, I...if nothing else, I wanted to keep\x01",
            "you from walking the path of thorns which\x01",
            "now lies before us.\x02\x03",

            "I couldn't bear the thought of you sharing\x01",
            "Lena's fate--of you losing your life to protect\x01",
            "someone else.\x02\x03",

            "#1120FBut, that is an insult. Not just to you, but to\x01",
            "your mother as well.\x02\x03",

            "I understand now, as terrifying as the\x01",
            "possibility still seems to me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x101,
        "#587F#3PDad...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x8,
        (
            "#6P#1122FI will be too busy with the work\x01",
            "of rebuilding the military to act\x01",
            "on my own.\x02\x03",

            "I fear that is exactly why they will\x01",
            "act now.\x02\x03",

            "This time, I really won't be able\x01",
            "to help you, Estelle.\x02\x03",

            "Are you sure this is what you want?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x101,
        (
            "#003F#3P...Yes.\x02\x03",

            "I know I've still got a lot to learn,\x01",
            "but I don't see any other way.\x02\x03",

            "#002FSo I'll do it.\x02\x03",

            "I'll put a stop to whatever horrible\x01",
            "thing this 'Ouroboros' has planned...\x01",
            "and I'll bring Joshua back home!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x8,
        (
            "#6P#1125FI see.\x02\x03",

            "#1122FThen there's nothing more to say.\x02\x03",

            "As a bracer, and as an independent woman...\x02\x03",

            "Do as you see fit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x101,
        "#586F#3PDad...\x02",
    )

    CloseMessageWindow()

    def lambda_28D4():
        OP_6D(70500, 0, 70000, 1000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_28D4)
    SetChrFlags(0x8, 0x40)
    OP_8E(0x101, 0x112B0, 0x0, 0x11008, 0xBB8, 0x0)
    SetChrPos(0x101, 70300, 0, 69450, 180)
    SetChrFlags(0x8, 0x8)
    SetChrChipByIndex(0x101, 24)
    SetChrFlags(0x101, 0x2)
    SetChrSubChip(0x101, 12)

    def lambda_292A():
        OP_6B(2700, 10000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_292A)

    def lambda_293A():
        OP_8C(0xFE, 225, 400)
        ExitThread()

    QueueWorkItem(0x142, 3, lambda_293A)
    OP_99(0x101, 0x0, 0x3, 0x3E8)
    Sleep(1000)

    ChrTalk(    #51
        0x101,
        "#3P#588F#40WI... I...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x8,
        (
            "#6P#1125FWell, no.\x01",
            "There is one more thing I must say.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x101,
        "#3P#587FHuh...?\x02",
    )

    CloseMessageWindow()
    OP_99(0x101, 0x3, 0x6, 0x3E8)
    Sleep(500)

    ChrTalk(    #54
        0x8,
        (
            "#6P#1122FEstelle. I'm counting on you.\x02\x03",

            "Bring back Joshua. Bring back\x01",
            "my damn fool of a son. Please.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x101,
        "#3P#586FAh...\x02",
    )

    CloseMessageWindow()
    OP_99(0x101, 0x9, 0xB, 0x3E8)
    OP_99(0x101, 0xB, 0x9, 0x3E8)
    Sleep(500)

    ChrTalk(    #56
        0x101,
        (
            "#3P#1080FRight... Piece of cake.\x02\x03",

            "I'll do it. I'll make sure we can\x01",
            "all live in this house again.\x02\x03",

            "#006FI WILL bring Joshua back--\x01",
            "no matter what stands in my way!\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(3000, 0, -1)
    OP_0D()
    OP_20(0xFA0)
    OP_21()
    Sleep(1500)
    OP_C4(0x1, 0x2)
    RemoveParty(0x41, 0xFF)
    SetChrChipByIndex(0x101, 65535)
    ClearChrFlags(0x101, 0x2)
    SetChrSubChip(0x101, 0)
    OP_C4(0x0, 0x10)
    FadeToBright(10, 0)
    OP_0D()
    PlayMovie(0x0, "ed6_2_op.avi", 0x7, 0x0)
    Sleep(2000)
    OP_56(0x2)
    FadeToDark(2000, 0, -1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x2D), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B75")
    OP_20(0x7D0)

    label("loc_2B75")

    OP_21()
    OP_0D()
    PlayMovie(0x1, "", 0x0, 0x0)
    Sleep(2000)
    OP_C4(0x1, 0x10)
    Sleep(1000)
    OP_AD(0x2400A3, 0x0, 0x0, 0x64)
    Sleep(4000)
    OP_56(0x2)
    OP_AE(0xC8)
    Sleep(2000)
    ClearMapFlags(0x2000000)
    NewScene("ED6_DT21/T5100   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_5_B70 end

    def Function_6_2BBB(): pass

    label("Function_6_2BBB")

    OP_BB(0x0, 0x0, 0x200042)
    OP_BB(0x0, 0x1, 0x1E)
    OP_BD()
    EventBegin(0x0)
    OP_6D(-7800, 200, 1380, 0)
    OP_67(0, 5720, -10000, 0)
    OP_6B(3300, 0)
    OP_6C(45000, 0)
    OP_6E(246, 0)
    OP_82(0x81, 0x0)
    OP_77(0xD0, 0xAE, 0x5D, 0x0, 0x0)
    SetChrPos(0x8, -8130, 200, 2260, 180)
    SetChrPos(0x9, -9800, 200, 2200, 180)
    SetChrFlags(0x101, 0x4)
    SetChrPos(0x101, -8220, 200, -630, 0)
    SetChrChipByIndex(0x8, 23)
    SetChrChipByIndex(0x9, 3)
    SetChrChipByIndex(0x101, 4)
    SetChrSubChip(0x8, 0)
    SetChrSubChip(0x9, 0)
    SetChrSubChip(0x101, 0)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    FadeToBright(1500, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #57
        0x8,
        (
            "#6P#1125FAs I said, Estelle, I have no intention of\x01",
            "stopping you.\x02\x03",

            "To be honest, however...you are no match for\x01",
            "the society, especially against their deadliest\x01",
            "agents. You simply lack the skills.\x02\x03",

            "#1122FSo I have a suggestion. Would you like to go\x01",
            "to Le Locle?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x101,
        "#4P#587FHuh? 'Le Locle'?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x8,
        (
            "#6P#1122FIt's a training ground run by the\x01",
            "Bracer Guild near the international\x01",
            "headquarters in the Leman State.\x02\x03",

            "Its base is set within a canyon that\x01",
            "contains a number of difficult training\x01",
            "facilities, covering skills of all kinds.\x02\x03",

            "#1125FRuins investigation techniques,\x01",
            "ranger, tracking and survival skills,\x01",
            "counter-terrorist operations...\x02\x03",

            "It is, bar none, the finest place on\x01",
            "the continent for teaching practical\x01",
            "bracer skills.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x101,
        (
            "#4P#505FWow, I never knew there was\x01",
            "a place like that.\x02\x03",

            "#003FBut, it's in Leman, isn't it?\x01",
            "So it's outside the country?\x02\x03",

            "#587FI don't...think I can leave Liberl\x01",
            "right now...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x9,
        (
            "#026F#6PWell, it's in a 'foreign country,' yes,\x01",
            "but it's only one day by airship.\x02\x03",

            "The training period lasts for...\x01",
            "about a month, I believe?\x02\x03",

            "#020FIf anything new comes up while you're\x01",
            "there, we'll send for you right away.\x02\x03",

            "How does that sound?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x101,
        "#4P#003FWell...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x8,
        (
            "#6P#1122FI recommend it, but the decision\x01",
            "is yours.\x02\x03",

            "You needn't answer today.\x01",
            "Take some time to think it over.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x101,
        (
            "#4P#500FNo, I've decided.\x02\x03",

            "#002FI'll take the training.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x9,
        "#023F#6POh, my...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x8,
        (
            "#6P#1120FExcellent. You sound rather determined.\x02\x03",

            "I get the feeling you've been thinking\x01",
            "about something like this for some time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x101,
        (
            "#4P#586FYeah, sorta.\x02\x03",

            "#003FTo be honest, looking back, I've just\x01",
            "been relying on Joshua this whole time.\x02\x03",

            "Whenever something happened, Joshua\x01",
            "would always guide me to the answer.\x02\x03",

            "But now...now I have to rely on my own\x01",
            "judgment.\x02\x03",

            "#002FSo, yes. I want to retrain myself at this\x01",
            "Le Locle place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x9,
        "#524F#6POh, Estelle...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x8,
        (
            "#6P#1125FI see.\x02\x03",

            "#1120FThen we'll file your application\x01",
            "to attend tomorrow.\x02\x03",

            "Rolent's guild branch will have\x01",
            "everything we need for it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x101,
        "#4P#006FOkay, then. Tomorrow.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x9,
        (
            "#021F#6PSay, Estelle.\x02\x03",

            "Once we're done with that, let's hop\x01",
            "back over to the department store in\x01",
            "Grancel for a minute, hmm?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x101,
        "#4P#004FThe department store? Why?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x9,
        (
            "#027F#6PWell, I haven't gotten you your\x01",
            "'senior bracer present' yet.\x02\x03",

            "And you, I think, are going to need\x01",
            "some new 'on the job' clothes... \x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrChipByIndex(0x101, 65535)
    ClearChrFlags(0x101, 0x4)
    OP_77(0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A2(0x10F1)
    NewScene("ED6_DT21/T5110   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_6_2BBB end

    def Function_7_35CE(): pass

    label("Function_7_35CE")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_35EE")
    Call(0, 19)
    FadeToBright(0, 0)
    Call(0, 20)

    label("loc_35EE")

    LoadEffect(0x0, "map\\\\mpsmk0.eff")
    LoadEffect(0x1, "map\\\\mp068_00.eff")
    OP_6D(-280, 0, 3400, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    SetChrFlags(0x101, 0x80)
    SetChrPos(0x103, -1410, 0, 2670, 90)
    SetChrChipByIndex(0x11, 25)
    SetChrSubChip(0x11, 1)
    SetChrPos(0x11, -600, 200, 2900, 0)
    SetChrPos(0xC, -640, 600, 4330, 0)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0xC, 0x4)
    SetChrFlags(0x11, 0x4)
    PlayEffect(0x0, 0x0, 0xFF, -630, 700, 2940, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0x1, 0xFF, -630, 0, 2940, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrFlags(0xF8, 0x4)
    SetChrFlags(0xF9, 0x4)
    SetChrPos(0xF8, -9800, 200, -630, 0)
    SetChrPos(0xF9, -8200, 200, -630, 0)
    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_END)),
        (5, "loc_375A"),
        (3, "loc_3762"),
        (4, "loc_376A"),
        (6, "loc_3772"),
        (7, "loc_377A"),
        (SWITCH_DEFAULT, "loc_3782"),
    )


    label("loc_375A")

    SetChrChipByIndex(0xF8, 7)
    Jump("loc_3782")

    label("loc_3762")

    SetChrChipByIndex(0xF8, 8)
    Jump("loc_3782")

    label("loc_376A")

    SetChrChipByIndex(0xF8, 9)
    Jump("loc_3782")

    label("loc_3772")

    SetChrChipByIndex(0xF8, 10)
    Jump("loc_3782")

    label("loc_377A")

    SetChrChipByIndex(0xF8, 11)
    Jump("loc_3782")

    label("loc_3782")

    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_END)),
        (5, "loc_379F"),
        (3, "loc_37A7"),
        (4, "loc_37AF"),
        (6, "loc_37B7"),
        (7, "loc_37BF"),
        (SWITCH_DEFAULT, "loc_37C7"),
    )


    label("loc_379F")

    SetChrChipByIndex(0xF9, 7)
    Jump("loc_37C7")

    label("loc_37A7")

    SetChrChipByIndex(0xF9, 8)
    Jump("loc_37C7")

    label("loc_37AF")

    SetChrChipByIndex(0xF9, 9)
    Jump("loc_37C7")

    label("loc_37B7")

    SetChrChipByIndex(0xF9, 10)
    Jump("loc_37C7")

    label("loc_37BF")

    SetChrChipByIndex(0xF9, 11)
    Jump("loc_37C7")

    label("loc_37C7")

    FadeToBright(1500, 0)

    def lambda_37D6():
        OP_6D(-7440, 0, 2710, 5000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_37D6)
    Sleep(4000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_82(0x0, 0x0)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/T0300   ._SN", 103, 0, 0)
    IdleLoop()
    Return()

    # Function_7_35CE end

    def Function_8_3808(): pass

    label("Function_8_3808")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3828")
    Call(0, 19)
    FadeToBright(0, 0)
    Call(0, 20)

    label("loc_3828")

    OP_6D(-8260, 200, 1880, 0)
    OP_67(0, 4880, -10000, 0)
    OP_6B(2740, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x103, 0x4)
    SetChrFlags(0xF8, 0x4)
    SetChrFlags(0xF9, 0x4)
    SetChrPos(0x103, -8130, 200, 2260, 180)
    SetChrPos(0x101, -9800, 200, 2200, 180)
    SetChrPos(0xF8, -9800, 200, -630, 0)
    SetChrPos(0xF9, -8200, 200, -630, 0)
    SetChrChipByIndex(0x101, 6)
    SetChrChipByIndex(0x103, 3)
    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_END)),
        (5, "loc_38E4"),
        (3, "loc_38EC"),
        (4, "loc_38F4"),
        (6, "loc_38FC"),
        (7, "loc_3904"),
        (SWITCH_DEFAULT, "loc_390C"),
    )


    label("loc_38E4")

    SetChrChipByIndex(0xF8, 7)
    Jump("loc_390C")

    label("loc_38EC")

    SetChrChipByIndex(0xF8, 8)
    Jump("loc_390C")

    label("loc_38F4")

    SetChrChipByIndex(0xF8, 9)
    Jump("loc_390C")

    label("loc_38FC")

    SetChrChipByIndex(0xF8, 10)
    Jump("loc_390C")

    label("loc_3904")

    SetChrChipByIndex(0xF8, 11)
    Jump("loc_390C")

    label("loc_390C")

    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_END)),
        (5, "loc_3929"),
        (3, "loc_3931"),
        (4, "loc_3939"),
        (6, "loc_3941"),
        (7, "loc_3949"),
        (SWITCH_DEFAULT, "loc_3951"),
    )


    label("loc_3929")

    SetChrChipByIndex(0xF9, 7)
    Jump("loc_3951")

    label("loc_3931")

    SetChrChipByIndex(0xF9, 8)
    Jump("loc_3951")

    label("loc_3939")

    SetChrChipByIndex(0xF9, 9)
    Jump("loc_3951")

    label("loc_3941")

    SetChrChipByIndex(0xF9, 10)
    Jump("loc_3951")

    label("loc_3949")

    SetChrChipByIndex(0xF9, 11)
    Jump("loc_3951")

    label("loc_3951")

    SetChrChipByIndex(0x11, 25)
    SetChrSubChip(0x11, 1)
    SetChrPos(0x11, -600, 200, 2900, 0)
    SetChrPos(0xC, -9100, 800, 800, 0)
    SetChrPos(0xC, -640, 600, 4330, 0)
    SetChrPos(0xD, -9800, 800, 1100, 0)
    SetChrPos(0xE, -8500, 800, 1100, 0)
    SetChrPos(0xF, -9800, 800, 100, 0)
    SetChrPos(0x10, -8500, 800, 100, 0)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    FadeToBright(1500, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #74
        0x101,
        (
            "#1016F#6PAhhhhhh... It's always relaxing to get\x01",
            "back home.\x02\x03",

            "#1017FI kinda wonder how much of that is 'cause\x01",
            "we're out of that fog, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x103,
        "#021FHThat's part of it, I'm sure.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3C82")

    ChrTalk(    #76
        0x106,
        (
            "#051FY'know, Scherazard.\x02\x03",

            "You sure do seem to know your way\x01",
            "around this place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0x103,
        (
            "#524FOf course I do.\x02\x03",

            "I've known this house for...a long time.\x01",
            "A very long time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0x101,
        (
            "#1015F#6PYeah, you've been coming over since\x01",
            "Mom was alive, so...\x02\x03",

            "#1001FThat's over ten years.\x01",
            "Wow, it HAS been a while!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x103,
        "#526FAbout that, give or take a few gray hairs.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0x107,
        (
            "#560FSchera, you were in a circus\x01",
            "troupe, right?\x02\x03",

            "How did you meet Estelle?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4E0E")

    label("loc_3C82")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3E8E")

    ChrTalk(    #81
        0x106,
        (
            "#051FY'know, Scherazard.\x02\x03",

            "You sure do seem to know your way\x01",
            "around this place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0x103,
        (
            "#524FOf course I do.\x02\x03",

            "I've known this house for...a long time.\x01",
            "A very long time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0x101,
        (
            "#1015F#6PYeah, you've been coming over since\x01",
            "Mom was alive, so...\x02\x03",

            "#1001FThat's over ten years.\x01",
            "Wow, it HAS been a while!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0x103,
        "#526FAbout that, give or take a few gray hairs.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0x104,
        (
            "#030FI believe you were part of a traveling\x01",
            "circus troupe in your early life, yes?\x02\x03",

            "I must confess, I'm curious to hear how\x01",
            "you met Estelle.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4E0E")

    label("loc_3E8E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4082")

    ChrTalk(    #86
        0x106,
        (
            "#051FY'know, Scherazard.\x02\x03",

            "You sure do seem to know your way\x01",
            "around this place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0x103,
        (
            "#524FOf course I do.\x02\x03",

            "I've known this house for...a long time.\x01",
            "A very long time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0x101,
        (
            "#1015F#6PYeah, you've been coming over since\x01",
            "Mom was alive, so...\x02\x03",

            "#1001FThat's over ten years.\x01",
            "Wow, it HAS been a while!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0x103,
        "#526FAbout that, give or take a few gray hairs.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0x105,
        (
            "#048FScherazard, you were part of a traveling\x01",
            "circus, weren't you?\x02\x03",

            "How did you come to make Estelle's\x01",
            "acquaintance?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4E0E")

    label("loc_4082")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_425F")

    ChrTalk(    #91
        0x106,
        (
            "#051FY'know, Scherazard.\x02\x03",

            "You sure do seem to know your way\x01",
            "around this place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0x103,
        (
            "#524FOf course I do.\x02\x03",

            "I've known this house for...a long time.\x01",
            "A very long time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0x101,
        (
            "#1015F#6PYeah, you've been coming over since\x01",
            "Mom was alive, so...\x02\x03",

            "#1001FThat's over ten years.\x01",
            "Wow, it HAS been a while!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0x103,
        "#526FAbout that, give or take a few gray hairs.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0x108,
        (
            "#070FAs I recall, you were in a traveling\x01",
            "circus, right?\x02\x03",

            "How did you end up meeting Estelle?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4E0E")

    label("loc_425F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4447")

    ChrTalk(    #96
        0x104,
        (
            "#030FIf I may, Schera.\x02\x03",

            "You stride through this home with a\x01",
            "familiarity equal to that of it being\x01",
            "your own.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0x103,
        (
            "#524FOf course I do.\x02\x03",

            "I've known this house for...a long time.\x01",
            "A very long time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0x101,
        (
            "#1015F#6PYeah, you've been coming over since\x01",
            "Mom was alive, so...\x02\x03",

            "#1001FThat's over ten years.\x01",
            "Wow, it HAS been a while!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0x103,
        "#526FAbout that, give or take a few gray hairs.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0x107,
        (
            "#560FSchera, you were in a circus troupe,\x01",
            "right?\x02\x03",

            "How did you meet Estelle?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4E0E")

    label("loc_4447")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_462A")

    ChrTalk(    #101
        0x107,
        (
            "#560FSchera, you know Estelle's house\x01",
            "really well, don't you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0x103,
        (
            "#524FOf course I do.\x02\x03",

            "I've known this house for...a long time.\x01",
            "A very long time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0x101,
        (
            "#1015F#6PYeah, you've been coming over since\x01",
            "Mom was alive, so...\x02\x03",

            "#1001FThat's over ten years.\x01",
            "Wow, it HAS been a while!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0x103,
        "#526FAbout that, give or take a few gray hairs.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0x105,
        (
            "#048FScherazard, you were part of a traveling\x01",
            "circus, weren't you?\x02\x03",

            "How did you come to make Estelle's\x01",
            "acquaintance?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4E0E")

    label("loc_462A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_47FB")

    ChrTalk(    #106
        0x107,
        (
            "#560FSchera, you really know Estelle's house\x01",
            "really well, don't you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0x103,
        (
            "#524FOf course I do.\x02\x03",

            "I've known this house for...a long time.\x01",
            "A very long time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0x101,
        (
            "#1015F#6PYeah, you've been coming over since\x01",
            "Mom was alive, so...\x02\x03",

            "#1001FThat's over ten years.\x01",
            "Wow, it HAS been a while!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0x103,
        "#526FAbout that, give or take a few gray hairs.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0x108,
        (
            "#070FAs I recall, you were in a traveling\x01",
            "circus, right?\x02\x03",

            "How'd you end up meeting Estelle?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4E0E")

    label("loc_47FB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4A0C")

    ChrTalk(    #111
        0x104,
        (
            "#030FIf I may, Schera.\x02\x03",

            "You stride through this home with a\x01",
            "familiarity equal to that of it being\x01",
            "your own.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0x103,
        (
            "#524FOf course I do.\x02\x03",

            "I've known this house for...a long time.\x01",
            "A very long time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0x101,
        (
            "#1015F#6PYeah, you've been coming over since\x01",
            "Mom was alive, so...\x02\x03",

            "#1001FThat's over ten years.\x01",
            "Wow, it HAS been a while!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0x103,
        "#526FAbout that, give or take a few gray hairs.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0x105,
        (
            "#048FScherazard, you were part of a traveling\x01",
            "circus, weren't you?\x02\x03",

            "How did you come to make Estelle's\x01",
            "acquaintance?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4E0E")

    label("loc_4A0C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4C04")

    ChrTalk(    #116
        0x104,
        (
            "#030FIf I may, Schera.\x02\x03",

            "You stride through this home with a\x01",
            "familiarity equal to that of it being\x01",
            "your own.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0x103,
        (
            "#524FOf course I do.\x02\x03",

            "I've known this house for...a long time.\x01",
            "A very long time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0x101,
        (
            "#1015F#6PYeah, you've been coming over since\x01",
            "Mom was alive, so...\x02\x03",

            "#1001FThat's over ten years.\x01",
            "Wow, it HAS been a while!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0x103,
        "#526FAbout that, give or take a few gray hairs.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0x108,
        (
            "#070FAs I recall, you were in a traveling\x01",
            "circus, right?\x02\x03",

            "How'd you end up meeting Estelle?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4E0E")

    label("loc_4C04")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4E0E")

    ChrTalk(    #121
        0x108,
        (
            "#070FIf you don't mind me saying, Scherazard.\x02\x03",

            "You glide through this house\x01",
            "like you know every corner.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0x103,
        (
            "#524FOf course I do.\x02\x03",

            "I've known this house for...a long time.\x01",
            "A very long time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0x101,
        (
            "#1015F#6PYeah, you've been coming over since\x01",
            "Mom was alive, so...\x02\x03",

            "#1001FThat's over ten years.\x01",
            "Wow, it HAS been a while!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0x103,
        "#526FAbout that, give or take a few gray hairs.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0x105,
        (
            "#040FScherazard, you were part of a traveling\x01",
            "circus, weren't you?\x02\x03",

            "How did you come to make Estelle's\x01",
            "acquaintance?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4E0E")


    ChrTalk(    #126
        0x103,
        "#021FWell, you see--\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 1)
    Sleep(300)
    OP_62(0x101, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)

    ChrTalk(    #127
        0x101,
        "#1004F#3PWait, Schera, you don't need to--\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x103, 0)
    Sleep(75)
    SetChrSubChip(0x103, 2)

    ChrTalk(    #128
        0x103,
        "#027FIt's fine. It's an old story.\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x103, 0)
    OP_63(0x101)
    Sleep(500)

    ChrTalk(    #129
        0x103,
        (
            "#026FIt would've been...\x01",
            "About twelve years ago now.\x02\x03",

            "Our troupe had come to Rolent to perform.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(1000)
    SetMessageWindowPos(90, 330, -1, -1)
    SetChrName("Scherazard")

    AnonymousTalk(    #130
        (
            "\x07\x00#027FEstelle, at that point, was even more fearless and\x01",
            "curious than she is now.\x02\x03",

            "After one of our shows, she strode into our tents\x01",
            "with purpose--the purpose of playing!\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_AD(0x24007D, 0x0, 0x0, 0x1F4)
    Sleep(1500)
    SetMessageWindowPos(90, 330, -1, -1)
    SetChrName("Scherazard")

    AnonymousTalk(    #131
        (
            "#524FCircus troupes...usually get met with some\x01",
            "suspicion by residents of a town outside of\x01",
            "performances, you see.\x02\x03",

            "As a result, we weren't really sure what to do\x01",
            "at first with this girl who came to visit us,\x01",
            "but, you see...\x02\x03",

            "#021FEstelle wasn't exactly a timid girl.\x02\x03",

            "She kept coming over every day, and everyone\x01",
            "came to really love her.\x02\x03",

            "#526FMyself especially, of course.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_AE(0x1F4)
    Sleep(1000)
    OP_AD(0x24007E, 0x0, 0x0, 0x1F4)
    Sleep(1500)
    SetMessageWindowPos(90, 330, -1, -1)
    SetChrName("Scherazard")

    AnonymousTalk(    #132
        (
            "#026FOne day, Estelle didn't want to go home\x01",
            "until long after the sun had set.\x02\x03",

            "Since there wasn't any other choice, I ended\x01",
            "up being the one who took her home.\x02\x03",

            "#027FThat's the day I met Cassius and Lena...\x01",
            "Ah, pardon, Lena is Estelle's late mother.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_AE(0x1F4)
    Sleep(1000)
    SetChrSubChip(0x101, 0)
    SetChrSubChip(0x103, 0)
    FadeToBright(500, 0)
    OP_0D()
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_532E")

    ChrTalk(    #133
        0x107,
        "#061FWow, that sounds like Estelle, all right!\x02",
    )

    CloseMessageWindow()
    Jump("loc_5452")

    label("loc_532E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_536F")

    ChrTalk(    #134
        0x106,
        "#051FHeh. Yeah, that sounds kinda familiar.\x02",
    )

    CloseMessageWindow()
    Jump("loc_5452")

    label("loc_536F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_53B8")

    ChrTalk(    #135
        0x104,
        (
            "#031FHm. A familiar story, in a way,\x01",
            "to be certain.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5452")

    label("loc_53B8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5403")

    ChrTalk(    #136
        0x105,
        (
            "#048FHaha... Yes, that certainly sounds\x01",
            "like Estelle.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5452")

    label("loc_5403")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5452")

    ChrTalk(    #137
        0x108,
        (
            "#071FHaha! Yes, I'd say that sounds like\x01",
            "Estelle, all right.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5452")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5490")

    ChrTalk(    #138
        0x107,
        "#061FHeehee, Estelle, you're incredible!\x02",
    )

    CloseMessageWindow()
    Jump("loc_55E9")

    label("loc_5490")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_54E7")

    ChrTalk(    #139
        0x106,
        (
            "#051FHeh, yeah, sounds like Estelle's\x01",
            "been gutsy from the get-go.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_55E9")

    label("loc_54E7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_554B")

    ChrTalk(    #140
        0x104,
        (
            "#031FHeh. So the fundamentals of our Estelle's\x01",
            "bravery were present even then.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_55E9")

    label("loc_554B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_559D")

    ChrTalk(    #141
        0x105,
        (
            "#048FHaha, so Estelle was bold and fearless\x01",
            "even as a child?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_55E9")

    label("loc_559D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_55E9")

    ChrTalk(    #142
        0x108,
        (
            "#071FHaha! It seems Estelle was fearless\x01",
            "even as a child.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_55E9")


    ChrTalk(    #143
        0x101,
        (
            "#1016F#6PAh-hahaha... Well...\x02\x03",

            "I don't really remember that much of it\x01",
            "since I was, like, FOUR back then, but...\x02\x03",

            "#1017FI do remember Schera would come by our\x01",
            "house any time the circus was in town\x01",
            "after that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0x103,
        "#021FMm-hmm. That's right.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5844")

    ChrTalk(    #145
        0x106,
        (
            "#050FBut, uh, Scherazard.\x02\x03",

            "If you were part of a traveling circus,\x01",
            "how'd you end up in Liberl as a bracer?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #146
        0x103,
        (
            "#524FYou could say...a lot happened.\x02\x03",

            "Eight years ago, when I decided\x01",
            "I wanted to be a bracer, I came to\x01",
            "Liberl to ask Cassius for help.\x02\x03",

            "I've been in Liberl ever since.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0x106,
        "#053FI get it... So you're tied to the old man.\x02",
    )

    CloseMessageWindow()
    Jump("loc_5C7D")

    label("loc_5844")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_59C4")

    ChrTalk(    #148
        0x104,
        (
            "#030FI must admit some confusion, though,\x01",
            "Schera.\x02\x03",

            "From the sound of it, your life in the\x01",
            "circus was a happy one. What led you\x01",
            "to Liberl and service as a bracer?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0x103,
        (
            "#524FYou could say...a lot happened.\x02\x03",

            "Eight years ago, when I decided\x01",
            "I wanted to be a bracer, I came to\x01",
            "Liberl to ask Cassius for help.\x02\x03",

            "I've been in Liberl ever since.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #150
        0x104,
        "#035FHmmm... I see.\x02",
    )

    CloseMessageWindow()
    Jump("loc_5C7D")

    label("loc_59C4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5B0F")

    ChrTalk(    #151
        0x108,
        (
            "#073FHmm. Though, Scherazard...\x02\x03",

            "How did you leave the circus and come\x01",
            "to live in Liberl as a bracer?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #152
        0x103,
        (
            "#524FYou could say...a lot happened.\x02\x03",

            "Eight years ago, when I decided\x01",
            "I wanted to be a bracer, I came to\x01",
            "Liberl to ask Cassius for help.\x02\x03",

            "I've been in Liberl ever since.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0x108,
        "#070FI see now, all right.\x02",
    )

    CloseMessageWindow()
    Jump("loc_5C7D")

    label("loc_5B0F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5C7D")

    ChrTalk(    #154
        0x107,
        (
            "#064FUm, it sounds like you visited a lot of\x01",
            "different countries as part of the circus\x01",
            "and liked it, right?\x02\x03",

            "So why'd you come to Liberl to be a bracer?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #155
        0x103,
        (
            "#524FYou could say...a lot happened.\x02\x03",

            "Eight years ago, when I decided\x01",
            "I wanted to be a bracer, I came to\x01",
            "Liberl to ask Cassius for help.\x02\x03",

            "I've been in Liberl ever since.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #156
        0x107,
        "#560FOh, wow!\x02",
    )

    CloseMessageWindow()

    label("loc_5C7D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5CD7")

    ChrTalk(    #157
        0x105,
        (
            "#044FOh, that reminds me.\x02\x03",

            "#542FWas, um, Joshua here in those days?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5DFF")

    label("loc_5CD7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5D2F")

    ChrTalk(    #158
        0x107,
        (
            "#064FOh, um, I was curious!\x02\x03",

            "#560FWas, um, Joshua here back then?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5DFF")

    label("loc_5D2F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5D86")

    ChrTalk(    #159
        0x108,
        (
            "#074FOut of curiosity...\x02\x03",

            "#070FWas Joshua around here back then?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5DFF")

    label("loc_5D86")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5DFF")

    ChrTalk(    #160
        0x104,
        (
            "#035FHmmm...\x01",
            "One thing I've been curious about.\x02\x03",

            "#030FWas Joshua part of the household\x01",
            "in those days?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5DFF")


    ChrTalk(    #161
        0x101,
        (
            "#1025F#6POh, um, no.\x02\x03",

            "Joshua came to live with us\x01",
            "three years after all that.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 1)
    Sleep(300)

    ChrTalk(    #162
        0x101,
        (
            "#1011F#6PActually, he showed up when you\x01",
            "were in Grancel during your junior\x01",
            "bracer tour, didn't he?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #163
        0x103,
        (
            "#027FThat he did.\x02\x03",

            "#021FI wandered Liberl, spreading good will and flowers\x01",
            "as a bracer does, and returned home to find a boy\x01",
            "I'd never seen living with Cassius and Estelle.\x02\x03",

            "To say it was a bit of a shock would be an\x01",
            "understatement.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1500, 0, -1)
    OP_0D()
    Sleep(500)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #164
        (
            "\x07\x05Estelle and the others enjoyed some small talk as\x01",
            "the morning sun tried to pierce the mist...\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #165
        (
            "\x07\x05Finally, with a little tea for the road, they left the\x01",
            "Bright house.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_82(0x81, 0x0)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrPos(0x0, -1160, 0, -2760, 171)
    SetChrPos(0x1, -1160, 0, -2760, 171)
    SetChrPos(0x2, -1160, 0, -2760, 171)
    SetChrPos(0x3, -1160, 0, -2760, 171)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0x103, 65535)
    SetChrChipByIndex(0xF8, 65535)
    SetChrChipByIndex(0xF9, 65535)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x103, 0x4)
    ClearChrFlags(0xF8, 0x4)
    ClearChrFlags(0xF9, 0x4)
    OP_6D(-1160, 0, -2760, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    Sleep(1000)
    FadeToBright(1000, 0)
    OP_A2(0x180D)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_617C")
    OP_28(0x8F, 0x1, 0x2000)
    OP_28(0x8F, 0x1, 0x4000)
    Jump("loc_6182")

    label("loc_617C")

    OP_28(0x8F, 0x1, 0x100)

    label("loc_6182")

    EventEnd(0x0)
    Return()

    # Function_8_3808 end

    def Function_9_6185(): pass

    label("Function_9_6185")

    EventBegin(0x0)
    OP_DB()
    SetChrChipByIndex(0x11, 25)
    SetChrSubChip(0x11, 1)
    SetChrPos(0x11, -600, 200, 2900, 0)
    SetChrPos(0xD, -9600, 800, 1100, 0)
    SetChrPos(0x14, -9950, 800, 1250, 0)
    SetChrPos(0xE, -8100, 800, 1100, 0)
    SetChrPos(0x13, -8500, 800, 1250, 0)
    SetChrPos(0xF, -8600, 800, 100, 0)
    SetChrPos(0x15, -8100, 800, 290, 0)
    SetChrPos(0x16, -9450, 800, 600, 0)
    SetChrPos(0xC, -640, 600, 4330, 0)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0x11, 0x80)
    LoadEffect(0x0, "map\\\\mpsmk0.eff")
    LoadEffect(0x1, "map\\\\mp068_00.eff")
    SetChrFlags(0x101, 0x4)
    SetChrPos(0x101, -8290, 200, -480, 0)
    SetChrChipByIndex(0x101, 12)
    SetChrPos(0x8, -9790, 200, 2290, 180)
    SetChrChipByIndex(0x8, 13)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x12, -1570, 0, 2810, 90)
    SetChrChipByIndex(0x12, 14)
    ClearChrFlags(0x12, 0x80)
    OP_6D(-1610, 200, 3420, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(338, 0)
    PlayEffect(0x0, 0x0, 0xFF, -630, 750, 2940, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0x1, 0xFF, -630, 0, 2940, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)
    OP_82(0x0, 0x0)
    Sleep(1000)
    OP_8E(0x12, 0xFFFFFA1A, 0x0, 0x1040, 0x3E8, 0x0)
    OP_8C(0x12, 90, 400)
    Sleep(300)
    OP_9F(0xC, 0xFF, 0xFF, 0xFF, 0x0, 0xC8)
    SetChrChipByIndex(0x12, 15)
    SetChrSubChip(0x12, 3)
    Sleep(300)
    OP_8C(0x12, 0, 300)
    OP_8C(0x12, 270, 300)

    def lambda_63DB():
        OP_6D(-8470, 200, 1050, 4000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_63DB)

    def lambda_63F3():
        OP_6E(270, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_63F3)
    OP_8F(0x12, 0xFFFFE4A8, 0xC8, 0x366, 0x7D0, 0x0)
    Sleep(500)
    SetChrPos(0xC, -7750, 800, 800, 0)
    OP_9F(0xC, 0xFF, 0xFF, 0xFF, 0xFF, 0xC8)
    SetChrChipByIndex(0x12, 14)
    Sleep(500)
    OP_62(0x101, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(100)
    OP_62(0x8, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    OP_8E(0x12, 0xFFFFE4A8, 0xC8, 0x834, 0x3E8, 0x0)
    OP_8E(0x12, 0xFFFFE340, 0xC8, 0x834, 0x3E8, 0x0)
    Fade(500)
    SetChrPos(0x12, -8240, 200, 2200, 180)
    SetChrChipByIndex(0x12, 16)
    OP_0D()
    Sleep(1000)
    OP_DC()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #166
        "\x07\x05Mornings spent together as a family, whole and complete...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F3)
    NewScene("ED6_DT21/T0300   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_9_6185 end

    def Function_10_6535(): pass

    label("Function_10_6535")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x307, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6544")
    Call(0, 11)
    Jump("loc_6548")

    label("loc_6544")

    Call(0, 15)

    label("loc_6548")

    Return()

    # Function_10_6535 end

    def Function_11_6549(): pass

    label("Function_11_6549")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x306, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6686")
    Fade(1000)
    OP_6D(73010, 0, -730, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    SetChrPos(0x101, 73010, 0, -730, 0)
    OP_0D()
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    OP_22(0x74, 0x0, 0x64)
    Sleep(500)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #167
        "\x07\x05The door is locked.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #168
        0x101,
        (
            "#293F#6PHuh?\x02\x03",

            "Was it this room?\x02\x03",

            "#296FUmmmm...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x101)
    Sleep(300)

    ChrTalk(    #169
        0x101,
        (
            "#291F#6P...I dunno!\x02\x03",

            "#290FMaybe I should ask Daddy!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1835)
    Jump("loc_66FA")

    label("loc_6686")

    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    OP_22(0x74, 0x0, 0x64)
    Sleep(500)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #170
        "\x07\x05The door is locked.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #171
        0x101,
        "#290FMaybe I should go ask Daddy!\x02",
    )

    CloseMessageWindow()

    label("loc_66FA")

    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Return()

    # Function_11_6549 end

    def Function_12_6702(): pass

    label("Function_12_6702")

    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x8, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0x8)
    ClearChrFlags(0x8, 0x10)
    TurnDirection(0x8, 0x0, 0)
    OP_51(0x8, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x8, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x8, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_6792")
    Jump("loc_67D4")

    label("loc_6792")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_67AE")
    OP_51(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_67D4")

    label("loc_67AE")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_67CA")
    OP_51(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_67D4")

    label("loc_67CA")

    OP_51(0x8, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_67D4")

    OP_51(0x8, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x8, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x8, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x306, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6B1C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_69F0")

    ChrTalk(    #172
        0x8,
        (
            "#080FWhat is it, Estelle?\x02\x03",

            "Do you want to play with Papa,\x01",
            "after all?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #173
        0x101,
        "#291FUmmm, not really!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #174
        0x8,
        "#083FEr, I see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #175
        0x101,
        "#290FDaddy, what'cha reading?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #176
        0x8,
        (
            "#084FAh, this?\x02\x03",

            "#080FIt's called 'The Great Bracer\x01",
            "guildhouses of Zemuria.'\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #177
        0x101,
        "#293FBray-zer?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #178
        0x8,
        (
            "#080FYes, although this book might be a bit\x01",
            "hard for you to understand, Estelle.\x02\x03",

            "#081FI know. How about I read you a picture\x01",
            "book like Mama does?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #179
        0x101,
        "#291FMmm... No, not right now!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #180
        0x8,
        "#083FErm. Well, if you wish.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_6B19")

    label("loc_69F0")


    ChrTalk(    #181
        0x8,
        (
            "#085FThe only Bracer Guild chapter\x01",
            "house in Liberl is in Grancel...\x02\x03",

            "If we had a guildhouse in each major city,\x01",
            "it would remove a tremendous amount of\x01",
            "pressure from the army in peacekeeping.\x02\x03",

            "#082FHmm. When I return to Leiston, I should\x01",
            "have another go at convincing Morgan it's\x01",
            "a good idea.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6B19")

    Jump("loc_73AF")

    label("loc_6B1C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x307, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6E86")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x306, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6E30")
    EventBegin(0x0)
    Fade(1000)
    OP_6D(3860, 0, 71420, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    SetChrPos(0x101, 4250, 0, 71160, 285)
    SetChrSubChip(0x8, 1)
    OP_0D()
    Sleep(200)

    ChrTalk(    #182
        0x101,
        (
            "#290F#4PHeeey, Daddy?\x02\x03",

            "What's in the room on the second floor?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #183
        0x8,
        (
            "#080F#6PAh, the one near the bedroom?\x01",
            "That's our storage room.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #184
        0x101,
        "#293F#4PStowwage room?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #185
        0x8,
        (
            "#080F#6PStorage, Estelle. It's a place where\x01",
            "you keep things you don't use much.\x01",
            "Like a toy chest, but bigger.\x02\x03",

            "We haven't been in there since...\x01",
            "How long now? It must be covered\x01",
            "in dust and cobwebs.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #186
        0x101,
        (
            "#296F#4POooooh.\x02\x03",

            "#290FWhere's the key to it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #187
        0x8,
        (
            "#080F#6PAh, it's...\x02\x03",

            "#084F...Wait, what are you going to do\x01",
            "in there?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #188
        0x101,
        "#291F#4PI wanna go exploring!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #189
        0x8,
        (
            "#083F#6PHmmmm...\x01",
            "Well, I suppose it can't hurt.\x02\x03",

            "#080FMama keeps the key to it.\x02\x03",

            "Go on and ask her for it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #190
        0x101,
        "#291F#4POkay!\x02",
    )

    CloseMessageWindow()
    OP_82(0x1, 0x0)
    OP_A2(0x1836)
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Jump("loc_6E83")

    label("loc_6E30")


    ChrTalk(    #191
        0x8,
        (
            "#080FMama keeps the key to the storeroom,\x01",
            "Estelle.\x02\x03",

            "Go on and ask her for it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6E83")

    Jump("loc_73AF")

    label("loc_6E86")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x307, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7026")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6F7F")

    ChrTalk(    #192
        0x8,
        (
            "#080FOho, you found the key, did you?\x02\x03",

            "Remember, Estelle, it's probably going to\x01",
            "be very dusty so try not to drag too much\x01",
            "around the rest of the house.\x02\x03",

            "Your mother will have a fit otherwise.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #193
        0x101,
        "#291FI promise I won't!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_7023")

    label("loc_6F7F")


    ChrTalk(    #194
        0x8,
        (
            "#080FRemember, Estelle, it's probably going to\x01",
            "be very dusty so try not to drag too much\x01",
            "around the rest of the house.\x02\x03",

            "Your mother will have a fit otherwise.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7023")

    Jump("loc_73AF")

    label("loc_7026")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_733F")

    ChrTalk(    #195
        0x8,
        (
            "#084FHmmm? What's that, Estelle?\x02\x03",

            "That's a very lovely harmonica you have there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #196
        0x101,
        (
            "#290FIt was in the storeroom.\x02\x03",

            "Is it yours, Daddy?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #197
        0x8,
        (
            "#080FIt isn't, but...\x02\x03",

            "I don't believe it's Lena's, either.\x01",
            "I wonder whose it is?\x02\x03",

            "#084FMay I see it for a moment, Estelle?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #198
        0x101,
        "#293FUmmmm, okay.\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)

    AnonymousTalk(    #199
        "\x07\x05Estelle handed Cassius the harmonica.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(    #200
        0x8,
        (
            "#084FLet me see, the stamp of...Rieveldt?\x01",
            "Why, this was made in Erebonia!\x02\x03",

            "#083FNow I REALLY have no idea whose\x01",
            "this might be.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #201
        0x101,
        "#293FHuuuuh?\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)

    AnonymousTalk(    #202
        (
            "\x07\x05Cassius handed the harmonica back to Estelle,\x01",
            "wrapping her fingers around it with a gentle motion.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(    #203
        0x8,
        (
            "#080FWell! You're the one who found it,\x01",
            "so perhaps it is a gift from Aidios,\x01",
            "hmm?\x02\x03",

            "Why not try playing it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #204
        0x101,
        "#290FOkay!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_73AF")

    label("loc_733F")


    ChrTalk(    #205
        0x8,
        (
            "#080FWell! You're the one who found it,\x01",
            "so perhaps it is a gift from Aidios,\x01",
            "hmm?\x02\x03",

            "Why not try playing it?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_73AF")

    SetChrSubChip(0x8, 0)
    TalkEnd(0x8)
    Return()

    # Function_12_6702 end

    def Function_13_73B8(): pass

    label("Function_13_73B8")

    TalkBegin(0x12)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x306, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_75D4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7524")

    ChrTalk(    #206
        0x12,
        (
            "#860FLet me see, we had stew yesterday, so...\x02\x03",

            "#861FTonight we'll have omelets, I think.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #207
        0x101,
        (
            "#293FReally?!\x02\x03",

            "#291FYaaay, yaaaay!\x01",
            "Mama's omelets are the best!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #208
        0x12,
        (
            "#864FOh, what's this? I didn't know you liked\x01",
            "them THAT much.\x02\x03",

            "#866FHeehee. Mama and Papa like omelets,\x01",
            "too. I suppose it's one of those things\x01",
            "you've inherited, sweetie.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)
    Jump("loc_75D1")

    label("loc_7524")


    ChrTalk(    #209
        0x12,
        (
            "#865FTonight will be chicken omelets\x01",
            "with some soft-cooked eggs.\x02\x03",

            "And with it...some onion gratin, and a\x01",
            "salad with wild vegetables.\x02\x03",

            "I hope that sounds good, sweetie.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_75D1")

    Jump("loc_7999")

    label("loc_75D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x306, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7642")

    ChrTalk(    #210
        0x12,
        (
            "#860FI'm sorry, sweetie.\x02\x03",

            "I'm cooking right now, so please try not\x01",
            "to distract me, all right?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7999")

    label("loc_7642")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x307, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x307, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_77BA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7728")

    ChrTalk(    #211
        0x12,
        (
            "#861FLooks like you found the key,\x01",
            "sweetie.\x02\x03",

            "#860FDon't move anything heavy or touch\x01",
            "anything sharp, all right?\x02\x03",

            "And once you're done exploring, remember\x01",
            "to wash your hands and face.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #212
        0x101,
        "#291FOkay!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x4)
    Jump("loc_77B7")

    label("loc_7728")


    ChrTalk(    #213
        0x12,
        (
            "#860FDon't move anything heavy or touch\x01",
            "anything sharp, all right?\x02\x03",

            "And once you're done exploring, remember\x01",
            "to wash your hands and face.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_77B7")

    Jump("loc_7999")

    label("loc_77BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x307, 3)), scpexpr(EXPR_END)), "loc_7999")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_790C")

    ChrTalk(    #214
        0x12,
        (
            "#864FOh, my goodness, that's a lovely harmonica.\x02\x03",

            "#865FDid you find that in our storage room?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #215
        0x101,
        (
            "#291FAhaha! Yep!\x02\x03",

            "#290FMama, Mama, is it yours?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #216
        0x12,
        (
            "#860FHmmmm. No, I don't remember ever owning\x01",
            "a harmonica.\x02\x03",

            "And I don't remember your father ever\x01",
            "serenading me with one, either...\x02\x03",

            "I wonder who it belongs to?\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)
    Jump("loc_7999")

    label("loc_790C")


    ChrTalk(    #217
        0x12,
        (
            "#861FIt looks like your little adventure\x01",
            "earned you a great treasure.\x02\x03",

            "#866FNow then, dinner will be ready soon,\x01",
            "so go wash your hands.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7999")

    TalkEnd(0x12)
    Return()

    # Function_13_73B8 end

    def Function_14_799D(): pass

    label("Function_14_799D")

    EventBegin(0x0)
    Fade(1000)
    OP_6D(8940, 0, 68850, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    SetChrPos(0x101, 8950, 0, 68820, 90)
    OP_0D()
    Sleep(200)

    ChrTalk(    #218
        0x101,
        (
            "#296F#6PUm, so, the top draaaawer...\x02\x03",

            "#292FMmph! Mmph!\x02\x03",

            "#291FHere it is! Yay!\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #219
        "\x07\x00Found #1016i.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x3F8, 1)
    OP_64(0x1, 0x1)
    OP_A2(0x1838)
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Return()

    # Function_14_799D end

    def Function_15_7AA0(): pass

    label("Function_15_7AA0")

    EventBegin(0x0)
    Fade(1000)
    OP_6D(73010, 0, -730, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    SetChrPos(0x101, 73010, 0, -730, 0)
    OP_0D()
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    OP_22(0x74, 0x0, 0x64)
    Sleep(500)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #220
        "\x07\x05The door is locked.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "[Use Storage Room Key]\x01",      # 0
            "[Don't]\x01",                     # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Sleep(100)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7BBB")
    OP_22(0x73, 0x0, 0x64)
    OP_71(0x4, 0x10)
    OP_64(0x0, 0x1)
    OP_A2(0x1839)

    label("loc_7BBB")

    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Return()

    # Function_15_7AA0 end

    def Function_16_7BC3(): pass

    label("Function_16_7BC3")

    EventBegin(0x0)
    SetChrFlags(0x101, 0x80)
    OP_6D(71060, 0, 149350, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(31000, 0)
    OP_6E(237, 0)
    FadeToBright(1000, 0)
    Sleep(500)

    def lambda_7C1B():
        OP_6D(70550, 0, 144740, 4000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7C1B)

    def lambda_7C33():
        OP_6E(280, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_7C33)

    def lambda_7C43():
        OP_6C(45000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_7C43)
    Sleep(1000)
    SetChrPos(0x101, 70970, 0, 139960, 0)
    ClearChrFlags(0x101, 0x80)
    OP_8E(0x101, 0x11396, 0x0, 0x23564, 0x7D0, 0x0)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #221
        0x101,
        (
            "#291FWooow! This room has lotsa stuff!\x02\x03",

            "#293FUm. But...\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 270, 400)
    Sleep(500)
    OP_8C(0x101, 90, 400)
    Sleep(500)
    OP_8C(0x101, 0, 400)
    Sleep(500)
    OP_62(0x101, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #222
        0x101,
        (
            "#295FThis is weird...\x02\x03",

            "Why does my heart feel so funny...\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x183A)
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Return()

    # Function_16_7BC3 end

    def Function_17_7D48(): pass

    label("Function_17_7D48")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x307, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7EDA")
    EventBegin(0x0)
    Fade(1000)
    OP_6D(70730, 0, 149460, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(28000, 0)
    OP_6E(233, 0)
    SetChrPos(0x101, 70540, 0, 147820, 0)
    OP_0D()
    Sleep(1000)
    OP_6F(0x8, 0)
    OP_70(0x8, 0xF)
    OP_22(0x2B, 0x0, 0x64)
    OP_73(0x8)
    Sleep(500)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #223
        "\x07\x00Found #1017i.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x3F9, 1)

    ChrTalk(    #224
        0x101,
        (
            "#291FWooow, it's pretty!\x02\x03",

            "#290FThis is a music thingy you blow, right?\x02\x03",

            "I'm gonna try playing it!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(1000)
    SetChrPos(0x101, 70340, 0, 147390, 0)
    OP_6D(70340, 0, 147390, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    OP_0D()
    OP_64(0x2, 0x1)
    OP_A2(0x183B)
    EventEnd(0x0)
    SetMapFlags(0x2000000)

    label("loc_7EDA")

    Return()

    # Function_17_7D48 end

    def Function_18_7EDB(): pass

    label("Function_18_7EDB")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x13), scpexpr(EXPR_PUSH_LONG, 0x3F9), scpexpr(EXPR_NEQ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_7EF1")
    Return()

    label("loc_7EF1")

    SetMapFlags(0x80)
    OP_C2()
    OP_48()
    EventBegin(0x0)
    Fade(500)
    SetChrChipByIndex(0x101, 19)
    SetChrSubChip(0x101, 0)
    OP_0D()
    OP_20(0x5DC)
    OP_21()
    OP_DB()
    OP_22(0x11B, 0x0, 0x64)

    def lambda_7F1C():

        label("loc_7F1C")

        OP_99(0x101, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_7F1C")

    QueueWorkItem2(0x101, 2, lambda_7F1C)
    Sleep(10000)
    Sleep(2000)
    Sleep(1500)
    Sleep(1500)
    OP_44(0x101, 0x2)
    OP_1D(0x75)
    Fade(500)
    SetChrSubChip(0x101, 8)
    OP_0D()
    Sleep(500)
    OP_DC()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7FEC")

    ChrTalk(    #225
        0x101,
        (
            "#290FIt's got a pretty sound...but it's kinda hard!\x02\x03",

            "#296FBut, but. It's weird.\x02\x03",

            "I feel like I've heard this before!\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    SetChrChipByIndex(0x101, 65535)
    SetChrSubChip(0x101, 0)
    OP_0D()
    OP_A2(0x6)
    Jump("loc_803E")

    label("loc_7FEC")


    ChrTalk(    #226
        0x101,
        (
            "#296FWhere...did I hear this?\x02\x03",

            "Maybe I should play it there.\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    SetChrChipByIndex(0x101, 65535)
    SetChrSubChip(0x101, 0)
    OP_0D()

    label("loc_803E")

    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Return()

    # Function_18_7EDB end

    def Function_19_8046(): pass

    label("Function_19_8046")

    FadeToDark(0, 0, -1)
    OP_A3(0x1200)
    OP_A3(0x1201)
    RemoveParty(0x2, 0xFF)
    RemoveParty(0x5, 0xFF)
    RemoveParty(0x9, 0xFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Set Scherazard as Partner\x01",      # 0
            "Set Agate as Partner\x01",           # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_80C2"),
        (1, "loc_80C8"),
        (SWITCH_DEFAULT, "loc_80CE"),
    )


    label("loc_80C2")

    OP_A2(0x1200)
    Jump("loc_80CE")

    label("loc_80C8")

    OP_A2(0x1201)
    Jump("loc_80CE")

    label("loc_80CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_80DC")
    AddParty(0x2, 0xF7, 0xFF)
    Jump("loc_80E0")

    label("loc_80DC")

    AddParty(0x5, 0xF7, 0xFF)

    label("loc_80E0")

    Return()

    # Function_19_8046 end

    def Function_20_80E1(): pass

    label("Function_20_80E1")

    ClearMapFlags(0x1)
    OP_6D(106730, -1920, 53920, 0)
    Sleep(100)
    OP_C9(0x0, 0x4, 0x0, 0x2, 0xFF, 0xFF, 0x5, 0x3, 0x4, 0x6, 0x7, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Sleep(1000)
    Return()

    # Function_20_80E1 end

    def Function_21_8133(): pass

    label("Function_21_8133")

    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "Rest\x01",      # 0
            "Stop\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_81CF")
    OP_20(0xBB8)
    FadeToDark(1000, 0, -1)
    Sleep(700)
    OP_22(0xD, 0x0, 0x64)
    OP_0D()
    OP_31(0x0, 0xFE, 0x0)
    OP_31(0x1, 0xFE, 0x0)
    OP_31(0x2, 0xFE, 0x0)
    OP_31(0x3, 0xFE, 0x0)
    OP_31(0x4, 0xFE, 0x0)
    OP_31(0x5, 0xFE, 0x0)
    OP_31(0x6, 0xFE, 0x0)
    OP_31(0x7, 0xFE, 0x0)
    Sleep(3500)
    OP_1E()
    FadeToBright(1000, 0)
    OP_56(0x0)
    TalkEnd(0xFF)
    Return()

    label("loc_81CF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_81E9")
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    label("loc_81E9")

    Return()

    # Function_21_8133 end

    SaveToFile()

Try(main)
