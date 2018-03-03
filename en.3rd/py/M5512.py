from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'M5512   ._SN',
        MapName             = 'Gaiden3',
        Location            = 'M5512.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60231",
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
        'ED6_DT29/CH14740 ._CH',             # 00
        'ED6_DT29/CH14741 ._CH',             # 01
        'ED6_DT29/CH14540 ._CH',             # 02
        'ED6_DT29/CH14541 ._CH',             # 03
        'ED6_DT29/CH15110 ._CH',             # 04
        'ED6_DT29/CH15111 ._CH',             # 05
    )

    AddCharChipPat(
        'ED6_DT29/CH14740P._CP',             # 00
        'ED6_DT29/CH14741P._CP',             # 01
        'ED6_DT29/CH14540P._CP',             # 02
        'ED6_DT29/CH14541P._CP',             # 03
        'ED6_DT29/CH15110P._CP',             # 04
        'ED6_DT29/CH15111P._CP',             # 05
    )

    DeclMonster(
        X                   = -48930,
        Z                   = 550,
        Y                   = 3110,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x196,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -29090,
        Z                   = 0,
        Y                   = 17490,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x199,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -17600,
        Z                   = -4000,
        Y                   = 24160,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x199,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -20720,
        Z                   = -4000,
        Y                   = -11360,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x199,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -7680,
        Z                   = 0,
        Y                   = 25650,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x198,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclActor(
        TriggerX            = -57550,
        TriggerZ            = 0,
        TriggerY            = -8700,
        TriggerRange        = 1000,
        ActorX              = -57550,
        ActorZ              = 1000,
        ActorY              = -8700,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -19420,
        TriggerZ            = -4000,
        TriggerY            = 38680,
        TriggerRange        = 1000,
        ActorX              = -19420,
        ActorZ              = -3000,
        ActorY              = 38680,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -23100,
        TriggerZ            = -4000,
        TriggerY            = -27760,
        TriggerRange        = 1000,
        ActorX              = -23100,
        ActorZ              = -3000,
        ActorY              = -27760,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -3430,
        TriggerZ            = 0,
        TriggerY            = 33040,
        TriggerRange        = 1000,
        ActorX              = -3430,
        ActorZ              = 1000,
        ActorY              = 33040,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -51110,
        TriggerZ            = 0,
        TriggerY            = 21930,
        TriggerRange        = 800,
        ActorX              = -51640,
        ActorZ              = 1000,
        ActorY              = 22460,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_21A",          # 00, 0
        "Function_1_21B",          # 01, 1
        "Function_2_297",          # 02, 2
        "Function_3_3EA",          # 03, 3
        "Function_4_511",          # 04, 4
        "Function_5_63C",          # 05, 5
        "Function_6_77A",          # 06, 6
    )


    def Function_0_21A(): pass

    label("Function_0_21A")

    Return()

    # Function_0_21A end

    def Function_1_21B(): pass

    label("Function_1_21B")

    OP_16(0x2, 0xFA0, 0xFFFDA670, 0xFFFDFC60, 0x2300A5)
    OP_22(0x1CD, 0x0, 0x64)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x534, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_244")
    OP_6F(0x0, 0)
    Jump("loc_24B")

    label("loc_244")

    OP_6F(0x0, 60)

    label("loc_24B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x534, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_25D")
    OP_6F(0x1, 0)
    Jump("loc_264")

    label("loc_25D")

    OP_6F(0x1, 60)

    label("loc_264")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x534, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_276")
    OP_6F(0x2, 0)
    Jump("loc_27D")

    label("loc_276")

    OP_6F(0x2, 60)

    label("loc_27D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x534, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_28F")
    OP_6F(0x3, 0)
    Jump("loc_296")

    label("loc_28F")

    OP_6F(0x3, 60)

    label("loc_296")

    Return()

    # Function_1_21B end

    def Function_2_297(): pass

    label("Function_2_297")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x534, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_370")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x0, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x16C, 1)"), scpexpr(EXPR_END)), "loc_305")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "\x07\x05Found \x1F\x6C\x01\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x29A0)
    Jump("loc_36D")

    label("loc_305")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "\x07\x05Found \x1F\x6C\x01\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\x6C\x01\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x0, 60)
    OP_70(0x0, 0x0)

    label("loc_36D")

    Jump("loc_3DC")

    label("loc_370")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        "\x07\x05Please, save us from these treasure chest messages. We're out of ideas…\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0x89, 0x0)

    label("loc_3DC")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_297 end

    def Function_3_3EA(): pass

    label("Function_3_3EA")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x534, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4C3")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FD, 1)"), scpexpr(EXPR_END)), "loc_458")
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
    OP_A2(0x29A1)
    Jump("loc_4C0")

    label("loc_458")

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
    OP_6F(0x1, 60)
    OP_70(0x1, 0x0)

    label("loc_4C0")

    Jump("loc_503")

    label("loc_4C3")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #5
        "\x07\x05Can't even sleep in peace...\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0x8A, 0x0)

    label("loc_503")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_3EA end

    def Function_4_511(): pass

    label("Function_4_511")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x534, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5EA")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1BE, 1)"), scpexpr(EXPR_END)), "loc_57F")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #6
        "\x07\x05Found \x1F\xBE\x01\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x29A2)
    Jump("loc_5E7")

    label("loc_57F")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #7
        (
            "\x07\x05Found \x1F\xBE\x01\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\xBE\x01\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x2, 60)
    OP_70(0x2, 0x0)

    label("loc_5E7")

    Jump("loc_62E")

    label("loc_5EA")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #8
        "\x07\x05Give it back! That wasn't yours!\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0x8B, 0x0)

    label("loc_62E")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_511 end

    def Function_5_63C(): pass

    label("Function_5_63C")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x534, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_715")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x3, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x294, 1)"), scpexpr(EXPR_END)), "loc_6AA")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #9
        "\x07\x05Found \x1F\x94\x02\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x29A3)
    Jump("loc_712")

    label("loc_6AA")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #10
        (
            "\x07\x05Found \x1F\x94\x02\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\x94\x02\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x3, 60)
    OP_70(0x3, 0x0)

    label("loc_712")

    Jump("loc_76C")

    label("loc_715")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #11
        "\x07\x05This chest is empty. And it smells like old people.\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0x8C, 0x0)

    label("loc_76C")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_63C end

    def Function_6_77A(): pass

    label("Function_6_77A")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #12
        "\x07\x05Saint-Croix Forest\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #13
        (
            "\x07\x05Recommended for ranger training and other\x01",
            "survival lessons.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_6_77A end

    SaveToFile()

Try(main)
