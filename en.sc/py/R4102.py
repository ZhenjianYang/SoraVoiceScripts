from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'R4102   ._SN',
        MapName             = 'Grancel',
        Location            = 'R4102.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60029",
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
        'Butler Phillip',                       # 9
        'Royal Guardsman',                      # 10
        'Royal Guardsman',                      # 11
        '紅い飛行艇影',                         # 12
        '紅い飛行艇影',                         # 13
        '紅い飛行艇影',                         # 14
        'Erbe Scenic Route',                    # 15
        'Grancel',                              # 16
        'Gurune Gate',                          # 17
        'Flame Velgr',                          # 18
        '丘陵ビー',                             # 19
        '沼チュパカブラ',                       # 20
        'ビー',                                 # 21
        'プリメーラ',                           # 22
        'チュパカブラ',                         # 23
        '丘陵ビー',                             # 24
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
        'ED6_DT09/CH10780 ._CH',             # 00
        'ED6_DT09/CH10781 ._CH',             # 01
        'ED6_DT09/CH10790 ._CH',             # 02
        'ED6_DT09/CH10791 ._CH',             # 03
        'ED6_DT09/CH10050 ._CH',             # 04
        'ED6_DT09/CH10051 ._CH',             # 05
        'ED6_DT09/CH10800 ._CH',             # 06
        'ED6_DT09/CH10801 ._CH',             # 07
        'ED6_DT09/CH10810 ._CH',             # 08
        'ED6_DT09/CH10811 ._CH',             # 09
        'ED6_DT09/CH10820 ._CH',             # 0A
        'ED6_DT09/CH10821 ._CH',             # 0B
        'ED6_DT09/CH11220 ._CH',             # 0C
        'ED6_DT09/CH11221 ._CH',             # 0D
        'ED6_DT09/CH11230 ._CH',             # 0E
        'ED6_DT09/CH11231 ._CH',             # 0F
        'ED6_DT07/CH02470 ._CH',             # 10
        'ED6_DT07/CH01600 ._CH',             # 11
        'ED6_DT07/CH01640 ._CH',             # 12
        'ED6_DT09/CH10730 ._CH',             # 13
        'ED6_DT09/CH10731 ._CH',             # 14
    )

    AddCharChipPat(
        'ED6_DT09/CH10780P._CP',             # 00
        'ED6_DT09/CH10781P._CP',             # 01
        'ED6_DT09/CH10790P._CP',             # 02
        'ED6_DT09/CH10791P._CP',             # 03
        'ED6_DT09/CH10050P._CP',             # 04
        'ED6_DT09/CH10051P._CP',             # 05
        'ED6_DT09/CH10800P._CP',             # 06
        'ED6_DT09/CH10801P._CP',             # 07
        'ED6_DT09/CH10810P._CP',             # 08
        'ED6_DT09/CH10811P._CP',             # 09
        'ED6_DT09/CH10820P._CP',             # 0A
        'ED6_DT09/CH10821P._CP',             # 0B
        'ED6_DT09/CH11220P._CP',             # 0C
        'ED6_DT09/CH11221P._CP',             # 0D
        'ED6_DT09/CH11230P._CP',             # 0E
        'ED6_DT09/CH11231P._CP',             # 0F
        'ED6_DT07/CH02470P._CP',             # 10
        'ED6_DT07/CH01600P._CP',             # 11
        'ED6_DT07/CH01640P._CP',             # 12
        'ED6_DT09/CH10730P._CP',             # 13
        'ED6_DT09/CH10731P._CP',             # 14
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
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
        X                   = 152050,
        Z                   = -2000,
        Y                   = -76100,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 18,
        ChipIndex           = 0x12,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 149980,
        Z                   = -2000,
        Y                   = -76100,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 18,
        ChipIndex           = 0x12,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
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
        Direction           = 0,
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
        Direction           = 0,
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
        X                   = 150880,
        Z                   = -2000,
        Y                   = -89600,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0xFF,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 2420,
        Z                   = 0,
        Y                   = 4600,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0xFF,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 177300,
        Z                   = 0,
        Y                   = 3160,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0xFF,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 149700,
        Z                   = -2000,
        Y                   = -62310,
        Direction           = 348,
        Unknown2            = 19,
        Unknown3            = 1245184,
        ChipIndex           = 0x0,
        NpcIndex            = 0x185,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclMonster(
        X                   = 47300,
        Z                   = 10,
        Y                   = -1820,
        Unknown_0C          = 0,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x295,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 50160,
        Z                   = 100,
        Y                   = -13420,
        Unknown_0C          = 0,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x297,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 114570,
        Z                   = -60,
        Y                   = -5920,
        Unknown_0C          = 0,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x295,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 140620,
        Z                   = -20,
        Y                   = 4510,
        Unknown_0C          = 0,
        Unknown_0E          = 14,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x29C,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 97120,
        Z                   = 10,
        Y                   = -44670,
        Unknown_0C          = 0,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x297,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 145000,
        Z                   = -2040,
        Y                   = -47610,
        Unknown_0C          = 0,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x295,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclEvent(
        X                   = 125500,
        Y                   = -2000,
        Z                   = -60800,
        Range               = 130100,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0xFFFF5038,
        Unknown_18          = 0x0,
        Unknown_1C          = 5,
    )

    DeclEvent(
        X                   = 92840,
        Y                   = -500,
        Z                   = -32910,
        Range               = 79430,
        Unknown_10          = 0x5DC,
        Unknown_14          = 0xFFFF8788,
        Unknown_18          = 0x0,
        Unknown_1C          = 13,
    )

    DeclEvent(
        X                   = 85840,
        Y                   = -1000,
        Z                   = -25620,
        Range               = 90190,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0xFFFFE516,
        Unknown_18          = 0x0,
        Unknown_1C          = 6,
    )

    DeclEvent(
        X                   = 167920,
        Y                   = -300,
        Z                   = 13000,
        Range               = 166500,
        Unknown_10          = 0x7D9,
        Unknown_14          = 0xFFFFECB4,
        Unknown_18          = 0x0,
        Unknown_1C          = 14,
    )

    DeclEvent(
        X                   = 156480,
        Y                   = -2100,
        Z                   = -79210,
        Range               = 145460,
        Unknown_10          = 0xFFFFFC18,
        Unknown_14          = 0xFFFECF64,
        Unknown_18          = 0x0,
        Unknown_1C          = 15,
    )

    DeclEvent(
        X                   = 149700,
        Y                   = -3000,
        Z                   = -62310,
        Range               = 3000,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 16,
    )


    DeclActor(
        TriggerX            = 84450,
        TriggerZ            = 0,
        TriggerY            = -13640,
        TriggerRange        = 1500,
        ActorX              = 84450,
        ActorZ              = 1700,
        ActorY              = -13640,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 17,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 87930,
        TriggerZ            = 0,
        TriggerY            = -13180,
        TriggerRange        = 1500,
        ActorX              = 87930,
        ActorZ              = 1700,
        ActorY              = -13180,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 18,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 88070,
        TriggerZ            = 0,
        TriggerY            = -25440,
        TriggerRange        = 1500,
        ActorX              = 88070,
        ActorZ              = 1700,
        ActorY              = -25440,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 19,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_466",          # 00, 0
        "Function_1_499",          # 01, 1
        "Function_2_54B",          # 02, 2
        "Function_3_619",          # 03, 3
        "Function_4_6DE",          # 04, 4
        "Function_5_7EE",          # 05, 5
        "Function_6_177D",         # 06, 6
        "Function_7_1E17",         # 07, 7
        "Function_8_1EA4",         # 08, 8
        "Function_9_2207",         # 09, 9
        "Function_10_229B",        # 0A, 10
        "Function_11_2333",        # 0B, 11
        "Function_12_23B4",        # 0C, 12
        "Function_13_240D",        # 0D, 13
        "Function_14_247B",        # 0E, 14
        "Function_15_28E7",        # 0F, 15
        "Function_16_2DE1",        # 10, 16
        "Function_17_2FB0",        # 11, 17
        "Function_18_2FFC",        # 12, 18
        "Function_19_305F",        # 13, 19
    )


    def Function_0_466(): pass

    label("Function_0_466")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_47C")
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)

    label("loc_47C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_498")
    OP_A3(0x10F0)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 8)

    label("loc_498")

    Return()

    # Function_0_466 end

    def Function_1_499(): pass

    label("Function_1_499")

    OP_16(0x2, 0xFA0, 0xFFFF6B90, 0xFFFDA288, 0x23003D)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4D5")
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x17, 0x80)

    label("loc_4D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x407, 0)), scpexpr(EXPR_END)), "loc_4EA")
    SetMapFlags(0x2000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_502")
    OP_B1("R4102_y")
    Jump("loc_51A")

    label("loc_502")

    OP_B1("R4102_n")
    OP_71(0x3, 0x4)
    OP_71(0x4, 0x4)
    OP_71(0x5, 0x4)

    label("loc_51A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_538")
    SetChrFlags(0x11, 0x80)
    OP_B2(0x0, 0x5, 0x80)
    Jump("loc_54A")

    label("loc_538")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2DF, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_54A")
    ClearChrFlags(0x11, 0x80)
    OP_B2(0x1, 0x5, 0x80)

    label("loc_54A")

    Return()

    # Function_1_499 end

    def Function_2_54B(): pass

    label("Function_2_54B")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_570")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_603")

    label("loc_570")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_589")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_603")

    label("loc_589")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5A2")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_603")

    label("loc_5A2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5BB")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_603")

    label("loc_5BB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5D4")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_603")

    label("loc_5D4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5ED")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_603")

    label("loc_5ED")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_603")
    OP_99(0xFE, 0x6, 0x7, 0x546)

    label("loc_603")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_618")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_603")

    label("loc_618")

    Return()

    # Function_2_54B end

    def Function_3_619(): pass

    label("Function_3_619")

    TalkBegin(0x9)

    ChrTalk(    #0
        0xFE,
        (
            "Access to the Erbe Scenic Route\x01",
            "is currently off limits by order of\x01",
            "the Royal Army.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "I'm sorry, but whoever you are,\x01",
            "I'm going to have to ask you\x01",
            "to refrain from going any farther.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x9)
    Return()

    # Function_3_619 end

    def Function_4_6DE(): pass

    label("Function_4_6DE")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_73F")

    ChrTalk(    #2
        0xFE,
        "This area isn't safe.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        (
            "I recommend you return to town\x01",
            "as soon as possible.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7EA")

    label("loc_73F")


    ChrTalk(    #4
        0xFE,
        (
            "Sorry, but it's an emergency.\x01",
            "No one's allowed to go past\x01",
            "this point.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        "Besides, this area isn't safe.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xFE,
        (
            "I recommend you return to town\x01",
            "as soon as possible.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_7EA")

    TalkEnd(0xA)
    Return()

    # Function_4_6DE end

    def Function_5_7EE(): pass

    label("Function_5_7EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C2, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 0)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_7FB")
    Return()

    label("loc_7FB")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_81F")
    Call(0, 10)
    Call(0, 11)
    AddParty(0x2E, 0xFF, 0xFF)
    FadeToBright(0, 0)

    label("loc_81F")

    SetChrPos(0x8, 111020, 0, -52590, 90)

    NpcTalk(    #7
        0x8,
        "Man's Voice",
        "Ah, yes, you are...\x02",
    )

    CloseMessageWindow()
    OP_62(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    Fade(1000)
    OP_6D(127830, -2000, -52550, 0)
    OP_67(0, 9160, -10000, 0)
    OP_6B(2830, 0)
    OP_6C(224000, 0)
    OP_6E(262, 0)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 120520, 0, -52830, 90)
    SetChrPos(0x101, 128410, -2000, -51900, 270)
    SetChrPos(0x12F, 131050, -2000, -52330, 270)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_981")
    SetChrPos(0x105, 128500, -2000, -53020, 270)
    SetChrPos(0xF7, 129840, -2000, -51660, 270)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_93D")
    SetChrPos(0x104, 129840, -2000, -53020, 270)
    Jump("loc_97E")

    label("loc_93D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_95F")
    SetChrPos(0x107, 129840, -2000, -53020, 270)
    Jump("loc_97E")

    label("loc_95F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_97E")
    SetChrPos(0x108, 129840, -2000, -53020, 270)

    label("loc_97E")

    Jump("loc_9B4")

    label("loc_981")

    SetChrPos(0xF7, 128500, -2000, -53020, 270)
    SetChrPos(0xF8, 129840, -2000, -51660, 270)
    SetChrPos(0xF9, 130000, -2000, -52830, 270)

    label("loc_9B4")

    OP_8E(0x8, 0x1EF8C, 0xFFFFF830, 0xFFFF329C, 0x7D0, 0x0)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E04")

    ChrTalk(    #8
        0x101,
        "#1004F#6PHuh...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x105,
        (
            "#044F#6POh, my. Phillip!\x02\x03",

            "#040FHow have you been?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x8,
        (
            "#720FYour concern does me too much credit,\x01",
            "Your Highness. I hope you and Miss Estelle\x01",
            "are well.\x02\x03",

            "Have you been to the villa recently?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x101,
        "#1006F#6PWe have, actually.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x105,
        (
            "#542F#6PYou were, um...'busy' in the capital,\x01",
            "I take it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x8,
        (
            "#720FYes, I was making some purchases on\x01",
            "the orders of His Highness the Duke.\x02\x03",

            "#721F...Did you, perchance, encounter His\x01",
            "Highness while you were at the villa?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x101,
        "#1016F#6PWe 'encountered' him, all right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x105,
        (
            "#045F#6PWe wanted to be nice and say hello.\x01",
            "It's been some time since the, um,\x01",
            "unpleasantness.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x8,
        (
            "#722FFrom your expressions, I take it he\x01",
            "said something thoughtless to you\x01",
            "once again.\x02\x03",

            "As his retainer, you have my utmost\x01",
            "apologies.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x105,
        (
            "#047F#6POh, you don't need to apologize for\x01",
            "him, Phillip.\x02\x03",

            "#040FI have to admit, I was a little worried\x01",
            "when I'd heard he was placed under\x01",
            "house arrest.\x02\x03",

            "He's seems to be taking it well,\x01",
            "however.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x8,
        (
            "#720FIt is kind of you to say so.\x02\x03",

            "Now, I fear I must be off. If you'll\x01",
            "pardon me, Your Highness.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_113C")

    label("loc_E04")


    ChrTalk(    #19
        0x101,
        "#1004F#6PHuh...? Oh, hey. It's Phillip!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x8,
        (
            "#720FMiss Estelle. It has been some time\x01",
            "since we last met.\x02\x03",

            "Have you been to the villa recently?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x101,
        (
            "#1006F#6PWe have, actually.\x02\x03",

            "I guess you had to go to Grancel for\x01",
            "some reason?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x8,
        (
            "#720FYes, I was making some purchases on\x01",
            "the orders of His Highness the Duke.\x02\x03",

            "#721F...Did you, perchance, encounter His\x01",
            "Highness while you were at the villa?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x101,
        "#1025F#6PWe 'encountered' him, all right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x8,
        (
            "#722FFrom your expression, I take it he\x01",
            "said something thoughtless to you\x01",
            "once again.\x02\x03",

            "As his retainer, you have my utmost\x01",
            "apologies.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x101,
        (
            "#1016F#6PAh, no, he wasn't really rude to ME, \x01",
            "specifically.\x02\x03",

            "#1006FYou don't need to apologize.\x01",
            "I wasn't bothered one bit, I swear.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x8,
        (
            "#720FYour kindness does you credit,\x01",
            "Miss Estelle.\x02\x03",

            "Now, I fear I must be off. If you'll\x01",
            "pardon me.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_113C")


    def lambda_1142():
        OP_8E(0xFE, 0x1F39C, 0xFFFFF830, 0xFFFF2C66, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1142)

    def lambda_115D():

        label("loc_115D")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_115D")

    QueueWorkItem2(0x101, 1, lambda_115D)

    def lambda_116E():

        label("loc_116E")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_116E")

    QueueWorkItem2(0x12F, 1, lambda_116E)

    def lambda_117F():

        label("loc_117F")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_117F")

    QueueWorkItem2(0xF7, 1, lambda_117F)

    def lambda_1190():

        label("loc_1190")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_1190")

    QueueWorkItem2(0xF8, 1, lambda_1190)

    def lambda_11A1():

        label("loc_11A1")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_11A1")

    QueueWorkItem2(0xF9, 1, lambda_11A1)
    WaitChrThread(0x8, 0x1)

    def lambda_11B7():
        OP_8E(0xFE, 0x22AB0, 0xFFFFF830, 0xFFFF2A90, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_11B7)

    def lambda_11D2():
        OP_6D(131000, -2000, -54400, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_11D2)

    def lambda_11EA():
        OP_67(0, 8920, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_11EA)
    WaitChrThread(0x8, 0x1)
    SetChrFlags(0x8, 0x80)

    def lambda_120C():
        OP_6D(129240, -2000, -52490, 1600)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_120C)

    def lambda_1224():
        OP_67(0, 8920, -10000, 1600)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_1224)
    WaitChrThread(0x101, 0x2)
    WaitChrThread(0x101, 0x3)
    OP_44(0x101, 0x1)
    OP_44(0x12F, 0x1)
    OP_44(0xF7, 0x1)
    OP_44(0xF8, 0x1)
    OP_44(0xF9, 0x1)

    ChrTalk(    #27
        0x101,
        (
            "#1007F#4P*sigh* Guess Phillip's job is even\x01",
            "harder now.\x02\x03",

            "#1015FHe's been taking care of Dunan\x01",
            "since Dunan was young, right?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_13E8")
    OP_8C(0x105, 360, 400)

    ChrTalk(    #28
        0x105,
        (
            "#040F#6PHe's been Dunan's retainer for\x01",
            "the past twenty years, from what\x01",
            "Grandmother tells me.\x02\x03",

            "I believe he was a member of the\x01",
            "Royal Guard before then.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 180, 400)

    ChrTalk(    #29
        0x101,
        (
            "#1004F#4PWait, really? Phillip?!\x02\x03",

            "#1006FWow, guess you really can't\x01",
            "judge by looks.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13E8")


    ChrTalk(    #30
        0x12F,
        (
            "#264F#5P...Huh.\x02\x03",

            "#263FYou really shouldn't underestimate\x01",
            "him. Even I can tell he's not just any\x01",
            "old guy.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_145C():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_145C)
    Sleep(50)

    def lambda_146F():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_146F)
    Sleep(50)

    def lambda_1482():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_1482)
    Sleep(50)

    def lambda_1495():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_1495)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_14E1")

    ChrTalk(    #31
        0x101,
        "#1004FHuh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x107,
        "#064FWhat do you mean, Renne?\x02",
    )

    CloseMessageWindow()
    Jump("loc_150B")

    label("loc_14E1")


    ChrTalk(    #33
        0x101,
        (
            "#1004FHuh?\x02\x03",

            "What do you mean, Renne?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_150B")

    TurnDirection(0x12F, 0x101, 400)

    ChrTalk(    #34
        0x12F,
        (
            "#260F#5POh, um, you know! Like how he\x01",
            "can walk with his eyes closed.\x02\x03",

            "I sure couldn't do that!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0xF7, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15CB")
    OP_62(0xF8, 0x0, 2300, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_1609")

    label("loc_15CB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15F2")
    OP_62(0xF8, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_1609")

    label("loc_15F2")

    OP_62(0xF8, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)

    label("loc_1609")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1630")
    OP_62(0xF9, 0x0, 2300, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_166E")

    label("loc_1630")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1657")
    OP_62(0xF9, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_166E")

    label("loc_1657")

    OP_62(0xF9, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)

    label("loc_166E")

    Sleep(1500)

    ChrTalk(    #35
        0x101,
        (
            "#1016FI think they're just narrowed, Renne,\x01",
            "not closed...\x02\x03",

            "#1006FI mean, you noticed how he opens\x01",
            "his eyes when surprised, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x12F,
        (
            "#264F#5PReally? I didn't!\x02\x03",

            "#261FI wanna see, I wanna see!\x01",
            "Maybe I can get a good look if\x01",
            "I surprise him next time!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    OP_A2(0x1618)
    EventEnd(0x0)
    Return()

    # Function_5_7EE end

    def Function_6_177D(): pass

    label("Function_6_177D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x407, 0)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1794")
    Return()

    label("loc_1794")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_17B4")
    Call(0, 10)
    Call(0, 12)
    FadeToBright(0, 0)

    label("loc_17B4")

    OP_20(0x7D0)
    Fade(1000)
    SetChrPos(0x101, 87670, 0, -18210, 270)
    SetChrPos(0x102, 87650, 0, -19540, 270)
    SetChrPos(0xF8, 89210, 0, -18030, 270)
    SetChrPos(0xF9, 89310, 0, -19440, 270)
    OP_6D(89370, 0, -19860, 0)
    OP_67(0, 7200, -10000, 0)
    OP_6B(1770, 0)
    OP_6C(134000, 0)
    OP_6E(431, 0)
    OP_0D()
    OP_43(0x101, 0x3, 0x0, 0x7)
    Sleep(1000)
    OP_62(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(100)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1897")
    OP_62(0xF8, 0x0, 2300, 0x26, 0x26, 0xFA, 0x1)
    Jump("loc_18CB")

    label("loc_1897")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_18B9")
    OP_62(0xF8, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Jump("loc_18CB")

    label("loc_18B9")

    OP_62(0xF8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    label("loc_18CB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_18ED")
    OP_62(0xF9, 0x0, 2300, 0x26, 0x26, 0xFA, 0x1)
    Jump("loc_1921")

    label("loc_18ED")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_190F")
    OP_62(0xF9, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Jump("loc_1921")

    label("loc_190F")

    OP_62(0xF9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    label("loc_1921")

    Sleep(1000)

    ChrTalk(    #37
        0x101,
        "#1004F#5PHey, isn't that...?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_199A")

    ChrTalk(    #38
        0x106,
        (
            "#052F#6PWhat the...? That's the sound\x01",
            "of an airship engine!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A2C")

    label("loc_199A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_19E8")

    ChrTalk(    #39
        0x103,
        (
            "#023F#6PWhat...? That's the sound\x01",
            "of an airship engine!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A2C")

    label("loc_19E8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1A2C")

    ChrTalk(    #40
        0x108,
        (
            "#073F#6PThat's...the sound of\x01",
            "an airship engine.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A2C")

    OP_62(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(50)
    OP_62(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A7C")
    OP_62(0xF8, 0x0, 2300, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_1AB0")

    label("loc_1A7C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A9E")
    OP_62(0xF8, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_1AB0")

    label("loc_1A9E")

    OP_62(0xF8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)

    label("loc_1AB0")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1AD7")
    OP_62(0xF9, 0x0, 2300, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_1B0B")

    label("loc_1AD7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1AF9")
    OP_62(0xF9, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_1B0B")

    label("loc_1AF9")

    OP_62(0xF9, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)

    label("loc_1B0B")

    Sleep(1500)
    OP_63(0x101)
    OP_63(0x102)
    OP_63(0xF8)
    OP_63(0xF9)
    Sleep(200)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B80")
    OP_62(0xF8, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1BBE")

    label("loc_1B80")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1BA7")
    OP_62(0xF8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1BBE")

    label("loc_1BA7")

    OP_62(0xF8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_1BBE")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1BEA")
    OP_62(0xF9, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1C28")

    label("loc_1BEA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1C11")
    OP_62(0xF9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1C28")

    label("loc_1C11")

    OP_62(0xF9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_1C28")

    Sleep(1000)

    ChrTalk(    #41
        0x101,
        "#1020F#5PW-Wait a second!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1C92")

    ChrTalk(    #42
        0x107,
        "#065F#6PIf it's an airship that can fly NOW...!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1D26")

    label("loc_1C92")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1CDB")

    ChrTalk(    #43
        0x108,
        (
            "#076F#6PThe only airships that\x01",
            "can fly now are...!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D26")

    label("loc_1CDB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1D26")

    ChrTalk(    #44
        0x103,
        (
            "#024F#6POh, no! An airship that\x01",
            "can fly NOW would be...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D26")

    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x102, 135, 500)

    ChrTalk(    #45
        0x102,
        "#1046F#6PThere!\x02",
    )

    CloseMessageWindow()

    def lambda_1D64():
        OP_6D(97800, 0, -23000, 2500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1D64)

    def lambda_1D7C():
        OP_67(0, 12960, -10000, 2500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1D7C)

    def lambda_1D94():
        OP_6B(2160, 2500)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_1D94)

    def lambda_1DA4():
        OP_6C(111000, 2500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1DA4)

    def lambda_1DB4():
        OP_6E(460, 2500)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_1DB4)

    def lambda_1DC4():
        OP_8C(0xFE, 135, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1DC4)
    Sleep(50)

    def lambda_1DD7():
        OP_8C(0xFE, 135, 500)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_1DD7)
    Sleep(50)

    def lambda_1DEA():
        OP_8C(0xFE, 135, 500)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_1DEA)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMapFlags(0x100000)
    OP_A2(0x10FF)
    OP_A2(0x10F9)
    NewScene("ED6_DT21/E0810   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_6_177D end

    def Function_7_1E17(): pass

    label("Function_7_1E17")

    OP_22(0x79, 0x1, 0x32)
    Sleep(200)
    OP_24(0x79, 0x35)
    Sleep(200)
    OP_24(0x79, 0x38)
    Sleep(200)
    OP_24(0x79, 0x3C)
    Sleep(200)
    OP_24(0x79, 0x3F)
    Sleep(200)
    OP_24(0x79, 0x42)
    Sleep(200)
    OP_24(0x79, 0x46)
    Sleep(200)
    OP_24(0x79, 0x49)
    Sleep(200)
    OP_24(0x79, 0x4C)
    Sleep(200)
    OP_24(0x79, 0x50)
    Sleep(200)
    OP_24(0x79, 0x53)
    Sleep(200)
    OP_24(0x79, 0x56)
    Sleep(200)
    OP_24(0x79, 0x5A)
    Sleep(200)
    OP_24(0x79, 0x5D)
    Sleep(200)
    OP_24(0x79, 0x60)
    Sleep(200)
    OP_24(0x79, 0x64)
    Return()

    # Function_7_1E17 end

    def Function_8_1EA4(): pass

    label("Function_8_1EA4")

    EventBegin(0x0)
    ClearMapFlags(0x100000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1EC9")
    Call(0, 10)
    Call(0, 12)
    FadeToBright(0, 0)

    label("loc_1EC9")

    OP_22(0x79, 0x1, 0x64)
    SetChrPos(0x101, 88010, 0, -18190, 135)
    SetChrPos(0x102, 87420, 0, -19640, 135)
    SetChrPos(0xF8, 89730, 0, -18750, 135)
    SetChrPos(0xF9, 89300, 0, -20100, 135)
    OP_6D(88080, 0, -19230, 0)
    OP_67(0, 8890, -10000, 0)
    OP_6B(2810, 0)
    OP_6C(260000, 0)
    OP_6E(262, 0)
    OP_72(0x0, 0x4)
    OP_72(0x1, 0x4)
    OP_72(0x2, 0x4)
    OP_A1(0xB, 0x0)
    OP_A1(0xC, 0x1)
    OP_A1(0xD, 0x2)
    SetChrPos(0xB, 104090, 2000, -30210, 315)
    SetChrPos(0xC, 109090, 2000, -25210, 315)
    SetChrPos(0xD, 99090, 2000, -35210, 315)
    TurnDirection(0x101, 0xB, 0)
    TurnDirection(0x102, 0xB, 0)
    TurnDirection(0xF8, 0xB, 0)
    TurnDirection(0xF9, 0xB, 0)
    FadeToBright(1000, 0)
    OP_0D()

    def lambda_1FCC():

        label("loc_1FCC")

        TurnDirection(0xFE, 0xB, 400)
        OP_48()
        Jump("loc_1FCC")

    QueueWorkItem2(0x101, 3, lambda_1FCC)

    def lambda_1FDD():

        label("loc_1FDD")

        TurnDirection(0xFE, 0xB, 400)
        OP_48()
        Jump("loc_1FDD")

    QueueWorkItem2(0x102, 3, lambda_1FDD)

    def lambda_1FEE():

        label("loc_1FEE")

        TurnDirection(0xFE, 0xB, 400)
        OP_48()
        Jump("loc_1FEE")

    QueueWorkItem2(0xF8, 3, lambda_1FEE)

    def lambda_1FFF():

        label("loc_1FFF")

        TurnDirection(0xFE, 0xB, 400)
        OP_48()
        Jump("loc_1FFF")

    QueueWorkItem2(0xF9, 3, lambda_1FFF)

    def lambda_2010():
        OP_90(0xFE, 0xFFFF8AD0, 0x0, 0x7530, 0x7530, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_2010)
    Sleep(1000)

    def lambda_2030():
        OP_90(0xFE, 0xFFFF8AD0, 0x0, 0x7530, 0x7530, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_2030)
    Sleep(1000)

    def lambda_2050():
        OP_90(0xFE, 0xFFFF8AD0, 0x0, 0x7530, 0x7530, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_2050)
    WaitChrThread(0xD, 0x1)
    OP_43(0x102, 0x2, 0x0, 0x9)
    OP_71(0x0, 0x4)
    OP_71(0x1, 0x4)
    OP_71(0x2, 0x4)
    OP_44(0x101, 0x3)
    OP_44(0x102, 0x3)
    OP_44(0xF8, 0x3)
    OP_44(0xF9, 0x3)

    ChrTalk(    #46
        0x101,
        (
            "#1020F#6PSociety airships!\x01",
            "Why are THEY here?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x102,
        (
            "#1046F#6PDamn. They're heading straight\x01",
            "for the capital!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2149")

    ChrTalk(    #48
        0x106,
        (
            "#057FSon of a bitch!\x01",
            "We need to chase them! NOW!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21BA")

    label("loc_2149")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_218B")

    ChrTalk(    #49
        0x103,
        (
            "#022FGoddess help us...\x01",
            "We MUST give chase!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21BA")

    label("loc_218B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_21BA")

    ChrTalk(    #50
        0x108,
        "#076FWe have to chase them!\x02",
    )

    CloseMessageWindow()

    label("loc_21BA")

    OP_A2(0x2038)
    OP_28(0x9C, 0x4, 0x2)
    OP_28(0x9C, 0x4, 0x8)
    OP_28(0x9C, 0x1, 0x1)
    OP_28(0xB5, 0x4, 0x40)
    OP_28(0xB6, 0x4, 0x40)
    OP_28(0xB7, 0x4, 0x40)
    OP_28(0xB8, 0x4, 0x40)
    OP_28(0xB9, 0x4, 0x40)
    OP_28(0xBA, 0x4, 0x40)
    OP_28(0xBB, 0x4, 0x40)
    OP_28(0xBC, 0x4, 0x40)
    OP_28(0xBD, 0x4, 0x40)
    OP_28(0xBE, 0x4, 0x40)
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Return()

    # Function_8_1EA4 end

    def Function_9_2207(): pass

    label("Function_9_2207")

    OP_24(0x79, 0x5F)
    Sleep(300)
    OP_24(0x79, 0x5A)
    Sleep(300)
    OP_24(0x79, 0x55)
    Sleep(300)
    OP_24(0x79, 0x50)
    Sleep(300)
    OP_24(0x79, 0x4B)
    Sleep(300)
    OP_24(0x79, 0x46)
    Sleep(300)
    OP_24(0x79, 0x41)
    Sleep(300)
    OP_24(0x79, 0x3C)
    Sleep(300)
    OP_24(0x79, 0x37)
    Sleep(300)
    OP_24(0x79, 0x32)
    Sleep(300)
    OP_24(0x79, 0x2D)
    Sleep(300)
    OP_24(0x79, 0x28)
    Sleep(300)
    OP_24(0x79, 0x23)
    Sleep(300)
    OP_24(0x79, 0x1E)
    Sleep(300)
    OP_24(0x79, 0x19)
    Sleep(300)
    OP_24(0x79, 0x14)
    Sleep(300)
    OP_23(0x79)
    Return()

    # Function_9_2207 end

    def Function_10_229B(): pass

    label("Function_10_229B")

    FadeToDark(0, 0, -1)
    OP_A3(0x1200)
    OP_A3(0x1201)
    RemoveParty(0x2, 0xFF)
    RemoveParty(0x5, 0xFF)
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
        (0, "loc_2314"),
        (1, "loc_231A"),
        (SWITCH_DEFAULT, "loc_2320"),
    )


    label("loc_2314")

    OP_A2(0x1200)
    Jump("loc_2320")

    label("loc_231A")

    OP_A2(0x1201)
    Jump("loc_2320")

    label("loc_2320")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_232E")
    AddParty(0x2, 0xF7, 0xFF)
    Jump("loc_2332")

    label("loc_232E")

    AddParty(0x5, 0xF7, 0xFF)

    label("loc_2332")

    Return()

    # Function_10_229B end

    def Function_11_2333(): pass

    label("Function_11_2333")

    ClearMapFlags(0x1)
    OP_6D(106730, -1920, 53920, 0)
    Sleep(100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_2376")
    FadeToBright(0, 0)
    OP_C9(0x0, 0x4, 0x0, 0x2, 0xFF, 0xFF, 0x3, 0x4, 0x6, 0x7, 0xFFFF)
    Jump("loc_2394")

    label("loc_2376")

    FadeToBright(0, 0)
    OP_C9(0x0, 0x4, 0x0, 0x5, 0xFF, 0xFF, 0x3, 0x4, 0x6, 0x7, 0xFFFF)

    label("loc_2394")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Sleep(1000)
    Return()

    # Function_11_2333 end

    def Function_12_23B4(): pass

    label("Function_12_23B4")

    ClearMapFlags(0x1)
    OP_6D(106730, -1920, 53920, 0)
    Sleep(100)
    FadeToBright(0, 0)
    OP_C9(0x0, 0x4, 0x0, 0x1, 0xFF, 0xFF, 0x5, 0x2, 0x6, 0x7, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Sleep(1000)
    Return()

    # Function_12_23B4 end

    def Function_13_240D(): pass

    label("Function_13_240D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C6, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C6, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_247A")
    EventBegin(0x1)

    ChrTalk(    #51
        0x101,
        (
            "#1002F(Gurune Gate should be east!\x01",
            "...I've got to hurry!!)\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    Fade(1000)
    SetChrPos(0x101, 84130, 0, -28960, 0)
    OP_0D()
    Sleep(50)
    EventEnd(0x4)

    label("loc_247A")

    Return()

    # Function_13_240D end

    def Function_14_247B(): pass

    label("Function_14_247B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x407, 2)), scpexpr(EXPR_END)), "loc_26D1")
    EventBegin(0x1)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_END)),
        (0, "loc_24A4"),
        (1, "loc_24F6"),
        (2, "loc_2551"),
        (5, "loc_25A6"),
        (7, "loc_25FB"),
        (6, "loc_264E"),
        (SWITCH_DEFAULT, "loc_26AE"),
    )


    label("loc_24A4")


    ChrTalk(    #52
        0x101,
        (
            "#1002FWe don't have time for side trips.\x01",
            "Let's hurry back to the capital!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_26AE")

    label("loc_24F6")


    ChrTalk(    #53
        0x102,
        (
            "#1042FWe don't have time to make side trips.\x01",
            "We need to hurry back to the capital!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_26AE")

    label("loc_2551")


    ChrTalk(    #54
        0x103,
        (
            "#022FWe don't have time for any side trips.\x01",
            "Let's hurry back to the capital!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_26AE")

    label("loc_25A6")


    ChrTalk(    #55
        0x106,
        (
            "#057FWe ain't got time to make side trips.\x01",
            "We gotta get back to the capital!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_26AE")

    label("loc_25FB")


    ChrTalk(    #56
        0x108,
        (
            "#072FWe don't have time for side trips.\x01",
            "We must hurry back to the capital!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_26AE")

    label("loc_264E")


    ChrTalk(    #57
        0x107,
        (
            "#062FI don't think we have time to make side\x01",
            "trips. We gotta hurry back to the capital!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_26AE")

    label("loc_26AE")

    OP_90(0x0, 0xFFFFFA24, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    SetMapFlags(0x2000000)
    Jump("loc_28E6")

    label("loc_26D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x407, 0)), scpexpr(EXPR_END)), "loc_28E6")
    EventBegin(0x1)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_END)),
        (0, "loc_26FA"),
        (1, "loc_273B"),
        (2, "loc_278A"),
        (5, "loc_27CF"),
        (7, "loc_2820"),
        (6, "loc_2877"),
        (SWITCH_DEFAULT, "loc_28C6"),
    )


    label("loc_26FA")


    ChrTalk(    #58
        0x101,
        (
            "#1002FNo, not this way!\x01",
            "Let's hurry back to the capital!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_28C6")

    label("loc_273B")


    ChrTalk(    #59
        0x102,
        (
            "#1042FNo, this is the wrong way!\x01",
            "We have to hurry back to the capital!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_28C6")

    label("loc_278A")


    ChrTalk(    #60
        0x103,
        (
            "#022FThis is the wrong way. Let's hurry\x01",
            "back to the capital!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_28C6")

    label("loc_27CF")


    ChrTalk(    #61
        0x106,
        (
            "#057FNo, this is the wrong way. C'mon,\x01",
            "we gotta get back to the capital!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_28C6")

    label("loc_2820")


    ChrTalk(    #62
        0x108,
        (
            "#072FThis isn't the right way. We must get\x01",
            "to the capital as soon as possible!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_28C6")

    label("loc_2877")


    ChrTalk(    #63
        0x107,
        (
            "#065FI think we're going the wrong\x01",
            "way. We gotta hurry to the capital!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_28C6")

    label("loc_28C6")

    OP_90(0x0, 0xFFFFFA24, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    SetMapFlags(0x2000000)

    label("loc_28E6")

    Return()

    # Function_14_247B end

    def Function_15_28E7(): pass

    label("Function_15_28E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x407, 2)), scpexpr(EXPR_END)), "loc_2B86")
    EventBegin(0x1)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_END)),
        (0, "loc_2910"),
        (1, "loc_2962"),
        (2, "loc_29BD"),
        (5, "loc_2A12"),
        (7, "loc_2A67"),
        (6, "loc_2ABA"),
        (SWITCH_DEFAULT, "loc_2B1E"),
    )


    label("loc_2910")


    ChrTalk(    #64
        0x101,
        (
            "#1002FWe don't have time for side trips.\x01",
            "Let's hurry back to the capital!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B1E")

    label("loc_2962")


    ChrTalk(    #65
        0x102,
        (
            "#1042FWe don't have time to make side trips.\x01",
            "We need to hurry back to the capital!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B1E")

    label("loc_29BD")


    ChrTalk(    #66
        0x103,
        (
            "#022FWe don't have time for any side trips.\x01",
            "Let's hurry back to the capital!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B1E")

    label("loc_2A12")


    ChrTalk(    #67
        0x106,
        (
            "#057FWe ain't got time to make side trips.\x01",
            "We gotta get back to the capital!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B1E")

    label("loc_2A67")


    ChrTalk(    #68
        0x108,
        (
            "#072FWe don't have time for side trips.\x01",
            "We must hurry back to the capital!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B1E")

    label("loc_2ABA")


    ChrTalk(    #69
        0x107,
        (
            "#062FUm, I don't think we have time to make side\x01",
            "trips. We gotta hurry back to the capital!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B1E")

    label("loc_2B1E")

    OP_59()
    Fade(1000)
    SetChrPos(0x0, 151000, -2000, -74190, 0)
    SetChrPos(0x1, 151000, -2000, -74190, 0)
    SetChrPos(0x2, 151000, -2000, -74190, 0)
    SetChrPos(0x3, 151000, -2000, -74190, 0)
    OP_69(0x0, 0x0)
    OP_0D()
    OP_8C(0x0, 0, 0)
    Sleep(50)
    EventEnd(0x4)
    SetMapFlags(0x2000000)
    Jump("loc_2DE0")

    label("loc_2B86")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x407, 0)), scpexpr(EXPR_END)), "loc_2DE0")
    EventBegin(0x1)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_END)),
        (0, "loc_2BAF"),
        (1, "loc_2BF0"),
        (2, "loc_2C3F"),
        (5, "loc_2C84"),
        (7, "loc_2CD5"),
        (6, "loc_2D2C"),
        (SWITCH_DEFAULT, "loc_2D7B"),
    )


    label("loc_2BAF")


    ChrTalk(    #70
        0x101,
        (
            "#1002FNo, not this way!\x01",
            "Let's hurry back to the capital!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D7B")

    label("loc_2BF0")


    ChrTalk(    #71
        0x102,
        (
            "#1042FNo, this is the wrong way!\x01",
            "We have to hurry back to the capital!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D7B")

    label("loc_2C3F")


    ChrTalk(    #72
        0x103,
        (
            "#022FThis is the wrong way. Let's hurry\x01",
            "back to the capital!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D7B")

    label("loc_2C84")


    ChrTalk(    #73
        0x106,
        (
            "#057FNo, this is the wrong way. C'mon,\x01",
            "we gotta get back to the capital!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D7B")

    label("loc_2CD5")


    ChrTalk(    #74
        0x108,
        (
            "#072FThis isn't the right way. We must get\x01",
            "to the capital as soon as possible!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D7B")

    label("loc_2D2C")


    ChrTalk(    #75
        0x107,
        (
            "#065FI think we're going the wrong\x01",
            "way. We gotta hurry to the capital!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D7B")

    label("loc_2D7B")

    OP_59()
    Fade(1000)
    SetChrPos(0x0, 151000, -2000, -74190, 0)
    SetChrPos(0x1, 151000, -2000, -74190, 0)
    SetChrPos(0x2, 151000, -2000, -74190, 0)
    SetChrPos(0x3, 151000, -2000, -74190, 0)
    OP_69(0x0, 0x0)
    OP_0D()
    OP_8C(0x0, 0, 0)
    Sleep(50)
    EventEnd(0x4)
    SetMapFlags(0x2000000)

    label("loc_2DE0")

    Return()

    # Function_15_28E7 end

    def Function_16_2DE1(): pass

    label("Function_16_2DE1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2DF, 3)), scpexpr(EXPR_END)), "loc_2DE9")
    Return()

    label("loc_2DE9")

    EventBegin(0x1)
    OP_51(0x0, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x2, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x3, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x4, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x5, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x6, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x7, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    SetChrSubChip(0x4, 0)
    SetChrSubChip(0x5, 0)
    SetChrSubChip(0x6, 0)
    SetChrSubChip(0x7, 0)
    SetChrName("")

    AnonymousTalk(    #76
        "\x07\x05A large monster is prowling around.\x02",
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        32,
        0,
        (
            "Exterminate\x01",      # 0
            "Leave Alone\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (1, "loc_2EDD"),
        (SWITCH_DEFAULT, "loc_2F00"),
    )


    label("loc_2EDD")

    Fade(500)
    OP_89(0x0, 145940, -2000, -57070, 143)
    OP_69(0x0, 0x0)
    OP_30(0x1)
    OP_0D()
    EventEnd(0x0)
    Return()

    label("loc_2F00")

    Battle(0xEE5, 0x0, 0x0, 0x0, 0xFF)
    EventBegin(0x1)
    OP_89(0x0, 145940, -2000, -57070, 143)
    OP_69(0x0, 0x0)
    OP_30(0x1)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (2, "loc_2F39"),
        (1, "loc_2F3C"),
        (SWITCH_DEFAULT, "loc_2F3F"),
    )


    label("loc_2F39")

    EventEnd(0x0)
    Return()

    label("loc_2F3C")

    OP_B4(0x0)
    Return()

    label("loc_2F3F")

    EventBegin(0x1)
    SetChrFlags(0x11, 0x80)
    OP_B2(0x0, 0x5, 0x80)
    OP_0D()
    Sleep(400)
    OP_22(0x17, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #77
        "\x07\x05Exterminated monster!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_A2(0x16FB)
    OP_28(0xA9, 0x4, 0x10)
    OP_28(0xA9, 0x4, 0x2)
    OP_28(0xA9, 0x1, 0x1)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    EventEnd(0x0)
    Return()

    # Function_16_2DE1 end

    def Function_17_2FB0(): pass

    label("Function_17_2FB0")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #78
        "\x07\x05West: Grancel - 168 selge\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_17_2FB0 end

    def Function_18_2FFC(): pass

    label("Function_18_2FFC")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #79
        "\x07\x05East: City of Rolent - 368 selge     Gurune Gate\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_18_2FFC end

    def Function_19_305F(): pass

    label("Function_19_305F")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #80
        "\x07\x05South: Erbe Royal Villa - 256 selge\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_19_305F end

    SaveToFile()

Try(main)
