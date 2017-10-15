from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 蔡斯

    CreateScenaFile(
        FileName            = 'R3400   ._SN',
        MapName             = 'Zeiss',
        Location            = 'R3400.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60030",
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
        'Air-Letten - Checkpoint',              # 9
        'Zeiss',                                # 10
        'Whale Frog',                           # 11
        '',                                     # 12
        '',                                     # 13
        '',                                     # 14
        '',                                     # 15
        '',                                     # 16
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
        'ED6_DT09/CH10130 ._CH',             # 00
        'ED6_DT09/CH10131 ._CH',             # 01
        'ED6_DT09/CH10750 ._CH',             # 02
        'ED6_DT09/CH10751 ._CH',             # 03
        'ED6_DT09/CH10760 ._CH',             # 04
        'ED6_DT09/CH10761 ._CH',             # 05
        'ED6_DT09/CH10770 ._CH',             # 06
        'ED6_DT09/CH10771 ._CH',             # 07
        'ED6_DT29/CH12410 ._CH',             # 08
        'ED6_DT29/CH12411 ._CH',             # 09
        'ED6_DT09/CH10500 ._CH',             # 0A
        'ED6_DT09/CH10501 ._CH',             # 0B
    )

    AddCharChipPat(
        'ED6_DT09/CH10130P._CP',             # 00
        'ED6_DT09/CH10131P._CP',             # 01
        'ED6_DT09/CH10750P._CP',             # 02
        'ED6_DT09/CH10751P._CP',             # 03
        'ED6_DT09/CH10760P._CP',             # 04
        'ED6_DT09/CH10761P._CP',             # 05
        'ED6_DT09/CH10770P._CP',             # 06
        'ED6_DT09/CH10771P._CP',             # 07
        'ED6_DT29/CH12410P._CP',             # 08
        'ED6_DT29/CH12411P._CP',             # 09
        'ED6_DT09/CH10500P._CP',             # 0A
        'ED6_DT09/CH10501P._CP',             # 0B
    )

    DeclNpc(
        X                   = -26110,
        Z                   = -20,
        Y                   = -38940,
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
        X                   = 189780,
        Z                   = -20,
        Y                   = -27490,
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
        X                   = 47000,
        Z                   = 0,
        Y                   = -25210,
        Direction           = 89,
        Unknown2            = 10,
        Unknown3            = 655360,
        ChipIndex           = 0x0,
        NpcIndex            = 0x185,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclMonster(
        X                   = 45900,
        Z                   = 20,
        Y                   = -46160,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x1CD,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 40140,
        Z                   = -10,
        Y                   = -13510,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x1CE,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 121900,
        Z                   = -40,
        Y                   = -57020,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x1CF,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 115250,
        Z                   = 10,
        Y                   = -35350,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x1D0,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 146080,
        Z                   = -30,
        Y                   = -31900,
        Unknown_0C          = 0,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x1CF,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclEvent(
        X                   = -15540,
        Y                   = 0,
        Z                   = -43640,
        Range               = -12240,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0xFFFF79F0,
        Unknown_18          = 0x0,
        Unknown_1C          = 8,
    )

    DeclEvent(
        X                   = 47000,
        Y                   = -1000,
        Z                   = -25210,
        Range               = 3000,
        Unknown_10          = 0xC80,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 3,
    )


    DeclActor(
        TriggerX            = 19790,
        TriggerZ            = 0,
        TriggerY            = -14460,
        TriggerRange        = 1000,
        ActorX              = 19250,
        ActorZ              = 10,
        ActorY              = -15050,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 55120,
        TriggerZ            = -70,
        TriggerY            = 8740,
        TriggerRange        = 1000,
        ActorX              = 55870,
        ActorZ              = -70,
        ActorY              = 8740,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 19690,
        TriggerZ            = -90,
        TriggerY            = 11550,
        TriggerRange        = 1000,
        ActorX              = 19240,
        ActorZ              = -90,
        ActorY              = 11060,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 124260,
        TriggerZ            = -30,
        TriggerY            = -53650,
        TriggerRange        = 1000,
        ActorX              = 124760,
        ActorZ              = -30,
        ActorY              = -53160,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_2C6",          # 00, 0
        "Function_1_2FF",          # 01, 1
        "Function_2_461",          # 02, 2
        "Function_3_477",          # 03, 3
        "Function_4_646",          # 04, 4
        "Function_5_7CE",          # 05, 5
        "Function_6_914",          # 06, 6
        "Function_7_A9F",          # 07, 7
        "Function_8_C0C",          # 08, 8
        "Function_9_C0D",          # 09, 9
        "Function_10_1065",        # 0A, 10
    )


    def Function_0_2C6(): pass

    label("Function_0_2C6")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2FE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2FE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 2)), scpexpr(EXPR_END)), "loc_2E7")
    OP_A2(0x2081)
    Jump("loc_2FE")

    label("loc_2E7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x150, 0x2)"), scpexpr(EXPR_END)), "loc_2F7")
    Event(0, 10)
    Jump("loc_2FB")

    label("loc_2F7")

    Event(0, 9)

    label("loc_2FB")

    OP_A2(0x2081)

    label("loc_2FE")

    Return()

    # Function_0_2C6 end

    def Function_1_2FF(): pass

    label("Function_1_2FF")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3A4")
    OP_71(0x0, 0x4)
    OP_71(0x1, 0x4)
    OP_71(0x2, 0x4)
    OP_71(0x3, 0x4)
    OP_71(0x4, 0x4)
    OP_71(0x5, 0x4)
    OP_71(0x6, 0x4)
    OP_71(0x7, 0x4)
    OP_71(0x8, 0x4)
    OP_71(0x9, 0x4)
    OP_71(0xA, 0x4)
    OP_71(0xB, 0x4)
    OP_71(0xC, 0x4)
    OP_71(0xD, 0x4)
    OP_72(0x12, 0x4)
    OP_79(0x0, 0x2)
    OP_79(0x1, 0x2)
    OP_79(0x2, 0x2)
    OP_79(0x3, 0x2)
    OP_79(0x4, 0x2)
    OP_79(0x5, 0x2)
    OP_79(0x6, 0x2)
    OP_79(0x7, 0x2)
    OP_79(0x8, 0x2)
    OP_79(0x9, 0x2)
    OP_79(0xA, 0x2)
    OP_79(0xB, 0x2)
    OP_79(0xC, 0x2)
    OP_79(0xD, 0x2)
    OP_79(0xF, 0x2)
    OP_79(0x10, 0x2)
    OP_7B()
    OP_C4(0x0, 0x1)
    OP_78(0x0, 0x0, 0x0)
    Jump("loc_3A4")

    label("loc_3A4")

    OP_16(0x2, 0xFA0, 0xFFFF5038, 0xFFFDB228, 0x230037)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2A4, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3C8")
    OP_6F(0xE, 0)
    Jump("loc_3CF")

    label("loc_3C8")

    OP_6F(0xE, 60)

    label("loc_3CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2A4, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3E1")
    OP_6F(0xF, 0)
    Jump("loc_3E8")

    label("loc_3E1")

    OP_6F(0xF, 60)

    label("loc_3E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2A4, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3FA")
    OP_6F(0x10, 0)
    Jump("loc_401")

    label("loc_3FA")

    OP_6F(0x10, 60)

    label("loc_401")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2A4, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_413")
    OP_6F(0x11, 0)
    Jump("loc_41A")

    label("loc_413")

    OP_6F(0x11, 60)

    label("loc_41A")

    OP_51(0xF, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xA, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_44E")
    SetChrFlags(0xA, 0x80)
    OP_B2(0x0, 0x1, 0x80)
    Jump("loc_460")

    label("loc_44E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x29F, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_460")
    ClearChrFlags(0xA, 0x80)
    OP_B2(0x1, 0x1, 0x80)

    label("loc_460")

    Return()

    # Function_1_2FF end

    def Function_2_461(): pass

    label("Function_2_461")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_476")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_461")

    label("loc_476")

    Return()

    # Function_2_461 end

    def Function_3_477(): pass

    label("Function_3_477")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x29F, 2)), scpexpr(EXPR_END)), "loc_47F")
    Return()

    label("loc_47F")

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

    AnonymousTalk(    #0
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
        (1, "loc_573"),
        (SWITCH_DEFAULT, "loc_596"),
    )


    label("loc_573")

    Fade(500)
    OP_89(0x0, 53120, 0, -24940, 270)
    OP_69(0x0, 0x0)
    OP_30(0x1)
    OP_0D()
    EventEnd(0x0)
    Return()

    label("loc_596")

    Battle(0xEE1, 0x0, 0x0, 0x0, 0xFF)
    EventBegin(0x1)
    OP_89(0x0, 53120, 0, -24940, 270)
    OP_69(0x0, 0x0)
    OP_30(0x1)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (2, "loc_5CF"),
        (1, "loc_5D2"),
        (SWITCH_DEFAULT, "loc_5D5"),
    )


    label("loc_5CF")

    EventEnd(0x0)
    Return()

    label("loc_5D2")

    OP_B4(0x0)
    Return()

    label("loc_5D5")

    EventBegin(0x1)
    SetChrFlags(0xA, 0x80)
    OP_B2(0x0, 0x1, 0x80)
    OP_0D()
    Sleep(400)
    OP_22(0x17, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        "\x07\x05Exterminated monster!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_A2(0x14FA)
    OP_28(0xA5, 0x4, 0x10)
    OP_28(0xA5, 0x4, 0x2)
    OP_28(0xA5, 0x1, 0x1)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    EventEnd(0x0)
    Return()

    # Function_3_477 end

    def Function_4_646(): pass

    label("Function_4_646")

    OP_EA(0x2, 0xF6, 0x1, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2A4, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_71E")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0xE, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FE, 1)"), scpexpr(EXPR_END)), "loc_6B7")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #2
        "Found \x1F\xFE\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1520)
    Jump("loc_71B")

    label("loc_6B7")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #3
        (
            "Found \x1F\xFE\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\xFE\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0xE, 60)
    OP_70(0xE, 0x0)

    label("loc_71B")

    Jump("loc_7C0")

    label("loc_71E")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #4
        (
            "\x07\x05As you close the empty chest, you weigh the\x01",
            "pluses and minuses of staying in there to jump\x01",
            "out scare the next person who checks it.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_7C0")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_646 end

    def Function_5_7CE(): pass

    label("Function_5_7CE")

    OP_EA(0x2, 0xF7, 0x1, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2A4, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8A6")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0xF, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1F6, 1)"), scpexpr(EXPR_END)), "loc_83F")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #5
        "Found \x1F\xF6\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1521)
    Jump("loc_8A3")

    label("loc_83F")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #6
        (
            "Found \x1F\xF6\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\xF6\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0xF, 60)
    OP_70(0xF, 0x0)

    label("loc_8A3")

    Jump("loc_906")

    label("loc_8A6")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #7
        (
            "\x07\x05You're not diggin this whole 'one item per chest'\x01",
            "thing, are you?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_906")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_7CE end

    def Function_6_914(): pass

    label("Function_6_914")

    OP_EA(0x2, 0xF8, 0x1, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2A4, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9EC")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x10, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x287, 1)"), scpexpr(EXPR_END)), "loc_985")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #8
        "Found \x1F\x87\x02\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1522)
    Jump("loc_9E9")

    label("loc_985")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #9
        (
            "Found \x1F\x87\x02\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\x87\x02\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x10, 60)
    OP_70(0x10, 0x0)

    label("loc_9E9")

    Jump("loc_A91")

    label("loc_9EC")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #10
        (
            "\x07\x05The empty chest's shape tempts you to climb on\x01",
            "top of it and start writing the next great Zemurian\x01",
            "novel. You somehow resist the urge.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_A91")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_914 end

    def Function_7_A9F(): pass

    label("Function_7_A9F")

    OP_EA(0x2, 0xF9, 0x1, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2A4, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B77")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x11, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x182, 1)"), scpexpr(EXPR_END)), "loc_B10")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #11
        "Found \x1F\x82\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1524)
    Jump("loc_B74")

    label("loc_B10")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #12
        (
            "Found \x1F\x82\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\x82\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x11, 60)
    OP_70(0x11, 0x0)

    label("loc_B74")

    Jump("loc_BFE")

    label("loc_B77")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #13
        (
            "\x07\x05You open the chest and wait for an item to\x01",
            "levitate from the chest and into your hands.\x01",
            "Nothing happens.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_BFE")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_7_A9F end

    def Function_8_C0C(): pass

    label("Function_8_C0C")

    Return()

    # Function_8_C0C end

    def Function_9_C0D(): pass

    label("Function_9_C0D")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_6D(-12000, 30, -38910, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, -18500, 40, -40040, 90)
    SetChrPos(0x102, -18500, 20, -38760, 90)
    SetChrPos(0xF8, -20000, 40, -40040, 90)
    SetChrPos(0xF9, -20000, 40, -38760, 90)

    def lambda_CA0():
        OP_8F(0xFE, 0xFFFFD01C, 0x14, 0xFFFF65E6, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_CA0)
    Sleep(50)

    def lambda_CC0():
        OP_8F(0xFE, 0xFFFFCF9A, 0xA, 0xFFFF6A50, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_CC0)
    Sleep(50)

    def lambda_CE0():
        OP_8F(0xFE, 0xFFFFCB4E, 0x28, 0xFFFF6528, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_CE0)
    Sleep(50)

    def lambda_D00():
        OP_8F(0xFE, 0xFFFFCA9A, 0x1E, 0xFFFF6942, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_D00)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0xF9, 0x1)
    Sleep(500)

    ChrTalk(    #14
        0x101,
        "#1020FHoly crap!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D6F")

    ChrTalk(    #15
        0x108,
        "#072FTotal darkness, huh?\x02",
    )

    CloseMessageWindow()
    Jump("loc_DFD")

    label("loc_D6F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_DBF")

    ChrTalk(    #16
        0x106,
        (
            "#055FFriggin' A...\x01",
            "Literally can't see a thing down here.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DFD")

    label("loc_DBF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_DFD")

    ChrTalk(    #17
        0x103,
        (
            "#022FBlast it all...\x01",
            "It's completely dark!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DFD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E6D")

    ChrTalk(    #18
        0x107,
        (
            "#065FI never realized how dark it'd get\x01",
            "down here without the lights!\x01",
            "Aaah, it's scary...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F32")

    label("loc_E6D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_EC9")

    ChrTalk(    #19
        0x103,
        (
            "#025FYou never stop to think about\x01",
            "even our lights being orbal now...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F32")

    label("loc_EC9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F32")

    ChrTalk(    #20
        0x106,
        (
            "#057FYeah, well...even our lights are orbal\x01",
            "now. You don't realize it till it's gone.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F32")


    ChrTalk(    #21
        0x102,
        (
            "#1043F#6PThe only hope we'd have of navigating down\x01",
            "here would be night-vision goggles.\x02\x03",

            "#1042FIf we don't have any, we should\x01",
            "check around town, in the general\x01",
            "goods store or something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x101,
        (
            "#1007FYeah, good idea.\x02\x03",

            "#1002FOne way or another, probably best to\x01",
            "find a way to see before going forward.\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x0)
    Return()

    # Function_9_C0D end

    def Function_10_1065(): pass

    label("Function_10_1065")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_6D(-12000, 30, -38910, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, -18500, 40, -40040, 90)
    SetChrPos(0x102, -18500, 20, -38760, 90)
    SetChrPos(0xF8, -20000, 40, -40040, 90)
    SetChrPos(0xF9, -20000, 40, -38760, 90)

    def lambda_10F8():
        OP_8F(0xFE, 0xFFFFD01C, 0x14, 0xFFFF65E6, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_10F8)
    Sleep(50)

    def lambda_1118():
        OP_8F(0xFE, 0xFFFFCF9A, 0xA, 0xFFFF6A50, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1118)
    Sleep(50)

    def lambda_1138():
        OP_8F(0xFE, 0xFFFFCB4E, 0x28, 0xFFFF6528, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_1138)
    Sleep(50)

    def lambda_1158():
        OP_8F(0xFE, 0xFFFFCA9A, 0x1E, 0xFFFF6942, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_1158)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0xF9, 0x1)
    Sleep(500)

    ChrTalk(    #23
        0x101,
        (
            "#1019FWell, with the night-vision goggles\x01",
            "on I can actually see...\x02\x03",

            "But without them, yeah, I know\x01",
            "what it feels like to be a bat now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x102,
        (
            "#1035F#6PThere's virtually no light down\x01",
            "here, otherwise.\x02\x03",

            "#1042FIn the interest of not getting lost, we\x01",
            "should wear the goggles whenever\x01",
            "we pass through here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x101,
        "#1002FGot it!\x02",
    )

    CloseMessageWindow()
    EventEnd(0x0)
    Return()

    # Function_10_1065 end

    SaveToFile()

Try(main)
