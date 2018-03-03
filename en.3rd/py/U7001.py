from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'U7001   ._SN',
        MapName             = 'Gaiden2',
        Location            = 'U7001.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60210",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            '',
            '',
            '',
            '',
            'ED6_DT21/U7001_5 ._SN',
            'ED6_DT21/SUB000  ._SN',
            ''
        ],
    )

    BuildStringList(
        '@FileName',                            # 8
        'Joshua',                               # 9
        'Father Kevin',                         # 10
        'Sister Ries',                          # 11
        'Tita',                                 # 12
        'Captain Schwarz',                      # 13
        'Major Vander',                         # 14
        'Josette',                              # 15
        'Princess Klaudia',                     # 16
        'Sieg',                                 # 17
        'Prince Olivert',                       # 18
        'Zin',                                  # 19
        'Anelace',                              # 20
        'Scherazard',                           # 21
        'Agate',                                # 22
        'Estelle',                              # 23
        'Richard',                              # 24
        'Renne',                                # 25
        'Gilbert',                              # 26
        'Dummy Camera',                         # 27
        ' ',                                    # 28
        ' ',                                    # 29
        ' ',                                    # 30
        ' ',                                    # 31
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
        'ED6_DT26/CH20622 ._CH',             # 00
        'ED6_DT27/CH03250 ._CH',             # 01
        'ED6_DT26/CH20660 ._CH',             # 02
        'ED6_DT26/CH20650 ._CH',             # 03
        'ED6_DT27/CH03150 ._CH',             # 04
        'ED6_DT27/CH03080 ._CH',             # 05
        'ED6_DT07/CH00060 ._CH',             # 06
        'ED6_DT27/CH03580 ._CH',             # 07
        'ED6_DT27/CH03570 ._CH',             # 08
        'ED6_DT27/CH03100 ._CH',             # 09
        'ED6_DT27/CH03210 ._CH',             # 0A
        'ED6_DT07/CH02323 ._CH',             # 0B
        'ED6_DT27/CH03260 ._CH',             # 0C
        'ED6_DT07/CH00070 ._CH',             # 0D
        'ED6_DT07/CH01630 ._CH',             # 0E
        'ED6_DT27/CH03240 ._CH',             # 0F
        'ED6_DT06/CH20053 ._CH',             # 10
        'ED6_DT27/CH03000 ._CH',             # 11
        'ED6_DT07/CH02030 ._CH',             # 12
        'ED6_DT27/CH03510 ._CH',             # 13
        'ED6_DT26/CH20655 ._CH',             # 14
        'ED6_DT27/CH03153 ._CH',             # 15
        'ED6_DT27/CH03103 ._CH',             # 16
        'ED6_DT27/CH03093 ._CH',             # 17
        'ED6_DT27/CH03243 ._CH',             # 18
        'ED6_DT06/CH20020 ._CH',             # 19
        'ED6_DT06/CH20021 ._CH',             # 1A
        'ED6_DT07/CH00312 ._CH',             # 1B
        'ED6_DT26/CH20501 ._CH',             # 1C
    )

    AddCharChipPat(
        'ED6_DT26/CH20622P._CP',             # 00
        'ED6_DT27/CH03250P._CP',             # 01
        'ED6_DT26/CH20660P._CP',             # 02
        'ED6_DT26/CH20650P._CP',             # 03
        'ED6_DT27/CH03150P._CP',             # 04
        'ED6_DT27/CH03080P._CP',             # 05
        'ED6_DT07/CH00060P._CP',             # 06
        'ED6_DT27/CH03580P._CP',             # 07
        'ED6_DT27/CH03570P._CP',             # 08
        'ED6_DT27/CH03100P._CP',             # 09
        'ED6_DT27/CH03210P._CP',             # 0A
        'ED6_DT07/CH02323P._CP',             # 0B
        'ED6_DT27/CH03260P._CP',             # 0C
        'ED6_DT07/CH00070P._CP',             # 0D
        'ED6_DT07/CH01630P._CP',             # 0E
        'ED6_DT27/CH03240P._CP',             # 0F
        'ED6_DT06/CH20053P._CP',             # 10
        'ED6_DT27/CH03000P._CP',             # 11
        'ED6_DT07/CH02030P._CP',             # 12
        'ED6_DT27/CH03510P._CP',             # 13
        'ED6_DT26/CH20655P._CP',             # 14
        'ED6_DT27/CH03153P._CP',             # 15
        'ED6_DT27/CH03103P._CP',             # 16
        'ED6_DT27/CH03093P._CP',             # 17
        'ED6_DT27/CH03243P._CP',             # 18
        'ED6_DT06/CH20020P._CP',             # 19
        'ED6_DT06/CH20021P._CP',             # 1A
        'ED6_DT07/CH00312P._CP',             # 1B
        'ED6_DT26/CH20501P._CP',             # 1C
    )

    DeclNpc(
        X                   = 9000000,
        Z                   = 9000000,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 5,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 9000000,
        Z                   = 9000000,
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
        X                   = 9000000,
        Z                   = 9000000,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 5,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 9000000,
        Z                   = 9000000,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 5,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = 9000000,
        Z                   = 9000000,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 5,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = 9000000,
        Z                   = 9000000,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 5,
        TalkScenaIndex      = 14,
    )

    DeclNpc(
        X                   = 9000000,
        Z                   = 9000000,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 5,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = 9000000,
        Z                   = 9000000,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 5,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = 9000000,
        Z                   = 9000000,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 9000000,
        Z                   = 9000000,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 13,
        TalkFunctionIndex   = 5,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 9000000,
        Z                   = 9000000,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 13,
        ChipIndex           = 0xD,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 9000000,
        Z                   = 9000000,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 5,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = 9000000,
        Z                   = 9000000,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 15,
        ChipIndex           = 0xF,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 5,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 9000000,
        Z                   = 9000000,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 16,
        ChipIndex           = 0x10,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 9000000,
        Z                   = 9000000,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 17,
        ChipIndex           = 0x11,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 9000000,
        Z                   = 9000000,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 18,
        ChipIndex           = 0x12,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 5,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = 9000000,
        Z                   = 9000000,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 19,
        ChipIndex           = 0x13,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 9000000,
        Z                   = 9000000,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 19,
        ChipIndex           = 0x13,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 5,
        TalkScenaIndex      = 15,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x1C0,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 9000000,
        Z                   = 9000000,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 26,
        ChipIndex           = 0x1A,
        NpcIndex            = 0x116,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 9000000,
        Z                   = 9000000,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 262170,
        ChipIndex           = 0x1A,
        NpcIndex            = 0x116,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 9000000,
        Z                   = 9000000,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1966105,
        ChipIndex           = 0x19,
        NpcIndex            = 0x116,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 9000000,
        Z                   = 9000000,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1835033,
        ChipIndex           = 0x19,
        NpcIndex            = 0x116,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclEvent(
        X                   = -3000,
        Y                   = -1000,
        Z                   = -21000,
        Range               = 2610,
        Unknown_10          = 0x1388,
        Unknown_14          = 0xFFFFBFF0,
        Unknown_18          = 0x0,
        Unknown_1C          = 21,
    )

    DeclEvent(
        X                   = 0,
        Y                   = 0,
        Z                   = 0,
        Range               = 0,
        Unknown_10          = 0x0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x2,
        Unknown_1C          = 9,
    )


    DeclActor(
        TriggerX            = 10,
        TriggerZ            = -10000,
        TriggerY            = -93360,
        TriggerRange        = 1800,
        ActorX              = 10,
        ActorZ              = -9500,
        ActorY              = -93360,
        Flags               = 0x7C,
        TalkScenaIndex      = 5,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 6580,
        TriggerZ            = -11000,
        TriggerY            = -91000,
        TriggerRange        = 1800,
        ActorX              = 6580,
        ActorZ              = -10000,
        ActorY              = -91000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 15,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -10060,
        TriggerZ            = -11000,
        TriggerY            = -97280,
        TriggerRange        = 1800,
        ActorX              = -10060,
        ActorZ              = -10000,
        ActorY              = -97280,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 17,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -6410,
        TriggerZ            = -11000,
        TriggerY            = -91400,
        TriggerRange        = 1800,
        ActorX              = -6410,
        ActorZ              = -10000,
        ActorY              = -91400,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 18,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 40,
        TriggerZ            = -11000,
        TriggerY            = -88660,
        TriggerRange        = 1800,
        ActorX              = 40,
        ActorZ              = -10000,
        ActorY              = -88660,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 19,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -6410,
        TriggerZ            = -11000,
        TriggerY            = -91400,
        TriggerRange        = 1800,
        ActorX              = -6410,
        ActorZ              = -10000,
        ActorY              = -91400,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 20,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_58A",          # 00, 0
        "Function_1_674",          # 01, 1
        "Function_2_8D0",          # 02, 2
        "Function_3_195D",         # 03, 3
        "Function_4_198A",         # 04, 4
        "Function_5_19F4",         # 05, 5
        "Function_6_3F2A",         # 06, 6
        "Function_7_3F82",         # 07, 7
        "Function_8_54CA",         # 08, 8
        "Function_9_5604",         # 09, 9
        "Function_10_571F",        # 0A, 10
        "Function_11_5D6D",        # 0B, 11
        "Function_12_6281",        # 0C, 12
        "Function_13_62AF",        # 0D, 13
        "Function_14_62E2",        # 0E, 14
        "Function_15_6402",        # 0F, 15
        "Function_16_67E8",        # 10, 16
        "Function_17_6D97",        # 11, 17
        "Function_18_7020",        # 12, 18
        "Function_19_7326",        # 13, 19
        "Function_20_7822",        # 14, 20
        "Function_21_78C4",        # 15, 21
    )


    def Function_0_58A(): pass

    label("Function_0_58A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5F2")
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_5A2"),
        (SWITCH_DEFAULT, "loc_5F2"),
    )


    label("loc_5A2")

    SetChrPos(0x0, -20, 1000, -21810, 180)
    SetChrPos(0x1, -20, 1000, -21810, 180)
    SetChrPos(0x2, -20, 1000, -21810, 180)
    SetChrPos(0x3, -20, 1000, -21810, 180)
    OP_30(0x1)
    OP_69(0x0, 0x0)
    Jump("loc_5F2")

    label("loc_5F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 7)), scpexpr(EXPR_END)), "loc_611")
    OP_A3(0x2507)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 8)
    Jump("loc_66B")

    label("loc_611")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 6)), scpexpr(EXPR_END)), "loc_630")
    OP_A3(0x2506)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 7)
    Jump("loc_66B")

    label("loc_630")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 5)), scpexpr(EXPR_END)), "loc_64F")
    OP_A3(0x2505)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 5)
    Jump("loc_66B")

    label("loc_64F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_66B")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 2)

    label("loc_66B")

    Call(0, 11)
    Call(0, 10)
    Return()

    # Function_0_58A end

    def Function_1_674(): pass

    label("Function_1_674")

    OP_16(0x2, 0xFA0, 0xFFFE2082, 0xFFFD8D0C, 0x23007B)
    OP_10(0x0, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x584, 0)), scpexpr(EXPR_END)), "loc_6A1")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0xD5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x2000000)
    Jump("loc_6C4")

    label("loc_6A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x521, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x540, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6C4")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6C4")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x49), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E1, 0)), scpexpr(EXPR_END)), "loc_6D1")
    OP_C4(0x0, 0x200)

    label("loc_6D1")

    LoadEffect(0x0, "map\\mp089_00.eff")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x540, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x560, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6F7")
    OP_65(0x0, 0x1)
    Jump("loc_6FB")

    label("loc_6F7")

    OP_64(0x0, 0x1)

    label("loc_6FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E0, 0)), scpexpr(EXPR_END)), "loc_706")
    OP_64(0x5, 0x1)

    label("loc_706")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E4, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_765")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4CE, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_762")
    LoadEffect(0x1, "map\\mp257_00.eff")
    PlayEffect(0x1, 0x0, 0xFF, -10060, -10000, -97280, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)

    label("loc_762")

    Jump("loc_771")

    label("loc_765")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4CE, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_771")
    OP_64(0x2, 0x1)

    label("loc_771")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x520, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x522, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7D0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4CE, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7CD")
    LoadEffect(0x1, "map\\mp257_00.eff")
    PlayEffect(0x1, 0x0, 0xFF, 6920, -10000, -91400, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)

    label("loc_7CD")

    Jump("loc_7E1")

    label("loc_7D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4CE, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4CB, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7E1")
    OP_64(0x1, 0x1)

    label("loc_7E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x540, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x541, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_840")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4CE, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_83D")
    LoadEffect(0x1, "map\\mp257_00.eff")
    PlayEffect(0x1, 0x0, 0xFF, -6410, -10000, -91400, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)

    label("loc_83D")

    Jump("loc_84C")

    label("loc_840")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4CE, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_84C")
    OP_64(0x3, 0x1)

    label("loc_84C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x560, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x562, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8AB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4CE, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8A8")
    LoadEffect(0x1, "map\\mp257_00.eff")
    PlayEffect(0x1, 0x0, 0xFF, 40, -10000, -88660, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)

    label("loc_8A8")

    Jump("loc_8B7")

    label("loc_8AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4CE, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8B7")
    OP_64(0x4, 0x1)

    label("loc_8B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8CF")
    OP_E5(0x1, 0xFF, 0x11, 262144)
    OP_E5(0x1, 0xFF, 0x13, 262144)

    label("loc_8CF")

    Return()

    # Function_1_674 end

    def Function_2_8D0(): pass

    label("Function_2_8D0")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_20(0x0)
    OP_C0(0x15, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Sleep(1000)
    OP_AD(0x2400E3, 0x0, 0x0, 0x64)
    Sleep(4000)
    OP_56(0x2)
    OP_AE(0xC8)
    Sleep(2000)
    SetChrPos(0x109, -1370, -11000, -90020, 0)
    SetChrPos(0x10F, -6970, -11000, -92640, 270)
    OP_6D(-2750, -7150, -71840, 0)
    OP_67(0, 8400, -10000, 0)
    OP_6B(3980, 0)
    OP_6C(313000, 0)
    OP_6E(529, 0)
    Sleep(1000)
    OP_43(0x109, 0x0, 0x0, 0x3)
    OP_43(0x10F, 0x0, 0x0, 0x4)
    OP_1D(0xD2)

    def lambda_9A0():
        OP_6D(-2750, -7150, -94090, 5000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_9A0)

    def lambda_9B8():
        OP_67(0, 6910, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_9B8)

    def lambda_9D0():
        OP_6B(4170, 5000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_9D0)

    def lambda_9E0():
        OP_6C(313000, 5000)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_9E0)

    def lambda_9F0():
        OP_6E(529, 5000)
        ExitThread()

    QueueWorkItem(0x10F, 2, lambda_9F0)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x109, 0x1)
    Sleep(1000)
    Fade(1000)
    OP_6D(-6020, -11000, -90210, 0)
    OP_67(0, 5770, -10000, 0)
    OP_6B(1950, 0)
    OP_6C(351000, 0)
    OP_6E(482, 0)
    OP_0D()
    Sleep(1000)
    WaitChrThread(0x109, 0x0)

    ChrTalk(    #0
        0x109,
        (
            "#1063F#6PIgnorant Cults...\x02\x03",

            "The Kin of Vegarna...\x02\x03",

            "The Cosmographica... \x01",
            "Oh, here's the Azure Fragments.\x02\x03",

            "#1065FWhoever manages this library must have some\x01",
            "out-of-this-world connections to've gathered\x01",
            "this many rare books from all over the place.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x109, 0, 400)
    Sleep(500)

    ChrTalk(    #1
        0x109,
        (
            "#1064F#6PWhoa! Is this a copy of Isthmian Tales?! \x01",
            "What's a banned book doing here?!\x02\x03",

            "#1068FThe guys over at the Congregation for the\x01",
            "Sacraments would flip their lid if they saw\x01",
            "this thing.\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x10F, 0x0)

    ChrTalk(    #2
        0x10F,
        (
            "#1446F#6PAnd there aren't just old and rare books, either.\x01",
            "I found one that was published this year.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x109, 225, 400)

    ChrTalk(    #3
        0x109,
        (
            "#1079F#2PNo way!\x02\x03",

            "#1069FWh-What's it called?\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x10F, 45, 400)
    Sleep(300)

    ChrTalk(    #4
        0x10F,
        (
            "#1440F#6PIt's called 'Liberlian Cuisine.'\x01",
            "Published by the Liberl News Service.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x109,
        (
            "#1068F#2PThat can't be real.\x02\x03",

            "#1069FWhat's that doing here mixed in with all\x01",
            "the other stuff?\x02\x03",

            "You sure you aren't pulling my leg?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x10F,
        (
            "#1802F#6PYour guess is as good as mine...\x02\x03",

            "#1447FThe photographs of food in it look delicious,\x01",
            "however.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x109,
        (
            "#1078F#2POh, I bet they do. There's this girl named\x01",
            "Dorothy who works for the LNS, and she's\x01",
            "one incredible photographer.\x02\x03",

            "#1079FOh, yeah. Don't know how I forgot but...\x01",
            "weren't you hungry?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x10F,
        (
            "#1447F#6PI was, but I finished eating while you were\x01",
            "busy looking at the books here.\x02\x03",

            "#1448FI did save some for you, of course.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_F8E():
        OP_6D(-5610, -11000, -89970, 1500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_F8E)
    OP_8F(0x10F, 0xFFFFEAA2, 0xFFFFD508, 0xFFFE9904, 0x7D0, 0x0)
    WaitChrThread(0x109, 0x0)
    OP_3E(0x193, 1)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #9
        "\x07\x05Ries handed over a smidgen of her \x1F\x93\x01\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_8F(0x10F, 0xFFFFE958, 0xFFFFD508, 0xFFFE97A6, 0x3E8, 0x0)

    ChrTalk(    #10
        0x109,
        (
            "#1064F#2PHow fast did you eat...?\x02\x03",

            "#1068FWait! We bought that poor store's entire\x01",
            "bread supply and this is all that's left?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x10F,
        (
            "#1442F#6PThey were perfectly baked, too.\x02\x03",

            "The flour used was clearly of high quality,\x01",
            "but bread like that can't be made without\x01",
            "excellent water, either.\x02\x03",

            "#1447FI think I like Liberl.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x109,
        (
            "#1840F#2PWell, I can't deny the country's got some\x01",
            "great grub to try all around...\x02\x03",

            "#1068F...Let's get off the subject of food, already!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x10F,
        (
            "#1446F#6PI know.\x02\x03",

            "#1443FThere's something truly odd about this\x01",
            "place.\x02\x03",

            "We should have a thorough look around.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x109,
        (
            "#1065F#2PYeah...\x02\x03",

            "#1079FOh. Come to think of it...\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(500)
    OP_22(0x8F, 0x0, 0x64)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x109, 0)
    SetChrSubChip(0x109, 0)
    OP_0D()
    Sleep(500)
    OP_62(0x10F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #15
        0x10F,
        (
            "#1802F#6P...\x02\x03",

            "It's completely stopped glowing now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x109,
        (
            "#1067F#2PMight as well be inactive again.\x02\x03",

            "#1063FI doubt it was a coincidence that it started\x01",
            "glowing just before we were sent here.\x02\x03",

            "This is no ordinary artifact, that's for sure.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x10F,
        (
            "#1443F#6P...\x02\x03",

            "#1446FGive it to me, Kevin.\x02\x03",

            "I'll look after it.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #18
        0x109,
        "#1064F#2PHuh? Why?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x10F,
        (
            "#1443F#6PProtecting you is my duty as your squire.\x02\x03",

            "As such, I can hardly stand by and let you\x01",
            "keep something that poses such danger on\x01",
            "your person. I should be the one to keep it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x109,
        "#1840F#2PWait a minute, Ries...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x10F,
        "#1443F#6PGive it to me.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x109,
        (
            "#1065F#2P*sigh* Look...\x02\x03",

            "#1063FFirst, we still don't have any conclusive proof \x01",
            "that this cube is the reason we ended up here.\x02\x03",

            "Second, despite me being the one who had it\x01",
            "up till this point, you're here with me anyway.\x02\x03",

            "So unless you plan to take it off me AND run\x01",
            "as far away from me as possible, who's holding\x01",
            "it won't make a damn bit of difference.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x10F,
        "#1441F#6PBut still!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x109,
        (
            "#1060F#2PSorry, but this time I'm actually ordering you.\x02\x03",

            "You wouldn't disobey an order from your superior,\x01",
            "would you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x10F,
        (
            "#1445F#6P...\x02\x03",

            "#1446FAll right, then.\x02\x03",

            "#1443FBut if we find out for sure that it really is\x01",
            "dangerous, promise me you'll get rid of it.\x02\x03",

            "That's all I want you to agree to.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x109,
        "#1840F#2PAll right. Promise.\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    Fade(500)
    OP_22(0x8F, 0x0, 0x64)
    SetChrChipByIndex(0x109, 65535)
    SetChrSubChip(0x109, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #27
        0x109,
        (
            "#1060F#2PAnyway, you up for some exploring?\x02\x03",

            "I don't know what's up with this place,\x01",
            "but it's time to try and find out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x10F,
        "#1440F#6PFine by me.\x02",
    )

    CloseMessageWindow()
    Sleep(300)

    def lambda_18C5():
        OP_6B(2800, 3000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_18C5)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_44(0x109, 0x0)
    OP_A2(0x2600)
    OP_6D(-4560, -11000, -93520, 0)
    OP_67(0, 7900, -10000, 0)
    OP_6B(2530, 0)
    OP_6C(315000, 0)
    OP_6E(450, 0)
    SetChrPos(0x109, -4560, -11000, -93520, 135)
    SetChrPos(0x10F, -4560, -11000, -93520, 135)
    OP_69(0x0, 0x0)
    Sleep(1000)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Return()

    # Function_2_8D0 end

    def Function_3_195D(): pass

    label("Function_3_195D")

    Sleep(2000)
    OP_8C(0x109, 270, 400)
    Sleep(300)
    OP_8E(0xFE, 0xFFFFED72, 0xFFFFD508, 0xFFFE9C74, 0x7D0, 0x0)
    OP_8C(0xFE, 315, 400)
    Return()

    # Function_3_195D end

    def Function_4_198A(): pass

    label("Function_4_198A")

    Sleep(1000)
    OP_8F(0xFE, 0xFFFFE372, 0xFFFFD508, 0xFFFE92E2, 0x1F4, 0x0)
    Sleep(300)
    OP_8C(0xFE, 315, 400)
    Sleep(500)
    OP_8C(0xFE, 270, 400)
    Sleep(3000)
    OP_8C(0xFE, 315, 400)
    OP_8F(0xFE, 0xFFFFE4C6, 0xFFFFD508, 0xFFFE9620, 0x1F4, 0x0)
    Sleep(300)
    OP_8C(0xFE, 0, 400)
    Sleep(500)
    OP_8C(0xFE, 315, 400)
    Return()

    # Function_4_198A end

    def Function_5_19F4(): pass

    label("Function_5_19F4")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    ClearMapFlags(0x1)
    SetChrPos(0x109, 350, 1000, -20010, 180)
    OP_9F(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x10F, 200, 1000, -33740, 180)
    SetChrPos(0x22, 200, 1000, -33740, 180)
    SetChrFlags(0xF0, 0x80)
    SetChrFlags(0xF1, 0x80)
    OP_6D(200, 1000, -33740, 0)
    OP_67(0, 7210, -10000, 0)
    OP_6B(2480, 0)
    OP_6C(315000, 0)
    OP_6E(315, 0)
    OP_6A(0x22)
    Sleep(500)

    def lambda_1A98():
        OP_8E(0xFE, 0xF0, 0x3E8, 0xFFFEAC82, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_1A98)

    def lambda_1AB3():
        OP_8E(0xFE, 0xF0, 0x3E8, 0xFFFEAC82, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x22, 0, lambda_1AB3)
    FadeToBright(2000, 0)
    OP_0D()
    OP_43(0x109, 0x0, 0x0, 0x6)

    ChrTalk(    #29 op#A op#5
        0x109,
        (
            "#3P#9ARies!\x02\x03",

            "#17AWait a sec!\x05\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1AFF():
        OP_8E(0xFE, 0xF0, 0x3E8, 0xFFFEAC82, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x22, 0, lambda_1AFF)
    Sleep(1200)

    def lambda_1B1F():
        OP_8E(0xFE, 0xF0, 0x3E8, 0xFFFEAC82, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x22, 0, lambda_1B1F)

    ChrTalk(    #30 op#A op#5
        0x10F,
        "#1445F#6P#7A...\x05\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #31 op#A op#5
        0x109,
        (
            "#1063F#24A#11PWhat's with you all of a sudden?\x02\x03",

            "#1079F#35AOh, I know. Are you feeling left out because\x01",
            "I'm the only one you know here and everyone\x01",
            "else is all buddy-buddy?\x02\x03",

            "#1068F#38ASorry, Ries. Probably wasn't fun to have to sit\x01",
            "through the whole happy reunion deal over and\x01",
            "over when you can't be a part of it.\x02\x03",

            "#1840F#15AI should've noticed earlier, really. I've been\x01",
            "pretty insensitive...so I'm really sorry, okay?\x05\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32 op#A op#5
        0x10F,
        "#1446F#6A#6P...\x05\x02",
    )

    CloseMessageWindow()
    OP_44(0x10F, 0x0)
    SetChrSubChip(0x10F, 0)
    OP_44(0x22, 0x0)
    OP_6A(0xFF)
    Sleep(500)
    OP_44(0x109, 0x0)
    OP_44(0x109, 0x1)
    SetChrSubChip(0x109, 0)
    Sleep(300)
    Fade(500)
    SetChrPos(0x109, 250, 1000, -72880, 180)
    SetChrPos(0x10F, 310, 1000, -75240, 180)
    OP_6D(-520, 1000, -74810, 0)
    OP_67(0, 6130, -10000, 0)
    OP_6B(2500, 0)
    OP_6C(219000, 0)
    OP_6E(315, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(    #33
        0x10F,
        "#1445F#5PWhen are you going to stop acting?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x109,
        "#1064F#12PHuh?\x02",
    )

    CloseMessageWindow()
    OP_1D(0xAD)
    Sleep(500)

    ChrTalk(    #35
        0x10F,
        (
            "#1446F#5PIt's true that I felt a little left out for a while.\x02\x03",

            "You've clearly gone through so much together,\x01",
            "and it's made you that much more fond of each\x01",
            "other in the days since.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x109,
        (
            "#1840F#12PHaha... Yeah, we had some amazing times.\x01",
            "Hard to come out the other end of stuff we\x01",
            "did without growing closer through it all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x10F,
        (
            "#1806F#5PWatching you all, how could I not have felt lonely?\x01",
            "How could I not have felt...jealous?\x02\x03",

            "You've been avoiding me for the past five years,\x01",
            "Kevin.\x02\x03",

            "#1445FThe thought that you'd grown close to so many\x01",
            "others while going out of your way to keep\x01",
            "me out of arms' reach did make me sad.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x109,
        "#1067F#12PY-You know I didn't mean it like that, Ries...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x10F,
        (
            "#1447F#5PBut at the same time, I was still happy you did.\x02\x03",

            "#1445FI knew how badly what happened to Rufina had\x01",
            "hurt you--how you were still blaming yourself for\x01",
            "it.\x02\x03",

            "I knew how you were driving yourself into a corner\x01",
            "over it, and how you were taking on nothing but\x01",
            "dirty jobs as if you were trying to punish yourself.\x02\x03",

            "And I couldn't confirm it for myself for sure, but\x01",
            "I just knew the rumors that you were desperate\x01",
            "to burn yourself out through them were true.\x02\x03",

            "#1806FSo that's the reason. That's why, as lonely as I felt\x01",
            "when you were off making new friends without me,\x01",
            "I was really, really happy more than anything.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x109,
        "#1841F#12PUmm... Ries, you do know that...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x10F,
        (
            "#1446F#5P...Except it turns out you haven't made any new\x01",
            "'friends' at all.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x10F, 0, 400)
    Sleep(300)

    ChrTalk(    #42
        0x10F,
        (
            "#1443F#5PYou're pulling the same exact thing you pulled with\x01",
            "me on them. Every single one at arms' length--they\x01",
            "can't get close to you. You won't get close to them.\x02\x03",

            "On the surface, you're a cheerful person having fun\x01",
            "with everyone, but on the inside, you're as cold as\x01",
            "can be.\x02\x03",

            "All you're doing is manipulating your own emotions\x01",
            "so people think you're someone you're not.\x02\x03",

            "After watching you ever since we were reunited,\x01",
            "that's become plain as day to me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x109,
        (
            "#1079F#12P...\x02\x03",

            "#1840FHaha. Man, I'm happy you're worried about me,\x01",
            "but you've totally got the wrong idea with this\x01",
            "one.\x02\x03",

            "#1071FSorry--I'm good at a lot of things, but pretending\x01",
            "to be someone I'm not isn't one of them.\x02\x03",

            "When I'm happy, you'll know about it, and when\x01",
            "I'm mad...well, I think you know I'm not so good\x01",
            "at hiding that, either.\x02\x03",

            "#1066FI'm the same transparent guy I always was.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x10F,
        (
            "#1447F#5POh, I didn't say you weren't easy to read.\x01",
            "For me, at least.\x02\x03",

            "#1806FAfter all, I know how genuinely shaken you\x01",
            "were by the Lord of Phantasma's message.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #45
        0x109,
        "#1076F#12P...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x10F,
        (
            "#1443F#5PTheir words--and the words of that Schwarzritter--\x01",
            "always come across as cryptic, but not to you.\x01",
            "Deep down, you know what they're talking about.\x02\x03",

            "You just constantly keep it from the rest of us\x01",
            "and try to keep us in the dark.\x02\x03",

            "#1445F...No. Maybe you've even managed to pull the\x01",
            "wool over your own eyes, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x109,
        "#1066F#12PHaha... Come on, now. You can't seriously...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x10F,
        (
            "#1446F#5P'Devour the new offering presented to you,\x01",
            "and display your seal once more.'\x02\x03",

            "#1805FYou know exactly what that means, don't you?\x01",
            "Go on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x109,
        (
            "#1067F#12P...\x02\x03",

            "#1841FYou know what? Maybe you should sit things\x01",
            "out for a bit. You're clearly really tired.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x10F,
        "#1444F#5P...What?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x109,
        (
            "#1840F#12PI get that you're as angry as you are upset with\x01",
            "me...but I think it's starting to make you jump to\x01",
            "some really out-there conclusions.\x02\x03",

            "And being tired out's only going to make it worse.\x01",
            "Can't you see how negative your line of thinking is?\x01",
            "You can't seriously believe all this is actually true.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x10F,
        "#1802F#5P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x109,
        (
            "#1065F#12PI'm not saying I don't deserve all the anger.\x01",
            "I totally do.\x02\x03",

            "I genuinely was busy, but at the same time,\x01",
            "I wasn't sure how to face you if we did end\x01",
            "up meeting, either...\x02\x03",

            "#1078FStill, we're gonna be working together from\x01",
            "now on, so--\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x10F,
        "#1445F#5PEnough.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x109,
        "#1064F#12P...Huh?\x02",
    )

    CloseMessageWindow()

    def lambda_2CED():
        OP_6D(-520, 1000, -74160, 1500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_2CED)

    def lambda_2D05():
        OP_8E(0xFE, 0x140, 0x3E8, 0xFFFEE094, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_2D05)
    WaitChrThread(0x10F, 0x0)
    WaitChrThread(0x109, 0x0)
    Fade(1000)

    def lambda_2D2F():
        OP_6B(2400, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_2D2F)
    SetChrChipByIndex(0x10F, 3)
    SetChrSubChip(0x10F, 0)
    SetChrFlags(0x10F, 0x2)
    OP_99(0x10F, 0x0, 0x2, 0x5DC)
    OP_22(0xA5, 0x0, 0x64)
    SetChrChipByIndex(0x109, 3)
    SetChrSubChip(0x109, 19)
    SetChrFlags(0x109, 0x2)

    def lambda_2D6B():
        OP_99(0xFE, 0x3, 0x8, 0x5DC)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_2D6B)

    def lambda_2D7B():
        OP_99(0xFE, 0x13, 0x1A, 0x5DC)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_2D7B)
    WaitChrThread(0x10F, 0x0)
    Fade(250)
    SetChrChipByIndex(0x10F, 65535)
    SetChrSubChip(0x10F, 0)
    ClearChrFlags(0x10F, 0x2)
    OP_0D()
    WaitChrThread(0x109, 0x0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #56
        0x109,
        "#1079F#12P...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x10F,
        (
            "#1441F#5PEverything you're saying is just...meaningless.\x02\x03",

            "Maybe the others don't realize that, but how dare\x01",
            "you think I, of all people, would fall for it?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2E64():
        OP_99(0xFE, 0x1A, 0x1C, 0x5DC)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_2E64)
    WaitChrThread(0x109, 0x0)
    Fade(250)
    SetChrChipByIndex(0x109, 65535)
    SetChrSubChip(0x109, 0)
    ClearChrFlags(0x109, 0x2)
    OP_0D()
    Sleep(300)

    ChrTalk(    #58
        0x109,
        "#1067F#12P...\x02",
    )

    CloseMessageWindow()

    def lambda_2EA6():
        OP_6D(-520, 1000, -74560, 1200)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_2EA6)

    def lambda_2EBE():
        OP_6B(2500, 1200)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_2EBE)

    def lambda_2ECE():
        OP_8F(0xFE, 0x14A, 0x3E8, 0xFFFEDE32, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_2ECE)
    WaitChrThread(0x109, 0x1)
    WaitChrThread(0x10F, 0x0)
    Sleep(300)

    ChrTalk(    #59
        0x10F,
        (
            "#1806F#5PI realize I'm turning my back on my duties as a\x01",
            "squire by doing this, but I can't bear to be near\x01",
            "you any longer.\x02\x03",

            "I can't stand to see the Kevin I thought I knew\x01",
            "so...empty.\x02\x03",

            "#1445FSo...\x02\x03",

            "...\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x10F, 180, 400)
    WaitChrThread(0x10F, 0x0)
    SetChrFlags(0x10F, 0x4)

    def lambda_2FD8():
        OP_6D(-520, 1000, -76500, 2000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_2FD8)

    def lambda_2FF0():
        OP_8E(0xFE, 0xFFFFFF7E, 0x3E8, 0xFFFEA070, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_2FF0)
    WaitChrThread(0x109, 0x0)
    Sleep(500)

    ChrTalk(    #60
        0x109,
        (
            "#1079F#12P...!\x02\x03",

            "#1067F...\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x10F, 0x1)
    SetChrFlags(0x10F, 0x80)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 350, 1000, -63600, 180)
    Sleep(500)

    ChrTalk(    #61
        0x10,
        "#1P...Kevin?\x02",
    )

    CloseMessageWindow()
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    Fade(500)
    OP_6D(-600, 1000, -68450, 0)
    OP_67(0, 5050, -10000, 0)
    OP_6B(2610, 0)
    OP_6C(315000, 0)
    OP_6E(313, 0)

    def lambda_30C9():
        OP_6D(-640, 1000, -70550, 3000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_30C9)

    def lambda_30E1():
        OP_8E(0xFE, 0xD2, 0x3E8, 0xFFFEED78, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_30E1)
    Sleep(1000)
    OP_8C(0x109, 0, 400)
    WaitChrThread(0x10, 0x0)
    WaitChrThread(0x109, 0x0)
    Sleep(300)

    ChrTalk(    #62
        0x109,
        (
            "#1067F#6POh. Hey...\x02\x03",

            "#1840FHaha. I'm sorry you had to see that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x10,
        (
            "#1500F#11PDon't worry about it.\x02\x03",

            "#1503F...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x109,
        (
            "#1075F#6P...I wanna know something, Joshua.\x02\x03",

            "#1060FYou've looked into me a fair bit since\x01",
            "I first stepped onto the scene, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x10,
        (
            "#1505F#11P...I have.\x02\x03",

            "#1502FI know that you're called the Heretic Hunter.\x02\x03",

            "I know that you're one of the twelve Dominions \x01",
            "that lead the Gralsritter.\x02\x03",

            "And I know you undertake the execution of\x01",
            "sinners the church deems most unforgivable\x01",
            "almost single-handedly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x109,
        (
            "#1066F#6PHeh. I figured you'd know your stuff.\x02\x03",

            "Wouldn't want any guys whose backgrounds\x01",
            "you hadn't thoroughly vetted being close to\x01",
            "your girlfriend for long, huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x10,
        (
            "#1503F#11PI can't deny it.\x02\x03",

            "#1505FStill, the only people you harm are those sinners.\x01",
            "Never anyone else.\x02\x03",

            "#1500FSo I decided that--for the time being, at least--\x01",
            "you weren't a threat to her or anyone else.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x109,
        "#1840F#6PHaha. I see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x10,
        "#1502F#11PWeissmann was your work, too, wasn't it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x109,
        (
            "#1075F#6PSure was.\x02\x03",

            "#1063FMy job was to get rid of him. That's it.\x02\x03",

            "Everything I did with you guys leading up to that\x01",
            "point was to get myself into a position to get it\x01",
            "done without him catching on.\x02\x03",

            "#1065FThat includes helping all of you out, naturally.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x10,
        (
            "#1505F#11P...Yeah. I know.\x02\x03",

            "#1503FYou must have been aware of the possibility\x01",
            "that Estelle would be taken on board the\x01",
            "Glorious, too.\x02\x03",

            "#1502FYou thought allowing it to happen would help\x01",
            "you in the long run, so you kept quiet about it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x109,
        (
            "#1075F#6PWow. Now that one I'm surprised you pieced\x01",
            "together.\x02\x03",

            "#1073FBut yep. You're absolutely right. I figured there\x01",
            "was a chance she might get abducted, but I did \x01",
            "exactly nothing to stop it.\x02\x03",

            "All I cared about was finding out what Weissmann\x01",
            "and you were up to...and where you were, for that\x01",
            "matter. Couldn't use better bait for that than her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x10,
        (
            "#1503F#11PI thought so.\x02\x03",

            "#1505FAnd yet all of that doesn't change how I'm\x01",
            "more grateful than words can express.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x109,
        "#1074F#6P...Why's that?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x10,
        (
            "#1503F#11PBecause if you hadn't helped me back then,\x01",
            "I would still be Weissmann's puppet.\x02\x03",

            "I would've broken with my own hands what \x01",
            "I value most in the whole world.\x02\x03",

            "#1500FThat's a debt I'll never be able to fully repay.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x109,
        (
            "#1073F#6POh, sweet Aidios. Now you're just being cute.\x02\x03",

            "#1075FI know you're smart enough to realize that's\x01",
            "not at ALL why I threw you a bone, right?\x02\x03",

            "I just wanted him off his guard enough to\x01",
            "create the opening I needed.\x02\x03",

            "#1072FHelping you was the perfect way to do that.\x01",
            "That was all there was to it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0x10,
        (
            "#1513F#11PAnd again: that doesn't change how grateful\x01",
            "I am to you.\x02\x03",

            "#1501FKnowing why you did what you did doesn't erase\x01",
            "the gratitude I feel. Not in the slightest.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0x109,
        (
            "#1071F#6PHaha...\x02\x03",

            "#1840FIt really is just as well you ended up quitting\x01",
            "Ouroboros.\x02\x03",

            "You'd suck to high heaven if you were an\x01",
            "Enforcer now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x10,
        (
            "#1513F#11PHaha... Honestly? You're totally right.\x02\x03",

            "#1500FIf Ries is sitting on the sidelines for now,\x01",
            "let me help you in her place.\x02\x03",

            "I might not be as capable of helping you as\x01",
            "she is, but I should be able to back you up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0x109,
        (
            "#1841F#6PYou don't need to feel indebted to me,\x01",
            "you know...\x02\x03",

            "#1840F...Well, I'll take what I can get. No doubt you're\x01",
            "worried sick about Estelle, too, so there's your\x01",
            "gold star reason for helping out besides me.\x02\x03",

            "So, thanks. I'm glad you've got my back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0x10,
        "#1513F#11PRight back at you.\x02",
    )

    CloseMessageWindow()

    def lambda_3E26():
        OP_6B(3000, 3000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_3E26)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_44(0x109, 0x0)
    OP_A2(0x2900)
    OP_28(0x2F, 0x4, 0x10)
    OP_28(0x2F, 0x4, 0x20)
    OP_28(0x30, 0x4, 0x10)
    OP_28(0x30, 0x4, 0x20)
    OP_28(0x31, 0x4, 0x10)
    OP_28(0x31, 0x4, 0x20)
    OP_28(0x32, 0x4, 0x4)
    OP_28(0x32, 0x4, 0x8)
    OP_28(0x32, 0x1, 0x1)
    OP_28(0x32, 0x1, 0x2)
    OP_28(0x32, 0x1, 0x4)
    OP_3F(0x358, 1)
    OP_3F(0x359, 1)
    OP_DB(0x0, 0x3)
    OP_A2(0x25C9)
    Call(6, 13)
    OP_DB(0x0, 0x7)
    OP_A2(0x25CD)
    Call(6, 17)
    SetChrFlags(0x10, 0x80)
    OP_DB(0x1, 0xE)
    ClearParty()
    AddParty(0x8, 0xEE, 0xFF)
    AddParty(0x1, 0xEF, 0xFF)
    OP_C0(0x15, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Sleep(1000)
    OP_DD(0x1, 0x0, 0x0, 258, 0, 0, 0)
    FadeToDark(0, 0, -1)
    OP_0D()
    OP_C0(0x20, 0x1, 0x102, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Sleep(500)
    OP_A2(0x2504)
    OP_A2(0x2508)
    NewScene("ED6_DT21/U7000   ._SN", 100, 0, 0)
    IdleLoop()
    EventEnd(0x0)
    Return()

    # Function_5_19F4 end

    def Function_6_3F2A(): pass

    label("Function_6_3F2A")

    SetChrPos(0x109, 200, 1000, -22740, 180)
    OP_9F(0x109, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    def lambda_3F4C():
        OP_8E(0xFE, 0xF0, 0x3E8, 0xFFFEAC82, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_3F4C)
    Sleep(4000)

    def lambda_3F6C():
        OP_8E(0xFE, 0xF0, 0x3E8, 0xFFFEAC82, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_3F6C)
    Return()

    # Function_6_3F2A end

    def Function_7_3F82(): pass

    label("Function_7_3F82")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_20(0x0)
    OP_C5(0x0, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS440._CH")
    OP_C5(0x1, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS441._CH")
    OP_C5(0x2, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS442._CH")
    OP_C5(0x3, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS443._CH")
    Sleep(1000)
    OP_22(0x73, 0x0, 0x64)
    Sleep(1000)
    OP_22(0x6A, 0x0, 0x64)
    Sleep(1500)
    SetMessageWindowPos(120, 150, -1, -1)
    SetChrName("Woman's Voice")

    AnonymousTalk(    #82
        "\x07\x0C#40WLook at me, Kevin Graham.\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(280, 280, -1, -1)
    SetChrName("Kevin")

    AnonymousTalk(    #83
        (
            "\x07\x0C#60W...\x02\x03",

            "...Instructor...Selnate?\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_1D(0xAF)
    Sleep(300)
    OP_C6(0x0, 0x3, -1, 2000, 0)
    Sleep(3000)
    SetMessageWindowPos(50, 250, -1, -1)
    SetChrName("Ein Selnate")

    AnonymousTalk(    #84
        (
            "\x07\x0C#30WYou look as though you haven't eaten in days.\x02\x03",

            "Although by the sounds of it, you really haven't. \x01",
            "Nor have you even been drinking anything.\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(350, 350, -1, -1)
    SetChrName("Kevin")

    AnonymousTalk(    #85
        "\x07\x0C#60W...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(50, 250, -1, -1)
    SetChrName("Ein Selnate")

    AnonymousTalk(    #86
        (
            "\x07\x0C#30WI was saddened to hear the news about Rufina\x01",
            "as well.\x02\x03",

            "But unfortunate accidents are a fact of life--\x01",
            "especially in our line of work.\x02\x03",

            "It's the risk we all choose to shoulder when we\x01",
            "depart on a mission.\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(350, 350, -1, -1)
    SetChrName("Kevin")

    AnonymousTalk(    #87
        (
            "\x07\x0C#60W...\x02\x03",

            "...Kill...me...\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(50, 250, -1, -1)
    SetChrName("Ein Selnate")

    AnonymousTalk(    #88
        "\x07\x0C#30WExcuse me?\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(350, 350, -1, -1)
    SetChrName("Kevin")

    AnonymousTalk(    #89
        (
            "\x07\x0C#60WI've got no reason to be a knight anymore.\x02\x03",

            "I've got no reason to even live anymore...\x02\x03",

            "And if someone has to kill me, I couldn't ask\x01",
            "for anyone better than you.\x02\x03",

            "I doubt I'd even have the time to feel pain\x01",
            "before you were done...so...\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(50, 250, -1, -1)
    SetChrName("Ein Selnate")

    AnonymousTalk(    #90
        (
            "\x07\x0C#30WIf that is your wish...\x01",
            "In what world did you think I would happily\x01",
            "oblige such an asinine request?\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(350, 350, -1, -1)
    SetChrName("Kevin")

    AnonymousTalk(    #91
        "\x07\x0C#40W...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(50, 250, -1, -1)
    SetChrName("Ein Selnate")

    AnonymousTalk(    #92
        (
            "\x07\x0C#30WYou do remember what you said when you first\x01",
            "became a squire, hmm?\x02\x03",

            "You said you offered your soul to the Goddess\x01",
            "above, and your body and blood to Her church\x01",
            "here on earth.\x02\x03",

            "After swearing that, you think you have the right\x01",
            "to beg for death, much less a painless one? Don't\x01",
            "make me laugh.\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(350, 350, -1, -1)
    SetChrName("Kevin")

    AnonymousTalk(    #93
        "\x07\x0C#40W...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(50, 250, -1, -1)
    SetChrName("Ein Selnate")

    AnonymousTalk(    #94
        (
            "\x07\x0C#30WHeh. Still, I was reluctant to even relay this\x01",
            "information for you...\x02\x03",

            "...but after seeing how pathetic a state you're in,\x01",
            "perhaps it won't be so difficult after all.\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(350, 350, -1, -1)
    SetChrName("Kevin")

    AnonymousTalk(    #95
        "\x07\x0C#40W...?\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(50, 250, -1, -1)
    SetChrName("Ein Selnate")

    AnonymousTalk(    #96
        (
            "\x07\x0C#30WSquire of the Gralsritter, Kevin Graham...\x02\x03",

            "From this day on, you are to assume the position\x01",
            "of Fifth Dominion.\x02\x03",

            "Your appointment was decided by the Congregation \x01",
            "of the Sacraments, and even His Holiness the Pope\x01",
            "has given his approval. The job is yours.\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(350, 350, -1, -1)
    SetChrName("Kevin")

    AnonymousTalk(    #97
        "\x07\x0C#60W...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x1, 0x3, -1, 500, 0)
    Sleep(1000)
    OP_C6(0x0, 0x3, 16777215, 500, 0)
    SetMessageWindowPos(350, 350, -1, -1)
    SetChrName("Kevin")

    AnonymousTalk(    #98
        "\x07\x0C#40W...Wha...t...?\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(50, 250, -1, -1)
    SetChrName("Ein Selnate")

    AnonymousTalk(    #99
        (
            "\x07\x0C#30WI imagine you must at least have heard rumors\x01",
            "that the position of Fifth Dominion was vacant.\x01",
            "Has been for several decades, too.\x02\x03",

            "Congratulations. It turns out that position was\x01",
            "meant for you.\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(350, 350, -1, -1)
    SetChrName("Kevin")

    AnonymousTalk(    #100
        "\x07\x0C#40W...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(50, 250, -1, -1)
    SetChrName("Ein Selnate")

    AnonymousTalk(    #101
        (
            "\x07\x0C#30WHeh. How the hell did that baby squire I once\x01",
            "help teach reach the same rank as me?\x02\x03",

            "I'm sure the fifth Merkabah will be pleased to\x01",
            "finally see the light of day.\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(350, 350, -1, -1)
    SetChrName("Kevin")

    AnonymousTalk(    #102
        "\x07\x0C#60W...Why...?\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(50, 250, -1, -1)
    SetChrName("Ein Selnate")

    AnonymousTalk(    #103
        (
            "\x07\x0C#30WOh, and incidentally, it's tradition to take on a\x01",
            "title of your choosing after becoming a Dominion.\x02\x03",

            "You might want to start giving some thought to \x01",
            "what you want sooner rather than later.\x02\x03",

            "As you already know, mine is 'Carnelia,' simple\x01",
            "a name as it is.\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(350, 350, -1, -1)
    SetChrName("Kevin")

    AnonymousTalk(    #104
        (
            "\x07\x0C#40WI-I don't care about titles... I don't care\x01",
            "about any of those things...\x02\x03",

            "Why...? Why me?\x02\x03",

            "I couldn't even protect Rufina...from...\x01",
            "...Why me...?\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(50, 250, -1, -1)
    SetChrName("Ein Selnate")

    AnonymousTalk(    #105
        (
            "\x07\x0C#30WAnd to that I say, 'That is of no consequence here.'\x02\x03",

            "'What is of consequence is that Rufina Argent was\x01",
            "a highly capable knight.'\x02\x03",

            "'She may not have manifested a Stigma of her own,\x01",
            "but her problem solving abilities were at times\x01",
            "greater than even a Dominion's.'\x02\x03",

            "'Her loss will be keenly felt...and it will be up to our\x01",
            "new Fifth Dominion to fill it.'\x02\x03",

            "The words of His Eminence the Cardinal.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x0, 0x3, -1, 0, 0)
    OP_C6(0x1, 0x3, 16777215, 500, 0)
    Sleep(1000)
    SetMessageWindowPos(350, 350, -1, -1)
    SetChrName("Kevin")

    AnonymousTalk(    #106
        (
            "\x07\x0C#40W...\x02\x03",

            "...Haha...hahaha...\x02\x03",

            "Oh, this is rich...\x02\x03",

            "This is just RICH...\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x2, 0x3, -1, 500, 0)
    Sleep(1000)
    OP_C6(0x0, 0x3, 16777215, 0, 0)
    SetMessageWindowPos(350, 350, -1, -1)
    SetChrName("Kevin")

    AnonymousTalk(    #107
        "\x07\x0C#30W#4SHahahahahahaha!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(50, 250, -1, -1)
    SetChrName("Ein Selnate")

    AnonymousTalk(    #108
        "\x07\x0C#30W...\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(350, 350, -1, -1)
    SetChrName("Kevin")

    AnonymousTalk(    #109
        (
            "\x07\x0C#30WHaha... Oh, man! It's so funny, it hurts.\x02\x03",

            "I become a knight to protect Rufina, then I end\x01",
            "up shooting to the top of the ranks over her dead \x01",
            "body!\x02\x03",

            "Ahaha! Amazing, huh? Who could've seen THAT \x01",
            "coming?\x02\x03",

            "I wish I could go back in time to tell myself when\x01",
            "I signed up what was gonna happen just to see my\x01",
            "own face! Hahaha!\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(500)
    SetMessageWindowPos(350, 350, -1, -1)
    SetChrName("Kevin")

    AnonymousTalk(    #110
        "\x07\x0C#30W#4SAhahahahaha!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(50, 250, -1, -1)
    SetChrName("Ein Selnate")

    AnonymousTalk(    #111
        "\x07\x0C#30W...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x0, 0x3, -1, 0, 0)
    OP_C6(0x2, 0x3, 16777215, 500, 0)
    Sleep(1000)
    SetMessageWindowPos(350, 350, -1, -1)
    SetChrName("Kevin")

    AnonymousTalk(    #112
        (
            "\x07\x0C#30W...Haha...hahaha...\x02\x03",

            "Hah...hah...\x02\x03",

            "...\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(50, 250, -1, -1)
    SetChrName("Ein Selnate")

    AnonymousTalk(    #113
        (
            "\x07\x0C#30WSo, what will you do?\x02\x03",

            "I should make it clear that you do have the right\x01",
            "to refuse your new appointment.\x02\x03",

            "Admittedly, no one in the Gralsritter's thousand-\x01",
            "year history has turned down a Dominion position, \x01",
            "so doing so would be unprecedented, but still.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(350, 350, -1, -1)
    SetChrName("Kevin")

    AnonymousTalk(    #114
        "\x07\x0C#30WHaha... Well, no shit.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x3, 0x3, -1, 500, 0)
    Sleep(1000)
    OP_C6(0x0, 0x3, 16777215, 0, 0)
    SetMessageWindowPos(350, 350, -1, -1)
    SetChrName("Kevin")

    AnonymousTalk(    #115
        (
            "\x07\x0C#30WNo, I humbly accept my new position.\x02\x03",

            "I'm ready to start work as soon as it's\x01",
            "there for me. Hell, start piling it on me\x01",
            "today! I'm up for it.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(50, 250, -1, -1)
    SetChrName("Ein Selnate")

    AnonymousTalk(    #116
        (
            "\x07\x0C#30W...All right, then.\x02\x03",

            "I'll see what I can do.\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(350, 350, -1, -1)
    SetChrName("Kevin")

    AnonymousTalk(    #117
        (
            "\x07\x0C#30WOh, and don't hold back on me, either. Throw me\x01",
            "the really hard stuff. The kind you'd need to be a\x01",
            "masochist to want to take on.\x02\x03",

            "And that title thing?\x02\x03",

            "Hmm...\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x3, 0x3, 16777215, 1500, 0)
    Sleep(2500)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("Kevin")

    AnonymousTalk(    #118
        (
            "\x07\x0C#40WLet's go with 'Heretic Hunter,' okay?\x01",
            "That sounds just perfect.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_20(0x1388)
    OP_21()
    Sleep(1000)
    OP_C7(0x1, 0xFF, 0x0)
    OP_AD(0x2400E7, 0x0, 0x0, 0x64)
    Sleep(4000)
    OP_56(0x2)
    OP_AE(0xC8)
    OP_20(0x7D0)
    Sleep(2000)
    Call(0, 8)
    Return()

    # Function_7_3F82 end

    def Function_8_54CA(): pass

    label("Function_8_54CA")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x4)
    SetChrPos(0x11, 200, -10500, -93300, 270)
    SetChrChipByIndex(0x11, 2)
    SetChrSubChip(0x11, 0)
    SetChrFlags(0x11, 0x800)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, 0, -11000, -94710, 0)
    SetChrChipByIndex(0x12, 4)
    SetChrSubChip(0x12, 0)
    SetChrFlags(0xEE, 0x80)
    SetChrFlags(0xEF, 0x80)
    SetChrFlags(0xF0, 0x80)
    SetChrFlags(0xF1, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x17, 0x80)
    SetChrFlags(0x18, 0x80)
    SetChrFlags(0x19, 0x80)
    SetChrFlags(0x1A, 0x80)
    SetChrFlags(0x1B, 0x80)
    SetChrFlags(0x1C, 0x80)
    SetChrFlags(0x1D, 0x80)
    SetChrFlags(0x1E, 0x80)
    SetChrFlags(0x1F, 0x80)
    SetChrFlags(0x20, 0x80)
    SetChrFlags(0x21, 0x80)
    OP_6D(-410, -11000, -92950, 0)
    OP_67(0, 7320, -10000, 0)
    OP_6B(2100, 0)
    OP_6C(323000, 0)
    OP_6E(421, 0)

    def lambda_55C7():
        OP_6B(1700, 6000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_55C7)
    OP_1D(0xAD)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(2500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMapFlags(0x2000000)
    OP_A2(0x2504)
    OP_A2(0x250B)
    NewScene("ED6_DT21/U7000   ._SN", 100, 0, 0)
    IdleLoop()
    EventEnd(0x0)
    Return()

    # Function_8_54CA end

    def Function_9_5604(): pass

    label("Function_9_5604")

    Call(0, 11)
    Call(0, 10)
    Call(0, 12)
    OP_C0(0x27, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x521, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x540, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_568E")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5671")
    ClearMapFlags(0x2000000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x1), scpexpr(EXPR_PUSH_LONG, 0x49), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_566E")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x49), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_20(0x1F4)
    OP_21()
    OP_1D(0x49)

    label("loc_566E")

    Jump("loc_568E")

    label("loc_5671")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD2), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_568E")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0xD2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_20(0x1F4)
    OP_21()
    OP_1D(0xD2)

    label("loc_568E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_571E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x564, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x564, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_56BB")
    NewScene("ED6_DT21/U7000   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    label("loc_56BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x562, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x562, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_42(0xB)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_56DC")
    NewScene("ED6_DT21/U7000   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    label("loc_56DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x561, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x561, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_56FD")
    NewScene("ED6_DT21/U7000   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    label("loc_56FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x560, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x560, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_571E")
    NewScene("ED6_DT21/U7000   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    label("loc_571E")

    Return()

    # Function_9_5604 end

    def Function_10_571F(): pass

    label("Function_10_571F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x584, 0)), scpexpr(EXPR_END)), "loc_5779")
    ClearChrFlags(0x21, 0x80)
    SetChrFlags(0x21, 0x800)
    SetChrChipByIndex(0x21, 28)
    SetChrSubChip(0x21, 0)
    OP_44(0x21, 0x0)
    SetChrFlags(0x21, 0x4)
    SetChrPos(0x21, 5160, -11000, -95940, 315)
    SetChrPos(0x16, 4050, -11000, -96420, 61)
    SetChrPos(0x1F, -8800, -11000, -95510, 291)
    Jump("loc_5D6C")

    label("loc_5779")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x565, 3)), scpexpr(EXPR_END)), "loc_5783")
    Jump("loc_5D6C")

    label("loc_5783")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x564, 0)), scpexpr(EXPR_END)), "loc_5801")
    SetChrPos(0x16, -10900, 1000, -91030, 325)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x564, 7)), scpexpr(EXPR_END)), "loc_57D5")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_57BA")
    OP_43(0x16, 0x0, 0x0, 0xE)
    Jump("loc_57D2")

    label("loc_57BA")

    SetChrPos(0x16, 9000000, 9000000, 0, 180)
    OP_44(0x16, 0xFF)
    OP_82(0x7, 0x0)

    label("loc_57D2")

    Jump("loc_57DC")

    label("loc_57D5")

    OP_43(0x16, 0x0, 0x0, 0xE)

    label("loc_57DC")

    SetChrPos(0x14, -6820, -11000, -92640, 309)
    SetChrPos(0x17, -5020, -11000, -91640, 325)
    Jump("loc_5D6C")

    label("loc_5801")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x562, 5)), scpexpr(EXPR_END)), "loc_583E")
    SetChrPos(0x10, -6010, -11000, -92450, 316)
    SetChrPos(0x17, -5150, -11000, -91780, 325)
    SetChrPos(0x16, -10900, 1000, -91030, 325)
    Jump("loc_5D6C")

    label("loc_583E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x561, 0)), scpexpr(EXPR_END)), "loc_589F")
    SetChrPos(0x17, -5150, -11000, -91780, 328)
    SetChrChipByIndex(0x1C, 24)
    SetChrSubChip(0x1C, 0)
    OP_44(0x1C, 0x0)
    SetChrFlags(0x1C, 0x4)
    SetChrPos(0x1C, -4580, -10700, -96300, 118)
    SetChrPos(0x23, -4930, -10700, -96560, 348)
    SetChrPos(0x25, -5200, -10500, -96570, 246)
    Jump("loc_5D6C")

    label("loc_589F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x560, 0)), scpexpr(EXPR_END)), "loc_58DC")
    SetChrPos(0x1C, 5830, -11000, -91440, 47)
    SetChrPos(0x17, -6010, -11000, -92450, 316)
    SetChrPos(0x16, -5150, -11000, -91780, 325)
    Jump("loc_5D6C")

    label("loc_58DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x540, 7)), scpexpr(EXPR_END)), "loc_591B")
    SetChrPos(0x16, -480, -11000, -91850, 179)
    SetChrChipByIndex(0x11, 2)
    SetChrSubChip(0x11, 0)
    OP_44(0x11, 0x0)
    SetChrFlags(0x11, 0x4)
    SetChrPos(0x11, 50, -10450, -93300, 270)
    Jump("loc_5D6C")

    label("loc_591B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x540, 4)), scpexpr(EXPR_END)), "loc_597C")
    SetChrPos(0x1C, 440, -11000, -94210, 319)
    SetChrPos(0x10, 1260, -11000, -89620, 15)
    SetChrPos(0x16, -480, -11000, -91850, 179)
    SetChrChipByIndex(0x11, 2)
    SetChrSubChip(0x11, 0)
    OP_44(0x11, 0x0)
    SetChrFlags(0x11, 0x4)
    SetChrPos(0x11, 50, -10450, -93300, 270)
    Jump("loc_5D6C")

    label("loc_597C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x540, 0)), scpexpr(EXPR_END)), "loc_59EE")
    SetChrPos(0x11, 50, -10450, -93300, 270)
    SetChrChipByIndex(0x11, 2)
    SetChrSubChip(0x11, 0)
    OP_44(0x11, 0x0)
    SetChrFlags(0x11, 0x4)
    SetChrPos(0x11, 50, -10450, -93300, 270)
    SetChrPos(0x10, 440, -11000, -94210, 319)
    SetChrPos(0x16, -480, -11000, -91850, 179)
    SetChrPos(0x17, -910, -11000, -94440, 31)
    Jump("loc_5D6C")

    label("loc_59EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x521, 6)), scpexpr(EXPR_END)), "loc_5ACA")
    SetChrPos(0x19, -3450, -11000, -95110, 120)
    SetChrChipByIndex(0x12, 21)
    SetChrSubChip(0x12, 0)
    OP_44(0x12, 0x0)
    SetChrFlags(0x12, 0x4)
    SetChrPos(0x12, -4470, -10700, -95930, 120)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5A81")
    SetChrPos(0x1C, -4920, -11000, -92550, 147)
    SetChrPos(0x16, -3550, -11000, -99540, 0)
    SetChrChipByIndex(0x1B, 23)
    SetChrSubChip(0x1B, 0)
    OP_44(0x1B, 0x0)
    SetChrFlags(0x1B, 0x4)
    SetChrPos(0x1B, -4950, -10700, -96800, 120)
    Jump("loc_5AC7")

    label("loc_5A81")

    SetChrPos(0x1C, -2300, -11000, -96280, 272)
    SetChrPos(0x16, -4070, -11000, -98430, 344)
    SetChrChipByIndex(0x1B, 23)
    SetChrSubChip(0x1B, 1)
    OP_44(0x1B, 0x0)
    SetChrFlags(0x1B, 0x4)
    SetChrPos(0x1B, -4950, -10700, -96800, 120)

    label("loc_5AC7")

    Jump("loc_5D6C")

    label("loc_5ACA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x521, 2)), scpexpr(EXPR_END)), "loc_5CAE")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5B2B")
    SetChrPos(0x12, 4050, -11000, -99830, 66)
    SetChrPos(0x13, 4960, -11000, -98150, 182)
    SetChrPos(0x16, 6270, -11000, -99980, 274)
    Jump("loc_5CAB")

    label("loc_5B2B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5B74")
    SetChrPos(0x13, 4150, -11000, -99850, 93)
    SetChrPos(0x16, 6270, -11000, -99980, 274)
    Jump("loc_5CAB")

    label("loc_5B74")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5BBD")
    SetChrPos(0x12, 4150, -11000, -99850, 93)
    SetChrPos(0x16, 6270, -11000, -99980, 274)
    Jump("loc_5CAB")

    label("loc_5BBD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5C06")
    SetChrPos(0x12, 4150, -11000, -99850, 93)
    SetChrPos(0x13, 6270, -11000, -99980, 274)
    Jump("loc_5CAB")

    label("loc_5C06")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5C3E")
    SetChrPos(0x16, 5760, -11000, -99090, 255)
    Jump("loc_5CAB")

    label("loc_5C3E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5C76")
    SetChrPos(0x13, 5760, -11000, -99090, 255)
    Jump("loc_5CAB")

    label("loc_5C76")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5CAB")
    SetChrPos(0x12, 5760, -11000, -99090, 255)

    label("loc_5CAB")

    Jump("loc_5D6C")

    label("loc_5CAE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x520, 5)), scpexpr(EXPR_END)), "loc_5CFC")
    SetChrPos(0x12, 13380, -11000, -95790, 71)
    SetChrPos(0x13, 12910, -11000, -96630, 25)
    SetChrPos(0x16, 11430, -11000, -96590, 73)
    SetChrPos(0x1B, 12030, -11000, -95090, 90)
    Jump("loc_5D6C")

    label("loc_5CFC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x520, 0)), scpexpr(EXPR_END)), "loc_5D39")
    SetChrPos(0x12, 13380, -11000, -95790, 71)
    SetChrPos(0x13, 12050, -11000, -97160, 45)
    SetChrPos(0x16, 10710, -11000, -97080, 62)
    Jump("loc_5D6C")

    label("loc_5D39")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x500, 0)), scpexpr(EXPR_END)), "loc_5D43")
    Jump("loc_5D6C")

    label("loc_5D43")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E2, 4)), scpexpr(EXPR_END)), "loc_5D6C")
    SetChrPos(0x14, 1050, -11000, -89570, 20)
    SetChrPos(0x15, -700, -11000, -89530, 0)

    label("loc_5D6C")

    Return()

    # Function_10_571F end

    def Function_11_5D6D(): pass

    label("Function_11_5D6D")

    OP_C0(0x23, 0x11, 0x181, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_C0(0x23, 0x12, 0x181, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_C0(0x23, 0x13, 0x181, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_C0(0x23, 0x14, 0x181, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_C0(0x23, 0x15, 0x181, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_C0(0x23, 0x16, 0x181, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_C0(0x23, 0x10, 0x181, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_C0(0x23, 0x17, 0x181, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_C0(0x23, 0x18, 0x181, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_C0(0x23, 0x19, 0x181, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_C0(0x23, 0x1A, 0x181, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_C0(0x23, 0x1B, 0x181, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_C0(0x23, 0x1C, 0x181, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_C0(0x23, 0x1D, 0x181, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_C0(0x23, 0x1E, 0x181, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_C0(0x23, 0x1F, 0x181, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_C0(0x23, 0x20, 0x181, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    SetChrPos(0x11, 9000000, 9000000, 0, 0)
    SetChrPos(0x12, 9000000, 9000000, 0, 0)
    SetChrPos(0x13, 9000000, 9000000, 0, 0)
    SetChrPos(0x14, 9000000, 9000000, 0, 0)
    SetChrPos(0x15, 9000000, 9000000, 0, 0)
    SetChrPos(0x16, 9000000, 9000000, 0, 0)
    SetChrPos(0x10, 9000000, 9000000, 0, 0)
    SetChrPos(0x17, 9000000, 9000000, 0, 0)
    SetChrPos(0x18, 9000000, 9000000, 0, 0)
    SetChrPos(0x19, 9000000, 9000000, 0, 0)
    SetChrPos(0x1A, 9000000, 9000000, 0, 0)
    SetChrPos(0x1B, 9000000, 9000000, 0, 0)
    SetChrPos(0x1C, 9000000, 9000000, 0, 0)
    SetChrPos(0x1D, 9000000, 9000000, 0, 0)
    SetChrPos(0x1E, 9000000, 9000000, 0, 0)
    SetChrPos(0x1F, 9000000, 9000000, 0, 0)
    SetChrPos(0x20, 9000000, 9000000, 0, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_60E6")
    SetChrFlags(0x13, 0x80)
    Jump("loc_60EB")

    label("loc_60E6")

    ClearChrFlags(0x13, 0x80)

    label("loc_60EB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6101")
    SetChrFlags(0x14, 0x80)
    Jump("loc_6106")

    label("loc_6101")

    ClearChrFlags(0x14, 0x80)

    label("loc_6106")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_611C")
    SetChrFlags(0x15, 0x80)
    Jump("loc_6121")

    label("loc_611C")

    ClearChrFlags(0x15, 0x80)

    label("loc_6121")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6137")
    SetChrFlags(0x16, 0x80)
    Jump("loc_613C")

    label("loc_6137")

    ClearChrFlags(0x16, 0x80)

    label("loc_613C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6152")
    SetChrFlags(0x10, 0x80)
    Jump("loc_6157")

    label("loc_6152")

    ClearChrFlags(0x10, 0x80)

    label("loc_6157")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_616D")
    SetChrFlags(0x17, 0x80)
    Jump("loc_6172")

    label("loc_616D")

    ClearChrFlags(0x17, 0x80)

    label("loc_6172")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6188")
    SetChrFlags(0x19, 0x80)
    Jump("loc_618D")

    label("loc_6188")

    ClearChrFlags(0x19, 0x80)

    label("loc_618D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_61A3")
    SetChrFlags(0x1A, 0x80)
    Jump("loc_61A8")

    label("loc_61A3")

    ClearChrFlags(0x1A, 0x80)

    label("loc_61A8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_61BE")
    SetChrFlags(0x1B, 0x80)
    Jump("loc_61C3")

    label("loc_61BE")

    ClearChrFlags(0x1B, 0x80)

    label("loc_61C3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_61D9")
    SetChrFlags(0x1C, 0x80)
    Jump("loc_61DE")

    label("loc_61D9")

    ClearChrFlags(0x1C, 0x80)

    label("loc_61DE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_61F4")
    SetChrFlags(0x1D, 0x80)
    Jump("loc_61F9")

    label("loc_61F4")

    ClearChrFlags(0x1D, 0x80)

    label("loc_61F9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_620F")
    SetChrFlags(0x1E, 0x80)
    Jump("loc_6214")

    label("loc_620F")

    ClearChrFlags(0x1E, 0x80)

    label("loc_6214")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xB)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_622A")
    SetChrFlags(0x1F, 0x80)
    Jump("loc_622F")

    label("loc_622A")

    ClearChrFlags(0x1F, 0x80)

    label("loc_622F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6245")
    SetChrFlags(0x20, 0x80)
    Jump("loc_624A")

    label("loc_6245")

    ClearChrFlags(0x20, 0x80)

    label("loc_624A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6260")
    SetChrFlags(0x12, 0x80)
    Jump("loc_6265")

    label("loc_6260")

    ClearChrFlags(0x12, 0x80)

    label("loc_6265")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_627B")
    SetChrFlags(0x11, 0x80)
    Jump("loc_6280")

    label("loc_627B")

    ClearChrFlags(0x11, 0x80)

    label("loc_6280")

    Return()

    # Function_11_5D6D end

    def Function_12_6281(): pass

    label("Function_12_6281")

    OP_A3(0x1)
    OP_A3(0x2)
    OP_A3(0x3)
    OP_A3(0x4)
    OP_A3(0x5)
    OP_A3(0x6)
    OP_A3(0x7)
    OP_A3(0x8)
    OP_A3(0x9)
    OP_A3(0xA)
    OP_A3(0xB)
    OP_A3(0xC)
    OP_A3(0xD)
    OP_A3(0xE)
    OP_A3(0xF)
    Return()

    # Function_12_6281 end

    def Function_13_62AF(): pass

    label("Function_13_62AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x540, 0)), scpexpr(EXPR_END)), "loc_62B9")
    Jump("loc_62E1")

    label("loc_62B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x521, 6)), scpexpr(EXPR_END)), "loc_62DD")
    SetChrChipByIndex(0xFE, 20)

    label("loc_62C5")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_62DA")
    OP_99(0xFE, 0x0, 0x1, 0x1F4)
    Jump("loc_62C5")

    label("loc_62DA")

    Jump("loc_62E1")

    label("loc_62DD")

    Call(6, 2)

    label("loc_62E1")

    Return()

    # Function_13_62AF end

    def Function_14_62E2(): pass

    label("Function_14_62E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x565, 3)), scpexpr(EXPR_END)), "loc_62F0")
    Call(6, 2)
    Jump("loc_6401")

    label("loc_62F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x564, 0)), scpexpr(EXPR_END)), "loc_63FD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x564, 7)), scpexpr(EXPR_END)), "loc_63B3")

    label("loc_62FE")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_63B0")
    SetChrChipByIndex(0xFE, 27)
    SetChrSubChip(0xFE, 0)
    OP_99(0xFE, 0x0, 0x2, 0x7D0)
    Sleep(1000)
    PlayEffect(0x0, 0x7, 0xFE, 200, 1000, 1000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_C0(0x24, 0x0, 0xFE, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2710), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_6386")
    OP_22(0x1F7, 0x0, 0x32)

    label("loc_6386")

    OP_99(0xFE, 0x3, 0x7, 0x7D0)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_63A8")
    Sleep(2000)
    Jump("loc_63AD")

    label("loc_63A8")

    Sleep(4000)

    label("loc_63AD")

    Jump("loc_62FE")

    label("loc_63B0")

    Jump("loc_63FA")

    label("loc_63B3")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_63FA")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_63DC")
    OP_62(0xFE, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x1)

    label("loc_63DC")

    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_63B3")

    label("loc_63FA")

    Jump("loc_6401")

    label("loc_63FD")

    Call(6, 2)

    label("loc_6401")

    Return()

    # Function_14_62E2 end

    def Function_15_6402(): pass

    label("Function_15_6402")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4CE, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x522, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_646B")
    OP_22(0x17, 0x0, 0x64)
    OP_82(0x0, 0x2)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #119
        "\x07\x05There are a number of interesting books here.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_A2(0x2672)
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Jump("loc_67E4")

    label("loc_646B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4CE, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4CB, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6633")
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #120
        "\x07\x05There are a number of interesting books here.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        1,
        (
            "Read 'Kitty-Talk for Dummies'\x01",      # 0
            "Read 'The Erbe Woodpecker'\x01",         # 1
            "Read 'Hertz's Adventure I'\x01",         # 2
            "Read 'Hertz's Adventure II'\x01",        # 3
            "Read '31 Cypress Trees'\x01",            # 4
            "Read 'From Fat to Fit'\x01",             # 5
            "Leave\x01",                              # 6
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_65C3")
    OP_B8(0xE1, 0x0)
    OP_F7(0x10, 0x30, 0x0)

    label("loc_65C3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_65DA")
    OP_B8(0xE2, 0x0)
    OP_F7(0x10, 0x31, 0x0)

    label("loc_65DA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_65F1")
    OP_B8(0xE3, 0x0)
    OP_F7(0x10, 0x32, 0x0)

    label("loc_65F1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6608")
    OP_B8(0xE4, 0x0)
    OP_F7(0x10, 0x33, 0x0)

    label("loc_6608")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_661F")
    OP_B8(0xE5, 0x0)
    OP_F7(0x10, 0x34, 0x0)

    label("loc_661F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6630")
    Call(0, 16)

    label("loc_6630")

    Jump("loc_67E4")

    label("loc_6633")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4CE, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4CB, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_67D4")
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #121
        "\x07\x05There are a number of interesting books here.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        1,
        (
            "Read 'Kitty-Talk for Dummies'\x01",      # 0
            "Read 'The Erbe Woodpecker'\x01",         # 1
            "Read 'Hertz's Adventure I'\x01",         # 2
            "Read 'Hertz's Adventure II'\x01",        # 3
            "Read '31 Cypress Trees'\x01",            # 4
            "Leave\x01",                              # 5
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6775")
    OP_B8(0xE1, 0x0)
    OP_F7(0x10, 0x30, 0x0)

    label("loc_6775")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_678C")
    OP_B8(0xE2, 0x0)
    OP_F7(0x10, 0x31, 0x0)

    label("loc_678C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_67A3")
    OP_B8(0xE3, 0x0)
    OP_F7(0x10, 0x32, 0x0)

    label("loc_67A3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_67BA")
    OP_B8(0xE4, 0x0)
    OP_F7(0x10, 0x33, 0x0)

    label("loc_67BA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_67D1")
    OP_B8(0xE5, 0x0)
    OP_F7(0x10, 0x34, 0x0)

    label("loc_67D1")

    Jump("loc_67E4")

    label("loc_67D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4CE, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4CB, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_67E4")
    Call(0, 16)

    label("loc_67E4")

    TalkEnd(0xFF)
    Return()

    # Function_15_6402 end

    def Function_16_67E8(): pass

    label("Function_16_67E8")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(72, 320, 56, 3)

    AnonymousTalk(    #122
        "\x07\x05There's a book called 'From Fat to Fit' written by Gilbert Stein.\x02",
    )

    CloseMessageWindow()
    CloseMessageWindow()
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "Read\x01",                  # 0
            "Back Away Slowly\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6D96")
    OP_62(0x0, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2500)
    OP_63(0x0)
    Sleep(800)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_END)),
        (8, "loc_68FC"),
        (14, "loc_6954"),
        (0, "loc_6989"),
        (1, "loc_69D2"),
        (4, "loc_6A6B"),
        (6, "loc_6AA7"),
        (5, "loc_6AC3"),
        (2, "loc_6B36"),
        (3, "loc_6B55"),
        (10, "loc_6BA0"),
        (9, "loc_6BDE"),
        (7, "loc_6C27"),
        (13, "loc_6C85"),
        (12, "loc_6CF9"),
        (11, "loc_6D1E"),
        (15, "loc_6D3C"),
        (SWITCH_DEFAULT, "loc_6D90"),
    )


    label("loc_68FC")


    ChrTalk(    #123
        0x109,
        (
            "#1064FWell, uhh...\x02\x03",

            "#1068FThis guy's...uh...dedicated. Yeah,\x01",
            "let's go with that.\x02",
        )
    )

    Jump("loc_6D90")

    label("loc_6954")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x584, 0)), scpexpr(EXPR_END)), "loc_6972")

    ChrTalk(    #124
        0x10F,
        "#1936F...*slam*\x02",
    )

    Jump("loc_6986")

    label("loc_6972")


    ChrTalk(    #125
        0x10F,
        "#1446F...*slam*\x02",
    )


    label("loc_6986")

    Jump("loc_6D90")

    label("loc_6989")


    ChrTalk(    #126
        0x101,
        (
            "#1019FOh, man! What is this thing?\x02\x03",

            "I think I'm gonna throw up...\x02",
        )
    )

    Jump("loc_6D90")

    label("loc_69D2")


    ChrTalk(    #127
        0x102,
        (
            "#1502FWh-What in...?\x02\x03",

            "#1508F(It looks like he tried to adapt Ouroboros'\x01",
            "jaeger strengthening program into a fitness\x01",
            "regime. That's...impressive.)\x02",
        )
    )

    Jump("loc_6D90")

    label("loc_6A6B")


    ChrTalk(    #128
        0x105,
        (
            "#1165FAha...haha...\x01",
            "(I almost feel sorry for him...)\x02",
        )
    )

    Jump("loc_6D90")

    label("loc_6AA7")


    ChrTalk(    #129
        0x107,
        "#065FPoor Gilbert...\x02",
    )

    Jump("loc_6D90")

    label("loc_6AC3")


    ChrTalk(    #130
        0x106,
        (
            "#055FDaaamn...\x02\x03",

            "#551FThis looks about as safe as a sword-balancing\x01",
            "act on my neck. He seriously tried this?\x02",
        )
    )

    Jump("loc_6D90")

    label("loc_6B36")


    ChrTalk(    #131
        0x103,
        "#1527FHuh. Fascinating.\x02",
    )

    Jump("loc_6D90")

    label("loc_6B55")


    ChrTalk(    #132
        0x104,
        "#1542F...Hmm...\x02",
    )

    CloseMessageWindow()
    OP_62(0x0, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #133
        0x104,
        "#1547FOoh la la...\x02",
    )

    Jump("loc_6D90")

    label("loc_6BA0")


    ChrTalk(    #134
        0x10B,
        (
            "#216FWhaaaaaat?!\x02\x03",

            "#215F...\x02\x03",

            "#413FI feel kind of ill...\x02",
        )
    )

    Jump("loc_6D90")

    label("loc_6BDE")


    ChrTalk(    #135
        0x10A,
        (
            "#1317FUrk...\x02\x03",

            "#817FI'm going to pretend I didn't see any of that.\x02",
        )
    )

    Jump("loc_6D90")

    label("loc_6C27")


    ChrTalk(    #136
        0x108,
        (
            "#074F...*sigh*\x02\x03",

            "#075FI really can't see there being much of a\x01",
            "market for this thing...\x02",
        )
    )

    Jump("loc_6D90")

    label("loc_6C85")

    OP_62(0x0, 0x0, 2000, 0x14, 0x17, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #137
        0x10E,
        (
            "#176F(I think I should return this to the shelf.\x01",
            "...The very back of the shelf.)\x02",
        )
    )

    Jump("loc_6D90")

    label("loc_6CF9")


    ChrTalk(    #138
        0x10D,
        "#272F...What a hopeless fool.\x02",
    )

    Jump("loc_6D90")

    label("loc_6D1E")


    ChrTalk(    #139
        0x10C,
        "#115FThis is...a book.\x02",
    )

    Jump("loc_6D90")

    label("loc_6D3C")


    ChrTalk(    #140
        0x110,
        (
            "#264FHmm...\x02\x03",

            "#261FHeehee. He's so dedicated. I'm ever\x01",
            "so slightly impressed.\x02",
        )
    )

    Jump("loc_6D90")

    label("loc_6D90")

    CloseMessageWindow()
    OP_F7(0x11, 0x0, 0x0)

    label("loc_6D96")

    Return()

    # Function_16_67E8 end

    def Function_17_6D97(): pass

    label("Function_17_6D97")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4CE, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6DF2")
    OP_22(0x17, 0x0, 0x64)
    OP_82(0x0, 0x2)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #141
        "\x07\x05All of Carnelia is on the bookshelf.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_A2(0x2670)
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Jump("loc_701F")

    label("loc_6DF2")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #142
        "\x07\x05All of Carnelia is on the bookshelf.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        1,
        (
            "Read Chapter 1\x01",       # 0
            "Read Chapter 2\x01",       # 1
            "Read Chapter 3\x01",       # 2
            "Read Chapter 4\x01",       # 3
            "Read Chapter 5\x01",       # 4
            "Read Chapter 6\x01",       # 5
            "Read Chapter 7\x01",       # 6
            "Read Chapter 8\x01",       # 7
            "Read Chapter 9\x01",       # 8
            "Read Chapter 10\x01",      # 9
            "Read Finale\x01",          # 10
            "Leave\x01",                # 11
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_5F(0x1)
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6F2A")
    OP_B8(0xE6, 0x0)
    OP_F7(0x10, 0x1, 0x0)

    label("loc_6F2A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6F41")
    OP_B8(0xE7, 0x0)
    OP_F7(0x10, 0x2, 0x0)

    label("loc_6F41")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6F58")
    OP_B8(0xE8, 0x0)
    OP_F7(0x10, 0x3, 0x0)

    label("loc_6F58")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6F6F")
    OP_B8(0xE9, 0x0)
    OP_F7(0x10, 0x4, 0x0)

    label("loc_6F6F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6F86")
    OP_B8(0xEA, 0x0)
    OP_F7(0x10, 0x5, 0x0)

    label("loc_6F86")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6F9D")
    OP_B8(0xEB, 0x0)
    OP_F7(0x10, 0x6, 0x0)

    label("loc_6F9D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6FB4")
    OP_B8(0xEC, 0x0)
    OP_F7(0x10, 0x7, 0x0)

    label("loc_6FB4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6FCB")
    OP_B8(0xED, 0x0)
    OP_F7(0x10, 0x8, 0x0)

    label("loc_6FCB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6FE2")
    OP_B8(0xEE, 0x0)
    OP_F7(0x10, 0x9, 0x0)

    label("loc_6FE2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6FF9")
    OP_B8(0xEF, 0x0)
    OP_F7(0x10, 0xA, 0x0)

    label("loc_6FF9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7010")
    OP_B8(0xF0, 0x0)
    OP_F7(0x10, 0xB, 0x0)

    label("loc_7010")

    FadeToBright(300, 0)
    OP_5F(0x0)
    TalkEnd(0xFF)

    label("loc_701F")

    Return()

    # Function_17_6D97 end

    def Function_18_7020(): pass

    label("Function_18_7020")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4CE, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_707F")
    OP_22(0x17, 0x0, 0x64)
    OP_82(0x0, 0x2)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #143
        "\x07\x05All of Gambler Jack is on the bookshelf.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_A2(0x2673)
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Jump("loc_7325")

    label("loc_707F")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #144
        "\x07\x05All of Gambler Jack is on the bookshelf.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        1,
        (
            "Read Chapter 1\x01",       # 0
            "Read Chapter 2\x01",       # 1
            "Read Chapter 3\x01",       # 2
            "Read Chapter 4\x01",       # 3
            "Read Chapter 5\x01",       # 4
            "Read Chapter 6\x01",       # 5
            "Read Chapter 7\x01",       # 6
            "Read Chapter 8\x01",       # 7
            "Read Chapter 9\x01",       # 8
            "Read Chapter 10\x01",      # 9
            "Read Chapter 11\x01",      # 10
            "Read Chapter 12\x01",      # 11
            "Read Chapter 13\x01",      # 12
            "Read Finale\x01",          # 13
            "Leave\x01",                # 14
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_5F(0x1)
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_71EB")
    OP_B8(0xFD, 0x0)
    OP_F7(0x10, 0xC, 0x0)

    label("loc_71EB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7202")
    OP_B8(0xFE, 0x0)
    OP_F7(0x10, 0xD, 0x0)

    label("loc_7202")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7219")
    OP_B8(0xFF, 0x0)
    OP_F7(0x10, 0xE, 0x0)

    label("loc_7219")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7230")
    OP_B8(0x100, 0x0)
    OP_F7(0x10, 0xF, 0x0)

    label("loc_7230")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7247")
    OP_B8(0x101, 0x0)
    OP_F7(0x10, 0x10, 0x0)

    label("loc_7247")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_725E")
    OP_B8(0x102, 0x0)
    OP_F7(0x10, 0x11, 0x0)

    label("loc_725E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7275")
    OP_B8(0x103, 0x0)
    OP_F7(0x10, 0x12, 0x0)

    label("loc_7275")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_728C")
    OP_B8(0x104, 0x0)
    OP_F7(0x10, 0x13, 0x0)

    label("loc_728C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_72A3")
    OP_B8(0x105, 0x0)
    OP_F7(0x10, 0x14, 0x0)

    label("loc_72A3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_72BA")
    OP_B8(0x106, 0x0)
    OP_F7(0x10, 0x15, 0x0)

    label("loc_72BA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_72D1")
    OP_B8(0x107, 0x0)
    OP_F7(0x10, 0x16, 0x0)

    label("loc_72D1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_72E8")
    OP_B8(0x108, 0x0)
    OP_F7(0x10, 0x17, 0x0)

    label("loc_72E8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_72FF")
    OP_B8(0x109, 0x0)
    OP_F7(0x10, 0x18, 0x0)

    label("loc_72FF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7316")
    OP_B8(0x10A, 0x0)
    OP_F7(0x10, 0x19, 0x0)

    label("loc_7316")

    FadeToBright(300, 0)
    OP_5F(0x0)
    TalkEnd(0xFF)

    label("loc_7325")

    Return()

    # Function_18_7020 end

    def Function_19_7326(): pass

    label("Function_19_7326")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4CE, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7388")
    OP_22(0x17, 0x0, 0x64)
    OP_82(0x0, 0x2)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #145
        "\x07\x05All of The Doll Knight is on the bookshelf.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_A2(0x2674)
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Jump("loc_7821")

    label("loc_7388")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #146
        "\x07\x05All of The Doll Knight is on the bookshelf.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        1,
        (
            "Read Ch1 - Ch11\x01",         # 0
            "Read Ch12 - Finale\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_741B"),
        (1, "loc_7614"),
        (SWITCH_DEFAULT, "loc_7812"),
    )


    label("loc_741B")

    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        1,
        (
            "Read Chapter 1\x01",       # 0
            "Read Chapter 2\x01",       # 1
            "Read Chapter 3\x01",       # 2
            "Read Chapter 4\x01",       # 3
            "Read Chapter 5\x01",       # 4
            "Read Chapter 6\x01",       # 5
            "Read Chapter 7\x01",       # 6
            "Read Chapter 8\x01",       # 7
            "Read Chapter 9\x01",       # 8
            "Read Chapter 10\x01",      # 9
            "Read Chapter 11\x01",      # 10
            "Leave\x01",                # 11
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_5F(0x1)
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_752B")
    OP_B8(0x10B, 0x0)
    OP_F7(0x10, 0x1A, 0x0)

    label("loc_752B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7542")
    OP_B8(0x10C, 0x0)
    OP_F7(0x10, 0x1B, 0x0)

    label("loc_7542")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7559")
    OP_B8(0x10D, 0x0)
    OP_F7(0x10, 0x1C, 0x0)

    label("loc_7559")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7570")
    OP_B8(0x10E, 0x0)
    OP_F7(0x10, 0x1D, 0x0)

    label("loc_7570")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7587")
    OP_B8(0x10F, 0x0)
    OP_F7(0x10, 0x1E, 0x0)

    label("loc_7587")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_759E")
    OP_B8(0x110, 0x0)
    OP_F7(0x10, 0x1F, 0x0)

    label("loc_759E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_75B5")
    OP_B8(0x111, 0x0)
    OP_F7(0x10, 0x20, 0x0)

    label("loc_75B5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_75CC")
    OP_B8(0x112, 0x0)
    OP_F7(0x10, 0x21, 0x0)

    label("loc_75CC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_75E3")
    OP_B8(0x113, 0x0)
    OP_F7(0x10, 0x22, 0x0)

    label("loc_75E3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_75FA")
    OP_B8(0x114, 0x0)
    OP_F7(0x10, 0x23, 0x0)

    label("loc_75FA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7611")
    OP_B8(0x115, 0x0)
    OP_F7(0x10, 0x24, 0x0)

    label("loc_7611")

    Jump("loc_7812")

    label("loc_7614")

    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        1,
        10,
        10,
        1,
        (
            "Read Chapter 12\x01",      # 0
            "Read Chapter 13\x01",      # 1
            "Read Chapter 14\x01",      # 2
            "Read Chapter 15\x01",      # 3
            "Read Chapter 16\x01",      # 4
            "Read Chapter 17\x01",      # 5
            "Read Chapter 18\x01",      # 6
            "Read Chapter 19\x01",      # 7
            "Read Chapter 20\x01",      # 8
            "Read Chapter 21\x01",      # 9
            "Read Finale\x01",          # 10
            "Leave\x01",                # 11
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_5F(0x1)
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7729")
    OP_B8(0x116, 0x0)
    OP_F7(0x10, 0x25, 0x0)

    label("loc_7729")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7740")
    OP_B8(0x117, 0x0)
    OP_F7(0x10, 0x26, 0x0)

    label("loc_7740")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7757")
    OP_B8(0x118, 0x0)
    OP_F7(0x10, 0x27, 0x0)

    label("loc_7757")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_776E")
    OP_B8(0x119, 0x0)
    OP_F7(0x10, 0x28, 0x0)

    label("loc_776E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7785")
    OP_B8(0x11A, 0x0)
    OP_F7(0x10, 0x29, 0x0)

    label("loc_7785")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_779C")
    OP_B8(0x11B, 0x0)
    OP_F7(0x10, 0x2A, 0x0)

    label("loc_779C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_77B3")
    OP_B8(0x11C, 0x0)
    OP_F7(0x10, 0x2B, 0x0)

    label("loc_77B3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_77CA")
    OP_B8(0x11D, 0x0)
    OP_F7(0x10, 0x2C, 0x0)

    label("loc_77CA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_77E1")
    OP_B8(0x11E, 0x0)
    OP_F7(0x10, 0x2D, 0x0)

    label("loc_77E1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_77F8")
    OP_B8(0x11F, 0x0)
    OP_F7(0x10, 0x2E, 0x0)

    label("loc_77F8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_780F")
    OP_B8(0x120, 0x0)
    OP_F7(0x10, 0x2F, 0x0)

    label("loc_780F")

    Jump("loc_7812")

    label("loc_7812")

    FadeToBright(300, 0)
    OP_5F(0x0)
    TalkEnd(0xFF)

    label("loc_7821")

    Return()

    # Function_19_7326 end

    def Function_20_7822(): pass

    label("Function_20_7822")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #147
        "\x07\x05There are a number of rare and valuable books here.\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(    #148
        "\x07\x05...For some reason, a copy of 'Liberlian Cuisine' also sits among them.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_20_7822 end

    def Function_21_78C4(): pass

    label("Function_21_78C4")

    SetMapFlags(0x80)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(500, 0, -1)

    def lambda_78E2():
        OP_90(0x0, 0x0, 0x0, 0x3E8, 0x514, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_78E2)
    OP_0D()
    NewScene("ED6_DT21/U7000   ._SN", 100, 0, 0)
    IdleLoop()
    EventEnd(0x0)
    Return()

    # Function_21_78C4 end

    SaveToFile()

Try(main)
