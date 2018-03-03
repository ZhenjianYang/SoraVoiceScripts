from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'M7202   ._SN',
        MapName             = 'Gaiden3',
        Location            = 'M7202.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60223",
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
        'Sealing Stone 14',                     # 9
        '',                                     # 10
        '',                                     # 11
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
        'ED6_DT29/CH14470 ._CH',             # 00
        'ED6_DT29/CH14471 ._CH',             # 01
        'ED6_DT29/CH15050 ._CH',             # 02
        'ED6_DT29/CH15051 ._CH',             # 03
        'ED6_DT29/CH15060 ._CH',             # 04
        'ED6_DT29/CH15061 ._CH',             # 05
        'ED6_DT29/CH14480 ._CH',             # 06
        'ED6_DT29/CH14481 ._CH',             # 07
        'ED6_DT29/CH14490 ._CH',             # 08
        'ED6_DT29/CH14491 ._CH',             # 09
        'ED6_DT29/CH14560 ._CH',             # 0A
        'ED6_DT29/CH14561 ._CH',             # 0B
        'ED6_DT29/CH14010 ._CH',             # 0C
        'ED6_DT29/CH14011 ._CH',             # 0D
        'ED6_DT26/CH20669 ._CH',             # 0E
    )

    AddCharChipPat(
        'ED6_DT29/CH14470P._CP',             # 00
        'ED6_DT29/CH14471P._CP',             # 01
        'ED6_DT29/CH15050P._CP',             # 02
        'ED6_DT29/CH15051P._CP',             # 03
        'ED6_DT29/CH15060P._CP',             # 04
        'ED6_DT29/CH15061P._CP',             # 05
        'ED6_DT29/CH14480P._CP',             # 06
        'ED6_DT29/CH14481P._CP',             # 07
        'ED6_DT29/CH14490P._CP',             # 08
        'ED6_DT29/CH14491P._CP',             # 09
        'ED6_DT29/CH14560P._CP',             # 0A
        'ED6_DT29/CH14561P._CP',             # 0B
        'ED6_DT29/CH14010P._CP',             # 0C
        'ED6_DT29/CH14011P._CP',             # 0D
        'ED6_DT26/CH20669P._CP',             # 0E
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1C4,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclMonster(
        X                   = -24160,
        Z                   = -6800,
        Y                   = -490,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x208,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 24710,
        Z                   = -6800,
        Y                   = -300,
        Unknown_0C          = 180,
        Unknown_0E          = 12,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x20E,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 57980,
        Z                   = -3200,
        Y                   = 39180,
        Unknown_0C          = 180,
        Unknown_0E          = 8,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x20C,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 21770,
        Z                   = -10800,
        Y                   = 86320,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x208,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 21820,
        Z                   = -10800,
        Y                   = 101120,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x208,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -350,
        Z                   = -1600,
        Y                   = 73940,
        Unknown_0C          = 180,
        Unknown_0E          = 8,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x20C,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -31970,
        Z                   = -1650,
        Y                   = 43830,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x209,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclEvent(
        X                   = -3980,
        Y                   = -2200,
        Z                   = 99990,
        Range               = 4360,
        Unknown_10          = 0x898,
        Unknown_14          = 0x19294,
        Unknown_18          = 0x0,
        Unknown_1C          = 5,
    )


    DeclActor(
        TriggerX            = 0,
        TriggerZ            = -1600,
        TriggerY            = 111640,
        TriggerRange        = 1000,
        ActorX              = 0,
        ActorZ              = -300,
        ActorY              = 111640,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -32000,
        TriggerZ            = -1650,
        TriggerY            = 40000,
        TriggerRange        = 1000,
        ActorX              = -32000,
        ActorZ              = -650,
        ActorY              = 40000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 58000,
        TriggerZ            = -7200,
        TriggerY            = 0,
        TriggerRange        = 1000,
        ActorX              = 58000,
        ActorZ              = -6200,
        ActorY              = 0,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 58000,
        TriggerZ            = -3200,
        TriggerY            = 45000,
        TriggerRange        = 1000,
        ActorX              = 58000,
        ActorZ              = -2200,
        ActorY              = 45000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_2B6",          # 00, 0
        "Function_1_30D",          # 01, 1
        "Function_2_481",          # 02, 2
        "Function_3_5D6",          # 03, 3
        "Function_4_717",          # 04, 4
        "Function_5_895",          # 05, 5
        "Function_6_11E3",         # 06, 6
        "Function_7_1600",         # 07, 7
        "Function_8_1DD3",         # 08, 8
        "Function_9_1EB1",         # 09, 9
        "Function_10_1F8F",        # 0A, 10
        "Function_11_206D",        # 0B, 11
        "Function_12_214B",        # 0C, 12
        "Function_13_2229",        # 0D, 13
        "Function_14_2307",        # 0E, 14
        "Function_15_2400",        # 0F, 15
        "Function_16_24BC",        # 10, 16
        "Function_17_2578",        # 11, 17
        "Function_18_2634",        # 12, 18
        "Function_19_26F0",        # 13, 19
        "Function_20_27AC",        # 14, 20
        "Function_21_28C2",        # 15, 21
        "Function_22_2910",        # 16, 22
    )


    def Function_0_2B6(): pass

    label("Function_0_2B6")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_30C")
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_2E2"),
        (101, "loc_2E9"),
        (102, "loc_2F0"),
        (103, "loc_2F7"),
        (104, "loc_2FE"),
        (105, "loc_305"),
        (SWITCH_DEFAULT, "loc_30C"),
    )


    label("loc_2E2")

    Event(0, 8)
    Jump("loc_30C")

    label("loc_2E9")

    Event(0, 9)
    Jump("loc_30C")

    label("loc_2F0")

    Event(0, 10)
    Jump("loc_30C")

    label("loc_2F7")

    Event(0, 11)
    Jump("loc_30C")

    label("loc_2FE")

    Event(0, 12)
    Jump("loc_30C")

    label("loc_305")

    Event(0, 13)
    Jump("loc_30C")

    label("loc_30C")

    Return()

    # Function_0_2B6 end

    def Function_1_30D(): pass

    label("Function_1_30D")

    OP_16(0x2, 0xFA0, 0xFFFE0C00, 0xFFFE8CE8, 0x23008D)
    OP_1B(0x0, 0x0, 0xE)
    OP_1B(0x1, 0x0, 0xF)
    OP_1B(0x2, 0x0, 0x10)
    OP_1B(0x3, 0x0, 0x11)
    OP_1B(0x4, 0x0, 0x12)
    OP_1B(0x5, 0x0, 0x13)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x540, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F9")
    ClearChrFlags(0x10, 0x80)
    OP_9F(0x10, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x10, 0, -300, 111640, 0)
    LoadEffect(0x7, "map\\mp253_00.eff")
    LoadEffect(0x6, "map\\mp253_01.eff")
    PlayEffect(0x7, 0x7, 0x10, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x6, 0x6, 0x10, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Jump("loc_3FD")

    label("loc_3F9")

    OP_64(0x0, 0x1)

    label("loc_3FD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x17, 0x0, 0x20)"), scpexpr(EXPR_END)), "loc_410")
    OP_71(0x402, 0x0)
    ExitThread()
    Jump("loc_414")

    label("loc_410")

    Call(0, 22)

    label("loc_414")

    OP_51(0x13, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x16, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x17, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x552, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_447")
    OP_6F(0x3, 0)
    Jump("loc_44E")

    label("loc_447")

    OP_6F(0x3, 60)

    label("loc_44E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x552, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_460")
    OP_6F(0x4, 0)
    Jump("loc_467")

    label("loc_460")

    OP_6F(0x4, 60)

    label("loc_467")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x552, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_479")
    OP_6F(0x5, 0)
    Jump("loc_480")

    label("loc_479")

    OP_6F(0x5, 60)

    label("loc_480")

    Return()

    # Function_1_30D end

    def Function_2_481(): pass

    label("Function_2_481")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x552, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_55A")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x3, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x6C, 1)"), scpexpr(EXPR_END)), "loc_4EF")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "\x07\x05Found \x1F\x6C\x00\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2A90)
    Jump("loc_557")

    label("loc_4EF")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "\x07\x05Found \x1F\x6C\x00\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\x6C\x00\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x3, 60)
    OP_70(0x3, 0x0)

    label("loc_557")

    Jump("loc_5C8")

    label("loc_55A")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        "\x07\x05Have you seen those chests from Erebonia? They're the strong, silent type.\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0xD4, 0x0)

    label("loc_5C8")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_481 end

    def Function_3_5D6(): pass

    label("Function_3_5D6")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x552, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6AF")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x4, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FD, 1)"), scpexpr(EXPR_END)), "loc_644")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #3
        "\x07\x05Found \x1F\xFD\x01\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2A91)
    Jump("loc_6AC")

    label("loc_644")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #4
        (
            "\x07\x05Found \x1F\xFD\x01\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\xFD\x01\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x4, 60)
    OP_70(0x4, 0x0)

    label("loc_6AC")

    Jump("loc_709")

    label("loc_6AF")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #5
        "\x07\x05I know I don't have hands, but I want to hold yours...\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0xD5, 0x0)

    label("loc_709")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_5D6 end

    def Function_4_717(): pass

    label("Function_4_717")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x552, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7F0")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x5, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x16D, 1)"), scpexpr(EXPR_END)), "loc_785")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #6
        "\x07\x05Found \x1F\x6D\x01\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2A92)
    Jump("loc_7ED")

    label("loc_785")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #7
        (
            "\x07\x05Found \x1F\x6D\x01\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\x6D\x01\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x5, 60)
    OP_70(0x5, 0x0)

    label("loc_7ED")

    Jump("loc_887")

    label("loc_7F0")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #8
        (
            "\x07\x05(3/12) 'Oh, my! Sato! Is it really you?' Sato was Hideko's senior in college,\x01",
            "and belonged to the same club as her.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0xD6, 0x0)

    label("loc_887")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_717 end

    def Function_5_895(): pass

    label("Function_5_895")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8A8")
    Call(0, 7)
    Return()

    label("loc_8A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x540, 5)), scpexpr(EXPR_END)), "loc_8B0")
    Return()

    label("loc_8B0")

    EventBegin(0x0)
    OP_8C(0x0, 0, 0)
    OP_8C(0x1, 0, 0)
    OP_8C(0x2, 0, 0)
    OP_8C(0x3, 0, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8F6")
    OP_62(0xEE, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_95D")

    label("loc_8F6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_91E")
    OP_62(0xEE, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_95D")

    label("loc_91E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_946")
    OP_62(0xEE, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_95D")

    label("loc_946")

    OP_62(0xEE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_95D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_985")
    OP_62(0xEF, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_9EC")

    label("loc_985")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9AD")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_9EC")

    label("loc_9AD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9D5")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_9EC")

    label("loc_9D5")

    OP_62(0xEF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_9EC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A14")
    OP_62(0xF0, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_A7B")

    label("loc_A14")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A3C")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_A7B")

    label("loc_A3C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A64")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_A7B")

    label("loc_A64")

    OP_62(0xF0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_A7B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AA3")
    OP_62(0xF1, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_B0A")

    label("loc_AA3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_ACB")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_B0A")

    label("loc_ACB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AF3")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_B0A")

    label("loc_AF3")

    OP_62(0xF1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_B0A")

    Sleep(1000)

    ChrTalk(    #9
        0x10F,
        "#1444F#6PWh-What is that...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x101,
        "#1004F#6P#4S...!!\x02",
    )

    CloseMessageWindow()

    def lambda_B4E():
        OP_6D(-40, 1230, 122310, 5000)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_B4E)

    def lambda_B66():
        OP_67(0, 1780, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_B66)

    def lambda_B7E():
        OP_6B(5200, 5000)
        ExitThread()

    QueueWorkItem(0x10F, 2, lambda_B7E)

    def lambda_B8E():
        OP_6C(0, 5000)
        ExitThread()

    QueueWorkItem(0x10F, 3, lambda_B8E)

    def lambda_B9E():
        OP_6E(240, 5000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B9E)
    WaitChrThread(0x10F, 0x0)
    WaitChrThread(0x10F, 0x2)
    SetChrPos(0x10F, 1310, -1200, 101560, 0)
    SetChrPos(0x101, 90, -1200, 101450, 0)
    SetChrPos(0xF0, 1680, -1200, 99810, 0)
    SetChrPos(0xF1, 110, -1200, 99700, 0)
    Sleep(500)

    ChrTalk(    #11
        0x101,
        "#1020F#5PPater-Mater?!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C49")

    ChrTalk(    #12
        0x10E,
        "#173F#5PI remember that robot!\x02",
    )

    CloseMessageWindow()

    label("loc_C49")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C82")

    ChrTalk(    #13
        0x104,
        "#1545F#5PHeh. Now THIS is a surprise.\x02",
    )

    CloseMessageWindow()

    label("loc_C82")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_CA8")

    ChrTalk(    #14
        0x103,
        "#1525F#5POh, my...\x02",
    )

    CloseMessageWindow()

    label("loc_CA8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_CD4")

    ChrTalk(    #15
        0x105,
        "#1163F#5PUnbelievable...\x02",
    )

    CloseMessageWindow()

    label("loc_CD4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D25")

    ChrTalk(    #16
        0x10B,
        (
            "#216F#5PIsn't that the thing that fought alongside\x01",
            "that kid?!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D25")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D60")

    ChrTalk(    #17
        0x106,
        "#055F#5PDamn... What's THAT doing here?\x02",
    )

    CloseMessageWindow()

    label("loc_D60")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_DAB")

    ChrTalk(    #18
        0x108,
        "#072F#5PI sure didn't expect we'd run into that here...\x02",
    )

    CloseMessageWindow()

    label("loc_DAB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E10")

    ChrTalk(    #19
        0x10A,
        (
            "#1317F#5PI feel like I saw that in the lakeside laboratory\x01",
            "Ouroboros was using...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E10")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E3C")

    ChrTalk(    #20
        0x10D,
        "#270F#5PIt's gigantic...\x02",
    )

    CloseMessageWindow()

    label("loc_E3C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xB)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E8B")

    ChrTalk(    #21
        0x10C,
        (
            "#112F#5PThis is the archaism that appeared in Grancel,\x01",
            "yes?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E8B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F72")

    ChrTalk(    #22
        0x107,
        (
            "#064F#5PWh-What's it doing here...?\x02\x03",

            "#065FWait! Could that stone have Renne inside,\x01",
            "then?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x102,
        (
            "#1505F#5PI'd say the chances are high.\x02\x03",

            "#1502FI certainly wasn't expecting to meet her here,\x01",
            "though...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1049")

    label("loc_F72")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_FDC")

    ChrTalk(    #24
        0x102,
        (
            "#1504F#5PWhat's it doing here...?\x02\x03",

            "#1502FAnd does that mean that stone contains...?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1049")

    label("loc_FDC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1049")

    ChrTalk(    #25
        0x107,
        (
            "#064F#5PWh-What's it doing here...?\x02\x03",

            "#065FWait! Could that stone have Renne inside,\x01",
            "then?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1049")

    Sleep(300)
    Fade(500)
    OP_6D(-700, -1200, 107500, 0)
    OP_67(0, 5680, -10000, 0)
    OP_6B(4110, 0)
    OP_6C(315000, 0)
    OP_6E(207, 0)
    SetChrPos(0x10F, 1310, -1200, 105560, 0)
    SetChrPos(0x101, 90, -1200, 105450, 0)
    SetChrPos(0xF0, 1680, -1200, 103810, 0)
    SetChrPos(0xF1, 110, -1200, 103700, 0)
    SetChrChipByIndex(0x0, 65535)
    SetChrChipByIndex(0x1, 65535)
    SetChrChipByIndex(0x2, 65535)
    SetChrChipByIndex(0x3, 65535)
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #26
        0x10F,
        (
            "#1443F#6PIt looks to me to be a large archaism used by \x01",
            "Ouroboros...\x02\x03",

            "Your reactions say there's more to it than that,\x01",
            "however.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x101,
        (
            "#1007F#5PYou could say that, yeah... \x02\x03",

            "#1002FLet's go get that stone.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2A05)
    OP_28(0x36, 0x1, 0x2)
    Sleep(300)
    EventEnd(0x0)
    Return()

    # Function_5_895 end

    def Function_6_11E3(): pass

    label("Function_6_11E3")

    EventBegin(0x0)
    Fade(500)
    OP_6D(-1000, -1430, 109500, 0)
    OP_67(0, 5230, -10000, 0)
    OP_6B(4150, 0)
    OP_6C(218000, 0)
    OP_6E(207, 0)
    OP_6D(-1000, -1430, 109500, 0)
    OP_67(0, 4990, -10000, 0)
    OP_6B(4150, 0)
    OP_6C(218000, 0)
    OP_6E(207, 0)
    SetChrPos(0x10F, 200, -1400, 108620, 0)
    SetChrPos(0x101, 0, -1600, 109740, 0)
    SetChrPos(0xF0, -1620, -1400, 108530, 45)
    SetChrPos(0xF1, 1800, -1200, 107910, 0)
    SetChrChipByIndex(0x0, 65535)
    SetChrChipByIndex(0x1, 65535)
    SetChrChipByIndex(0x2, 65535)
    SetChrChipByIndex(0x3, 65535)
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    OP_0D()
    Sleep(300)
    OP_8E(0x101, 0x0, 0xFFFFF9C0, 0x1AF72, 0x3E8, 0x0)
    Sleep(500)
    Fade(250)
    SetChrChipByIndex(0x101, 14)
    SetChrSubChip(0x101, 0)
    OP_0D()
    Sleep(300)
    OP_8F(0x10, 0xFFFFFFCE, 0xFFFFFDA8, 0x1B0D0, 0x1F4, 0x0)
    Sleep(500)
    Fade(500)
    OP_82(0x7, 0x0)
    OP_82(0x6, 0x0)
    SetChrFlags(0x10, 0x80)
    OP_0D()
    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #28
        "\x07\x05Found \x1F\x5F\x03\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x35F, 1)
    OP_64(0x0, 0x1)

    ChrTalk(    #29
        0x101,
        "#1025F#5P#40W...\x02",
    )

    CloseMessageWindow()
    Fade(250)
    SetChrChipByIndex(0x101, 65535)
    SetChrSubChip(0x101, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(    #30
        0x101,
        (
            "#1016F#5P#40WAhaha... After all this time, we've finally found\x01",
            "you.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_140F")

    ChrTalk(    #31
        0x102,
        "#1514F#5PYeah...\x02",
    )

    CloseMessageWindow()

    label("loc_140F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1434")

    ChrTalk(    #32
        0x107,
        "#560F#5PHeehee...\x02",
    )

    CloseMessageWindow()

    label("loc_1434")


    ChrTalk(    #33
        0x10F,
        (
            "#1447F#5PYou must have spent a long while looking for\x01",
            "the person inside.\x02\x03",

            "#1448FThen we shouldn't keep you waiting any longer.\x01",
            "Let's hurry back to the garden and release them\x01",
            "right away.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 180, 400)
    Sleep(300)

    ChrTalk(    #34
        0x101,
        "#1025F#12PYeah... Thanks, Ries.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x2A06)
    OP_28(0x36, 0x1, 0x4)
    OP_28(0x36, 0x1, 0x8)
    Sleep(500)
    OP_6D(200, -1600, 109620, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(5000, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, 200, -1600, 109620, 0)
    SetChrPos(0x1, 200, -1600, 109620, 0)
    SetChrPos(0x2, 200, -1600, 109620, 0)
    SetChrPos(0x3, 200, -1600, 109620, 0)
    SetChrChipByIndex(0x0, 65535)
    SetChrChipByIndex(0x1, 65535)
    SetChrChipByIndex(0x2, 65535)
    SetChrChipByIndex(0x3, 65535)
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    OP_69(0x0, 0x0)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_6_11E3 end

    def Function_7_1600(): pass

    label("Function_7_1600")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1610")
    Return()

    label("loc_1610")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0xF, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_161E")
    Return()

    label("loc_161E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x541, 0)), scpexpr(EXPR_END)), "loc_1626")
    Return()

    label("loc_1626")

    EventBegin(0x0)
    OP_8C(0x110, 0, 0)
    OP_62(0x110, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #35
        0x110,
        "#1308F#6PPater-Mater!\x02",
    )

    CloseMessageWindow()

    def lambda_166C():
        OP_6D(100, -100, 133990, 5000)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_166C)

    def lambda_1684():
        OP_67(0, 2770, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_1684)

    def lambda_169C():
        OP_6B(4400, 5000)
        ExitThread()

    QueueWorkItem(0x10F, 2, lambda_169C)

    def lambda_16AC():
        OP_6C(0, 5000)
        ExitThread()

    QueueWorkItem(0x10F, 3, lambda_16AC)

    def lambda_16BC():
        OP_6E(262, 5000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_16BC)
    WaitChrThread(0x10F, 0x0)
    WaitChrThread(0x10F, 0x1)
    Sleep(1000)
    Fade(1000)
    OP_6D(-3980, -1200, 130900, 0)
    OP_67(0, 2600, -10000, 0)
    OP_6B(4990, 0)
    OP_6C(338000, 0)
    OP_6E(270, 0)
    SetChrPos(0x101, 940, -1200, 118140, 7)
    SetChrPos(0x10F, -1120, -1200, 118300, 7)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_176C")
    SetChrPos(0x110, -320, -1200, 119490, 7)
    SetChrPos(0xF1, 80, -1200, 117080, 7)
    Jump("loc_179C")

    label("loc_176C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_179C")
    SetChrPos(0x110, -320, -1200, 119490, 7)
    SetChrPos(0xF0, 80, -1200, 117080, 7)

    label("loc_179C")

    OP_0D()
    Sleep(500)

    ChrTalk(    #36
        0x110,
        (
            "#1307F#5PAre you okay...?\x02\x03",

            "Can you hear me?\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    FadeToDark(300, 0, 100)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, 120, -1, -1)

    AnonymousTalk(    #37
        "\x07\x05\x18#2S#80W...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    FadeToBright(300, 0)
    OP_62(0x110, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x110)
    Sleep(500)

    ChrTalk(    #38
        0x110,
        "#268F#5PIt looks like he can't.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x101,
        "#1026F#5POh, no...\x02",
    )

    CloseMessageWindow()
    Sleep(150)
    Fade(500)
    OP_6D(-1240, -1200, 120760, 0)
    OP_67(0, 4240, -10000, 0)
    OP_6B(3410, 0)
    OP_6C(326000, 0)
    OP_6E(270, 0)

    def lambda_18C5():
        TurnDirection(0xFE, 0x110, 0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_18C5)

    def lambda_18D3():
        TurnDirection(0xFE, 0x110, 0)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_18D3)
    OP_0D()
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1935")

    ChrTalk(    #40
        0x107,
        (
            "#065F#6PI-Is there some kind of problem in his orbal\x01",
            "engines?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1ACB")

    label("loc_1935")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_198A")

    ChrTalk(    #41
        0x102,
        (
            "#1502F#6PI-Is there some kind of problem in his orbal\x01",
            "engines?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1ACB")

    label("loc_198A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_19DE")

    ChrTalk(    #42
        0x10B,
        (
            "#212F#6PI-Is there some kind of problem in his orbal\x01",
            "engines?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1ACB")

    label("loc_19DE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1A32")

    ChrTalk(    #43
        0x10E,
        (
            "#178F#6PI-Is there some kind of problem in his orbal\x01",
            "engines?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1ACB")

    label("loc_1A32")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1A86")

    ChrTalk(    #44
        0x10D,
        (
            "#270F#6PI-Is there some kind of problem in his orbal\x01",
            "engines?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1ACB")

    label("loc_1A86")


    ChrTalk(    #45
        0x10F,
        (
            "#1802F#11PI-Is there some kind of problem in his orbal\x01",
            "engines?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1ACB")


    ChrTalk(    #46
        0x110,
        (
            "#268F#5PIt looks that way...\x02\x03",

            "#1300FWhether that's because he's damaged or this\x01",
            "world's power has rendered him unable to move,\x01",
            "I don't know...\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x110, 180, 400)
    Sleep(300)

    ChrTalk(    #47
        0x110,
        (
            "#263F#11P...Still, let's let him sleep for now.\x02\x03",

            "#260FHe'll wake up eventually. I'm sure of that much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x10F,
        "#1444F#5PHow can you be so sure?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x110,
        (
            "#261F#11PBecause he's my papa and mama rolled into\x01",
            "one, of course.\x02\x03",

            "#265FHe always comes flying when he knows I need\x01",
            "it.\x02\x03",

            "This time won't be any different.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1CC1")

    ChrTalk(    #50
        0x102,
        "#1503F#6P...\x02",
    )

    CloseMessageWindow()
    Jump("loc_1CE5")

    label("loc_1CC1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1CE5")

    ChrTalk(    #51
        0x107,
        "#063F#6PRenne...\x02",
    )

    CloseMessageWindow()

    label("loc_1CE5")


    ChrTalk(    #52
        0x10F,
        "#1445F#5P...I see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x101,
        (
            "#1003F#6P...\x02\x03",

            "#1006FAnyway, let's get going, then, shall we?\x02\x03",

            "Maybe we'll end up running into something\x01",
            "that'll help us get him moving somewhere in \x01",
            "Phantasma, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x110,
        "#261F#11PHeehee. Yup!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2A08)
    OP_28(0x36, 0x1, 0x80)
    Sleep(300)
    EventEnd(0x0)
    Return()

    # Function_7_1600 end

    def Function_8_1DD3(): pass

    label("Function_8_1DD3")

    OP_DE(0x0, 0x0, 0x1)
    EventBegin(0x2)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x0, -100, 370, 60, 0)
    SetChrPos(0x1, -100, 370, 60, 0)
    SetChrPos(0x2, -100, 370, 60, 0)
    SetChrPos(0x3, -100, 370, 60, 0)
    OP_69(0x0, 0x0)
    LoadEffect(0x0, "map\\mp200_02.eff")
    PlayEffect(0x0, 0xFF, 0xFF, -100, 370, 60, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Call(0, 20)
    EventEnd(0x0)
    OP_4F(0x31, (scpexpr(EXPR_PUSH_LONG, 0x14F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_C0(0x16, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Return()

    # Function_8_1DD3 end

    def Function_9_1EB1(): pass

    label("Function_9_1EB1")

    OP_DE(0x0, 0x1, 0x1)
    EventBegin(0x2)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x0, 210, 3700, 49810, 180)
    SetChrPos(0x1, 210, 3700, 49810, 180)
    SetChrPos(0x2, 210, 3700, 49810, 180)
    SetChrPos(0x3, 210, 3700, 49810, 180)
    OP_69(0x0, 0x0)
    LoadEffect(0x0, "map\\mp200_02.eff")
    PlayEffect(0x0, 0xFF, 0xFF, 210, 3700, 49810, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Call(0, 20)
    EventEnd(0x0)
    OP_4F(0x31, (scpexpr(EXPR_PUSH_LONG, 0x14F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_C0(0x16, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Return()

    # Function_9_1EB1 end

    def Function_10_1F8F(): pass

    label("Function_10_1F8F")

    OP_DE(0x0, 0x2, 0x1)
    EventBegin(0x2)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x0, -49790, -7100, 25790, 180)
    SetChrPos(0x1, -49790, -7100, 25790, 180)
    SetChrPos(0x2, -49790, -7100, 25790, 180)
    SetChrPos(0x3, -49790, -7100, 25790, 180)
    OP_69(0x0, 0x0)
    LoadEffect(0x0, "map\\mp200_02.eff")
    PlayEffect(0x0, 0xFF, 0xFF, -49790, -7100, 25790, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Call(0, 20)
    EventEnd(0x0)
    OP_4F(0x31, (scpexpr(EXPR_PUSH_LONG, 0x14F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_C0(0x16, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Return()

    # Function_10_1F8F end

    def Function_11_206D(): pass

    label("Function_11_206D")

    OP_DE(0x0, 0x3, 0x1)
    EventBegin(0x2)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x0, 160, -7100, -50290, 0)
    SetChrPos(0x1, 160, -7100, -50290, 0)
    SetChrPos(0x2, 160, -7100, -50290, 0)
    SetChrPos(0x3, 160, -7100, -50290, 0)
    OP_69(0x0, 0x0)
    LoadEffect(0x0, "map\\mp200_02.eff")
    PlayEffect(0x0, 0xFF, 0xFF, 160, -7100, -50290, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Call(0, 20)
    EventEnd(0x0)
    OP_4F(0x31, (scpexpr(EXPR_PUSH_LONG, 0x14F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_C0(0x16, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Return()

    # Function_11_206D end

    def Function_12_214B(): pass

    label("Function_12_214B")

    OP_DE(0x0, 0x4, 0x1)
    EventBegin(0x2)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x0, -21940, -11150, 93890, 90)
    SetChrPos(0x1, -21940, -11150, 93890, 90)
    SetChrPos(0x2, -21940, -11150, 93890, 90)
    SetChrPos(0x3, -21940, -11150, 93890, 90)
    OP_69(0x0, 0x0)
    LoadEffect(0x0, "map\\mp200_02.eff")
    PlayEffect(0x0, 0xFF, 0xFF, -21940, -11150, 93890, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Call(0, 20)
    EventEnd(0x0)
    OP_4F(0x31, (scpexpr(EXPR_PUSH_LONG, 0x14F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_C0(0x16, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Return()

    # Function_12_214B end

    def Function_13_2229(): pass

    label("Function_13_2229")

    OP_DE(0x0, 0x5, 0x1)
    EventBegin(0x2)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x0, 32159, -1550, 39880, 0)
    SetChrPos(0x1, 32159, -1550, 39880, 0)
    SetChrPos(0x2, 32159, -1550, 39880, 0)
    SetChrPos(0x3, 32159, -1550, 39880, 0)
    OP_69(0x0, 0x0)
    LoadEffect(0x0, "map\\mp200_02.eff")
    PlayEffect(0x0, 0xFF, 0xFF, 32159, -1550, 39880, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Call(0, 20)
    EventEnd(0x0)
    OP_4F(0x31, (scpexpr(EXPR_PUSH_LONG, 0x14F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_C0(0x16, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Return()

    # Function_13_2229 end

    def Function_14_2307(): pass

    label("Function_14_2307")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    OP_6D(-770, 370, -900, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(5000, 0)
    OP_6C(225000, 0)
    OP_6E(262, 0)
    SetChrPos(0x3, -100, 370, 60, 180)
    SetChrPos(0x2, -100, 370, 60, 180)
    SetChrPos(0x1, -100, 370, 60, 180)
    SetChrPos(0x0, -100, 370, 60, 180)
    OP_69(0x0, 0x0)
    OP_0D()
    LoadEffect(0x0, "map\\mp200_01.eff")
    PlayEffect(0x0, 0xFF, 0xFF, -100, 370, 60, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Call(0, 21)
    NewScene("ED6_DT21/M7201   ._SN", 106, 0, 0)
    IdleLoop()
    Return()

    # Function_14_2307 end

    def Function_15_2400(): pass

    label("Function_15_2400")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    SetChrPos(0x3, 210, 3700, 49810, 0)
    SetChrPos(0x2, 210, 3700, 49810, 0)
    SetChrPos(0x1, 210, 3700, 49810, 0)
    SetChrPos(0x0, 210, 3700, 49810, 0)
    OP_69(0x0, 0x0)
    OP_0D()
    LoadEffect(0x0, "map\\mp200_01.eff")
    PlayEffect(0x0, 0xFF, 0xFF, 210, 3700, 49810, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Call(0, 21)
    NewScene("ED6_DT21/M7203   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_15_2400 end

    def Function_16_24BC(): pass

    label("Function_16_24BC")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    SetChrPos(0x3, -49790, -7100, 25790, 0)
    SetChrPos(0x2, -49790, -7100, 25790, 0)
    SetChrPos(0x1, -49790, -7100, 25790, 0)
    SetChrPos(0x0, -49790, -7100, 25790, 0)
    OP_69(0x0, 0x0)
    OP_0D()
    LoadEffect(0x0, "map\\mp200_01.eff")
    PlayEffect(0x0, 0xFF, 0xFF, -49790, -7100, 25790, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Call(0, 21)
    NewScene("ED6_DT21/M7203   ._SN", 101, 0, 0)
    IdleLoop()
    Return()

    # Function_16_24BC end

    def Function_17_2578(): pass

    label("Function_17_2578")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    SetChrPos(0x3, 160, -7100, -50290, 180)
    SetChrPos(0x2, 160, -7100, -50290, 180)
    SetChrPos(0x1, 160, -7100, -50290, 180)
    SetChrPos(0x0, 160, -7100, -50290, 180)
    OP_69(0x0, 0x0)
    OP_0D()
    LoadEffect(0x0, "map\\mp200_01.eff")
    PlayEffect(0x0, 0xFF, 0xFF, 160, -7100, -50290, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Call(0, 21)
    NewScene("ED6_DT21/M7203   ._SN", 102, 0, 0)
    IdleLoop()
    Return()

    # Function_17_2578 end

    def Function_18_2634(): pass

    label("Function_18_2634")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    SetChrPos(0x3, -21940, -11150, 93890, 270)
    SetChrPos(0x2, -21940, -11150, 93890, 270)
    SetChrPos(0x1, -21940, -11150, 93890, 270)
    SetChrPos(0x0, -21940, -11150, 93890, 270)
    OP_69(0x0, 0x0)
    OP_0D()
    LoadEffect(0x0, "map\\mp200_01.eff")
    PlayEffect(0x0, 0xFF, 0xFF, -21940, -11150, 93890, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Call(0, 21)
    NewScene("ED6_DT21/M7203   ._SN", 103, 0, 0)
    IdleLoop()
    Return()

    # Function_18_2634 end

    def Function_19_26F0(): pass

    label("Function_19_26F0")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    SetChrPos(0x3, 32159, -1550, 39880, 180)
    SetChrPos(0x2, 32159, -1550, 39880, 180)
    SetChrPos(0x1, 32159, -1550, 39880, 180)
    SetChrPos(0x0, 32159, -1550, 39880, 180)
    OP_69(0x0, 0x0)
    OP_0D()
    LoadEffect(0x0, "map\\mp200_01.eff")
    PlayEffect(0x0, 0xFF, 0xFF, 32159, -1550, 39880, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Call(0, 21)
    NewScene("ED6_DT21/M7203   ._SN", 104, 0, 0)
    IdleLoop()
    Return()

    # Function_19_26F0 end

    def Function_20_27AC(): pass

    label("Function_20_27AC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_27D5")
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_27C9():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_27C9)

    label("loc_27D5")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_27FE")
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_27F2():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_27F2)

    label("loc_27FE")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2827")
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_281B():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_281B)

    label("loc_2827")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2850")
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_2844():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_2844)

    label("loc_2850")

    Sleep(800)
    OP_44(0x0, 0x1)
    OP_44(0x1, 0x1)
    OP_44(0x2, 0x1)
    OP_44(0x3, 0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_287C")
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_287C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2893")
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_2893")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_28AA")
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_28AA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_28C1")
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_28C1")

    Return()

    # Function_20_27AC end

    def Function_21_28C2(): pass

    label("Function_21_28C2")


    def lambda_28C8():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_28C8)

    def lambda_28DA():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_28DA)

    def lambda_28EC():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_28EC)

    def lambda_28FE():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_28FE)
    Sleep(1000)
    Return()

    # Function_21_28C2 end

    def Function_22_2910(): pass

    label("Function_22_2910")

    OP_E5(0x0, 0x2, 0x0, 262144)
    OP_E5(0x0, 0x2, 0x1, 262144)
    OP_E5(0x0, 0x2, 0x2, 262144)
    OP_E5(0x0, 0x2, 0x3, 262144)
    OP_E5(0x0, 0x2, 0x4, 262144)
    OP_E5(0x0, 0x2, 0x5, 262144)
    OP_E5(0x0, 0x2, 0x6, 262144)
    OP_E5(0x0, 0x2, 0x7, 262144)
    OP_E5(0x0, 0x2, 0x8, 262144)
    OP_E5(0x0, 0x2, 0x9, 262144)
    OP_E5(0x0, 0x2, 0xA, 262144)
    OP_E5(0x0, 0x2, 0xB, 262144)
    OP_E5(0x0, 0x2, 0xC, 262144)
    OP_E5(0x0, 0x2, 0xD, 262144)
    OP_E5(0x0, 0x2, 0xE, 262144)
    OP_E5(0x0, 0x2, 0xF, 262144)
    OP_E5(0x0, 0x2, 0x10, 262144)
    OP_E5(0x0, 0x2, 0x11, 262144)
    OP_E5(0x0, 0x2, 0x12, 262144)
    OP_E5(0x0, 0x2, 0x13, 262144)
    OP_E5(0x0, 0x2, 0x14, 262144)
    OP_E5(0x0, 0x2, 0x15, 262144)
    OP_E5(0x0, 0x2, 0x16, 262144)
    OP_E5(0x0, 0x2, 0x17, 262144)
    OP_E5(0x0, 0x2, 0x18, 262144)
    OP_E5(0x0, 0x2, 0x19, 262144)
    OP_E5(0x0, 0x2, 0x1A, 262144)
    OP_E5(0x0, 0x2, 0x1B, 262144)
    OP_E5(0x0, 0x2, 0x1C, 262144)
    OP_E5(0x0, 0x2, 0x1D, 262144)
    OP_E5(0x0, 0x2, 0x1E, 262144)
    OP_E5(0x0, 0x2, 0x1F, 262144)
    OP_E5(0x0, 0x2, 0x20, 262144)
    OP_E5(0x0, 0x2, 0x21, 262144)
    OP_E5(0x0, 0x2, 0x22, 262144)
    OP_E5(0x0, 0x2, 0x23, 262144)
    OP_E5(0x0, 0x2, 0x24, 262144)
    OP_E5(0x0, 0x2, 0x25, 262144)
    OP_E5(0x0, 0x2, 0x26, 262144)
    OP_E5(0x0, 0x2, 0x27, 262144)
    OP_E5(0x0, 0x2, 0x28, 262144)
    OP_E5(0x0, 0x2, 0x29, 262144)
    OP_E5(0x0, 0x2, 0x2A, 262144)
    OP_E5(0x0, 0x2, 0x2B, 262144)
    OP_E5(0x0, 0x2, 0x2C, 262144)
    OP_E5(0x0, 0x2, 0x2D, 262144)
    OP_E5(0x0, 0x2, 0x2E, 262144)
    OP_E5(0x0, 0x2, 0x2F, 262144)
    OP_E5(0x0, 0x2, 0x30, 262144)
    OP_E5(0x0, 0x2, 0x31, 262144)
    OP_E5(0x0, 0x2, 0x32, 262144)
    OP_E5(0x0, 0x2, 0x33, 262144)
    OP_E5(0x0, 0x2, 0x34, 262144)
    OP_E5(0x0, 0x2, 0x35, 262144)
    OP_E5(0x0, 0x2, 0x36, 262144)
    OP_E5(0x0, 0x2, 0x37, 262144)
    OP_E5(0x0, 0x2, 0x38, 262144)
    OP_E5(0x0, 0x2, 0x39, 262144)
    OP_E5(0x0, 0x2, 0x3A, 262144)
    OP_E5(0x0, 0x2, 0x3B, 262144)
    OP_E5(0x0, 0x2, 0x3C, 262144)
    OP_E5(0x0, 0x2, 0x3D, 262144)
    OP_E5(0x0, 0x2, 0x3E, 262144)
    OP_E5(0x0, 0x2, 0x3F, 262144)
    OP_E5(0x0, 0x2, 0x40, 262144)
    OP_E5(0x0, 0x2, 0x41, 262144)
    OP_E5(0x0, 0x2, 0x42, 262144)
    OP_E5(0x0, 0x2, 0x43, 262144)
    OP_E5(0x0, 0x2, 0x44, 262144)
    OP_E5(0x0, 0x2, 0x45, 262144)
    OP_E5(0x0, 0x2, 0x46, 262144)
    OP_E5(0x0, 0x2, 0x47, 262144)
    OP_E5(0x0, 0x2, 0x48, 262144)
    OP_E5(0x0, 0x2, 0x49, 262144)
    OP_E5(0x0, 0x2, 0x4A, 262144)
    OP_E5(0x0, 0x2, 0x4B, 262144)
    OP_E5(0x0, 0x2, 0x4C, 262144)
    OP_E5(0x0, 0x2, 0x4D, 262144)
    OP_E5(0x0, 0x2, 0x4E, 262144)
    OP_E5(0x0, 0x2, 0x4F, 262144)
    OP_E5(0x0, 0x2, 0x50, 262144)
    OP_E5(0x0, 0x2, 0x51, 262144)
    OP_E5(0x0, 0x2, 0x52, 262144)
    OP_E5(0x0, 0x2, 0x53, 262144)
    OP_E5(0x0, 0x2, 0x54, 262144)
    OP_E5(0x0, 0x2, 0x55, 262144)
    OP_E5(0x0, 0x2, 0x56, 262144)
    OP_E5(0x0, 0x2, 0x57, 262144)
    OP_E5(0x0, 0x2, 0x58, 262144)
    OP_E5(0x0, 0x2, 0x59, 262144)
    OP_E5(0x0, 0x2, 0x5A, 262144)
    OP_E5(0x0, 0x2, 0x5B, 262144)
    OP_E5(0x0, 0x2, 0x5C, 262144)
    OP_E5(0x0, 0x2, 0x5D, 262144)
    OP_E5(0x0, 0x2, 0x5E, 262144)
    OP_E5(0x0, 0x2, 0x5F, 262144)
    OP_E5(0x0, 0x2, 0x60, 262144)
    OP_E5(0x0, 0x2, 0x61, 262144)
    OP_E5(0x0, 0x2, 0x62, 262144)
    OP_E5(0x0, 0x2, 0x63, 262144)
    OP_E5(0x0, 0x2, 0x64, 262144)
    OP_E5(0x0, 0x2, 0x65, 262144)
    OP_E5(0x0, 0x2, 0x66, 262144)
    OP_E5(0x0, 0x2, 0x67, 262144)
    OP_E5(0x0, 0x2, 0x68, 262144)
    OP_E5(0x0, 0x2, 0x69, 262144)
    OP_E5(0x0, 0x2, 0x6A, 262144)
    OP_E5(0x0, 0x2, 0x6B, 262144)
    OP_E5(0x0, 0x2, 0x6C, 262144)
    OP_E5(0x0, 0x2, 0x6D, 262144)
    OP_E5(0x0, 0x2, 0x6E, 262144)
    OP_E5(0x0, 0x2, 0x6F, 262144)
    OP_E5(0x0, 0x2, 0x70, 262144)
    OP_E5(0x0, 0x2, 0x71, 262144)
    OP_E5(0x0, 0x2, 0x72, 262144)
    OP_E5(0x0, 0x2, 0x73, 262144)
    OP_E5(0x0, 0x2, 0x74, 262144)
    OP_E5(0x0, 0x2, 0x75, 262144)
    OP_E5(0x0, 0x2, 0x76, 262144)
    OP_E5(0x0, 0x2, 0x77, 262144)
    OP_E5(0x0, 0x2, 0x78, 262144)
    OP_E5(0x0, 0x2, 0x79, 262144)
    OP_E5(0x0, 0x2, 0x7A, 262144)
    OP_E5(0x0, 0x2, 0x7B, 262144)
    OP_E5(0x0, 0x2, 0x7C, 262144)
    OP_E5(0x0, 0x2, 0x7D, 262144)
    OP_E5(0x0, 0x2, 0x7E, 262144)
    OP_E5(0x0, 0x2, 0x7F, 262144)
    OP_E5(0x0, 0x2, 0x80, 262144)
    OP_E5(0x0, 0x2, 0x81, 262144)
    OP_E5(0x0, 0x2, 0x82, 262144)
    OP_E5(0x0, 0x2, 0x83, 262144)
    OP_E5(0x0, 0x2, 0x84, 262144)
    OP_E5(0x0, 0x2, 0x85, 262144)
    OP_E5(0x0, 0x2, 0x86, 262144)
    OP_E5(0x0, 0x2, 0x87, 262144)
    OP_E5(0x0, 0x2, 0x88, 262144)
    OP_E5(0x0, 0x2, 0x89, 262144)
    OP_E5(0x0, 0x2, 0x8A, 262144)
    OP_E5(0x0, 0x2, 0x8B, 262144)
    OP_E5(0x0, 0x2, 0x8C, 262144)
    OP_E5(0x0, 0x2, 0x8D, 262144)
    OP_E5(0x0, 0x2, 0x8E, 262144)
    OP_E5(0x0, 0x2, 0x8F, 262144)
    OP_E5(0x0, 0x2, 0x90, 262144)
    OP_E5(0x0, 0x2, 0x91, 262144)
    OP_E5(0x0, 0x2, 0x92, 262144)
    OP_E5(0x0, 0x2, 0x93, 262144)
    OP_E5(0x0, 0x2, 0x94, 262144)
    OP_E5(0x0, 0x2, 0x95, 262144)
    OP_E5(0x0, 0x2, 0x96, 262144)
    OP_E5(0x0, 0x2, 0x97, 262144)
    OP_E5(0x0, 0x2, 0x98, 262144)
    OP_E5(0x0, 0x2, 0x99, 262144)
    OP_E5(0x0, 0x2, 0x9A, 262144)
    OP_E5(0x0, 0x2, 0x9B, 262144)
    OP_E5(0x0, 0x2, 0x9C, 262144)
    OP_E5(0x0, 0x2, 0x9D, 262144)
    OP_E5(0x0, 0x2, 0x9E, 262144)
    OP_E5(0x0, 0x2, 0x9F, 262144)
    OP_E5(0x0, 0x2, 0xA0, 262144)
    OP_E5(0x0, 0x2, 0xA1, 262144)
    OP_E5(0x0, 0x2, 0xA2, 262144)
    OP_E5(0x0, 0x2, 0xA3, 262144)
    OP_E5(0x0, 0x2, 0xA4, 262144)
    OP_E5(0x0, 0x2, 0xA5, 262144)
    OP_E5(0x0, 0x2, 0xA6, 262144)
    OP_E5(0x0, 0x2, 0xA7, 262144)
    OP_E5(0x0, 0x2, 0xA8, 262144)
    OP_E5(0x0, 0x2, 0xA9, 262144)
    OP_E5(0x0, 0x2, 0xAA, 262144)
    OP_E5(0x0, 0x2, 0xAB, 262144)
    OP_E5(0x0, 0x2, 0xAC, 262144)
    OP_E5(0x0, 0x2, 0xAD, 262144)
    OP_E5(0x0, 0x2, 0xAE, 262144)
    OP_E5(0x0, 0x2, 0xAF, 262144)
    OP_E5(0x0, 0x2, 0xB0, 262144)
    OP_E5(0x0, 0x2, 0xB1, 262144)
    OP_E5(0x0, 0x2, 0xB2, 262144)
    OP_E5(0x2, 0x2, 0x0, 800)
    OP_E5(0x2, 0x2, 0x1, 800)
    OP_E5(0x2, 0x2, 0x2, 800)
    OP_E5(0x2, 0x2, 0x3, 800)
    OP_E5(0x2, 0x2, 0x4, 800)
    OP_E5(0x2, 0x2, 0x5, 800)
    OP_E5(0x2, 0x2, 0x6, 800)
    OP_E5(0x2, 0x2, 0x7, 800)
    OP_E5(0x2, 0x2, 0x8, 800)
    OP_E5(0x2, 0x2, 0x9, 800)
    OP_E5(0x2, 0x2, 0xA, 800)
    OP_E5(0x2, 0x2, 0xB, 800)
    OP_E5(0x2, 0x2, 0xC, 800)
    OP_E5(0x2, 0x2, 0xD, 800)
    OP_E5(0x2, 0x2, 0xE, 800)
    OP_E5(0x2, 0x2, 0xF, 800)
    OP_E5(0x2, 0x2, 0x10, 800)
    OP_E5(0x2, 0x2, 0x11, 800)
    OP_E5(0x2, 0x2, 0x12, 800)
    OP_E5(0x2, 0x2, 0x13, 800)
    OP_E5(0x2, 0x2, 0x14, 800)
    OP_E5(0x2, 0x2, 0x15, 800)
    OP_E5(0x2, 0x2, 0x16, 800)
    OP_E5(0x2, 0x2, 0x17, 800)
    OP_E5(0x2, 0x2, 0x18, 800)
    OP_E5(0x2, 0x2, 0x19, 800)
    OP_E5(0x2, 0x2, 0x1A, 800)
    OP_E5(0x2, 0x2, 0x1B, 800)
    OP_E5(0x2, 0x2, 0x1C, 800)
    OP_E5(0x2, 0x2, 0x1D, 800)
    OP_E5(0x2, 0x2, 0x1E, 800)
    OP_E5(0x2, 0x2, 0x1F, 800)
    OP_E5(0x2, 0x2, 0x20, 800)
    OP_E5(0x2, 0x2, 0x21, 800)
    OP_E5(0x2, 0x2, 0x22, 800)
    OP_E5(0x2, 0x2, 0x23, 800)
    OP_E5(0x2, 0x2, 0x24, 800)
    OP_E5(0x2, 0x2, 0x25, 800)
    OP_E5(0x2, 0x2, 0x26, 800)
    OP_E5(0x2, 0x2, 0x27, 800)
    OP_E5(0x2, 0x2, 0x28, 800)
    OP_E5(0x2, 0x2, 0x29, 800)
    OP_E5(0x2, 0x2, 0x2A, 800)
    OP_E5(0x2, 0x2, 0x2B, 800)
    OP_E5(0x2, 0x2, 0x2C, 800)
    OP_E5(0x2, 0x2, 0x2D, 800)
    OP_E5(0x2, 0x2, 0x2E, 800)
    OP_E5(0x2, 0x2, 0x2F, 800)
    OP_E5(0x2, 0x2, 0x30, 800)
    OP_E5(0x2, 0x2, 0x31, 800)
    OP_E5(0x2, 0x2, 0x32, 800)
    OP_E5(0x2, 0x2, 0x33, 800)
    OP_E5(0x2, 0x2, 0x34, 800)
    OP_E5(0x2, 0x2, 0x35, 800)
    OP_E5(0x2, 0x2, 0x36, 800)
    OP_E5(0x2, 0x2, 0x37, 800)
    OP_E5(0x2, 0x2, 0x38, 800)
    OP_E5(0x2, 0x2, 0x39, 800)
    OP_E5(0x2, 0x2, 0x3A, 800)
    OP_E5(0x2, 0x2, 0x3B, 800)
    OP_E5(0x2, 0x2, 0x3C, 800)
    OP_E5(0x2, 0x2, 0x3D, 800)
    OP_E5(0x2, 0x2, 0x3E, 800)
    OP_E5(0x2, 0x2, 0x3F, 800)
    OP_E5(0x2, 0x2, 0x40, 800)
    OP_E5(0x2, 0x2, 0x41, 800)
    OP_E5(0x2, 0x2, 0x42, 800)
    OP_E5(0x2, 0x2, 0x43, 800)
    OP_E5(0x2, 0x2, 0x44, 800)
    OP_E5(0x2, 0x2, 0x45, 800)
    OP_E5(0x2, 0x2, 0x46, 800)
    OP_E5(0x2, 0x2, 0x47, 800)
    OP_E5(0x2, 0x2, 0x48, 800)
    OP_E5(0x2, 0x2, 0x49, 800)
    OP_E5(0x2, 0x2, 0x4A, 800)
    OP_E5(0x2, 0x2, 0x4B, 800)
    OP_E5(0x2, 0x2, 0x4C, 800)
    OP_E5(0x2, 0x2, 0x4D, 800)
    OP_E5(0x2, 0x2, 0x4E, 800)
    OP_E5(0x2, 0x2, 0x4F, 800)
    OP_E5(0x2, 0x2, 0x50, 800)
    OP_E5(0x2, 0x2, 0x51, 800)
    OP_E5(0x2, 0x2, 0x52, 800)
    OP_E5(0x2, 0x2, 0x53, 800)
    OP_E5(0x2, 0x2, 0x54, 800)
    OP_E5(0x2, 0x2, 0x55, 800)
    OP_E5(0x2, 0x2, 0x56, 800)
    OP_E5(0x2, 0x2, 0x57, 800)
    OP_E5(0x2, 0x2, 0x58, 800)
    OP_E5(0x2, 0x2, 0x59, 800)
    OP_E5(0x2, 0x2, 0x5A, 800)
    OP_E5(0x2, 0x2, 0x5B, 800)
    OP_E5(0x2, 0x2, 0x5C, 800)
    OP_E5(0x2, 0x2, 0x5D, 800)
    OP_E5(0x2, 0x2, 0x5E, 800)
    OP_E5(0x2, 0x2, 0x5F, 800)
    OP_E5(0x2, 0x2, 0x60, 800)
    OP_E5(0x2, 0x2, 0x61, 800)
    OP_E5(0x2, 0x2, 0x62, 800)
    OP_E5(0x2, 0x2, 0x63, 800)
    OP_E5(0x2, 0x2, 0x64, 800)
    OP_E5(0x2, 0x2, 0x65, 800)
    OP_E5(0x2, 0x2, 0x66, 800)
    OP_E5(0x2, 0x2, 0x67, 800)
    OP_E5(0x2, 0x2, 0x68, 800)
    OP_E5(0x2, 0x2, 0x69, 800)
    OP_E5(0x2, 0x2, 0x6A, 800)
    OP_E5(0x2, 0x2, 0x6B, 800)
    OP_E5(0x2, 0x2, 0x6C, 800)
    OP_E5(0x2, 0x2, 0x6D, 800)
    OP_E5(0x2, 0x2, 0x6E, 800)
    OP_E5(0x2, 0x2, 0x6F, 800)
    OP_E5(0x2, 0x2, 0x70, 800)
    OP_E5(0x2, 0x2, 0x71, 800)
    OP_E5(0x2, 0x2, 0x72, 800)
    OP_E5(0x2, 0x2, 0x73, 800)
    OP_E5(0x2, 0x2, 0x74, 800)
    OP_E5(0x2, 0x2, 0x75, 800)
    OP_E5(0x2, 0x2, 0x76, 800)
    OP_E5(0x2, 0x2, 0x77, 800)
    OP_E5(0x2, 0x2, 0x78, 800)
    OP_E5(0x2, 0x2, 0x79, 800)
    OP_E5(0x2, 0x2, 0x7A, 800)
    OP_E5(0x2, 0x2, 0x7B, 800)
    OP_E5(0x2, 0x2, 0x7C, 800)
    OP_E5(0x2, 0x2, 0x7D, 800)
    OP_E5(0x2, 0x2, 0x7E, 800)
    OP_E5(0x2, 0x2, 0x7F, 800)
    OP_E5(0x2, 0x2, 0x80, 800)
    OP_E5(0x2, 0x2, 0x81, 800)
    OP_E5(0x2, 0x2, 0x82, 800)
    OP_E5(0x2, 0x2, 0x83, 800)
    OP_E5(0x2, 0x2, 0x84, 800)
    OP_E5(0x2, 0x2, 0x85, 800)
    OP_E5(0x2, 0x2, 0x86, 800)
    OP_E5(0x2, 0x2, 0x87, 800)
    OP_E5(0x2, 0x2, 0x88, 800)
    OP_E5(0x2, 0x2, 0x89, 800)
    OP_E5(0x2, 0x2, 0x8A, 800)
    OP_E5(0x2, 0x2, 0x8B, 800)
    OP_E5(0x2, 0x2, 0x8C, 800)
    OP_E5(0x2, 0x2, 0x8D, 800)
    OP_E5(0x2, 0x2, 0x8E, 800)
    OP_E5(0x2, 0x2, 0x8F, 800)
    OP_E5(0x2, 0x2, 0x90, 800)
    OP_E5(0x2, 0x2, 0x91, 800)
    OP_E5(0x2, 0x2, 0x92, 800)
    OP_E5(0x2, 0x2, 0x93, 800)
    OP_E5(0x2, 0x2, 0x94, 800)
    OP_E5(0x2, 0x2, 0x95, 800)
    OP_E5(0x2, 0x2, 0x96, 800)
    OP_E5(0x2, 0x2, 0x97, 800)
    OP_E5(0x2, 0x2, 0x98, 800)
    OP_E5(0x2, 0x2, 0x99, 800)
    OP_E5(0x2, 0x2, 0x9A, 800)
    OP_E5(0x2, 0x2, 0x9B, 800)
    OP_E5(0x2, 0x2, 0x9C, 800)
    OP_E5(0x2, 0x2, 0x9D, 800)
    OP_E5(0x2, 0x2, 0x9E, 800)
    OP_E5(0x2, 0x2, 0x9F, 800)
    OP_E5(0x2, 0x2, 0xA0, 800)
    OP_E5(0x2, 0x2, 0xA1, 800)
    OP_E5(0x2, 0x2, 0xA2, 800)
    OP_E5(0x2, 0x2, 0xA3, 800)
    OP_E5(0x2, 0x2, 0xA4, 800)
    OP_E5(0x2, 0x2, 0xA5, 800)
    OP_E5(0x2, 0x2, 0xA6, 800)
    OP_E5(0x2, 0x2, 0xA7, 800)
    OP_E5(0x2, 0x2, 0xA8, 800)
    OP_E5(0x2, 0x2, 0xA9, 800)
    OP_E5(0x2, 0x2, 0xAA, 800)
    OP_E5(0x2, 0x2, 0xAB, 800)
    OP_E5(0x2, 0x2, 0xAC, 800)
    OP_E5(0x2, 0x2, 0xAD, 800)
    OP_E5(0x2, 0x2, 0xAE, 800)
    OP_E5(0x2, 0x2, 0xAF, 800)
    OP_E5(0x2, 0x2, 0xB0, 800)
    OP_E5(0x2, 0x2, 0xB1, 800)
    OP_E5(0x2, 0x2, 0xB2, 800)
    Return()

    # Function_22_2910 end

    SaveToFile()

Try(main)
