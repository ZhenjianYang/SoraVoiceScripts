from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 柏斯

    CreateScenaFile(
        FileName            = 'C1215   ._SN',
        MapName             = 'Bose',
        Location            = 'C1215.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60033",
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
        'ED6_DT09/CH10410 ._CH',             # 00
        'ED6_DT09/CH10411 ._CH',             # 01
        'ED6_DT09/CH10420 ._CH',             # 02
        'ED6_DT09/CH10421 ._CH',             # 03
        'ED6_DT09/CH10430 ._CH',             # 04
        'ED6_DT09/CH10431 ._CH',             # 05
        'ED6_DT09/CH10440 ._CH',             # 06
        'ED6_DT09/CH10441 ._CH',             # 07
        'ED6_DT29/CH12500 ._CH',             # 08
    )

    AddCharChipPat(
        'ED6_DT09/CH10410P._CP',             # 00
        'ED6_DT09/CH10411P._CP',             # 01
        'ED6_DT09/CH10420P._CP',             # 02
        'ED6_DT09/CH10421P._CP',             # 03
        'ED6_DT09/CH10430P._CP',             # 04
        'ED6_DT09/CH10431P._CP',             # 05
        'ED6_DT09/CH10440P._CP',             # 06
        'ED6_DT09/CH10441P._CP',             # 07
        'ED6_DT29/CH12500P._CP',             # 08
    )

    DeclNpc(
        X                   = -8890,
        Z                   = 1000,
        Y                   = 8860,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -60,
        Z                   = 0,
        Y                   = -18410,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclMonster(
        X                   = -30,
        Z                   = 0,
        Y                   = 17960,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x8F,
        Unknown_18          = 7083,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -60,
        Z                   = 0,
        Y                   = -6100,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x8F,
        Unknown_18          = 7084,
        Unknown_1A          = 0,
    )


    DeclActor(
        TriggerX            = 11840,
        TriggerZ            = 0,
        TriggerY            = 40,
        TriggerRange        = 1000,
        ActorX              = 12620,
        ActorZ              = 0,
        ActorY              = 60,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -11810,
        TriggerZ            = 0,
        TriggerY            = -40,
        TriggerRange        = 1000,
        ActorX              = -12660,
        ActorZ              = 0,
        ActorY              = 90,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -8390,
        TriggerZ            = 0,
        TriggerY            = 8360,
        TriggerRange        = 1000,
        ActorX              = -8890,
        ActorZ              = 0,
        ActorY              = 8860,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 8290,
        TriggerZ            = 0,
        TriggerY            = 8360,
        TriggerRange        = 1000,
        ActorX              = 8750,
        ActorZ              = 0,
        ActorY              = 8820,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_1FA",          # 00, 0
        "Function_1_1FB",          # 01, 1
        "Function_2_278",          # 02, 2
        "Function_3_28E",          # 03, 3
        "Function_4_41D",          # 04, 4
        "Function_5_5B4",          # 05, 5
        "Function_6_7D3",          # 06, 6
    )


    def Function_0_1FA(): pass

    label("Function_0_1FA")

    Return()

    # Function_0_1FA end

    def Function_1_1FB(): pass

    label("Function_1_1FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x36C, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_20D")
    OP_6F(0x0, 0)
    Jump("loc_214")

    label("loc_20D")

    OP_6F(0x0, 60)

    label("loc_214")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x36D, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_226")
    OP_6F(0x1, 0)
    Jump("loc_22D")

    label("loc_226")

    OP_6F(0x1, 60)

    label("loc_22D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x36D, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_23F")
    OP_6F(0x2, 0)
    Jump("loc_246")

    label("loc_23F")

    OP_6F(0x2, 60)

    label("loc_246")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x36D, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_258")
    OP_6F(0x3, 0)
    Jump("loc_25F")

    label("loc_258")

    OP_6F(0x3, 60)

    label("loc_25F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x375, 3)), scpexpr(EXPR_END)), "loc_26B")
    SetChrFlags(0xA, 0x80)

    label("loc_26B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x375, 4)), scpexpr(EXPR_END)), "loc_277")
    SetChrFlags(0xB, 0x80)

    label("loc_277")

    Return()

    # Function_1_1FB end

    def Function_2_278(): pass

    label("Function_2_278")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_28D")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_278")

    label("loc_28D")

    Return()

    # Function_2_278 end

    def Function_3_28E(): pass

    label("Function_3_28E")

    OP_EA(0x2, 0x43, 0x0, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x36C, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_366")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x0, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x185, 1)"), scpexpr(EXPR_END)), "loc_2FF")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "Found \x1F\x85\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1B67)
    Jump("loc_363")

    label("loc_2FF")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "Found \x1F\x85\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\x85\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x0, 60)
    OP_70(0x0, 0x0)

    label("loc_363")

    Jump("loc_40F")

    label("loc_366")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        (
            "\x07\x05You sneakily crack the lid of the chest and take\x01",
            "a peek inside. Sadly, no treasure chest fairies\x01",
            "flying around in there. No items, either.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_40F")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_28E end

    def Function_4_41D(): pass

    label("Function_4_41D")

    OP_EA(0x2, 0x44, 0x0, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x36D, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4F5")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x153, 1)"), scpexpr(EXPR_END)), "loc_48E")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #3
        "Found \x1F\x53\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1B69)
    Jump("loc_4F2")

    label("loc_48E")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #4
        (
            "Found \x1F\x53\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\x53\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x1, 60)
    OP_70(0x1, 0x0)

    label("loc_4F2")

    Jump("loc_5A6")

    label("loc_4F5")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #5
        (
            "\x07\x05This chest may not have anything in the way of\x01",
            "riches or possessions, but it's filled to the brim\x01",
            "with hope for the future and love for the world.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_5A6")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_41D end

    def Function_5_5B4(): pass

    label("Function_5_5B4")

    OP_EA(0x2, 0x45, 0x0, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x36D, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_74F")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x36D, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_69E")
    OP_9F(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    TurnDirection(0x8, 0x0, 0)
    OP_91(0x8, 0x0, 0x3E8, 0x0, 0x0, 0x0)

    def lambda_60B():
        OP_91(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x258, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_60B)

    def lambda_626():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x258)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_626)
    ClearChrFlags(0x8, 0x80)

    AnonymousTalk(    #6
        "\x07\x05Monsters appeared!\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Battle(0x92, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0x8, 0x80)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_679"),
        (2, "loc_68B"),
        (1, "loc_69B"),
        (SWITCH_DEFAULT, "loc_69E"),
    )


    label("loc_679")

    OP_A2(0x1B6C)
    OP_6F(0x2, 60)
    Sleep(500)
    Jump("loc_69E")

    label("loc_68B")

    OP_6F(0x2, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_69B")

    OP_B4(0x0)
    Return()

    label("loc_69E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x17B, 1)"), scpexpr(EXPR_END)), "loc_6EA")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #7
        "Found \x1F\x7B\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1B6B)
    Jump("loc_74C")

    label("loc_6EA")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #8
        (
            "Found \x1F\x7B\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\x7B\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x2, 60)
    OP_70(0x2, 0x0)

    label("loc_74C")

    Jump("loc_7C5")

    label("loc_74F")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #9
        (
            "\x07\x05You kick the chest open, but all you get for your\x01",
            "talented footwork is a stubbed toe. Ow.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_7C5")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_5B4 end

    def Function_6_7D3(): pass

    label("Function_6_7D3")

    OP_EA(0x2, 0x46, 0x0, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x36D, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8AB")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x3, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x145, 1)"), scpexpr(EXPR_END)), "loc_844")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #10
        "Found \x1F\x45\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1B6D)
    Jump("loc_8A8")

    label("loc_844")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #11
        (
            "Found \x1F\x45\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\x45\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x3, 60)
    OP_70(0x3, 0x0)

    label("loc_8A8")

    Jump("loc_947")

    label("loc_8AB")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #12
        (
            "\x07\x05Let's take all the typos we accidentally left in\x01",
            "this game at launch and shove them all in here.\x01",
            "Pretend they never happened.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_947")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_7D3 end

    SaveToFile()

Try(main)
