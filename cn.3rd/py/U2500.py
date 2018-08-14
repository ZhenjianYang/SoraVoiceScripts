from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

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
        '徘徊魔兽',                             # 9
        '徘徊魔兽',                             # 10
        '徘徊魔兽',                             # 11
        '',                                     # 12
        '',                                     # 13
        '',                                     # 14
        '',                                     # 15
        '',                                     # 16
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
        "Function_3_746",          # 03, 3
        "Function_4_7E8",          # 04, 4
        "Function_5_88A",          # 05, 5
        "Function_6_92C",          # 06, 6
        "Function_7_97B",          # 07, 7
        "Function_8_9DD",          # 08, 8
        "Function_9_A43",          # 09, 9
        "Function_10_DCB",         # 0A, 10
        "Function_11_F73",         # 0B, 11
        "Function_12_1CDD",        # 0C, 12
        "Function_13_1D6E",        # 0D, 13
        "Function_14_1DFF",        # 0E, 14
        "Function_15_1E96",        # 0F, 15
        "Function_16_212E",        # 10, 16
        "Function_17_22C5",        # 11, 17
        "Function_18_2429",        # 12, 18
        "Function_19_253F",        # 13, 19
        "Function_20_258D",        # 14, 20
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x575, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_705")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0xC, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x2DF, 1)"), scpexpr(EXPR_END)), "loc_694")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "\x07\x00得到了\x1F\xDF\x02\x07\x00。\x02",
    )

    Jump("loc_679")

    label("loc_679")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2BAC)
    Jump("loc_702")

    label("loc_694")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "宝箱里装有\x1F\xDF\x02\x07\x00。\x01",
            "不过现有的数量太多，\x1F\xDF\x02\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_6E3")

    label("loc_6E3")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0xC, 60)
    OP_70(0xC, 0x0)

    label("loc_702")

    Jump("loc_738")

    label("loc_705")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_738")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_620 end

    def Function_3_746(): pass

    label("Function_3_746")

    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x575, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7BA")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0xD, 0x1E)
    OP_73(0xD)
    OP_6F(0xD, 30)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    AddMira(10000)

    AnonymousTalk(    #3
        "\x07\x00得到了\x07\x02１００００米拉\x07\x00。\x02",
    )

    Jump("loc_7A8")

    label("loc_7A8")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x2BAD)
    Jump("loc_7D6")

    label("loc_7BA")


    AnonymousTalk(    #4
        "\x07\x05宝箱中什么都没有。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_7D6")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_746 end

    def Function_4_7E8(): pass

    label("Function_4_7E8")

    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x575, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_85C")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0xE, 0x1E)
    OP_73(0xE)
    OP_6F(0xE, 30)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    AddMira(10000)

    AnonymousTalk(    #5
        "\x07\x00得到了\x07\x02１００００米拉\x07\x00。\x02",
    )

    Jump("loc_84A")

    label("loc_84A")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x2BAE)
    Jump("loc_878")

    label("loc_85C")


    AnonymousTalk(    #6
        "\x07\x05宝箱中什么都没有。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_878")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_7E8 end

    def Function_5_88A(): pass

    label("Function_5_88A")

    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x575, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8FE")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0xF, 0x1E)
    OP_73(0xF)
    OP_6F(0xF, 30)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    AddMira(10000)

    AnonymousTalk(    #7
        "\x07\x00得到了\x07\x02１００００米拉\x07\x00。\x02",
    )

    Jump("loc_8EC")

    label("loc_8EC")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x2BAF)
    Jump("loc_91A")

    label("loc_8FE")


    AnonymousTalk(    #8
        "\x07\x05宝箱中什么都没有。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_91A")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_88A end

    def Function_6_92C(): pass

    label("Function_6_92C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x568, 3)), scpexpr(EXPR_END)), "loc_958")
    OP_C0(0x1F, 0x1, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Jump("loc_97A")

    label("loc_958")

    OP_C0(0x1F, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)

    label("loc_97A")

    Return()

    # Function_6_92C end

    def Function_7_97B(): pass

    label("Function_7_97B")

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

    # Function_7_97B end

    def Function_8_9DD(): pass

    label("Function_8_9DD")

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

    # Function_8_9DD end

    def Function_9_A43(): pass

    label("Function_9_A43")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x560, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A88")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x568, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x568, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x569, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x569, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x56A, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x56A, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A88")
    OP_CE(0x4, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A2(0x2506)
    NewScene("ED6_DT21/U2500   ._SN", 100, 0, 1)
    IdleLoop()
    Return()

    label("loc_A88")

    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B0E")
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, 37370, 0, 26500, 0)
    SetChrPos(0x1, 37370, 0, 26500, 0)
    SetChrPos(0x2, 37370, 0, 26500, 0)
    SetChrPos(0x3, 37370, 0, 26500, 0)
    OP_69(0x0, 0x0)
    Jump("loc_DBA")

    label("loc_B0E")

    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B94")
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, 35790, 0, 74080, 180)
    SetChrPos(0x1, 35790, 0, 74080, 180)
    SetChrPos(0x2, 35790, 0, 74080, 180)
    SetChrPos(0x3, 35790, 0, 74080, 180)
    OP_69(0x0, 0x0)
    Jump("loc_DBA")

    label("loc_B94")

    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C1A")
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, 45220, 0, 46150, 270)
    SetChrPos(0x1, 45220, 0, 46150, 270)
    SetChrPos(0x2, 45220, 0, 46150, 270)
    SetChrPos(0x3, 45220, 0, 46150, 270)
    OP_69(0x0, 0x0)
    Jump("loc_DBA")

    label("loc_C1A")

    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CA0")
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(0, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, 63530, 0, 15260, 0)
    SetChrPos(0x1, 63530, 0, 15260, 0)
    SetChrPos(0x2, 63530, 0, 15260, 0)
    SetChrPos(0x3, 63530, 0, 15260, 0)
    OP_69(0x0, 0x0)
    Jump("loc_DBA")

    label("loc_CA0")

    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D26")
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, 17420, 0, 34850, 90)
    SetChrPos(0x1, 17420, 0, 34850, 90)
    SetChrPos(0x2, 17420, 0, 34850, 90)
    SetChrPos(0x3, 17420, 0, 34850, 90)
    OP_69(0x0, 0x0)
    Jump("loc_DBA")

    label("loc_D26")

    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DBA")
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

    label("loc_DBA")

    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_9_A43 end

    def Function_10_DCB(): pass

    label("Function_10_DCB")

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

    def lambda_E2E():
        OP_6D(69190, 450, 28060, 6000)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_E2E)

    def lambda_E46():
        OP_67(0, 4780, -10000, 6000)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_E46)

    def lambda_E5E():
        OP_6B(3100, 6000)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_E5E)

    def lambda_E6E():
        OP_6C(90000, 6000)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_E6E)

    def lambda_E7E():
        OP_6E(304, 6000)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_E7E)
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
    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EEE")
    OP_A2(0x2504)
    NewScene("ED6_DT21/U2500   ._SN", 100, 0, 1)
    IdleLoop()
    Jump("loc_F72")

    label("loc_EEE")

    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F09")
    OP_A2(0x2504)
    NewScene("ED6_DT21/U2510   ._SN", 100, 0, 1)
    IdleLoop()
    Jump("loc_F72")

    label("loc_F09")

    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F24")
    OP_A2(0x2504)
    NewScene("ED6_DT21/U2511   ._SN", 100, 0, 1)
    IdleLoop()
    Jump("loc_F72")

    label("loc_F24")

    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F3F")
    OP_A2(0x2504)
    NewScene("ED6_DT21/U2512   ._SN", 100, 0, 1)
    IdleLoop()
    Jump("loc_F72")

    label("loc_F3F")

    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F5A")
    OP_A2(0x2505)
    NewScene("ED6_DT21/U2512   ._SN", 109, 0, 1)
    IdleLoop()
    Jump("loc_F72")

    label("loc_F5A")

    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F72")
    OP_A2(0x2504)
    NewScene("ED6_DT21/U2513   ._SN", 100, 0, 1)
    IdleLoop()

    label("loc_F72")

    Return()

    # Function_10_DCB end

    def Function_11_F73(): pass

    label("Function_11_F73")

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
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_103E")
    SetChrPos(0xEF, 18850, 0, 45710, 90)
    SetChrPos(0xF0, 18020, 0, 46830, 90)
    SetChrPos(0xF1, 17090, 0, 45920, 90)
    Jump("loc_10C3")

    label("loc_103E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1082")
    SetChrPos(0xF0, 18850, 0, 45710, 90)
    SetChrPos(0xEF, 18020, 0, 46830, 90)
    SetChrPos(0xF1, 17090, 0, 45920, 90)
    Jump("loc_10C3")

    label("loc_1082")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10C3")
    SetChrPos(0xF1, 18850, 0, 45710, 90)
    SetChrPos(0xEF, 18020, 0, 46830, 90)
    SetChrPos(0xF0, 17090, 0, 45920, 90)

    label("loc_10C3")

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

    def lambda_1232():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_1232)

    def lambda_1244():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_1244)

    def lambda_1256():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_1256)

    def lambda_1268():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_1268)
    Sleep(1500)
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12BD")
    OP_62(0xEF, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1324")

    label("loc_12BD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12E5")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1324")

    label("loc_12E5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_130D")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1324")

    label("loc_130D")

    OP_62(0xEF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_1324")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1351")
    OP_62(0xF0, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_13B8")

    label("loc_1351")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1379")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_13B8")

    label("loc_1379")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13A1")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_13B8")

    label("loc_13A1")

    OP_62(0xF0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_13B8")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13E5")
    OP_62(0xF1, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_144C")

    label("loc_13E5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_140D")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_144C")

    label("loc_140D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1435")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_144C")

    label("loc_1435")

    OP_62(0xF1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_144C")

    Sleep(1000)

    ChrTalk(    #9
        0x109,
        "#1079F#5P什、什么……！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x105,
        (
            "#1163F#5P王立学院……\x01",
            "但是，这个样子……\x02",
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

    def lambda_14FE():
        OP_6D(48040, 300, 46550, 6000)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_14FE)

    def lambda_1516():
        OP_67(0, 9790, -10000, 6000)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_1516)

    def lambda_152E():
        OP_6B(4900, 6000)
        ExitThread()

    QueueWorkItem(0xF0, 1, lambda_152E)

    def lambda_153E():
        OP_6C(45000, 6000)
        ExitThread()

    QueueWorkItem(0xF1, 1, lambda_153E)

    def lambda_154E():
        OP_6E(362, 6000)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_154E)
    Sleep(1000)
    OP_C8(0x200, 0x46, "C_PLAC34._CH", 0x1, 0x3E8)
    Sleep(1500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1603")

    def lambda_158B():
        OP_8F(0xFE, 0x5B04, 0x0, 0xB522, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_158B)
    Sleep(300)

    def lambda_15AB():
        OP_8F(0xFE, 0x55F0, 0x0, 0xB18A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_15AB)
    Sleep(100)

    def lambda_15CB():
        OP_8F(0xFE, 0x55F0, 0x0, 0xB7DE, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_15CB)
    Sleep(100)

    def lambda_15EB():
        OP_8F(0xFE, 0x5208, 0x0, 0xB40A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_15EB)
    Jump("loc_1718")

    label("loc_1603")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_168F")

    def lambda_1617():
        OP_8F(0xFE, 0x5B04, 0x0, 0xB522, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_1617)
    Sleep(300)

    def lambda_1637():
        OP_8F(0xFE, 0x55F0, 0x0, 0xB18A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1637)
    Sleep(100)

    def lambda_1657():
        OP_8F(0xFE, 0x55F0, 0x0, 0xB7DE, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_1657)
    Sleep(100)

    def lambda_1677():
        OP_8F(0xFE, 0x5208, 0x0, 0xB40A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_1677)
    Jump("loc_1718")

    label("loc_168F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1718")

    def lambda_16A3():
        OP_8F(0xFE, 0x5B04, 0x0, 0xB522, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_16A3)
    Sleep(300)

    def lambda_16C3():
        OP_8F(0xFE, 0x55F0, 0x0, 0xB18A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_16C3)
    Sleep(100)

    def lambda_16E3():
        OP_8F(0xFE, 0x55F0, 0x0, 0xB7DE, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_16E3)
    Sleep(100)

    def lambda_1703():
        OP_8F(0xFE, 0x5208, 0x0, 0xB40A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_1703)

    label("loc_1718")

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
            "#1063F#6P无色的学舍……\x01",
            "真如文字所描述的那样。\x02\x03",

            "#1841F话说回来，\x01",
            "这还真是噩梦般的景象呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x105,
        "#1169F#5P是啊……\x02",
    )

    CloseMessageWindow()
    OP_8C(0x105, 270, 400)
    Sleep(300)

    ChrTalk(    #13
        0x105,
        (
            "#1162F#11P首先还是在学院内\x01",
            "探索一番吧。\x02\x03",

            "一共有主楼、社团大楼、女生宿舍、\x01",
            "男生宿舍和礼堂共五栋建筑物。\x02\x03",

            "而且在后面还有\x01",
            "旧校舍的废址。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x109,
        (
            "#1065F#6P明白。\x02\x03",

            "#1063F看来这里和王都一样，\x01",
            "也有甲胄兵到处徘徊。\x01",
            "大家小心行事吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x105,
        "#1162F#11P是……！\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1A40")

    ChrTalk(    #16
        0x101,
        "#1002F#6PＯＫ！\x02",
    )

    CloseMessageWindow()
    Jump("loc_1A69")

    label("loc_1A40")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1A69")

    ChrTalk(    #17
        0x10B,
        "#212F#6PＯＫ！\x02",
    )

    CloseMessageWindow()

    label("loc_1A69")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1A93")

    ChrTalk(    #18
        0x106,
        "#057F#6P哦！\x02",
    )

    CloseMessageWindow()
    Jump("loc_1ABA")

    label("loc_1A93")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1ABA")

    ChrTalk(    #19
        0x108,
        "#072F#6P哦！\x02",
    )

    CloseMessageWindow()

    label("loc_1ABA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1AEC")

    ChrTalk(    #20
        0x10E,
        "#178F#6P明白了……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_1B1B")

    label("loc_1AEC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xB)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B1B")

    ChrTalk(    #21
        0x10C,
        "#112F#6P明白了……！\x02",
    )

    CloseMessageWindow()

    label("loc_1B1B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B4A")

    ChrTalk(    #22
        0x10D,
        "#270F#6P知道了……！\x02",
    )

    CloseMessageWindow()

    label("loc_1B4A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B7E")

    ChrTalk(    #23
        0x107,
        "#065F#6P我、我知道了！\x02",
    )

    CloseMessageWindow()
    Jump("loc_1BAB")

    label("loc_1B7E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1BAB")

    ChrTalk(    #24
        0x10A,
        "#812F#6P我知道了！\x02",
    )

    CloseMessageWindow()

    label("loc_1BAB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1BDC")

    ChrTalk(    #25
        0x10F,
        "#1443F#6P了解……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_1C3D")

    label("loc_1BDC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1C0D")

    ChrTalk(    #26
        0x102,
        "#1502F#6P了解……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_1C3D")

    label("loc_1C0D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1C3D")

    ChrTalk(    #27
        0x103,
        "#1522F#6P了解了……！\x02",
    )

    CloseMessageWindow()

    label("loc_1C3D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1C76")

    ChrTalk(    #28
        0x104,
        (
            "#1545F#6P啊啊……\x01",
            "那我们走吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C76")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1CAE")

    ChrTalk(    #29
        0x110,
        (
            "#263F#6P嘻嘻……\x01",
            "真是期待呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1CAE")

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

    # Function_11_F73 end

    def Function_12_1CDD(): pass

    label("Function_12_1CDD")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1D6D")
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
    Jump("Function_12_1CDD")

    label("loc_1D6D")

    Return()

    # Function_12_1CDD end

    def Function_13_1D6E(): pass

    label("Function_13_1D6E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1DFE")
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
    Jump("Function_13_1D6E")

    label("loc_1DFE")

    Return()

    # Function_13_1D6E end

    def Function_14_1DFF(): pass

    label("Function_14_1DFF")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1E95")
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
    Jump("Function_14_1DFF")

    label("loc_1E95")

    Return()

    # Function_14_1DFF end

    def Function_15_1E96(): pass

    label("Function_15_1E96")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B2, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F65")
    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(500)
    OP_22(0x161, 0x0, 0x64)
    Fade(1000)
    PlayEffect(0x80, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x81, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x83, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_0D()
    OP_AA(5120)
    Sleep(500)
    Jump("loc_1F68")

    label("loc_1F65")

    TalkBegin(0xFF)

    label("loc_1F68")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #30
        "\x07\x05请选择\x18\x02",
    )

    Jump("loc_1F92")

    label("loc_1F92")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1FA5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_20FD")

    Menu(
        1,
        -1,
        150,
        1,
        (
            "回复ＨＰ·ＥＰ\x01",      # 0
            "获得武具\x01",            # 1
            "合成结晶回路\x01",        # 2
            "结束\x01",                # 3
        )
    )

    Jump("loc_1FF7")

    label("loc_1FF7")

    MenuEnd(0x0)
    OP_5F(0x1)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2014"),
        (1, "loc_208F"),
        (2, "loc_20BE"),
        (SWITCH_DEFAULT, "loc_20ED"),
    )


    label("loc_2014")

    FadeToBright(300, 0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
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
    Jump("loc_20FA")

    label("loc_208F")

    OP_A9(0x26)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #31
        "\x07\x05请选择\x18\x02",
    )

    Jump("loc_20BB")

    label("loc_20BB")

    Jump("loc_20FA")

    label("loc_20BE")

    OP_A9(0x9)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #32
        "\x07\x05请选择\x18\x02",
    )

    Jump("loc_20EA")

    label("loc_20EA")

    Jump("loc_20FA")

    label("loc_20ED")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_20FA")

    label("loc_20FA")

    Jump("loc_1FA5")

    label("loc_20FD")

    OP_5F(0x1)
    OP_56(0x0)
    FadeToBright(300, 0)
    Sleep(300)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B2, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_212A")
    OP_A2(0x2597)
    EventEnd(0x1)
    Jump("loc_212D")

    label("loc_212A")

    TalkEnd(0xFF)

    label("loc_212D")

    Return()

    # Function_15_1E96 end

    def Function_16_212E(): pass

    label("Function_16_212E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x560, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x560, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_213F")
    Call(0, 11)
    Return()

    label("loc_213F")

    OP_DE(0x0, 0x1E, 0x1)
    EventBegin(0x2)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
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

    # Function_16_212E end

    def Function_17_22C5(): pass

    label("Function_17_22C5")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
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

    # Function_17_22C5 end

    def Function_18_2429(): pass

    label("Function_18_2429")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2452")
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_2446():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_2446)

    label("loc_2452")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_247B")
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_246F():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_246F)

    label("loc_247B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_24A4")
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_2498():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_2498)

    label("loc_24A4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_24CD")
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_24C1():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_24C1)

    label("loc_24CD")

    Sleep(800)
    OP_44(0x0, 0x1)
    OP_44(0x1, 0x1)
    OP_44(0x2, 0x1)
    OP_44(0x3, 0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_24F9")
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_24F9")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2510")
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_2510")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2527")
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_2527")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_253E")
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_253E")

    Return()

    # Function_18_2429 end

    def Function_19_253F(): pass

    label("Function_19_253F")


    def lambda_2545():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_2545)

    def lambda_2557():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_2557)

    def lambda_2569():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_2569)

    def lambda_257B():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_257B)
    Sleep(1000)
    Return()

    # Function_19_253F end

    def Function_20_258D(): pass

    label("Function_20_258D")

    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #33
        "\x07\x05门上了锁。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_20_258D end

    SaveToFile()

Try(main)
