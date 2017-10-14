from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'C5501   ._SN',
        MapName             = 'Other',
        Location            = 'C5501.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60031",
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
        'ED6_DT29/CH12190 ._CH',             # 00
        'ED6_DT29/CH12191 ._CH',             # 01
        'ED6_DT29/CH12200 ._CH',             # 02
        'ED6_DT29/CH12201 ._CH',             # 03
        'ED6_DT29/CH12210 ._CH',             # 04
        'ED6_DT29/CH12211 ._CH',             # 05
        'ED6_DT29/CH12220 ._CH',             # 06
        'ED6_DT29/CH12221 ._CH',             # 07
    )

    AddCharChipPat(
        'ED6_DT29/CH12190P._CP',             # 00
        'ED6_DT29/CH12191P._CP',             # 01
        'ED6_DT29/CH12200P._CP',             # 02
        'ED6_DT29/CH12201P._CP',             # 03
        'ED6_DT29/CH12210P._CP',             # 04
        'ED6_DT29/CH12211P._CP',             # 05
        'ED6_DT29/CH12220P._CP',             # 06
        'ED6_DT29/CH12221P._CP',             # 07
    )

    DeclNpc(
        X                   = 53280,
        Z                   = -1000,
        Y                   = 81930,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclMonster(
        X                   = 15760,
        Z                   = 0,
        Y                   = 94290,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x387,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 64760,
        Z                   = 0,
        Y                   = 102650,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x388,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 48300,
        Z                   = 0,
        Y                   = 54110,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x387,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 56540,
        Z                   = 0,
        Y                   = 54200,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x388,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 26440,
        Z                   = -2000,
        Y                   = 80620,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x387,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 45680,
        Z                   = -2000,
        Y                   = 78160,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x387,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclActor(
        TriggerX            = 16750,
        TriggerZ            = 0,
        TriggerY            = 57710,
        TriggerRange        = 1700,
        ActorX              = 16750,
        ActorZ              = 2500,
        ActorY              = 57710,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 9,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 46510,
        TriggerZ            = 0,
        TriggerY            = 67900,
        TriggerRange        = 1700,
        ActorX              = 46510,
        ActorZ              = 2500,
        ActorY              = 67900,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 53050,
        TriggerZ            = 0,
        TriggerY            = 92420,
        TriggerRange        = 1700,
        ActorX              = 53050,
        ActorZ              = 2500,
        ActorY              = 92420,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 8,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 52570,
        TriggerZ            = -2000,
        TriggerY            = 81930,
        TriggerRange        = 1000,
        ActorX              = 53280,
        ActorZ              = -2000,
        ActorY              = 81930,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 57950,
        TriggerZ            = 0,
        TriggerY            = 48100,
        TriggerRange        = 1000,
        ActorX              = 58010,
        ActorZ              = 0,
        ActorY              = 47400,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 52950,
        TriggerZ            = 0,
        TriggerY            = 48100,
        TriggerRange        = 1000,
        ActorX              = 52990,
        ActorZ              = 0,
        ActorY              = 47400,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 47460,
        TriggerZ            = 0,
        TriggerY            = 48100,
        TriggerRange        = 1000,
        ActorX              = 47460,
        ActorZ              = 0,
        ActorY              = 47440,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_2AE",          # 00, 0
        "Function_1_2AF",          # 01, 1
        "Function_2_3A5",          # 02, 2
        "Function_3_3BB",          # 03, 3
        "Function_4_5A5",          # 04, 4
        "Function_5_6FA",          # 05, 5
        "Function_6_86D",          # 06, 6
        "Function_7_9A9",          # 07, 7
        "Function_8_BC0",          # 08, 8
        "Function_9_BF6",          # 09, 9
    )


    def Function_0_2AE(): pass

    label("Function_0_2AE")

    Return()

    # Function_0_2AE end

    def Function_1_2AF(): pass

    label("Function_1_2AF")

    OP_22(0x1C7, 0x0, 0x64)
    OP_72(0x0, 0x28)
    OP_72(0x1, 0x28)
    OP_72(0x2, 0x28)
    OP_72(0x3, 0x28)
    OP_72(0x4, 0x28)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x214, 4)), scpexpr(EXPR_END)), "loc_2E2")
    OP_6F(0x1, 120)
    OP_6F(0x2, 60)

    label("loc_2E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x214, 5)), scpexpr(EXPR_END)), "loc_2F7")
    OP_6F(0x1, 120)
    OP_6F(0x2, 160)

    label("loc_2F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x214, 6)), scpexpr(EXPR_END)), "loc_30C")
    OP_6F(0x0, 60)
    OP_6F(0x4, 260)

    label("loc_30C")

    OP_4F(0x2A, (scpexpr(EXPR_PUSH_LONG, 0x6D6), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x220, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_328")
    OP_6F(0x5, 0)
    Jump("loc_32F")

    label("loc_328")

    OP_6F(0x5, 60)

    label("loc_32F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x220, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_341")
    OP_6F(0x6, 0)
    Jump("loc_348")

    label("loc_341")

    OP_6F(0x6, 60)

    label("loc_348")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x220, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_35A")
    OP_6F(0x7, 0)
    Jump("loc_361")

    label("loc_35A")

    OP_6F(0x7, 60)

    label("loc_361")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x220, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_373")
    OP_6F(0x8, 0)
    Jump("loc_37A")

    label("loc_373")

    OP_6F(0x8, 60)

    label("loc_37A")

    OP_E0(0x6, 0x90, 0xE2, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x80, 0xBB, 0x0, 0x0)
    OP_E0(0x7, 0x8, 0xCF, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x80, 0xBB, 0x0, 0x0)
    OP_E0(0x8, 0x80, 0xBB, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x80, 0xBB, 0x0, 0x0)
    Return()

    # Function_1_2AF end

    def Function_2_3A5(): pass

    label("Function_2_3A5")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3BA")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_3A5")

    label("loc_3BA")

    Return()

    # Function_2_3A5 end

    def Function_3_3BB(): pass

    label("Function_3_3BB")

    OP_EA(0x2, 0x83, 0x1, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x220, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_556")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x5, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x220, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4A5")
    OP_9F(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    TurnDirection(0x8, 0x0, 0)
    OP_91(0x8, 0x0, 0x3E8, 0x0, 0x0, 0x0)

    def lambda_412():
        OP_91(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x258, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_412)

    def lambda_42D():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x258)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_42D)
    ClearChrFlags(0x8, 0x80)

    AnonymousTalk(    #0
        "\x07\x05Monsters appeared!\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Battle(0x391, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0x8, 0x80)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_480"),
        (2, "loc_492"),
        (1, "loc_4A2"),
        (SWITCH_DEFAULT, "loc_4A5"),
    )


    label("loc_480")

    OP_A2(0x1104)
    OP_6F(0x5, 60)
    Sleep(500)
    Jump("loc_4A5")

    label("loc_492")

    OP_6F(0x5, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_4A2")

    OP_B4(0x0)
    Return()

    label("loc_4A5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x145, 1)"), scpexpr(EXPR_END)), "loc_4F1")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #1
        "Found \x1F\x45\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1103)
    Jump("loc_553")

    label("loc_4F1")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #2
        (
            "Found \x1F\x45\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\x45\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x5, 60)
    OP_70(0x5, 0x0)

    label("loc_553")

    Jump("loc_597")

    label("loc_556")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #3
        "\x07\x05For Sale: Reviving Balm, never used.\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_597")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_3BB end

    def Function_4_5A5(): pass

    label("Function_4_5A5")

    OP_EA(0x2, 0x84, 0x1, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x220, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_67D")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x6, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1F5, 1)"), scpexpr(EXPR_END)), "loc_616")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #4
        "Found \x1F\xF5\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1105)
    Jump("loc_67A")

    label("loc_616")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #5
        (
            "Found \x1F\xF5\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\xF5\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x6, 60)
    OP_70(0x6, 0x0)

    label("loc_67A")

    Jump("loc_6EC")

    label("loc_67D")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #6
        (
            "\x07\x05You open the chest to the familiar sight of\x01",
            "nothing. Oh, how you've missed this!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_6EC")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_5A5 end

    def Function_5_6FA(): pass

    label("Function_5_6FA")

    OP_EA(0x2, 0x85, 0x1, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x220, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7D2")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x7, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FC, 1)"), scpexpr(EXPR_END)), "loc_76B")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #7
        "Found \x1F\xFC\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1106)
    Jump("loc_7CF")

    label("loc_76B")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #8
        (
            "Found \x1F\xFC\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\xFC\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x7, 60)
    OP_70(0x7, 0x0)

    label("loc_7CF")

    Jump("loc_85F")

    label("loc_7D2")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #9
        (
            "\x07\x05Oh, sure. Just take it! My name's Sven, by the\x01",
            "way. I bet asking my name never even crossed\x01",
            "your mind, did it?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_85F")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_6FA end

    def Function_6_86D(): pass

    label("Function_6_86D")

    OP_EA(0x2, 0x86, 0x1, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x220, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_945")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x8, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FE, 1)"), scpexpr(EXPR_END)), "loc_8DE")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #10
        "Found \x1F\xFE\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1107)
    Jump("loc_942")

    label("loc_8DE")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #11
        (
            "Found \x1F\xFE\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\xFE\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x8, 60)
    OP_70(0x8, 0x0)

    label("loc_942")

    Jump("loc_99B")

    label("loc_945")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #12
        (
            "\x07\x05There is nothing in the chest. NOTHING.\x01",
            "Now shoo. Shoo!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_99B")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_86D end

    def Function_7_9A9(): pass

    label("Function_7_9A9")

    TalkBegin(0xFF)
    ClearMapFlags(0x1)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #13
        "\x07\x05There's a lever here that can be moved.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x214, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x214, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_AF8")

    Menu(
        0,
        260,
        200,
        1,
        (
            "Flip Right\x01",      # 0
            "Flip Left\x01",       # 1
            "Stop\x01",            # 2
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_56(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A92")
    OP_6F(0x2, 0)
    OP_70(0x2, 0x3C)
    OP_22(0xFA, 0x0, 0x64)
    OP_73(0x2)
    OP_A2(0x10A4)
    Sleep(500)
    OP_6D(52660, -60, 67850, 1200)
    OP_6F(0x1, 0)
    OP_70(0x1, 0x78)
    OP_22(0xFB, 0x0, 0x64)
    OP_73(0x1)
    Sleep(1000)
    Fade(500)
    OP_69(0x0, 0x0)
    Jump("loc_AF5")

    label("loc_A92")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AF5")
    OP_6F(0x2, 100)
    OP_70(0x2, 0xA0)
    OP_22(0xFA, 0x0, 0x64)
    OP_73(0x2)
    OP_A2(0x10A5)
    Sleep(500)
    OP_6D(52660, -60, 67850, 1200)
    OP_6F(0x1, 0)
    OP_70(0x1, 0x78)
    OP_22(0xFB, 0x0, 0x64)
    OP_73(0x1)
    Sleep(1000)
    Fade(500)
    OP_69(0x0, 0x0)

    label("loc_AF5")

    Jump("loc_BB7")

    label("loc_AF8")


    Menu(
        0,
        260,
        200,
        1,
        (
            "Return To Original Position\x01",      # 0
            "Stop\x01",                             # 1
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_56(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BB7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x214, 4)), scpexpr(EXPR_END)), "loc_B5A")
    OP_6F(0x2, 60)
    OP_70(0x2, 0x0)
    OP_22(0xFA, 0x0, 0x64)
    OP_73(0x2)
    OP_A3(0x10A4)
    Jump("loc_B7A")

    label("loc_B5A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x214, 5)), scpexpr(EXPR_END)), "loc_B7A")
    OP_6F(0x2, 160)
    OP_70(0x2, 0x64)
    OP_22(0xFA, 0x0, 0x64)
    OP_73(0x2)
    OP_A3(0x10A5)

    label("loc_B7A")

    Sleep(500)
    OP_6D(52660, -60, 67850, 1200)
    OP_6F(0x1, 120)
    OP_70(0x1, 0x0)
    OP_22(0xFB, 0x0, 0x64)
    OP_73(0x1)
    Sleep(1000)
    Fade(500)
    OP_69(0x0, 0x0)

    label("loc_BB7")

    SetMapFlags(0x1)
    TalkEnd(0xFF)
    Return()

    # Function_7_9A9 end

    def Function_8_BC0(): pass

    label("Function_8_BC0")

    TalkBegin(0xFF)

    AnonymousTalk(    #14
        "\x07\x05It's rusted and seems like it won't work.\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFF)
    Return()

    # Function_8_BC0 end

    def Function_9_BF6(): pass

    label("Function_9_BF6")

    SetMapFlags(0x80)
    ClearMapFlags(0x1)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #15
        "\x07\x05There's a lever here that can be moved.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x214, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CB5")

    Menu(
        0,
        260,
        200,
        1,
        (
            "Drop Lever\x01",      # 0
            "Stop\x01",            # 1
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_56(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CB2")
    EventBegin(0x0)
    OP_6F(0x0, 0)
    OP_70(0x0, 0x3C)
    OP_22(0xFA, 0x0, 0x64)
    OP_73(0x0)
    OP_6F(0x4, 0)
    OP_70(0x4, 0xFA)
    OP_22(0xFC, 0x0, 0x64)
    OP_73(0x4)
    OP_A2(0x10A6)
    SetMapFlags(0x1)
    EventEnd(0x3)
    Return()

    label("loc_CB2")

    Jump("loc_D2D")

    label("loc_CB5")


    Menu(
        0,
        260,
        200,
        1,
        (
            "Return To Original Position\x01",      # 0
            "Stop\x01",                             # 1
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_56(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D2D")
    EventBegin(0x0)
    OP_6F(0x0, 60)
    OP_70(0x0, 0x0)
    OP_22(0xFA, 0x0, 0x64)
    OP_73(0x0)
    OP_6F(0x4, 250)
    OP_70(0x4, 0x0)
    OP_22(0xFC, 0x0, 0x64)
    OP_73(0x4)
    OP_A3(0x10A6)
    SetMapFlags(0x1)
    EventEnd(0x3)
    Return()

    label("loc_D2D")

    OP_69(0x0, 0x258)
    ClearMapFlags(0x80)
    SetMapFlags(0x1)
    TalkEnd(0xFF)
    Return()

    # Function_9_BF6 end

    SaveToFile()

Try(main)
