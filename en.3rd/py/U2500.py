from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'U2500   ._SN',
        MapName             = 'Gaiden2',
        Location            = 'U2500.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60231",
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
        'Wandering Monster',                    # 9
        'Wandering Monster',                    # 10
        'Wandering Monster',                    # 11
        '',                                     # 12
        '',                                     # 13
        '',                                     # 14
        '',                                     # 15
        '',                                     # 16
        '',                                     # 17
        '',                                     # 18
        '',                                     # 19
        '',                                     # 20
        '',                                     # 21
        '',                                     # 22
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
        'ED6_DT29/CH15140 ._CH',             # 00
        'ED6_DT29/CH15141 ._CH',             # 01
        'ED6_DT29/CH14650 ._CH',             # 02
        'ED6_DT29/CH14651 ._CH',             # 03
    )

    AddCharChipPat(
        'ED6_DT29/CH15140P._CP',             # 00
        'ED6_DT29/CH15141P._CP',             # 01
        'ED6_DT29/CH14650P._CP',             # 02
        'ED6_DT29/CH14651P._CP',             # 03
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


    DeclMonster(
        X                   = 37370,
        Z                   = 0,
        Y                   = 26500,
        Unknown_0C          = 0,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x26D,
        Unknown_18          = 11072,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 35790,
        Z                   = 0,
        Y                   = 74080,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x26E,
        Unknown_18          = 11073,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 45220,
        Z                   = 0,
        Y                   = 46150,
        Unknown_0C          = 270,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x26C,
        Unknown_18          = 11074,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 37370,
        Z                   = 0,
        Y                   = 26500,
        Unknown_0C          = 0,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x26C,
        Unknown_18          = 11072,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 35790,
        Z                   = 0,
        Y                   = 74080,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x26C,
        Unknown_18          = 11073,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 45220,
        Z                   = 0,
        Y                   = 46150,
        Unknown_0C          = 270,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x26C,
        Unknown_18          = 11074,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 63530,
        Z                   = 0,
        Y                   = 15260,
        Unknown_0C          = 270,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x26C,
        Unknown_18          = 11074,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 15900,
        Z                   = 0,
        Y                   = 34680,
        Unknown_0C          = 270,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x26C,
        Unknown_18          = 11074,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 63530,
        Z                   = 0,
        Y                   = 15260,
        Unknown_0C          = 270,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x2B7,
        Unknown_18          = 11127,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 15900,
        Z                   = 0,
        Y                   = 34680,
        Unknown_0C          = 90,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x2B8,
        Unknown_18          = 11128,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 60930,
        Z                   = 0,
        Y                   = 55660,
        Unknown_0C          = 0,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x2B6,
        Unknown_18          = 11129,
        Unknown_1A          = 0,
    )


    DeclEvent(
        X                   = 0,
        Y                   = 0,
        Z                   = 0,
        Range               = 0,
        Unknown_10          = 0x0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x20,
        Unknown_1C          = 6,
    )


    DeclActor(
        TriggerX            = 33760,
        TriggerZ            = -2000,
        TriggerY            = 51470,
        TriggerRange        = 1000,
        ActorX              = 33760,
        ActorZ              = 0,
        ActorY              = 51470,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 15,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 62940,
        TriggerZ            = 1000,
        TriggerY            = 79680,
        TriggerRange        = 1000,
        ActorX              = 62940,
        ActorZ              = 1000,
        ActorY              = 79680,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 30000,
        TriggerZ            = 1000,
        TriggerY            = 18220,
        TriggerRange        = 1000,
        ActorX              = 30000,
        ActorZ              = 1000,
        ActorY              = 18220,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 30000,
        TriggerZ            = 1000,
        TriggerY            = 20170,
        TriggerRange        = 1000,
        ActorX              = 30000,
        ActorZ              = 1000,
        ActorY              = 20170,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 16470,
        TriggerZ            = 1000,
        TriggerY            = 59660,
        TriggerRange        = 1000,
        ActorX              = 16470,
        ActorZ              = 1000,
        ActorY              = 59660,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 13530,
        TriggerZ            = 0,
        TriggerY            = 45970,
        TriggerRange        = 800,
        ActorX              = 13530,
        ActorZ              = 1000,
        ActorY              = 45970,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 20,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 66400,
        TriggerZ            = 0,
        TriggerY            = 28020,
        TriggerRange        = 800,
        ActorX              = 66400,
        ActorZ              = 1000,
        ActorY              = 28020,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 20,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_37A",          # 00, 0
        "Function_1_473",          # 01, 1
        "Function_2_620",          # 02, 2
        "Function_3_759",          # 03, 3
        "Function_4_85E",          # 04, 4
        "Function_5_9BB",          # 05, 5
        "Function_6_A69",          # 06, 6
        "Function_7_AB8",          # 07, 7
        "Function_8_B1A",          # 08, 8
        "Function_9_B80",          # 09, 9
        "Function_10_F08",         # 0A, 10
        "Function_11_10B0",        # 0B, 11
        "Function_12_1EBE",        # 0C, 12
        "Function_13_1F4F",        # 0D, 13
        "Function_14_1FE0",        # 0E, 14
        "Function_15_2077",        # 0F, 15
        "Function_16_22F9",        # 10, 16
        "Function_17_2490",        # 11, 17
        "Function_18_25F4",        # 12, 18
        "Function_19_270A",        # 13, 19
        "Function_20_2758",        # 14, 20
    )


    def Function_0_37A(): pass

    label("Function_0_37A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_399")
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (130, "loc_392"),
        (SWITCH_DEFAULT, "loc_399"),
    )


    label("loc_392")

    Event(0, 16)
    Jump("loc_399")

    label("loc_399")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 6)), scpexpr(EXPR_END)), "loc_3B1")
    OP_A3(0x2506)
    SetMapFlags(0x10000000)
    OP_B5(0x0)
    Event(0, 10)
    Jump("loc_3C6")

    label("loc_3B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_3C6")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    OP_B5(0x0)
    Event(0, 9)

    label("loc_3C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x560, 6)), scpexpr(EXPR_END)), "loc_3E9")
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x1B, 0x80)
    SetChrFlags(0x1C, 0x80)
    Jump("loc_43A")

    label("loc_3E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x568, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_40D")
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x17, 0x80)
    SetChrFlags(0x18, 0x80)
    SetChrFlags(0x19, 0x80)
    SetChrFlags(0x1A, 0x80)
    Jump("loc_43A")

    label("loc_40D")

    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x17, 0x80)
    SetChrFlags(0x19, 0x80)
    SetChrFlags(0x1A, 0x80)
    SetChrFlags(0x1B, 0x80)
    SetChrFlags(0x1C, 0x80)

    label("loc_43A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x560, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_472")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x568, 0)), scpexpr(EXPR_END)), "loc_44E")
    SetChrFlags(0x13, 0x80)

    label("loc_44E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x568, 1)), scpexpr(EXPR_END)), "loc_45A")
    SetChrFlags(0x14, 0x80)

    label("loc_45A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x56E, 7)), scpexpr(EXPR_END)), "loc_466")
    SetChrFlags(0x1B, 0x80)

    label("loc_466")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x56F, 0)), scpexpr(EXPR_END)), "loc_472")
    SetChrFlags(0x1C, 0x80)

    label("loc_472")

    Return()

    # Function_0_37A end

    def Function_1_473(): pass

    label("Function_1_473")

    OP_16(0x2, 0xFA0, 0xFFFEA840, 0xFFFEBFB0, 0x23004C)
    OP_B1("U2500_n")
    OP_1B(0x1E, 0x0, 0x11)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B2, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4A4")
    OP_82(0x80, 0x0)
    OP_82(0x81, 0x0)
    OP_82(0x83, 0x0)

    label("loc_4A4")

    OP_72(0x1009, 0x0)
    ExitThread()
    OP_6F(0x9, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x560, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4C9")
    OP_72(0x100A, 0x0)
    ExitThread()
    OP_6F(0xA, 0)
    Jump("loc_4CD")

    label("loc_4C9")

    OP_64(0x6, 0x1)

    label("loc_4CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x560, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5BB")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x29), scpexpr(EXPR_PUSH_LONG, 0x26D), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4EA")
    OP_CE(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4EA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x29), scpexpr(EXPR_PUSH_LONG, 0x26E), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4FF")
    OP_CE(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4FF")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x29), scpexpr(EXPR_PUSH_LONG, 0x26C), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_514")
    OP_CE(0x3, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_514")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x29), scpexpr(EXPR_PUSH_LONG, 0x2B7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_529")
    OP_CE(0x3, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_529")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x29), scpexpr(EXPR_PUSH_LONG, 0x2B8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_53E")
    OP_CE(0x3, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_53E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x29), scpexpr(EXPR_PUSH_LONG, 0x2B6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_553")
    OP_CE(0x3, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_553")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x568, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x568, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x56E, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x56F, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_572")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x568, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_572")
    Event(0, 7)

    label("loc_572")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x568, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x56F, 1)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5BB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x568, 3)), scpexpr(EXPR_END)), "loc_58B")
    Event(0, 8)
    Jump("loc_5BB")

    label("loc_58B")

    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x17, 0x80)
    SetChrFlags(0x1B, 0x80)
    SetChrFlags(0x1C, 0x80)
    OP_A3(0x2B40)
    OP_A3(0x2B41)
    OP_A3(0x2B77)
    OP_A3(0x2B78)
    OP_A3(0x2B42)
    OP_A3(0x2B79)

    label("loc_5BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x575, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5CD")
    OP_6F(0xC, 0)
    Jump("loc_5D4")

    label("loc_5CD")

    OP_6F(0xC, 60)

    label("loc_5D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x575, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5E6")
    OP_6F(0xD, 0)
    Jump("loc_5ED")

    label("loc_5E6")

    OP_6F(0xD, 60)

    label("loc_5ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x575, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5FF")
    OP_6F(0xE, 0)
    Jump("loc_606")

    label("loc_5FF")

    OP_6F(0xE, 60)

    label("loc_606")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x575, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_618")
    OP_6F(0xF, 0)
    Jump("loc_61F")

    label("loc_618")

    OP_6F(0xF, 60)

    label("loc_61F")

    Return()

    # Function_1_473 end

    def Function_2_620(): pass

    label("Function_2_620")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x575, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6F9")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0xC, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x2DF, 1)"), scpexpr(EXPR_END)), "loc_68E")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "\x07\x05Found \x1F\xDF\x02\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2BAC)
    Jump("loc_6F6")

    label("loc_68E")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "\x07\x05Found \x1F\xDF\x02\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\xDF\x02\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0xC, 60)
    OP_70(0xC, 0x0)

    label("loc_6F6")

    Jump("loc_74B")

    label("loc_6F9")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        "\x07\x05Your excuse for thievery is as wooden as I am.\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0xE6, 0x0)

    label("loc_74B")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_620 end

    def Function_3_759(): pass

    label("Function_3_759")

    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x575, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7C7")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0xD, 0x1E)
    OP_73(0xD)
    OP_6F(0xD, 30)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    AddMira(10000)

    AnonymousTalk(    #3
        "\x07\x05Received \x07\x0210,000 mira\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x2BAD)
    Jump("loc_847")

    label("loc_7C7")


    AnonymousTalk(    #4
        (
            "\x07\x05Step right up, step right up! Grab your free item today! Not you, sir--\x01",
            "you've already got yours. Leave some for others.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_847")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    OP_F7(0x19, 0xE7, 0x0)
    Return()

    # Function_3_759 end

    def Function_4_85E(): pass

    label("Function_4_85E")

    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x575, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8CC")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0xE, 0x1E)
    OP_73(0xE)
    OP_6F(0xE, 30)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    AddMira(10000)

    AnonymousTalk(    #5
        "\x07\x05Received \x07\x0010,000 mira\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x2BAE)
    Jump("loc_9A4")

    label("loc_8CC")


    AnonymousTalk(    #6
        (
            "\x07\x05[7/36] 'I ask you this: do you love me? I have the only key that locks the\x01",
            "chest. Should you return my love, I wish for us to meet once more in that\x01",
            "shop, and together, we will forever secure our love inside.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_9A4")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    OP_F7(0x19, 0xE8, 0x0)
    Return()

    # Function_4_85E end

    def Function_5_9BB(): pass

    label("Function_5_9BB")

    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x575, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A29")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0xF, 0x1E)
    OP_73(0xF)
    OP_6F(0xF, 30)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    AddMira(10000)

    AnonymousTalk(    #7
        "\x07\x05Received \x07\x0010,000 mira\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x2BAF)
    Jump("loc_A52")

    label("loc_A29")


    AnonymousTalk(    #8
        "\x07\x05Think outside the box. Er, chest.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_A52")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    OP_F7(0x19, 0xE9, 0x0)
    Return()

    # Function_5_9BB end

    def Function_6_A69(): pass

    label("Function_6_A69")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x568, 3)), scpexpr(EXPR_END)), "loc_A95")
    OP_C0(0x1F, 0x1, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Jump("loc_AB7")

    label("loc_A95")

    OP_C0(0x1F, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)

    label("loc_AB7")

    Return()

    # Function_6_A69 end

    def Function_7_AB8(): pass

    label("Function_7_AB8")

    EventBegin(0x0)
    Sleep(1000)
    OP_22(0x138, 0x0, 0x64)
    FadeToDark(1000, 16777215, -1)
    OP_0D()
    OP_C4(0x0, 0x10)
    FadeToBright(2000, 16777215)
    OP_0D()
    FadeToDark(0, 0, -1)
    OP_0D()
    OP_C4(0x1, 0x10)
    OP_A3(0x2B40)
    OP_A3(0x2B41)
    OP_A3(0x2B77)
    OP_A3(0x2B78)
    OP_A3(0x2B42)
    OP_A3(0x2B79)
    OP_A2(0x2B43)
    OP_28(0x37, 0x1, 0x20)
    OP_A2(0x2504)
    NewScene("ED6_DT21/U2500   ._SN", 100, 0, 1)
    IdleLoop()
    EventEnd(0x0)
    Return()

    # Function_7_AB8 end

    def Function_8_B1A(): pass

    label("Function_8_B1A")

    EventBegin(0x0)
    Sleep(1000)
    OP_22(0x138, 0x0, 0x64)
    FadeToDark(1000, 16777215, -1)
    OP_0D()
    OP_C4(0x0, 0x10)
    FadeToBright(2000, 16777215)
    OP_0D()
    FadeToDark(0, 0, -1)
    OP_0D()
    OP_C4(0x1, 0x10)
    OP_A3(0x2B40)
    OP_A3(0x2B41)
    OP_A3(0x2B77)
    OP_A3(0x2B78)
    OP_A3(0x2B42)
    OP_A3(0x2B79)
    OP_A3(0x2B43)
    OP_28(0x37, 0x1, 0x40)
    OP_64(0x2, 0x1)
    OP_A2(0x2504)
    NewScene("ED6_DT21/U2500   ._SN", 100, 0, 1)
    IdleLoop()
    EventEnd(0x0)
    Return()

    # Function_8_B1A end

    def Function_9_B80(): pass

    label("Function_9_B80")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x560, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BC5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x568, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x568, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x569, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x569, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x56A, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x56A, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_BC5")
    OP_CE(0x4, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A2(0x2506)
    NewScene("ED6_DT21/U2500   ._SN", 100, 0, 1)
    IdleLoop()
    Return()

    label("loc_BC5")

    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C4B")
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, 37370, 0, 26500, 0)
    SetChrPos(0x1, 37370, 0, 26500, 0)
    SetChrPos(0x2, 37370, 0, 26500, 0)
    SetChrPos(0x3, 37370, 0, 26500, 0)
    OP_69(0x0, 0x0)
    Jump("loc_EF7")

    label("loc_C4B")

    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CD1")
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, 35790, 0, 74080, 180)
    SetChrPos(0x1, 35790, 0, 74080, 180)
    SetChrPos(0x2, 35790, 0, 74080, 180)
    SetChrPos(0x3, 35790, 0, 74080, 180)
    OP_69(0x0, 0x0)
    Jump("loc_EF7")

    label("loc_CD1")

    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D57")
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, 45220, 0, 46150, 270)
    SetChrPos(0x1, 45220, 0, 46150, 270)
    SetChrPos(0x2, 45220, 0, 46150, 270)
    SetChrPos(0x3, 45220, 0, 46150, 270)
    OP_69(0x0, 0x0)
    Jump("loc_EF7")

    label("loc_D57")

    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DDD")
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(0, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, 63530, 0, 15260, 0)
    SetChrPos(0x1, 63530, 0, 15260, 0)
    SetChrPos(0x2, 63530, 0, 15260, 0)
    SetChrPos(0x3, 63530, 0, 15260, 0)
    OP_69(0x0, 0x0)
    Jump("loc_EF7")

    label("loc_DDD")

    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E63")
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, 17420, 0, 34850, 90)
    SetChrPos(0x1, 17420, 0, 34850, 90)
    SetChrPos(0x2, 17420, 0, 34850, 90)
    SetChrPos(0x3, 17420, 0, 34850, 90)
    OP_69(0x0, 0x0)
    Jump("loc_EF7")

    label("loc_E63")

    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EF7")
    OP_6D(60930, 0, 55660, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(180000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, 60930, 0, 55660, 180)
    SetChrPos(0x1, 60930, 0, 55660, 180)
    SetChrPos(0x2, 60930, 0, 55660, 180)
    SetChrPos(0x3, 60930, 0, 55660, 180)
    OP_69(0x0, 0x0)

    label("loc_EF7")

    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_9_B80 end

    def Function_10_F08(): pass

    label("Function_10_F08")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_6D(42120, 5150, 28820, 0)
    OP_67(0, 8100, -10000, 0)
    OP_6B(2940, 0)
    OP_6C(135000, 0)
    OP_6E(386, 0)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)

    def lambda_F6B():
        OP_6D(69190, 450, 28060, 6000)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_F6B)

    def lambda_F83():
        OP_67(0, 4780, -10000, 6000)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_F83)

    def lambda_F9B():
        OP_6B(3100, 6000)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_F9B)

    def lambda_FAB():
        OP_6C(90000, 6000)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_FAB)

    def lambda_FBB():
        OP_6E(304, 6000)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_FBB)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0xEE, 0x0)
    Sleep(500)
    OP_22(0x73, 0x0, 0x64)
    Sleep(1000)
    OP_72(0x100A, 0x0)
    ExitThread()
    OP_6F(0xA, 0)
    OP_70(0xA, 0x3C)
    Sleep(1500)
    OP_A2(0x2B06)
    OP_28(0x37, 0x1, 0x80)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_102B")
    OP_A2(0x2504)
    NewScene("ED6_DT21/U2500   ._SN", 100, 0, 1)
    IdleLoop()
    Jump("loc_10AF")

    label("loc_102B")

    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1046")
    OP_A2(0x2504)
    NewScene("ED6_DT21/U2510   ._SN", 100, 0, 1)
    IdleLoop()
    Jump("loc_10AF")

    label("loc_1046")

    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1061")
    OP_A2(0x2504)
    NewScene("ED6_DT21/U2511   ._SN", 100, 0, 1)
    IdleLoop()
    Jump("loc_10AF")

    label("loc_1061")

    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_107C")
    OP_A2(0x2504)
    NewScene("ED6_DT21/U2512   ._SN", 100, 0, 1)
    IdleLoop()
    Jump("loc_10AF")

    label("loc_107C")

    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1097")
    OP_A2(0x2505)
    NewScene("ED6_DT21/U2512   ._SN", 109, 0, 1)
    IdleLoop()
    Jump("loc_10AF")

    label("loc_1097")

    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10AF")
    OP_A2(0x2504)
    NewScene("ED6_DT21/U2513   ._SN", 100, 0, 1)
    IdleLoop()

    label("loc_10AF")

    Return()

    # Function_10_F08 end

    def Function_11_10B0(): pass

    label("Function_11_10B0")

    OP_DE(0x0, 0x1E, 0x1)
    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x10, 37370, 0, 26500, 0)
    SetChrPos(0x11, 35790, 0, 74080, 180)
    SetChrPos(0x12, 45220, 0, 46150, 270)
    OP_43(0x10, 0x0, 0x0, 0xC)
    OP_43(0x11, 0x0, 0x0, 0xD)
    OP_43(0x12, 0x0, 0x0, 0xE)
    SetChrPos(0x109, 18050, 0, 44980, 90)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_117B")
    SetChrPos(0xEF, 18850, 0, 45710, 90)
    SetChrPos(0xF0, 18020, 0, 46830, 90)
    SetChrPos(0xF1, 17090, 0, 45920, 90)
    Jump("loc_1200")

    label("loc_117B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11BF")
    SetChrPos(0xF0, 18850, 0, 45710, 90)
    SetChrPos(0xEF, 18020, 0, 46830, 90)
    SetChrPos(0xF1, 17090, 0, 45920, 90)
    Jump("loc_1200")

    label("loc_11BF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1200")
    SetChrPos(0xF1, 18850, 0, 45710, 90)
    SetChrPos(0xEF, 18020, 0, 46830, 90)
    SetChrPos(0xF0, 17090, 0, 45920, 90)

    label("loc_1200")

    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_6D(17340, 0, 46820, 0)
    OP_67(0, 7590, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(314000, 0)
    OP_6E(280, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)
    LoadEffect(0x0, "map\\mp200_02.eff")
    PlayEffect(0x0, 0xFF, 0xEE, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xEF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xF0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xF1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)

    def lambda_136F():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_136F)

    def lambda_1381():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_1381)

    def lambda_1393():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_1393)

    def lambda_13A5():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_13A5)
    Sleep(1500)
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13FA")
    OP_62(0xEF, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1461")

    label("loc_13FA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1422")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1461")

    label("loc_1422")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_144A")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1461")

    label("loc_144A")

    OP_62(0xEF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_1461")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_148E")
    OP_62(0xF0, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_14F5")

    label("loc_148E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14B6")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_14F5")

    label("loc_14B6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14DE")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_14F5")

    label("loc_14DE")

    OP_62(0xF0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_14F5")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1522")
    OP_62(0xF1, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1589")

    label("loc_1522")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_154A")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1589")

    label("loc_154A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1572")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1589")

    label("loc_1572")

    OP_62(0xF1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_1589")

    Sleep(1000)

    ChrTalk(    #9
        0x109,
        "#1079F#5PWh-What the...?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x105,
        (
            "#1163F#5PThe royal academy? But everything's been drained \x01",
            "of color...\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(1000)
    ClearMapFlags(0x10)
    OP_6D(30000, 300, 46550, 0)
    OP_67(0, 9040, -10000, 0)
    OP_6B(4820, 0)
    OP_6C(45000, 0)
    OP_6E(362, 0)

    def lambda_164B():
        OP_6D(48040, 300, 46550, 6000)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_164B)

    def lambda_1663():
        OP_67(0, 9790, -10000, 6000)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_1663)

    def lambda_167B():
        OP_6B(4900, 6000)
        ExitThread()

    QueueWorkItem(0xF0, 1, lambda_167B)

    def lambda_168B():
        OP_6C(45000, 6000)
        ExitThread()

    QueueWorkItem(0xF1, 1, lambda_168B)

    def lambda_169B():
        OP_6E(362, 6000)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_169B)
    Sleep(1000)
    OP_C8(0x200, 0x46, "C_PLAC34._CH", 0x1, 0x3E8)
    Sleep(1500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1750")

    def lambda_16D8():
        OP_8F(0xFE, 0x5B04, 0x0, 0xB522, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_16D8)
    Sleep(300)

    def lambda_16F8():
        OP_8F(0xFE, 0x55F0, 0x0, 0xB18A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_16F8)
    Sleep(100)

    def lambda_1718():
        OP_8F(0xFE, 0x55F0, 0x0, 0xB7DE, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_1718)
    Sleep(100)

    def lambda_1738():
        OP_8F(0xFE, 0x5208, 0x0, 0xB40A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_1738)
    Jump("loc_1865")

    label("loc_1750")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_17DC")

    def lambda_1764():
        OP_8F(0xFE, 0x5B04, 0x0, 0xB522, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_1764)
    Sleep(300)

    def lambda_1784():
        OP_8F(0xFE, 0x55F0, 0x0, 0xB18A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1784)
    Sleep(100)

    def lambda_17A4():
        OP_8F(0xFE, 0x55F0, 0x0, 0xB7DE, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_17A4)
    Sleep(100)

    def lambda_17C4():
        OP_8F(0xFE, 0x5208, 0x0, 0xB40A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_17C4)
    Jump("loc_1865")

    label("loc_17DC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1865")

    def lambda_17F0():
        OP_8F(0xFE, 0x5B04, 0x0, 0xB522, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_17F0)
    Sleep(300)

    def lambda_1810():
        OP_8F(0xFE, 0x55F0, 0x0, 0xB18A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1810)
    Sleep(100)

    def lambda_1830():
        OP_8F(0xFE, 0x55F0, 0x0, 0xB7DE, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_1830)
    Sleep(100)

    def lambda_1850():
        OP_8F(0xFE, 0x5208, 0x0, 0xB40A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_1850)

    label("loc_1865")

    WaitChrThread(0xEE, 0x1)
    Fade(1000)
    OP_6D(46530, 0, 46790, 0)
    OP_67(0, 8600, -10000, 0)
    OP_6B(2100, 0)
    OP_6C(45000, 0)
    OP_6E(421, 0)
    OP_0D()
    Sleep(1500)
    Fade(1000)
    OP_6D(37030, 0, 71070, 0)
    OP_67(0, 8600, -10000, 0)
    OP_6B(2100, 0)
    OP_6C(45000, 0)
    OP_6E(421, 0)
    OP_0D()
    Sleep(1500)
    Fade(1000)
    OP_6D(36920, 0, 25790, 0)
    OP_67(0, 8600, -10000, 0)
    OP_6B(2100, 0)
    OP_6C(134000, 0)
    OP_6E(421, 0)
    OP_0D()
    Sleep(1500)
    Fade(1000)
    SetMapFlags(0x10)
    OP_6D(23800, 0, 47340, 0)
    OP_67(0, 8570, -10000, 0)
    OP_6B(2540, 0)
    OP_6C(44000, 0)
    OP_6E(277, 0)
    OP_0D()
    Sleep(500)
    WaitChrThread(0xEE, 0x0)
    WaitChrThread(0xEF, 0x0)
    WaitChrThread(0xF0, 0x0)
    WaitChrThread(0xF1, 0x0)

    ChrTalk(    #11
        0x109,
        (
            "#1063F#6PAnd now we know what 'monochrome schoolhouse'\x01",
            "was supposed to mean.\x02\x03",

            "#1841FSure is creepy to be in a world of black and white\x01",
            "like this, though...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x105,
        "#1169F#5PI feel the same way...\x02",
    )

    CloseMessageWindow()
    OP_8C(0x105, 270, 400)
    Sleep(300)

    ChrTalk(    #13
        0x105,
        (
            "#1162F#11PEven if it is creepy, however, we still have to explore\x01",
            "the grounds from top to bottom, so we may as well\x01",
            "get started.\x02\x03",

            "There are five buildings in all: the main building, the\x01",
            "clubhouse, the girls' dorm, the boys' dorm, and the\x01",
            "auditorium.\x02\x03",

            "There's also the old schoolhouse, which is accessible\x01",
            "via the path at the back of the main grounds.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x109,
        (
            "#1065F#6PGood to know.\x02\x03",

            "#1063FWe're going to need to keep an eye out\x01",
            "for those knights prowling around, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x105,
        "#1162F#11PRight!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1C88")

    ChrTalk(    #16
        0x101,
        "#1002F#6PGot it!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1CAB")

    label("loc_1C88")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1CAB")

    ChrTalk(    #17
        0x10B,
        "#212F#6PGot it!\x02",
    )

    CloseMessageWindow()

    label("loc_1CAB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1CD0")

    ChrTalk(    #18
        0x106,
        "#057F#6PRight!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1CF2")

    label("loc_1CD0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1CF2")

    ChrTalk(    #19
        0x108,
        "#072F#6PRight!\x02",
    )

    CloseMessageWindow()

    label("loc_1CF2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1D1C")

    ChrTalk(    #20
        0x10E,
        "#178F#6PUnderstood!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1D43")

    label("loc_1D1C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xB)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1D43")

    ChrTalk(    #21
        0x10C,
        "#112F#6PUnderstood!\x02",
    )

    CloseMessageWindow()

    label("loc_1D43")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1D6A")

    ChrTalk(    #22
        0x10D,
        "#270F#6PUnderstood!\x02",
    )

    CloseMessageWindow()

    label("loc_1D6A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1D91")

    ChrTalk(    #23
        0x107,
        "#065F#6PR-Right!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1DB7")

    label("loc_1D91")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1DB7")

    ChrTalk(    #24
        0x10A,
        "#812F#6PAll right!\x02",
    )

    CloseMessageWindow()

    label("loc_1DB7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1DE2")

    ChrTalk(    #25
        0x10F,
        "#1443F#6PUnderstood!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1E2C")

    label("loc_1DE2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1E09")

    ChrTalk(    #26
        0x102,
        "#1502F#6PGot it!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1E2C")

    label("loc_1E09")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1E2C")

    ChrTalk(    #27
        0x103,
        "#1522F#6PRight!\x02",
    )

    CloseMessageWindow()

    label("loc_1E2C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1E52")

    ChrTalk(    #28
        0x104,
        "#1545F#6POn we go.\x02",
    )

    CloseMessageWindow()

    label("loc_1E52")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1E8F")

    ChrTalk(    #29
        0x110,
        "#263F#6PI can't wait to see what we find.\x02",
    )

    CloseMessageWindow()

    label("loc_1E8F")

    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    OP_A2(0x2B05)
    OP_28(0x37, 0x1, 0x10)
    Sleep(300)
    EventEnd(0x0)
    Return()

    # Function_11_10B0 end

    def Function_12_1EBE(): pass

    label("Function_12_1EBE")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1F4E")
    SetChrChipByIndex(0xFE, 1)
    OP_8E(0xFE, 0x87E6, 0x0, 0x6EDC, 0x3E8, 0x0)
    SetChrChipByIndex(0xFE, 0)
    Sleep(500)
    OP_8C(0xFE, 0, 400)
    Sleep(1000)
    OP_8C(0xFE, 270, 400)
    Sleep(1500)
    OP_8C(0xFE, 135, 400)
    SetChrChipByIndex(0xFE, 1)
    OP_8E(0xFE, 0x92B8, 0x0, 0x5BE0, 0x3E8, 0x0)
    SetChrChipByIndex(0xFE, 0)
    Sleep(500)
    OP_8C(0xFE, 180, 400)
    Sleep(1000)
    OP_8C(0xFE, 90, 400)
    Sleep(1500)
    OP_8C(0xFE, 315, 400)
    Jump("Function_12_1EBE")

    label("loc_1F4E")

    Return()

    # Function_12_1EBE end

    def Function_13_1F4F(): pass

    label("Function_13_1F4F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1FDF")
    SetChrChipByIndex(0xFE, 1)
    OP_8E(0xFE, 0x8B6A, 0x0, 0x1034C, 0x3E8, 0x0)
    SetChrChipByIndex(0xFE, 0)
    Sleep(500)
    OP_8C(0xFE, 270, 400)
    Sleep(1000)
    OP_8C(0xFE, 90, 400)
    Sleep(1500)
    OP_8C(0xFE, 0, 400)
    SetChrChipByIndex(0xFE, 1)
    OP_8E(0xFE, 0x8AAC, 0x0, 0x121EC, 0x3E8, 0x0)
    SetChrChipByIndex(0xFE, 0)
    Sleep(500)
    OP_8C(0xFE, 90, 400)
    Sleep(1000)
    OP_8C(0xFE, 270, 400)
    Sleep(1500)
    OP_8C(0xFE, 180, 400)
    Jump("Function_13_1F4F")

    label("loc_1FDF")

    Return()

    # Function_13_1F4F end

    def Function_14_1FE0(): pass

    label("Function_14_1FE0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2076")
    OP_8C(0xFE, 0, 400)
    SetChrChipByIndex(0xFE, 3)
    OP_8E(0xFE, 0xB2E8, 0x0, 0xBF86, 0x3E8, 0x0)
    SetChrChipByIndex(0xFE, 2)
    Sleep(1000)
    OP_8C(0xFE, 225, 400)
    SetChrChipByIndex(0xFE, 3)
    OP_8E(0xFE, 0xACC6, 0x0, 0xB568, 0x3E8, 0x0)
    SetChrChipByIndex(0xFE, 2)
    Sleep(1500)
    OP_8C(0xFE, 270, 400)
    Sleep(1500)
    OP_8C(0xFE, 135, 400)
    SetChrChipByIndex(0xFE, 3)
    OP_8E(0xFE, 0xB1B2, 0x0, 0xABB8, 0x3E8, 0x0)
    SetChrChipByIndex(0xFE, 2)
    Sleep(1500)
    Jump("Function_14_1FE0")

    label("loc_2076")

    Return()

    # Function_14_1FE0 end

    def Function_15_2077(): pass

    label("Function_15_2077")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B2, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2146")
    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(500)
    OP_22(0x161, 0x0, 0x64)
    Fade(1000)
    PlayEffect(0x80, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x81, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x83, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_0D()
    OP_AA(5120)
    Sleep(500)
    Jump("loc_2149")

    label("loc_2146")

    TalkBegin(0xFF)

    label("loc_2149")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #30
        "\x07\x05Select an Option\x18\x02",
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2185")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_22C8")

    Menu(
        1,
        -1,
        150,
        1,
        (
            "Restore HP/EP\x01",          # 0
            "Shop\x01",                   # 1
            "Synthesize Quartz\x01",      # 2
            "End\x01",                    # 3
        )
    )

    MenuEnd(0x0)
    OP_5F(0x1)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_21E1"),
        (1, "loc_225C"),
        (2, "loc_228A"),
        (SWITCH_DEFAULT, "loc_22B8"),
    )


    label("loc_21E1")

    FadeToBright(300, 0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(300)
    OP_20(0x3E8)
    OP_22(0xC, 0x0, 0x64)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_22(0xD, 0x0, 0x64)
    OP_C0(0x15, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_30(0x1)
    Sleep(3500)
    OP_1D(0xE7)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToBright(1000, 0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_22C5")

    label("loc_225C")

    OP_A9(0x26)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #31
        "\x07\x05Select an Option\x18\x02",
    )

    Jump("loc_22C5")

    label("loc_228A")

    OP_A9(0x9)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #32
        "\x07\x05Select an Option\x18\x02",
    )

    Jump("loc_22C5")

    label("loc_22B8")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_22C5")

    label("loc_22C5")

    Jump("loc_2185")

    label("loc_22C8")

    OP_5F(0x1)
    OP_56(0x0)
    FadeToBright(300, 0)
    Sleep(300)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B2, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22F5")
    OP_A2(0x2597)
    EventEnd(0x1)
    Jump("loc_22F8")

    label("loc_22F5")

    TalkEnd(0xFF)

    label("loc_22F8")

    Return()

    # Function_15_2077 end

    def Function_16_22F9(): pass

    label("Function_16_22F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x560, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x560, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_230A")
    Call(0, 11)
    Return()

    label("loc_230A")

    OP_DE(0x0, 0x1E, 0x1)
    EventBegin(0x2)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x0, 18850, 0, 45710, 90)
    SetChrPos(0x1, 18050, 0, 44980, 90)
    SetChrPos(0x2, 18020, 0, 46830, 90)
    SetChrPos(0x3, 17090, 0, 45920, 90)
    OP_69(0x0, 0x0)
    OP_6C(315000, 0)
    LoadEffect(0x0, "map\\mp200_02.eff")
    PlayEffect(0x0, 0xFF, 0xEE, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xEF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xF0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xF1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Call(0, 18)
    EventEnd(0x0)
    OP_4F(0x31, (scpexpr(EXPR_PUSH_LONG, 0x5B), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_C0(0x16, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Return()

    # Function_16_22F9 end

    def Function_17_2490(): pass

    label("Function_17_2490")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    SetChrPos(0x3, 18850, 0, 45710, 270)
    SetChrPos(0x2, 18050, 0, 44980, 270)
    SetChrPos(0x1, 18020, 0, 46830, 270)
    SetChrPos(0x0, 17090, 0, 45920, 270)
    OP_69(0x0, 0x0)
    OP_6C(315000, 0)
    OP_0D()
    LoadEffect(0x0, "map\\mp200_01.eff")
    PlayEffect(0x0, 0xFF, 0xEE, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xEF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xF0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xF1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Call(0, 19)
    NewScene("ED6_DT21/M4112   ._SN", 102, 0, 0)
    IdleLoop()
    Return()

    # Function_17_2490 end

    def Function_18_25F4(): pass

    label("Function_18_25F4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_261D")
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_2611():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_2611)

    label("loc_261D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2646")
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_263A():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_263A)

    label("loc_2646")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_266F")
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_2663():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_2663)

    label("loc_266F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2698")
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_268C():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_268C)

    label("loc_2698")

    Sleep(800)
    OP_44(0x0, 0x1)
    OP_44(0x1, 0x1)
    OP_44(0x2, 0x1)
    OP_44(0x3, 0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_26C4")
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_26C4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_26DB")
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_26DB")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_26F2")
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_26F2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2709")
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_2709")

    Return()

    # Function_18_25F4 end

    def Function_19_270A(): pass

    label("Function_19_270A")


    def lambda_2710():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_2710)

    def lambda_2722():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_2722)

    def lambda_2734():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_2734)

    def lambda_2746():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_2746)
    Sleep(1000)
    Return()

    # Function_19_270A end

    def Function_20_2758(): pass

    label("Function_20_2758")

    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #33
        "\x07\x05The door is locked.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_20_2758 end

    SaveToFile()

Try(main)
