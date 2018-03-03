from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'U4404   ._SN',
        MapName             = 'gaiden2',
        Location            = 'U4404.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60221",
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
        'ED6_DT29/CH14450 ._CH',             # 00
        'ED6_DT29/CH14451 ._CH',             # 01
        'ED6_DT29/CH14730 ._CH',             # 02
        'ED6_DT29/CH14730 ._CH',             # 03
        'ED6_DT29/CH14790 ._CH',             # 04
        'ED6_DT29/CH14791 ._CH',             # 05
    )

    AddCharChipPat(
        'ED6_DT29/CH14450P._CP',             # 00
        'ED6_DT29/CH14451P._CP',             # 01
        'ED6_DT29/CH14730P._CP',             # 02
        'ED6_DT29/CH14730P._CP',             # 03
        'ED6_DT29/CH14790P._CP',             # 04
        'ED6_DT29/CH14791P._CP',             # 05
    )

    DeclMonster(
        X                   = -1730,
        Z                   = 0,
        Y                   = 10930,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xDF,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -12250,
        Z                   = 0,
        Y                   = 51840,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xDD,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -8330,
        Z                   = 0,
        Y                   = 72990,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xDE,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 21250,
        Z                   = 0,
        Y                   = 112440,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xDF,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -960,
        Z                   = 0,
        Y                   = 56400,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xDD,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 18550,
        Z                   = 0,
        Y                   = 26840,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xDE,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclActor(
        TriggerX            = 10760,
        TriggerZ            = 0,
        TriggerY            = 120990,
        TriggerRange        = 1000,
        ActorX              = 10760,
        ActorZ              = 1000,
        ActorY              = 120990,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 45390,
        TriggerZ            = 0,
        TriggerY            = 49070,
        TriggerRange        = 1000,
        ActorX              = 45390,
        ActorZ              = 1000,
        ActorY              = 49070,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -18600,
        TriggerZ            = 0,
        TriggerY            = 107760,
        TriggerRange        = 1000,
        ActorX              = -18600,
        ActorZ              = 1000,
        ActorY              = 107760,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 28990,
        TriggerZ            = 0,
        TriggerY            = 30440,
        TriggerRange        = 1000,
        ActorX              = 28990,
        ActorZ              = 1000,
        ActorY              = 30440,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 28440,
        TriggerZ            = 0,
        TriggerY            = 22530,
        TriggerRange        = 1000,
        ActorX              = 28440,
        ActorZ              = 1000,
        ActorY              = 22530,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -34390,
        TriggerZ            = 0,
        TriggerY            = 75950,
        TriggerRange        = 1000,
        ActorX              = -34390,
        ActorZ              = 1000,
        ActorY              = 75950,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 27030,
        TriggerZ            = 0,
        TriggerY            = 76890,
        TriggerRange        = 1000,
        ActorX              = 27030,
        ActorZ              = 1000,
        ActorY              = 76890,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 8,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_27E",          # 00, 0
        "Function_1_27F",          # 01, 1
        "Function_2_35C",          # 02, 2
        "Function_3_4DA",          # 03, 3
        "Function_4_63D",          # 04, 4
        "Function_5_7AD",          # 05, 5
        "Function_6_927",          # 06, 6
        "Function_7_A64",          # 07, 7
        "Function_8_C20",          # 08, 8
    )


    def Function_0_27E(): pass

    label("Function_0_27E")

    Return()

    # Function_0_27E end

    def Function_1_27F(): pass

    label("Function_1_27F")

    OP_16(0x2, 0xFA0, 0xFFFE2370, 0xFFFEE2D8, 0x23006E)
    OP_22(0x1C5, 0x1, 0x64)
    OP_51(0x10, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F6, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2BE")
    OP_6F(0xD, 0)
    Jump("loc_2C5")

    label("loc_2BE")

    OP_6F(0xD, 60)

    label("loc_2C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F6, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D7")
    OP_6F(0xE, 0)
    Jump("loc_2DE")

    label("loc_2D7")

    OP_6F(0xE, 60)

    label("loc_2DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F6, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F0")
    OP_6F(0xF, 0)
    Jump("loc_2F7")

    label("loc_2F0")

    OP_6F(0xF, 60)

    label("loc_2F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F6, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_309")
    OP_6F(0x10, 0)
    Jump("loc_310")

    label("loc_309")

    OP_6F(0x10, 60)

    label("loc_310")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F6, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_322")
    OP_6F(0x11, 0)
    Jump("loc_329")

    label("loc_322")

    OP_6F(0x11, 60)

    label("loc_329")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F6, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_33B")
    OP_6F(0x12, 0)
    Jump("loc_342")

    label("loc_33B")

    OP_6F(0x12, 60)

    label("loc_342")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F6, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_354")
    OP_6F(0x13, 0)
    Jump("loc_35B")

    label("loc_354")

    OP_6F(0x13, 60)

    label("loc_35B")

    Return()

    # Function_1_27F end

    def Function_2_35C(): pass

    label("Function_2_35C")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F6, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_435")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0xD, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1F6, 1)"), scpexpr(EXPR_END)), "loc_3CA")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "\x07\x05Found \x1F\xF6\x01\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x27B0)
    Jump("loc_432")

    label("loc_3CA")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "\x07\x05Found \x1F\xF6\x01\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\xF6\x01\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0xD, 60)
    OP_70(0xD, 0x0)

    label("loc_432")

    Jump("loc_4CC")

    label("loc_435")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        (
            "\x07\x05Didn't you know? Repetition is my favorite form of humor!\x01",
            "Didn't you know? Repetition is my favorite form of humor!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0x139, 0x0)

    label("loc_4CC")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_35C end

    def Function_3_4DA(): pass

    label("Function_3_4DA")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F6, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5B3")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0xE, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1F8, 1)"), scpexpr(EXPR_END)), "loc_548")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #3
        "\x07\x05Found \x1F\xF8\x01\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x27B1)
    Jump("loc_5B0")

    label("loc_548")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #4
        (
            "\x07\x05Found \x1F\xF8\x01\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\xF8\x01\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0xE, 60)
    OP_70(0xE, 0x0)

    label("loc_5B0")

    Jump("loc_62F")

    label("loc_5B3")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #5
        (
            "\x07\x05Hey, do you know a doctor? I am feeling a deep pain in my chest.\x01",
            "Oh, wait. I AM a chest!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0x13A, 0x0)

    label("loc_62F")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_4DA end

    def Function_4_63D(): pass

    label("Function_4_63D")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F6, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_716")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0xF, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1F8, 1)"), scpexpr(EXPR_END)), "loc_6AB")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #6
        "\x07\x05Found \x1F\xF8\x01\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x27B2)
    Jump("loc_713")

    label("loc_6AB")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #7
        (
            "\x07\x05Found \x1F\xF8\x01\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\xF8\x01\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0xF, 60)
    OP_70(0xF, 0x0)

    label("loc_713")

    Jump("loc_79F")

    label("loc_716")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #8
        (
            "\x07\x05There is a 'Beware of Chest' sign. You reach to open the chest anyway\x01",
            "and it tries to bite your hand.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0x13B, 0x0)

    label("loc_79F")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_63D end

    def Function_5_7AD(): pass

    label("Function_5_7AD")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F6, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_886")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x10, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x18A, 1)"), scpexpr(EXPR_END)), "loc_81B")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #9
        "\x07\x05Found \x1F\x8A\x01\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x27B3)
    Jump("loc_883")

    label("loc_81B")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #10
        (
            "\x07\x05Found \x1F\x8A\x01\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\x8A\x01\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x10, 60)
    OP_70(0x10, 0x0)

    label("loc_883")

    Jump("loc_919")

    label("loc_886")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #11
        (
            "\x07\x05do do do do do do do do do do do do do do do do\x01",
            "dodododododododododododododododo... ... ... DO DO DO DOOOOOO ♪\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0x13C, 0x0)

    label("loc_919")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_7AD end

    def Function_6_927(): pass

    label("Function_6_927")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F6, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A00")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x11, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1F6, 1)"), scpexpr(EXPR_END)), "loc_995")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #12
        "\x07\x05Found \x1F\xF6\x01\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x27B4)
    Jump("loc_9FD")

    label("loc_995")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #13
        (
            "\x07\x05Found \x1F\xF6\x01\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\xF6\x01\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x11, 60)
    OP_70(0x11, 0x0)

    label("loc_9FD")

    Jump("loc_A56")

    label("loc_A00")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #14
        "\x07\x05So you're back, Rean Quartze--!! Wait. Wrong game.\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0x13D, 0x0)

    label("loc_A56")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_927 end

    def Function_7_A64(): pass

    label("Function_7_A64")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F6, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B3D")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x12, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x2D0, 1)"), scpexpr(EXPR_END)), "loc_AD2")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #15
        "\x07\x05Found \x1F\xD0\x02\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x27B5)
    Jump("loc_B3A")

    label("loc_AD2")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #16
        (
            "\x07\x05Found \x1F\xD0\x02\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\xD0\x02\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x12, 60)
    OP_70(0x12, 0x0)

    label("loc_B3A")

    Jump("loc_C12")

    label("loc_B3D")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #17
        (
            "\x07\x05[25/36] 'You say to think about the history. What about the mira? Think\x01",
            "about THAT. I'll bet we could go live it up at the casinos in Crossbell City\x01",
            "for weeks off of one brick!'\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0x13E, 0x0)

    label("loc_C12")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_7_A64 end

    def Function_8_C20(): pass

    label("Function_8_C20")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F6, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CF9")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x13, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FE, 1)"), scpexpr(EXPR_END)), "loc_C8E")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #18
        "\x07\x05Found \x1F\xFE\x01\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x27B6)
    Jump("loc_CF6")

    label("loc_C8E")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #19
        (
            "\x07\x05Found \x1F\xFE\x01\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\xFE\x01\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x13, 60)
    OP_70(0x13, 0x0)

    label("loc_CF6")

    Jump("loc_D4D")

    label("loc_CF9")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #20
        "\x07\x05[28/36] 'Have you asked Jubilee what SHE wants?'\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0x13F, 0x0)

    label("loc_D4D")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_8_C20 end

    SaveToFile()

Try(main)
