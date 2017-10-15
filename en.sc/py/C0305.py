from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'C0305   ._SN',
        MapName             = 'Rolent',
        Location            = 'C0305.x',
        MapIndex            = 19,
        MapDefaultBGM       = "ed60021",
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
        '',                                     # 9
        '',                                     # 10
        '',                                     # 11
        '',                                     # 12
        '',                                     # 13
        '',                                     # 14
        '',                                     # 15
        '',                                     # 16
    )

    DeclEntryPoint(
        Unknown_00              = 35000,
        Unknown_04              = 0,
        Unknown_08              = 16000,
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
        Unknown_3A              = 19,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT29/CH12430 ._CH',             # 00
        'ED6_DT29/CH12431 ._CH',             # 01
        'ED6_DT09/CH10010 ._CH',             # 02
        'ED6_DT09/CH10011 ._CH',             # 03
        'ED6_DT09/CH10280 ._CH',             # 04
        'ED6_DT09/CH10281 ._CH',             # 05
        'ED6_DT29/CH12400 ._CH',             # 06
        'ED6_DT29/CH12401 ._CH',             # 07
    )

    AddCharChipPat(
        'ED6_DT29/CH12430P._CP',             # 00
        'ED6_DT29/CH12431P._CP',             # 01
        'ED6_DT09/CH10010P._CP',             # 02
        'ED6_DT09/CH10011P._CP',             # 03
        'ED6_DT09/CH10280P._CP',             # 04
        'ED6_DT09/CH10281P._CP',             # 05
        'ED6_DT29/CH12400P._CP',             # 06
        'ED6_DT29/CH12401P._CP',             # 07
    )

    DeclMonster(
        X                   = 6930,
        Z                   = 40,
        Y                   = -26770,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3E,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -5350,
        Z                   = -180,
        Y                   = -27890,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3F,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -15690,
        Z                   = -310,
        Y                   = 1410,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3E,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -3030,
        Z                   = 410,
        Y                   = 24850,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3F,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 6930,
        Z                   = 40,
        Y                   = -26770,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x40,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -5350,
        Z                   = -180,
        Y                   = -27890,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x41,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -15690,
        Z                   = -310,
        Y                   = 1410,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x42,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -3030,
        Z                   = 410,
        Y                   = 24850,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x41,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclActor(
        TriggerX            = -14410,
        TriggerZ            = -120,
        TriggerY            = 8350,
        TriggerRange        = 1000,
        ActorX              = -14410,
        ActorZ              = -120,
        ActorY              = 9060,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -22500,
        TriggerZ            = -150,
        TriggerY            = 35130,
        TriggerRange        = 1000,
        ActorX              = -22500,
        ActorZ              = -150,
        ActorY              = 35720,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 18070,
        TriggerZ            = -120,
        TriggerY            = 17440,
        TriggerRange        = 1000,
        ActorX              = 18470,
        ActorZ              = -120,
        ActorY              = 17840,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -9770,
        TriggerZ            = -170,
        TriggerY            = 41560,
        TriggerRange        = 1800,
        ActorX              = -9770,
        ActorZ              = 1200,
        ActorY              = 41560,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_25A",          # 00, 0
        "Function_1_25B",          # 01, 1
        "Function_2_356",          # 02, 2
        "Function_3_49C",          # 03, 3
        "Function_4_5F2",          # 04, 4
        "Function_5_77D",          # 05, 5
    )


    def Function_0_25A(): pass

    label("Function_0_25A")

    Return()

    # Function_0_25A end

    def Function_1_25B(): pass

    label("Function_1_25B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x316, 0)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_26A")
    OP_64(0x3, 0x1)

    label("loc_26A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x32C, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_27C")
    OP_6F(0x4, 0)
    Jump("loc_283")

    label("loc_27C")

    OP_6F(0x4, 60)

    label("loc_283")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x32C, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_295")
    OP_6F(0x5, 0)
    Jump("loc_29C")

    label("loc_295")

    OP_6F(0x5, 60)

    label("loc_29C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x32C, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2AE")
    OP_6F(0x6, 0)
    Jump("loc_2B5")

    label("loc_2AE")

    OP_6F(0x6, 60)

    label("loc_2B5")

    OP_51(0xC, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xD, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xE, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xF, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 4)), scpexpr(EXPR_END)), "loc_2FF")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    Jump("loc_313")

    label("loc_2FF")

    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)

    label("loc_313")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_341")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 4)), scpexpr(EXPR_END)), "loc_341")
    SetMapFlags(0x10)
    OP_11(0xE6, 0xF0, 0xFF, 0x0, 0xEA60, 0x0)
    OP_C4(0x0, 0x4)

    label("loc_341")

    OP_71(0x0, 0x4)
    OP_71(0x1, 0x4)
    OP_71(0x2, 0x4)
    OP_71(0x3, 0x4)
    Return()

    # Function_1_25B end

    def Function_2_356(): pass

    label("Function_2_356")

    OP_EA(0x2, 0x2, 0x0, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x32C, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_42E")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x4, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x4D, 1)"), scpexpr(EXPR_END)), "loc_3C7")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "Found \x1F\x4D\x00\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1961)
    Jump("loc_42B")

    label("loc_3C7")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "Found \x1F\x4D\x00\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\x4D\x00\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x4, 60)
    OP_70(0x4, 0x0)

    label("loc_42B")

    Jump("loc_48E")

    label("loc_42E")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        (
            "\x07\x05This chest is completely empty, and yet\x01",
            "somehow it seems content.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_48E")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_356 end

    def Function_3_49C(): pass

    label("Function_3_49C")

    OP_EA(0x2, 0x3, 0x0, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x32C, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_574")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x5, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x17A, 1)"), scpexpr(EXPR_END)), "loc_50D")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #3
        "Found \x1F\x7A\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1962)
    Jump("loc_571")

    label("loc_50D")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #4
        (
            "Found \x1F\x7A\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\x7A\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x5, 60)
    OP_70(0x5, 0x0)

    label("loc_571")

    Jump("loc_5E4")

    label("loc_574")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #5
        (
            "\x07\x05The chest is empty. Please come back tomorrow\x01",
            "at 9 AM sharp for your free refill.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_5E4")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_49C end

    def Function_4_5F2(): pass

    label("Function_4_5F2")

    OP_EA(0x2, 0x4, 0x0, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x32C, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6CA")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x6, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FD, 1)"), scpexpr(EXPR_END)), "loc_663")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #6
        "Found \x1F\xFD\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1964)
    Jump("loc_6C7")

    label("loc_663")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #7
        (
            "Found \x1F\xFD\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\xFD\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x6, 60)
    OP_70(0x6, 0x0)

    label("loc_6C7")

    Jump("loc_76F")

    label("loc_6CA")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #8
        (
            "\x07\x05There once was a chest who had something in\x01",
            "this world. Something to stand for, to care about.\x01",
            "I was that chest, before you RUINED me.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_76F")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_5F2 end

    def Function_5_77D(): pass

    label("Function_5_77D")

    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x103, -7530, -30, 39130, 315)
    SetChrPos(0x101, -8530, -80, 38500, 315)
    SetChrPos(0xF8, -7670, -50, 37260, 315)
    SetChrPos(0xF9, -6710, 30, 37730, 315)
    OP_6D(-7900, -60, 38750, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(0, 0)
    OP_6E(262, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #9
        0x101,
        "#1004F#6PHuh? Wait...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_85E")

    ChrTalk(    #10
        0x107,
        "#064FIs something wrong, Estelle?\x02",
    )

    CloseMessageWindow()
    Jump("loc_92C")

    label("loc_85E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_88E")

    ChrTalk(    #11
        0x105,
        "#044FEstelle? What is it?\x02",
    )

    CloseMessageWindow()
    Jump("loc_92C")

    label("loc_88E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8CA")

    ChrTalk(    #12
        0x104,
        "#033FEstelle? What furrows your brow?\x02",
    )

    CloseMessageWindow()
    Jump("loc_92C")

    label("loc_8CA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8FC")

    ChrTalk(    #13
        0x106,
        "#053FSomethin' up, Estelle?\x02",
    )

    CloseMessageWindow()
    Jump("loc_92C")

    label("loc_8FC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_92C")

    ChrTalk(    #14
        0x108,
        "#073FEstelle? You all right?\x02",
    )

    CloseMessageWindow()

    label("loc_92C")


    ChrTalk(    #15
        0x101,
        (
            "#1016F#6PAh, I'm fine! It's nothing.\x02\x03",

            "#1015F(Wasn't there a road here?\x01",
            "Maybe I'm just losing it.)\x02\x03",

            "(I could have sworn there was one...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x103,
        "#022F#6P...\x02",
    )

    CloseMessageWindow()
    OP_A2(0x18B0)
    OP_64(0x3, 0x1)
    EventEnd(0x0)
    Return()

    # Function_5_77D end

    SaveToFile()

Try(main)
