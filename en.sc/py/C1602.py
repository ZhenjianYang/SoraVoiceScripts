from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'C1602   ._SN',
        MapName             = 'Bose',
        Location            = 'C1602.x',
        MapIndex            = 250,
        MapDefaultBGM       = "ed60125",
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
        '',                                     # 17
        '',                                     # 18
        '',                                     # 19
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
        'ED6_DT29/CH12450 ._CH',             # 00
        'ED6_DT29/CH12451 ._CH',             # 01
        'ED6_DT09/CH10840 ._CH',             # 02
        'ED6_DT09/CH10841 ._CH',             # 03
        'ED6_DT29/CH12460 ._CH',             # 04
        'ED6_DT29/CH12461 ._CH',             # 05
        'ED6_DT09/CH10550 ._CH',             # 06
        'ED6_DT09/CH10551 ._CH',             # 07
        'ED6_DT29/CH12500 ._CH',             # 08
        'ED6_DT29/CH12501 ._CH',             # 09
        'ED6_DT29/CH12560 ._CH',             # 0A
        'ED6_DT29/CH12561 ._CH',             # 0B
    )

    AddCharChipPat(
        'ED6_DT29/CH12450P._CP',             # 00
        'ED6_DT29/CH12451P._CP',             # 01
        'ED6_DT09/CH10840P._CP',             # 02
        'ED6_DT09/CH10841P._CP',             # 03
        'ED6_DT29/CH12460P._CP',             # 04
        'ED6_DT29/CH12461P._CP',             # 05
        'ED6_DT09/CH10550P._CP',             # 06
        'ED6_DT09/CH10551P._CP',             # 07
        'ED6_DT29/CH12500P._CP',             # 08
        'ED6_DT29/CH12501P._CP',             # 09
        'ED6_DT29/CH12560P._CP',             # 0A
        'ED6_DT29/CH12561P._CP',             # 0B
    )

    DeclMonster(
        X                   = 33560,
        Z                   = 0,
        Y                   = -17800,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3C6,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 9220,
        Z                   = -1000,
        Y                   = -5220,
        Unknown_0C          = 180,
        Unknown_0E          = 10,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3C8,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 10130,
        Z                   = 0,
        Y                   = 41950,
        Unknown_0C          = 180,
        Unknown_0E          = 8,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3C7,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -31690,
        Z                   = 0,
        Y                   = 17530,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3C6,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -22920,
        Z                   = -1000,
        Y                   = 3720,
        Unknown_0C          = 180,
        Unknown_0E          = 8,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3C7,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -17070,
        Z                   = -500,
        Y                   = -6360,
        Unknown_0C          = 180,
        Unknown_0E          = 10,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3C8,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 159370,
        Z                   = 0,
        Y                   = -1020,
        Unknown_0C          = 180,
        Unknown_0E          = 8,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3C7,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 184150,
        Z                   = -500,
        Y                   = -2380,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3C3,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 186100,
        Z                   = 0,
        Y                   = 12660,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3C3,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 209310,
        Z                   = 0,
        Y                   = -1090,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3C6,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 230690,
        Z                   = -500,
        Y                   = -3880,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3C3,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclActor(
        TriggerX            = 16510,
        TriggerZ            = 0,
        TriggerY            = 40840,
        TriggerRange        = 1000,
        ActorX              = 17170,
        ActorZ              = 0,
        ActorY              = 40840,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 245230,
        TriggerZ            = 0,
        TriggerY            = 25460,
        TriggerRange        = 1000,
        ActorX              = 245680,
        ActorZ              = 0,
        ActorY              = 25970,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 9970,
        TriggerZ            = 0,
        TriggerY            = 48740,
        TriggerRange        = 1000,
        ActorX              = 10010,
        ActorZ              = 0,
        ActorY              = 49440,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -16170,
        TriggerZ            = 0,
        TriggerY            = 17900,
        TriggerRange        = 1000,
        ActorX              = -15800,
        ActorZ              = 0,
        ActorY              = 18460,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_2CE",          # 00, 0
        "Function_1_2DF",          # 01, 1
        "Function_2_3CD",          # 02, 2
        "Function_3_54A",          # 03, 3
        "Function_4_658",          # 04, 4
        "Function_5_7C1",          # 05, 5
    )


    def Function_0_2CE(): pass

    label("Function_0_2CE")

    OP_11(0xFF, 0xFF, 0xFF, 0x9C40, 0x12110, 0x0)
    Return()

    # Function_0_2CE end

    def Function_1_2DF(): pass

    label("Function_1_2DF")

    OP_22(0x1C7, 0x0, 0x64)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x372, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F6")
    OP_6F(0x0, 0)
    Jump("loc_2FD")

    label("loc_2F6")

    OP_6F(0x0, 60)

    label("loc_2FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x372, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_30F")
    OP_6F(0x1, 0)
    Jump("loc_316")

    label("loc_30F")

    OP_6F(0x1, 60)

    label("loc_316")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x372, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_328")
    OP_6F(0x2, 0)
    Jump("loc_32F")

    label("loc_328")

    OP_6F(0x2, 60)

    label("loc_32F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x372, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_341")
    OP_6F(0x3, 0)
    Jump("loc_348")

    label("loc_341")

    OP_6F(0x3, 60)

    label("loc_348")

    OP_51(0x9, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xA, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xC, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xD, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xE, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xF, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x12, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3C2")
    OP_4F(0x2A, (scpexpr(EXPR_PUSH_LONG, 0x578), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3CC")

    label("loc_3C2")

    OP_4F(0x2A, (scpexpr(EXPR_PUSH_LONG, 0x12C), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3CC")

    Return()

    # Function_1_2DF end

    def Function_2_3CD(): pass

    label("Function_2_3CD")

    OP_EA(0x2, 0x63, 0x0, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x372, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4A5")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x0, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x8B, 1)"), scpexpr(EXPR_END)), "loc_43E")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "Found \x1F\x8B\x00\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1B90)
    Jump("loc_4A2")

    label("loc_43E")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "Found \x1F\x8B\x00\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\x8B\x00\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x0, 60)
    OP_70(0x0, 0x0)

    label("loc_4A2")

    Jump("loc_53C")

    label("loc_4A5")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        (
            "\x07\x05It's empty, but if you planted a seed and kept\x01",
            "coming back to water it, you might be able to\x01",
            "grow a potato or something.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_53C")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_3CD end

    def Function_3_54A(): pass

    label("Function_3_54A")

    OP_EA(0x2, 0x64, 0x0, 0x0)
    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x372, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5E0")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1, 0x1E)
    OP_73(0x1)
    OP_6F(0x1, 30)
    AddSepith(0x0, 0x64)
    AddSepith(0x6, 0x64)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #3
        (
            "Found\x01",
            "#2C#56IEarth Sepith x100\x01",
            "#61IMirage Sepith x100#0C.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x1B92)
    Jump("loc_646")

    label("loc_5E0")


    AnonymousTalk(    #4
        (
            "\x07\x05If you're reading this, please send help.\x01",
            "We've been stuck on this game for years... -Loc Team\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_646")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_54A end

    def Function_4_658(): pass

    label("Function_4_658")

    OP_EA(0x2, 0x65, 0x0, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x372, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_730")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FE, 1)"), scpexpr(EXPR_END)), "loc_6C9")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #5
        "Found \x1F\xFE\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1B94)
    Jump("loc_72D")

    label("loc_6C9")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #6
        (
            "Found \x1F\xFE\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\xFE\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x2, 60)
    OP_70(0x2, 0x0)

    label("loc_72D")

    Jump("loc_7B3")

    label("loc_730")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #7
        (
            "\x07\x05Psychically sensing that there's nothing inside,\x01",
            "you walk away from the chest without disturbing\x01",
            "it.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_7B3")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_658 end

    def Function_5_7C1(): pass

    label("Function_5_7C1")

    OP_EA(0x2, 0x66, 0x0, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x372, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_899")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x3, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1E3, 1)"), scpexpr(EXPR_END)), "loc_832")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #8
        "Found \x1F\xE3\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1B95)
    Jump("loc_896")

    label("loc_832")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #9
        (
            "Found \x1F\xE3\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\xE3\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x3, 60)
    OP_70(0x3, 0x0)

    label("loc_896")

    Jump("loc_8D7")

    label("loc_899")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #10
        "\x07\x05I... I GUESS you can keep it...\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_8D7")

    Sleep(30)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x20D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_95D")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_AC(0x30)"), scpexpr(EXPR_END)), "loc_8F6")
    Jump("loc_95D")

    label("loc_8F6")


    AnonymousTalk(    #11
        (
            "\x07\x00Found a scrap of paper with a [ #483i ]\x01",
            "recipe written on it.\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #12
        "\x07\x00Learned [ #483i ] recipe.\x02",
    )

    CloseMessageWindow()

    label("loc_95D")

    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_7C1 end

    SaveToFile()

Try(main)
