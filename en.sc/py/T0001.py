from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 调试地图

    CreateScenaFile(
        FileName            = 'T0001   ._SN',
        MapName             = 'map1',
        Location            = 'T0001.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60000",
        Flags               = 0,
        EntryFunctionIndex  = 19,
        Reserved            = 0,
        IncludedScenario    = [
            'ED6_DT21/T0001   ._SN',
            'ED6_DT21/T0001_1 ._SN',
            'ED6_DT21/T0001_2 ._SN',
            'ED6_DT21/T0001_3 ._SN',
            'ED6_DT21/T0001_4 ._SN',
            'ED6_DT21/T0001_5 ._SN',
            '',
            ''
        ],
    )

    BuildStringList(
        '@FileName',                            # 8
        'Villager 1',                           # 9
        'Unya',                                 # 10
        'Treasure Chest',                       # 11
        'Treasure Chest',                       # 12
        '',                                     # 13
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
        InitFunctionIndex       = 1,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 2,
    )


    AddCharChip(
        'ED6_DT07/CH01000 ._CH',             # 00
        'ED6_DT09/CH10000 ._CH',             # 01
        'ED6_DT09/CH10001 ._CH',             # 02
    )

    AddCharChipPat(
        'ED6_DT07/CH01000P._CP',             # 00
        'ED6_DT09/CH10000P._CP',             # 01
        'ED6_DT09/CH10001P._CP',             # 02
    )

    DeclNpc(
        X                   = 4000,
        Z                   = 0,
        Y                   = -4000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 6,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = -4000,
        Z                   = 0,
        Y                   = -2000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = -4000,
        Z                   = 0,
        Y                   = -4000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x0,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -5000,
        Z                   = 0,
        Y                   = -6000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x0,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclMonster(
        X                   = 10000,
        Z                   = 0,
        Y                   = -4000,
        Unknown_0C          = 0,
        Unknown_0E          = 1,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x7D0,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclEvent(
        X                   = 10000,
        Y                   = 0,
        Z                   = -1000,
        Range               = 11000,
        Unknown_10          = 0x3E8,
        Unknown_14          = 0x0,
        Unknown_18          = 0x0,
        Unknown_1C          = 11,
    )


    DeclActor(
        TriggerX            = -2000,
        TriggerZ            = 1000,
        TriggerY            = 0,
        TriggerRange        = 1000,
        ActorX              = -2000,
        ActorZ              = 1000,
        ActorY              = 0,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 11,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -2000,
        TriggerZ            = 1000,
        TriggerY            = 0,
        TriggerRange        = 2000,
        ActorX              = -2000,
        ActorZ              = 1000,
        ActorY              = 0,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 11,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_1C6",          # 00, 0
        "Function_1_1C7",          # 01, 1
        "Function_2_45F",          # 02, 2
        "Function_3_468",          # 03, 3
        "Function_4_469",          # 04, 4
        "Function_5_46E",          # 05, 5
        "Function_6_76C",          # 06, 6
        "Function_7_791",          # 07, 7
        "Function_8_7CD",          # 08, 8
        "Function_9_7E2",          # 09, 9
        "Function_10_806",         # 0A, 10
        "Function_11_8D0",         # 0B, 11
        "Function_12_129D",        # 0C, 12
        "Function_13_148F",        # 0D, 13
        "Function_14_1653",        # 0E, 14
        "Function_15_1915",        # 0F, 15
        "Function_16_1A79",        # 10, 16
        "Function_17_1AFD",        # 11, 17
        "Function_18_1B0B",        # 12, 18
        "Function_19_1B15",        # 13, 19
        "Function_20_1B8D",        # 14, 20
        "Function_21_1BAF",        # 15, 21
        "Function_22_1C86",        # 16, 22
        "Function_23_1CAC",        # 17, 23
        "Function_24_1CD0",        # 18, 24
        "Function_25_1CEE",        # 19, 25
        "Function_26_1D15",        # 1A, 26
        "Function_27_1D35",        # 1B, 27
        "Function_28_1DE1",        # 1C, 28
    )


    def Function_0_1C6(): pass

    label("Function_0_1C6")

    Return()

    # Function_0_1C6 end

    def Function_1_1C7(): pass

    label("Function_1_1C7")

    Event(0, 11)
    OP_62(0x9, 0xFFFFFDA8, 300, 0x80, 0x21, 0xFA, 0x0)
    SetChrFlags(0x9, 0x6)
    OP_51(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x9, -4000, 1000, -2000, 0)
    OP_51(0x9, 0x2A, (scpexpr(EXPR_PUSH_LONG, 0x7530), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x9, 0x2B, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x9, 0x2C, (scpexpr(EXPR_PUSH_LONG, 0x15F90), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x9, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x9, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x9, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_44F")
    OP_A2(0x1000)
    RemoveParty(0x0, 0xFF)
    AddParty(0x9, 0xF6, 0x0)
    AddParty(0xD, 0xF7, 0x1)
    AddParty(0x8, 0xF8, 0x2)
    AddParty(0xE, 0xF9, 0x3)
    Call(2, 58)
    OP_31(0x0, 0x7, 0x4)
    OP_31(0x0, 0x0, 0x3)
    OP_31(0x1, 0x7, 0x3)
    OP_31(0x0, 0x7, 0x3)
    OP_35(0x0, 0x96)
    OP_35(0x0, 0x97)
    OP_35(0x0, 0x98)
    OP_35(0x0, 0x99)
    OP_35(0x0, 0x9A)
    OP_35(0x1, 0xA0)
    OP_35(0x1, 0xA1)
    OP_35(0x1, 0xA4)
    OP_35(0x1, 0xA2)
    OP_35(0x1, 0xA3)
    OP_35(0x2, 0xAA)
    OP_35(0x2, 0xAB)
    OP_35(0x2, 0xAC)
    OP_35(0x3, 0xB4)
    OP_35(0x3, 0xB5)
    OP_35(0x3, 0xB6)
    OP_35(0x4, 0xBE)
    OP_35(0x4, 0xBF)
    OP_35(0x5, 0xC8)
    OP_35(0x5, 0xC9)
    OP_35(0x5, 0xCA)
    OP_35(0x5, 0xCB)
    OP_35(0x6, 0xD2)
    OP_35(0x6, 0xD3)
    OP_35(0x7, 0xDD)
    OP_35(0x7, 0xDE)
    OP_35(0x7, 0xDC)
    OP_35(0x0, 0x8C)
    OP_35(0x1, 0x8C)
    OP_35(0x2, 0x8C)
    OP_35(0x3, 0x8C)
    OP_35(0x4, 0x8C)
    OP_35(0x5, 0x8C)
    OP_35(0x6, 0x8C)
    OP_35(0x7, 0x8C)
    OP_36(0x0, 0xE6)
    OP_36(0x0, 0xE7)
    OP_36(0x0, 0xE8)
    OP_36(0x1, 0xEB)
    OP_36(0x1, 0xEC)
    OP_36(0x1, 0xED)
    OP_36(0x2, 0xF0)
    OP_36(0x2, 0xF1)
    OP_36(0x3, 0xF5)
    OP_36(0x3, 0xF6)
    OP_36(0x4, 0xFA)
    OP_36(0x4, 0xFB)
    OP_36(0x5, 0xFF)
    OP_36(0x5, 0x100)
    OP_36(0x5, 0x101)
    OP_36(0x6, 0x104)
    OP_36(0x6, 0x105)
    OP_36(0x7, 0x109)
    OP_36(0x7, 0x10A)
    OP_36(0x7, 0x10B)
    OP_36(0xA, 0x112)
    OP_35(0x8, 0x82)
    OP_36(0x8, 0x10E)
    OP_3E(0x258, 1)
    OP_3E(0x259, 1)
    OP_3E(0x25E, 1)
    OP_3E(0x1F5, 50)
    OP_31(0xE, 0x0, 0x55)
    OP_31(0xE, 0xFE, 0x0)
    OP_41(0xE, 0x87, 0xFF)
    OP_41(0xE, 0x107, 0xFF)
    OP_41(0xE, 0x128, 0xFF)
    OP_35(0xE, 0x0)
    OP_BB(0xE, 0x6, 0x11A)
    OP_37(0xE, 0x80, 0x3)
    OP_37(0xE, 0x81, 0x3)
    OP_37(0xE, 0x82, 0x2)
    OP_37(0xE, 0x83, 0x3)
    OP_37(0xE, 0x84, 0x2)
    OP_37(0xE, 0x85, 0x2)
    OP_37(0xE, 0x86, 0x2)
    OP_41(0xE, 0x276, 0x0)
    OP_41(0xE, 0x275, 0x1)
    OP_41(0xE, 0x2CB, 0x3)
    OP_41(0xE, 0x294, 0x4)
    OP_41(0xE, 0x29A, 0x5)
    OP_41(0xE, 0x2A2, 0x6)
    OP_31(0xF, 0x0, 0x56)
    OP_31(0xF, 0xFE, 0x0)
    OP_41(0xF, 0xA5, 0xFF)
    OP_41(0xF, 0x107, 0xFF)
    OP_41(0xF, 0x128, 0xFF)
    OP_35(0xF, 0x0)
    OP_BB(0xF, 0x6, 0x114)
    OP_37(0xF, 0x80, 0x2)
    OP_37(0xF, 0x81, 0x3)
    OP_37(0xF, 0x82, 0x2)
    OP_37(0xF, 0x83, 0x2)
    OP_37(0xF, 0x84, 0x2)
    OP_37(0xF, 0x85, 0x3)
    OP_37(0xF, 0x86, 0x3)
    OP_41(0xF, 0x294, 0x0)
    OP_41(0xF, 0x275, 0x1)
    OP_41(0xF, 0x298, 0x2)
    OP_41(0xF, 0x2D7, 0x3)
    OP_41(0xF, 0x272, 0x4)
    OP_41(0xF, 0x29A, 0x5)
    OP_31(0xB, 0x0, 0x55)
    OP_31(0xB, 0xFE, 0x0)
    OP_35(0xB, 0x0)
    OP_31(0xC, 0x0, 0x55)
    OP_31(0xC, 0xFE, 0x0)
    OP_35(0xC, 0x0)
    SetMapFlags(0x1000000)

    label("loc_44F")

    SetMapFlags(0x1)
    ClearMapFlags(0x20)
    ClearMapFlags(0x400000)
    Return()

    # Function_1_1C7 end

    def Function_2_45F(): pass

    label("Function_2_45F")

    OP_D7(0x1, 50000, 0)
    Return()

    # Function_2_45F end

    def Function_3_468(): pass

    label("Function_3_468")

    Return()

    # Function_3_468 end

    def Function_4_469(): pass

    label("Function_4_469")

    Call(0, 11)
    Return()

    # Function_4_469 end

    def Function_5_46E(): pass

    label("Function_5_46E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_END)), "loc_48E")

    ChrTalk(    #0
        0xFE,
        "Local Flags set!\x02",
    )

    CloseMessageWindow()

    label("loc_48E")

    OP_A2(0x12)
    SetMessageWindowPos(100, 100, 15, 2)

    AnonymousTalk(    #1
        (
            "#200WSpecify coordinates to display.\x02\x01",

            "#WFor realz!\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #2 op#A
        (
            "#20A2Wait a moment~\x02",

            "#AIf you don't specify anything,\x01",
            "it will center the screen~\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)

    AnonymousTalk(    #3
        "Specify default coordinates to reset.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    ChrTalk(    #4
        0xFE,
        "#010F#1PTop-Left\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        "#010F#2PTop-Right\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xFE,
        "#010F#3PBottom-Left\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        "#010F#4PBottom-Right\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xFE,
        "#010F#5PTop-Center\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xFE,
        "#010F#6PBottom-Center\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xFE,
        (
            "Did you know you can press\x01",
            "F11 to change stuff too?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xFE,
        "#010FI'm Aina! And I'm awesome!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x1,
        "#020FOh? Hahahahah.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x1,
        (
            "#020FHow odd to meet Aina\x01",
            "in such a weird place.\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("Joshua")

    AnonymousTalk(    #14
        (
            "#000F夏休#4RWelp.#Testing messages..\x02\x01",

            "#4SAaaahhh...\x02",
        )
    )

    CloseMessageWindow()
    OP_61(0x101)

    AnonymousTalk(    #15
        (
            "#F#2SABCDE#10R a   b   c   d   e#\x02\x01",

            "FGHIJKLMNO#10R FG  HI  JK  LM  NO#PQRSTUVWXY#10R PQ  RS  TU  VW  XY#\x01",
            "and also Z, I guess.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    TalkEnd(0xFE)
    Return()

    # Function_5_46E end

    def Function_6_76C(): pass

    label("Function_6_76C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_790")
    OP_8D(0xFE, 5000, -5000, 15000, 9000, 2000)
    OP_48()
    Jump("Function_6_76C")

    label("loc_790")

    Return()

    # Function_6_76C end

    def Function_7_791(): pass

    label("Function_7_791")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7CC")
    OP_70(0x1, 0x32)
    OP_8D(0xFE, -10000, -10000, 1000, 1000, 2000)
    OP_6F(0x1, 0)
    OP_72(0x1, 0x8)
    Sleep(2000)
    Jump("Function_7_791")

    label("loc_7CC")

    Return()

    # Function_7_791 end

    def Function_8_7CD(): pass

    label("Function_8_7CD")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7E1")
    OP_8C(0xFE, 180, 5000)
    OP_48()
    Jump("Function_8_7CD")

    label("loc_7E1")

    Return()

    # Function_8_7CD end

    def Function_9_7E2(): pass

    label("Function_9_7E2")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_805")
    OP_8D(0x0, 10000, 10000, -10000, -10000, 2000)
    Jump("Function_9_7E2")

    label("loc_805")

    Return()

    # Function_9_7E2 end

    def Function_10_806(): pass

    label("Function_10_806")

    OP_A1(0xA, 0x4)
    SetChrFlags(0xA, 0x4)
    ClearChrFlags(0xA, 0x100)
    SetChrPos(0xA, 0, 0, 0, 0)
    OP_98(0x0, 0xA)
    OP_98(0x1, 0x2710, 0x7D0, 0x2710)
    OP_98(0x1, 0x1388, 0x1770, 0x4E20)

    def lambda_84C():
        OP_98(0x2, 0xA, 0x7D0, 0x6)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_84C)
    WaitChrThread(0xA, 0x2)
    OP_8E(0xA, 0xFFFFF448, 0x0, 0x0, 0x7D0, 0x0)
    OP_98(0x0, 0xA)
    OP_98(0x1, 0x1B58, 0x0, 0x1388)
    OP_98(0x1, 0x2710, 0x7D0, 0x1F40)
    OP_98(0x1, 0x3A98, 0x1388, 0x1B58)
    OP_98(0x2, 0xA, 0x7D0, 0x2)
    OP_98(0x0, 0xA)
    OP_98(0x1, 0x2710, 0xFFFFEC78, 0x7D0)
    OP_98(0x1, 0x2710, 0x2710, 0xFFFFEC78)
    OP_98(0x2, 0xA, 0x7D0, 0x2)
    Return()

    # Function_10_806 end

    def Function_11_8D0(): pass

    label("Function_11_8D0")

    OP_16(0x1)
    EventBegin(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    AnonymousTalk(    #16
        "I've got your number. Heehee.\x02",
    )

    OP_57(0x0, 0x0, 0x12, "#1CTest Menu")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_91B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_128F")

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Test Maps\x01",                    # 0
            "Game Maps\x01",                    # 1
            "Characters\x01",                   # 2
            "Monsters\x01",                     # 3
            "Battle\x01",                       # 4
            "Battle (Algorithm Test)\x01",      # 5
            "Battle (Map Check)\x01",           # 6
            "Minigames\x01",                    # 7
            "Events\x01",                       # 8
            "Shop Test\x01",                    # 9
            "Character Art Change\x01",         # 10
            "Trap Land\x01",                    # 11
            "Portraits\x01",                    # 12
            "Party Select Menu\x01",            # 13
            "Blur\x01",                         # 14
            "Item Menu\x01",                    # 15
            "Save Menu\x01",                    # 16
            "Set all handbook flags\x01",       # 17
            "Get all recipes\x01",              # 18
            "Game Clear\x01",                   # 19
            "Camp Menu\x01",                    # 20
            "Movies\x01",                       # 21
            "Partner Change\x01",               # 22
            "Disk Change\x01",                  # 23
            "Data Inherit Check\x01",           # 24
            "NG+ Flag Check (Casino)\x01",      # 25
            "Cancel\x01",                       # 26
        )
    )

    MenuEnd(0x0)
    OP_16(0x1)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_B00"),
        (1, "loc_B07"),
        (2, "loc_B0E"),
        (3, "loc_B15"),
        (4, "loc_B1C"),
        (5, "loc_B23"),
        (6, "loc_B2A"),
        (7, "loc_B31"),
        (8, "loc_B38"),
        (9, "loc_B42"),
        (10, "loc_B4E"),
        (11, "loc_C09"),
        (12, "loc_C15"),
        (13, "loc_E16"),
        (14, "loc_EC4"),
        (15, "loc_EF6"),
        (16, "loc_EFD"),
        (17, "loc_F01"),
        (18, "loc_F08"),
        (19, "loc_F0F"),
        (20, "loc_F2B"),
        (21, "loc_118A"),
        (22, "loc_11B7"),
        (23, "loc_11CB"),
        (24, "loc_1271"),
        (25, "loc_1278"),
        (SWITCH_DEFAULT, "loc_127F"),
    )


    label("loc_B00")

    Call(0, 15)
    Jump("loc_128C")

    label("loc_B07")

    Call(3, 6)
    Jump("loc_128C")

    label("loc_B0E")

    Call(3, 0)
    Jump("loc_128C")

    label("loc_B15")

    Call(3, 3)
    Jump("loc_128C")

    label("loc_B1C")

    Call(2, 0)
    Jump("loc_128C")

    label("loc_B23")

    Call(1, 0)
    Jump("loc_128C")

    label("loc_B2A")

    Call(2, 1)
    Jump("loc_128C")

    label("loc_B31")

    Call(2, 59)
    Jump("loc_128C")

    label("loc_B38")

    OP_66(0x1)
    Call(4, 0)
    Jump("loc_128C")

    label("loc_B42")

    OP_5F(0x0)
    OP_56(0x0)
    Call(0, 21)
    Jump("loc_128C")

    label("loc_B4E")


    Menu(
        1,
        -1,
        -1,
        1,
        (
            "Estelle (SC), Joshua (SC)\x01",              # 0
            "Estelle (FC), Joshua (FC)\x01",              # 1
            "Joshua (SC Finale), Kloe (Formal)\x01",      # 2
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_BC5"),
        (1, "loc_BD6"),
        (2, "loc_BE7"),
        (SWITCH_DEFAULT, "loc_BF8"),
    )


    label("loc_BC5")

    OP_BB(0x0, 0x1, 0x0)
    OP_BB(0x1, 0x1, 0x1)
    Jump("loc_BF8")

    label("loc_BD6")

    OP_BB(0x0, 0x1, 0x1E)
    OP_BB(0x1, 0x1, 0x1F)
    Jump("loc_BF8")

    label("loc_BE7")

    OP_BB(0x4, 0x1, 0x1D)
    OP_BB(0x1, 0x1, 0x1C)
    Jump("loc_BF8")

    label("loc_BF8")

    OP_5F(0x1)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_BD()
    Jump("loc_128C")

    label("loc_C09")

    NewScene("ED6_DT21/A0019   ._SN", 0, 0, 0)
    IdleLoop()
    Jump("loc_128C")

    label("loc_C15")

    OP_5F(0x0)
    OP_56(0x0)
    Sleep(1000)
    OP_D9(0x0, "CTI00110")
    Sleep(2000)
    OP_D9(0x1)
    OP_C5(0x0, 0x0, 0x0, 0x200, 0x200, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x1FF, 0x1FF, 0xFFFFFF, 0x0, "C_VIS000._CH")
    OP_C6(0x0, 0x3, -1, 1000, 0)
    Sleep(2000)
    OP_C5(0x1, 0xFF9C, 0xFF9C, 0x64, 0x64, 0x154, 0xFA, 0x300, 0x200, 0x0, 0x0, 0xFF, 0xFF, 0xFFFFFF, 0x0, "C_VIS001._CH")
    OP_C6(0x1, 0x3, -1, 1000, 0)
    Sleep(2000)
    OP_C5(0x0, 0xFF9C, 0xFF9C, 0x64, 0x64, 0x168, 0x104, 0x300, 0x200, 0x0, 0x0, 0xFF, 0xFF, 0xFFFFFF, 0x0, "C_VIS002._CH")
    OP_C6(0x0, 0x3, -1, 1000, 0)
    Sleep(2000)
    OP_C5(0x2, 0xFF9C, 0xFF9C, 0x64, 0x64, 0x17C, 0x104, 0x300, 0x200, 0x0, 0x0, 0xFF, 0xFF, 0xFFFFFF, 0x0, "C_VIS002._CH")
    OP_C6(0x2, 0x3, -1, 1000, 0)
    Sleep(2000)
    OP_C5(0x3, 0xFF9C, 0xFF9C, 0x64, 0x64, 0x190, 0x104, 0x300, 0x200, 0x0, 0x0, 0xFF, 0xFF, 0xFFFFFF, 0x0, "C_VIS002._CH")
    OP_C6(0x3, 0x3, -1, 1000, 0)
    OP_C6(0x0, 0x0, 0, 0, 1000)
    OP_C6(0x0, 0x2, 90000, 2000, 0)
    OP_C7(0x0, 0x0, 0x0)

    AnonymousTalk(    #17
        "わお\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x0, 0x0, 360000, 260000, 0)
    Sleep(1000)
    OP_C6(0x1, 0x4, 0, 0, 0)
    Sleep(1000)
    OP_C6(0x0, 0x3, 16777215, 1000, 0)
    OP_C6(0x0, 0x1, 0, 1000, 1000)
    OP_C6(0x1, 0x3, 16777215, 1000, 0)
    OP_C6(0x2, 0x3, 16777215, 500, 0)
    OP_C6(0x3, 0x1, 10000, 0, 500)
    OP_C7(0x0, 0xFF, 0x3)
    OP_C7(0x1, 0xFF, 0x0)
    Jump("loc_128C")

    label("loc_E16")

    OP_5F(0x0)
    OP_56(0x0)
    OP_C9(0x0, 0x4, 0x0, 0xFF, 0xFF, 0xFF, 0x1, 0x2, 0x3, 0x4, 0x5, 0x6, 0x7, 0x8, 0x9, 0xD, 0xA, 0xF, 0xE, 0xB, 0xC, 0xFFFF)

    ChrTalk(    #18
        0xF8,
        "Okay!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF7)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E76")

    ChrTalk(    #19
        0xF7,
        "Partner 1: Kloe.\x02",
    )

    Jump("loc_EC0")

    label("loc_E76")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E9D")

    ChrTalk(    #20
        0xF7,
        "Partner 1: Joshua.\x02",
    )

    Jump("loc_EC0")

    label("loc_E9D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF7)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EC0")

    ChrTalk(    #21
        0xF7,
        "Partner 1: Agate.\x02",
    )


    label("loc_EC0")

    CloseMessageWindow()
    Jump("loc_128C")

    label("loc_EC4")

    BlurSwitch(0x3E8, 0xBBFFFFFF, 0x0, 0x0, 0x0)

    ChrTalk(    #22
        0xF6,
        "Blur\x02",
    )

    Sleep(2000)
    OP_15(0x1F4)

    ChrTalk(    #23
        0xF6,
        "Off!\x02",
    )

    CloseMessageWindow()
    Jump("loc_128C")

    label("loc_EF6")

    OP_18()
    ExitThread()
    ExitThread()
    ExitThread()
    Jump("loc_128C")

    label("loc_EFD")

    ShowSaveMenu()
    Jump("loc_128C")

    label("loc_F01")

    Call(5, 0)
    Jump("loc_128C")

    label("loc_F08")

    Call(5, 1)
    Jump("loc_128C")

    label("loc_F0F")

    OP_4F(0x31, (scpexpr(EXPR_PUSH_LONG, 0x12B), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A2(0x22AE)
    FadeToDark(500, 0, -1)
    ShowSaveMenu()
    OP_B4(0x1)
    Jump("loc_128C")

    label("loc_F2B")

    EventBegin(0x0)
    OP_5F(0x0)
    OP_56(0x0)
    OP_A3(0x16)

    label("loc_F35")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1174")
    FadeToDark(1000, 0, -1)
    OP_0D()

    AnonymousTalk(    #24
        (
            "\x06\x18\x07\x05* Reorganizing party.\x01",
            "  Select your members, make any necessary changes,\x01",
            "  and then select Proceed to continue.\x07\x00\x02",
        )
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Organize Party\x01",        # 0
            "Change Equipment\x01",      # 1
            "Proceed\x01",               # 2
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_56(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_107C")
    OP_A2(0x16)
    SetChrName("")

    AnonymousTalk(    #25
        (
            "\x07\x05* Reorganizing party.\x01",
            "  Please select your members.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(100)
    OP_C9(0x0, 0x4, 0x0, 0x8, 0xFF, 0xFF, 0x5, 0x2, 0x6, 0x3, 0x4, 0x7, 0xFFFF)
    Jump("loc_1171")

    label("loc_107C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10E8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 6)), scpexpr(EXPR_END)), "loc_10B5")
    OP_C0(0x13, 0x78, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Jump("loc_10E5")

    label("loc_10B5")


    AnonymousTalk(    #26
        "\x07\x05* Please select your party first.\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(100)

    label("loc_10E5")

    Jump("loc_1171")

    label("loc_10E8")

    SetChrName("")

    AnonymousTalk(    #27
        "\x06\x18\x07\x05Proceed?\x07\x00\x02",
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Yes\x01",      # 0
            "No\x01",       # 1
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_56(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1151")
    SetChrName("")

    AnonymousTalk(    #28
        "\x06\x18\x07\x05Proceeding.\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Jump("loc_1174")

    label("loc_1151")

    SetChrName("")

    AnonymousTalk(    #29
        "\x06\x18\x07\x05Returning to menu.\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_1174")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToBright(0, 0)
    OP_0D()
    Jump("loc_128C")

    label("loc_1171")

    Jump("loc_F35")

    label("loc_118A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 5)), scpexpr(EXPR_END)), "loc_119E")
    PlayMovie(0x1, "", 0x0, 0x0)
    OP_A3(0x15)
    Jump("loc_11B4")

    label("loc_119E")

    PlayMovie(0x0, "ED6_DT41.dat", 0x0, 0x0)
    OP_A2(0x15)

    label("loc_11B4")

    Jump("loc_128C")

    label("loc_11B7")

    Call(0, 27)
    FadeToBright(0, 0)
    Call(0, 28)
    Jump("loc_128C")

    label("loc_11CB")

    OP_5F(0x0)

    AnonymousTalk(    #30
        "RAM Saving!\x02",
    )

    CloseMessageWindow()
    OP_E9(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xCA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1201")

    AnonymousTalk(    #31
        "ラムッロード！！\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_1201")


    AnonymousTalk(    #32
        "Disk chaaaaange!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC8), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1228")
    OP_E6(0x2)
    Jump("loc_122A")

    label("loc_1228")

    OP_E6(0x1)

    label("loc_122A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC9), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1251")

    AnonymousTalk(    #33
        (
            "RAM Load\x01",
            "completed!\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_E9(0x2)

    label("loc_1251")


    AnonymousTalk(    #34
        (
            "RAM Delete\x01",
            "completed!\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_E9(0x0)
    Jump("loc_128C")

    label("loc_1271")

    Call(0, 12)
    Jump("loc_128C")

    label("loc_1278")

    Call(0, 13)
    Jump("loc_128C")

    label("loc_127F")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_128C")

    label("loc_128C")

    Jump("loc_91B")

    label("loc_128F")

    OP_5F(0x0)
    OP_56(0x0)
    OP_DA()
    Sleep(300)
    EventEnd(0x0)
    Return()

    # Function_11_8D0 end

    def Function_12_129D(): pass

    label("Function_12_129D")

    EventBegin(0x0)
    OP_5F(0x0)
    OP_5F(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 2)), scpexpr(EXPR_END)), "loc_12D5")

    AnonymousTalk(    #35
        (
            "Equipment\x01",
            "has been carried over!\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Jump("loc_12F6")

    label("loc_12D5")


    AnonymousTalk(    #36
        (
            "Equipment\x01",
            "not carried over?\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_12F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 3)), scpexpr(EXPR_END)), "loc_1323")

    AnonymousTalk(    #37
        (
            "Items\x01",
            "have been carried over!\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Jump("loc_1340")

    label("loc_1323")


    AnonymousTalk(    #38
        (
            "Items\x01",
            "not carried over?\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_1340")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 5)), scpexpr(EXPR_END)), "loc_136D")

    AnonymousTalk(    #39
        (
            "Status\x01",
            "has been carried over!\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Jump("loc_138B")

    label("loc_136D")


    AnonymousTalk(    #40
        (
            "Status\x01",
            "not carried over?\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_138B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 6)), scpexpr(EXPR_END)), "loc_13B6")

    AnonymousTalk(    #41
        (
            "Mira\x01",
            "has been carried over!\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Jump("loc_13D2")

    label("loc_13B6")


    AnonymousTalk(    #42
        (
            "Mira\x01",
            "not carried over?\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_13D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 4)), scpexpr(EXPR_END)), "loc_1401")

    AnonymousTalk(    #43
        (
            "Notebook\x01",
            "has been carried over!\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Jump("loc_1421")

    label("loc_1401")


    AnonymousTalk(    #44
        (
            "Notebook\x01",
            "not carried over?\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_1421")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x208, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_40(0x35C, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1469")

    AnonymousTalk(    #45
        (
            "FC Clear Data\x01",
            "has been carried over!\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Jump("loc_148E")

    label("loc_1469")


    AnonymousTalk(    #46
        (
            "FC Clear Data\x01",
            "not carried over?\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_148E")

    Return()

    # Function_12_129D end

    def Function_13_148F(): pass

    label("Function_13_148F")

    EventBegin(0x0)
    OP_5F(0x0)
    OP_5F(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1578")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x455, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_150F")

    AnonymousTalk(    #47
        (
            "SC Clear Data\x01",
            "not carried over?\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #48
        (
            "Since it's Chapter 8,\x01",
            "opening Chapter 8 Casino Shop.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_A9(0x6C)
    Jump("loc_1575")

    label("loc_150F")


    AnonymousTalk(    #49
        (
            "SC Clear Data\x01",
            "has been carried over!\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #50
        (
            "Since it's Chapter 8,\x01",
            "opening Chapter 8 Casino Shop.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_A9(0x80)

    label("loc_1575")

    Jump("loc_1652")

    label("loc_1578")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x455, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15E8")

    AnonymousTalk(    #51
        (
            "SC Clear Data\x01",
            "not carried over?\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #52
        (
            "Since it's not Chapter 8,\x01",
            "opening Chapter 1 Casino Shop.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_A9(0x69)
    Jump("loc_1652")

    label("loc_15E8")


    AnonymousTalk(    #53
        (
            "SC Clear Data\x01",
            "has been carried over!\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #54
        (
            "Since it's not Chapter 8,\x01",
            "opening Chapter 1 Casino Shop.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_A9(0x7D)

    label("loc_1652")

    Return()

    # Function_13_148F end

    def Function_14_1653(): pass

    label("Function_14_1653")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1914")

    Menu(
        1,
        10,
        100,
        1,
        (
            "Equipment\x01",          # 0
            "Items\x01",              # 1
            "Status\x01",             # 2
            "Mira\x01",               # 3
            "Notebook\x01",           # 4
            "FC Clear Data\x01",      # 5
            "Cancel\x01",             # 6
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_5F(0x1)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_16CD"),
        (1, "loc_172B"),
        (2, "loc_1782"),
        (3, "loc_17DA"),
        (4, "loc_182E"),
        (5, "loc_188A"),
        (SWITCH_DEFAULT, "loc_1904"),
    )


    label("loc_16CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 2)), scpexpr(EXPR_END)), "loc_16FD")

    AnonymousTalk(    #55
        (
            "Equipment\x01",
            "has been carried over!\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Jump("loc_171E")

    label("loc_16FD")


    AnonymousTalk(    #56
        (
            "Equipment\x01",
            "not carried over?\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_171E")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1911")

    label("loc_172B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 3)), scpexpr(EXPR_END)), "loc_1758")

    AnonymousTalk(    #57
        (
            "Items\x01",
            "have been carried over!\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Jump("loc_1775")

    label("loc_1758")


    AnonymousTalk(    #58
        (
            "Items\x01",
            "not carried over?\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_1775")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1911")

    label("loc_1782")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 5)), scpexpr(EXPR_END)), "loc_17AF")

    AnonymousTalk(    #59
        (
            "Status\x01",
            "has been carried over!\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Jump("loc_17CD")

    label("loc_17AF")


    AnonymousTalk(    #60
        (
            "Status\x01",
            "not carried over?\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_17CD")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1911")

    label("loc_17DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 6)), scpexpr(EXPR_END)), "loc_1805")

    AnonymousTalk(    #61
        (
            "Mira\x01",
            "has been carried over!\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Jump("loc_1821")

    label("loc_1805")


    AnonymousTalk(    #62
        (
            "Mira\x01",
            "not carried over?\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_1821")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1911")

    label("loc_182E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 4)), scpexpr(EXPR_END)), "loc_185D")

    AnonymousTalk(    #63
        (
            "Notebook\x01",
            "has been carried over!\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Jump("loc_187D")

    label("loc_185D")


    AnonymousTalk(    #64
        (
            "Notebook\x01",
            "not carried over?\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_187D")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1911")

    label("loc_188A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x208, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_40(0x35C, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_18D2")

    AnonymousTalk(    #65
        (
            "FC Clear Data\x01",
            "has been carried over!\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Jump("loc_18F7")

    label("loc_18D2")


    AnonymousTalk(    #66
        (
            "FC Clear Data\x01",
            "not carried over?\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_18F7")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1911")

    label("loc_1904")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1911")

    label("loc_1911")

    Jump("Function_14_1653")

    label("loc_1914")

    Return()

    # Function_14_1653 end

    def Function_15_1915(): pass

    label("Function_15_1915")


    AnonymousTalk(    #67
        "\x06テストマップを選んでくださいよ。\x02",
    )


    label("loc_1939")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1A69")

    Menu(
        1,
        10,
        100,
        1,
        (
            "Test Map 20\x01",      # 0
            "Test Map 21\x01",      # 1
            "Test Map 22\x01",      # 2
            "Test Map 23\x01",      # 3
            "Test Map 24\x01",      # 4
            "Test Map 25\x01",      # 5
            "Test Map 26\x01",      # 6
            "Test Map 27\x01",      # 7
            "Test Map 28\x01",      # 8
            "Test Map 29\x01",      # 9
            "Cancel\x01",           # 10
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1A02"),
        (1, "loc_1A0B"),
        (2, "loc_1A14"),
        (3, "loc_1A1D"),
        (4, "loc_1A26"),
        (5, "loc_1A2F"),
        (6, "loc_1A38"),
        (7, "loc_1A41"),
        (8, "loc_1A4A"),
        (9, "loc_1A53"),
        (SWITCH_DEFAULT, "loc_1A5C"),
    )


    label("loc_1A02")

    NewScene("ED6_DT21/T0020   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_1A0B")

    NewScene("ED6_DT21/T0021   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_1A14")

    NewScene("ED6_DT21/T0022   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_1A1D")

    NewScene("ED6_DT21/T0023   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_1A26")

    NewScene("ED6_DT21/T0024   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_1A2F")

    NewScene("ED6_DT21/T0025   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_1A38")

    NewScene("ED6_DT21/T0026   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_1A41")

    NewScene("ED6_DT21/T0027   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_1A4A")

    NewScene("ED6_DT21/T0028   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_1A53")

    NewScene("ED6_DT21/T0029   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_1A5C")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1939")

    label("loc_1A69")

    OP_5F(0x1)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_15_1915 end

    def Function_16_1A79(): pass

    label("Function_16_1A79")


    AnonymousTalk(    #68
        "\x06Which?\x02",
    )


    label("loc_1A83")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1AED")

    Menu(
        1,
        10,
        100,
        1,
        (
            "Map Object 1\x01",      # 0
            "Map Object 2\x01",      # 1
            "Cancel\x01",            # 2
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1ACE"),
        (1, "loc_1AD7"),
        (SWITCH_DEFAULT, "loc_1AE0"),
    )


    label("loc_1ACE")

    NewScene("ED6_DT21/T0070   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_1AD7")

    NewScene("ED6_DT21/T0071   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_1AE0")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1A83")

    label("loc_1AED")

    OP_5F(0x1)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_16_1A79 end

    def Function_17_1AFD(): pass

    label("Function_17_1AFD")

    OP_6B(5000, 3000)
    Call(0, 18)
    Return()

    # Function_17_1AFD end

    def Function_18_1B0B(): pass

    label("Function_18_1B0B")

    OP_6C(0, 20000)
    Return()

    # Function_18_1B0B end

    def Function_19_1B15(): pass

    label("Function_19_1B15")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x13), scpexpr(EXPR_PUSH_LONG, 0x382), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B6A")
    EventBegin(0x0)
    OP_C2()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CD(0x9)"), scpexpr(EXPR_END)), "loc_1B4B")
    Sleep(1000)
    OP_62(0x0, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Jump("loc_1B65")

    label("loc_1B4B")


    AnonymousTalk(    #69
        "There's no reaction.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_1B65")

    EventEnd(0x0)
    Jump("loc_1B8C")

    label("loc_1B6A")


    AnonymousTalk(    #70
        "Nothing happened. (ByScript)\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_1B8C")

    Return()

    # Function_19_1B15 end

    def Function_20_1B8D(): pass

    label("Function_20_1B8D")


    ChrTalk(    #71
        0x0,
        "Welcome to the Factory!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_A9(0x0)
    Return()

    # Function_20_1B8D end

    def Function_21_1BAF(): pass

    label("Function_21_1BAF")

    SetChrName("Sara")

    AnonymousTalk(    #72
        "\x06Which shop?\x02",
    )


    Menu(
        1,
        10,
        100,
        1,
        (
            "Factory\x01",              # 0
            "Weapon Shop\x01",          # 1
            "Tool Shop\x01",            # 2
            "Inn\x01",                  # 3
            "Guild\x01",                # 4
            "Read Book\x01",            # 5
            "Casino Exchange\x01",      # 6
            "Cancel\x01",               # 7
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_5F(0x1)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1C46"),
        (1, "loc_1C4D"),
        (2, "loc_1C54"),
        (3, "loc_1C5B"),
        (4, "loc_1C62"),
        (5, "loc_1C69"),
        (6, "loc_1C71"),
        (SWITCH_DEFAULT, "loc_1C78"),
    )


    label("loc_1C46")

    Call(0, 20)
    Jump("loc_1C7B")

    label("loc_1C4D")

    Call(0, 22)
    Jump("loc_1C7B")

    label("loc_1C54")

    Call(0, 23)
    Jump("loc_1C7B")

    label("loc_1C5B")

    Call(0, 24)
    Jump("loc_1C7B")

    label("loc_1C62")

    Call(0, 25)
    Jump("loc_1C7B")

    label("loc_1C69")

    OP_B8(0x347, 0x0)
    Jump("loc_1C7B")

    label("loc_1C71")

    Call(0, 26)
    Jump("loc_1C7B")

    label("loc_1C78")

    Jump("loc_1C7B")

    label("loc_1C7B")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_21_1BAF end

    def Function_22_1C86(): pass

    label("Function_22_1C86")


    ChrTalk(    #73
        0x0,
        "Welcome to the Weapon Shop!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_A9(0x1)
    Return()

    # Function_22_1C86 end

    def Function_23_1CAC(): pass

    label("Function_23_1CAC")


    ChrTalk(    #74
        0x0,
        "Welcome to the Item Shop!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_A9(0x2)
    Return()

    # Function_23_1CAC end

    def Function_24_1CD0(): pass

    label("Function_24_1CD0")


    ChrTalk(    #75
        0x0,
        "Welcome to the Inn!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_A9(0x5)
    Return()

    # Function_24_1CD0 end

    def Function_25_1CEE(): pass

    label("Function_25_1CEE")


    ChrTalk(    #76
        0x0,
        "Welcome to the guild!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_2A(0x65, 0x66, 0x1, 0xFFFF)
    Return()

    # Function_25_1CEE end

    def Function_26_1D15(): pass

    label("Function_26_1D15")


    ChrTalk(    #77
        0x0,
        "This is the exchange.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_A9(0x69)
    Return()

    # Function_26_1D15 end

    def Function_27_1D35(): pass

    label("Function_27_1D35")

    FadeToDark(0, 0, -1)
    ClearParty()
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
            "Set Scherazade as Partner\x01",      # 0
            "Set Agate as Partner\x01",           # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1DB2"),
        (1, "loc_1DB8"),
        (SWITCH_DEFAULT, "loc_1DBE"),
    )


    label("loc_1DB2")

    OP_A2(0x1200)
    Jump("loc_1DBE")

    label("loc_1DB8")

    OP_A2(0x1201)
    Jump("loc_1DBE")

    label("loc_1DBE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_1DDC")

    AnonymousTalk(    #78
        "ほげっちゃ\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    AddParty(0x2, 0xF7, 0xFF)
    Jump("loc_1DE0")

    label("loc_1DDC")

    AddParty(0x5, 0xF7, 0xFF)

    label("loc_1DE0")

    Return()

    # Function_27_1D35 end

    def Function_28_1DE1(): pass

    label("Function_28_1DE1")

    ClearMapFlags(0x1)
    OP_6D(106730, -1920, 53920, 0)
    Sleep(100)
    OP_C9(0x0, 0x4, 0x0, 0xFF, 0xFF, 0xFF, 0x1, 0x2, 0x3, 0x4, 0x5, 0x6, 0x7, 0x8, 0x9, 0xD, 0xA, 0xF, 0xE, 0xB, 0xC, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Sleep(1000)
    Return()

    # Function_28_1DE1 end

    SaveToFile()

Try(main)
