from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'C5500   ._SN',
        MapName             = 'Other',
        Location            = 'C5500.x',
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

    DeclMonster(
        X                   = -54250,
        Z                   = 0,
        Y                   = 61360,
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
        X                   = -45920,
        Z                   = 0,
        Y                   = 60730,
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
        X                   = -50020,
        Z                   = 0,
        Y                   = 99780,
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
        X                   = -4000,
        Z                   = 0,
        Y                   = 54580,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x388,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclActor(
        TriggerX            = -32900,
        TriggerZ            = 0,
        TriggerY            = 84900,
        TriggerRange        = 1700,
        ActorX              = -32900,
        ActorZ              = 2500,
        ActorY              = 84900,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -13900,
        TriggerZ            = 0,
        TriggerY            = 73100,
        TriggerRange        = 1700,
        ActorX              = -13900,
        ActorZ              = 2500,
        ActorY              = 73100,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -44000,
        TriggerZ            = 0,
        TriggerY            = 52210,
        TriggerRange        = 1000,
        ActorX              = -44000,
        ActorZ              = 0,
        ActorY              = 51460,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -49990,
        TriggerZ            = 0,
        TriggerY            = 52200,
        TriggerRange        = 1000,
        ActorX              = -49990,
        ActorZ              = 0,
        ActorY              = 51590,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -55490,
        TriggerZ            = 0,
        TriggerY            = 52210,
        TriggerRange        = 1000,
        ActorX              = -55490,
        ActorZ              = 0,
        ActorY              = 51550,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_20E",          # 00, 0
        "Function_1_20F",          # 01, 1
        "Function_2_2CD",          # 02, 2
        "Function_3_3F7",          # 03, 3
        "Function_4_560",          # 04, 4
        "Function_5_690",          # 05, 5
        "Function_6_8F5",          # 06, 6
    )


    def Function_0_20E(): pass

    label("Function_0_20E")

    Return()

    # Function_0_20E end

    def Function_1_20F(): pass

    label("Function_1_20F")

    OP_22(0x1C7, 0x0, 0x64)
    OP_72(0x0, 0x28)
    OP_72(0x1, 0x28)
    OP_72(0x2, 0x28)
    OP_72(0x3, 0x28)
    OP_72(0x4, 0x28)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x214, 1)), scpexpr(EXPR_END)), "loc_242")
    OP_6F(0x0, 120)
    OP_6F(0x1, 60)

    label("loc_242")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x214, 0)), scpexpr(EXPR_END)), "loc_257")
    OP_6F(0x0, 120)
    OP_6F(0x1, 160)

    label("loc_257")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x214, 3)), scpexpr(EXPR_END)), "loc_26C")
    OP_6F(0x3, 120)
    OP_6F(0x4, 60)

    label("loc_26C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x214, 2)), scpexpr(EXPR_END)), "loc_281")
    OP_6F(0x2, 120)
    OP_6F(0x4, 160)

    label("loc_281")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x220, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_293")
    OP_6F(0x5, 0)
    Jump("loc_29A")

    label("loc_293")

    OP_6F(0x5, 60)

    label("loc_29A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x220, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2AC")
    OP_6F(0x6, 0)
    Jump("loc_2B3")

    label("loc_2AC")

    OP_6F(0x6, 60)

    label("loc_2B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x220, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C5")
    OP_6F(0x7, 0)
    Jump("loc_2CC")

    label("loc_2C5")

    OP_6F(0x7, 60)

    label("loc_2CC")

    Return()

    # Function_1_20F end

    def Function_2_2CD(): pass

    label("Function_2_2CD")

    OP_EA(0x2, 0x80, 0x1, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x220, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A5")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x5, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x264, 1)"), scpexpr(EXPR_END)), "loc_33E")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "Found \x1F\x64\x02\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1100)
    Jump("loc_3A2")

    label("loc_33E")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "Found \x1F\x64\x02\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\x64\x02\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x5, 60)
    OP_70(0x5, 0x0)

    label("loc_3A2")

    Jump("loc_3E9")

    label("loc_3A5")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        "\x07\x05This is what your curiosity gets you.\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_3E9")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_2CD end

    def Function_3_3F7(): pass

    label("Function_3_3F7")

    OP_EA(0x2, 0x81, 0x1, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x220, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4CF")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x6, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1F5, 1)"), scpexpr(EXPR_END)), "loc_468")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #3
        "Found \x1F\xF5\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1101)
    Jump("loc_4CC")

    label("loc_468")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #4
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

    label("loc_4CC")

    Jump("loc_552")

    label("loc_4CF")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #5
        (
            "\x07\x05A small spider skitters from one side of the empty\x01",
            "chest to the other. It's actually kind of cute...\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_552")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_3F7 end

    def Function_4_560(): pass

    label("Function_4_560")

    OP_EA(0x2, 0x82, 0x1, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x220, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_638")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x7, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FE, 1)"), scpexpr(EXPR_END)), "loc_5D1")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #6
        "Found \x1F\xFE\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1102)
    Jump("loc_635")

    label("loc_5D1")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #7
        (
            "Found \x1F\xFE\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\xFE\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x7, 60)
    OP_70(0x7, 0x0)

    label("loc_635")

    Jump("loc_682")

    label("loc_638")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #8
        "\x07\x05What? There's nothing in here? BOOO-RIIING.\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_682")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_560 end

    def Function_5_690(): pass

    label("Function_5_690")

    TalkBegin(0xFF)
    ClearMapFlags(0x1)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #9
        "\x07\x05There's a lever here that can be moved.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x214, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x214, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7E6")

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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_779")
    OP_6F(0x1, 0)
    OP_70(0x1, 0x3C)
    OP_22(0xFA, 0x0, 0x64)
    OP_73(0x1)
    OP_A2(0x10A1)
    OP_6D(-32340, -60, 91590, 1200)
    Sleep(300)
    OP_6F(0x0, 0)
    OP_70(0x0, 0x78)
    OP_22(0xFB, 0x0, 0x64)
    OP_73(0x0)
    Sleep(1000)
    Fade(500)
    OP_69(0x0, 0x0)
    Jump("loc_7DC")

    label("loc_779")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7DC")
    OP_6F(0x1, 100)
    OP_70(0x1, 0xA0)
    OP_22(0xFA, 0x0, 0x64)
    OP_73(0x1)
    OP_A2(0x10A0)
    OP_6D(-32340, -60, 91590, 1200)
    Sleep(300)
    OP_6F(0x0, 0)
    OP_70(0x0, 0x78)
    OP_22(0xFB, 0x0, 0x64)
    OP_73(0x0)
    Sleep(1000)
    Fade(500)
    OP_69(0x0, 0x0)

    label("loc_7DC")

    OP_69(0x0, 0x258)
    Jump("loc_8EC")

    label("loc_7E6")


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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8EC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x214, 1)), scpexpr(EXPR_END)), "loc_88A")
    OP_6F(0x1, 60)
    OP_70(0x1, 0x0)
    OP_22(0xFA, 0x0, 0x64)
    OP_73(0x1)
    OP_A3(0x10A1)
    Sleep(500)
    OP_6D(-32340, -60, 91590, 1200)
    Sleep(300)
    OP_6F(0x0, 120)
    OP_70(0x0, 0x0)
    OP_22(0xFB, 0x0, 0x64)
    OP_73(0x0)
    Sleep(1000)
    Fade(500)
    OP_69(0x0, 0x0)
    Jump("loc_8EC")

    label("loc_88A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x214, 0)), scpexpr(EXPR_END)), "loc_8EC")
    OP_6F(0x1, 160)
    OP_70(0x1, 0x64)
    OP_22(0xFA, 0x0, 0x64)
    OP_73(0x1)
    OP_A3(0x10A0)
    Sleep(500)
    OP_6D(-32340, -60, 91590, 1200)
    Sleep(300)
    OP_6F(0x0, 120)
    OP_70(0x0, 0x0)
    OP_22(0xFB, 0x0, 0x64)
    OP_73(0x0)
    Sleep(1000)
    Fade(500)
    OP_69(0x0, 0x0)

    label("loc_8EC")

    SetMapFlags(0x1)
    TalkEnd(0xFF)
    Return()

    # Function_5_690 end

    def Function_6_8F5(): pass

    label("Function_6_8F5")

    TalkBegin(0xFF)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #10
        "\x07\x05There's a lever here that can be moved.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x214, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x214, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9F1")

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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9B2")
    OP_6F(0x4, 0)
    OP_70(0x4, 0x3C)
    OP_22(0xFA, 0x0, 0x64)
    OP_73(0x4)
    OP_A2(0x10A3)
    OP_6F(0x3, 0)
    OP_70(0x3, 0x78)
    OP_22(0xFB, 0x0, 0x64)
    OP_73(0x3)
    Jump("loc_9EE")

    label("loc_9B2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9EE")
    OP_6F(0x4, 100)
    OP_70(0x4, 0xA0)
    OP_22(0xFA, 0x0, 0x64)
    OP_73(0x4)
    OP_A2(0x10A2)
    OP_6F(0x2, 0)
    OP_70(0x2, 0x78)
    OP_22(0xFB, 0x0, 0x64)
    OP_73(0x2)

    label("loc_9EE")

    Jump("loc_A9F")

    label("loc_9F1")


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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A9F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x214, 3)), scpexpr(EXPR_END)), "loc_A69")
    OP_6F(0x4, 60)
    OP_70(0x4, 0x0)
    OP_22(0xFA, 0x0, 0x64)
    OP_73(0x4)
    OP_6F(0x3, 120)
    OP_70(0x3, 0x0)
    OP_22(0xFB, 0x0, 0x64)
    OP_73(0x3)
    OP_A3(0x10A3)
    Jump("loc_A9F")

    label("loc_A69")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x214, 2)), scpexpr(EXPR_END)), "loc_A9F")
    OP_6F(0x4, 160)
    OP_70(0x4, 0x64)
    OP_22(0xFA, 0x0, 0x64)
    OP_73(0x4)
    OP_6F(0x2, 120)
    OP_70(0x2, 0x0)
    OP_22(0xFB, 0x0, 0x64)
    OP_73(0x2)
    OP_A3(0x10A2)

    label("loc_A9F")

    TalkEnd(0xFF)
    Return()

    # Function_6_8F5 end

    SaveToFile()

Try(main)
