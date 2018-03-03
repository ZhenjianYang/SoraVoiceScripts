from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'U4141   ._SN',
        MapName             = 'Gaiden2',
        Location            = 'U4141.x',
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


    DeclActor(
        TriggerX            = 12730,
        TriggerZ            = 0,
        TriggerY            = -7330,
        TriggerRange        = 1000,
        ActorX              = 12730,
        ActorZ              = 1000,
        ActorY              = -7330,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 13510,
        TriggerZ            = 0,
        TriggerY            = 11190,
        TriggerRange        = 1000,
        ActorX              = 13510,
        ActorZ              = 1000,
        ActorY              = 11190,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -14510,
        TriggerZ            = 0,
        TriggerY            = 3850,
        TriggerRange        = 1000,
        ActorX              = -14510,
        ActorZ              = 1000,
        ActorY              = 3850,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_116",          # 00, 0
        "Function_1_117",          # 01, 1
        "Function_2_163",          # 02, 2
        "Function_3_31B",          # 03, 3
        "Function_4_4D1",          # 04, 4
    )


    def Function_0_116(): pass

    label("Function_0_116")

    Return()

    # Function_0_116 end

    def Function_1_117(): pass

    label("Function_1_117")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F8, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_129")
    OP_6F(0x5, 0)
    Jump("loc_130")

    label("loc_129")

    OP_6F(0x5, 60)

    label("loc_130")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F8, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_142")
    OP_6F(0x6, 0)
    Jump("loc_149")

    label("loc_142")

    OP_6F(0x6, 60)

    label("loc_149")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F8, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15B")
    OP_6F(0x7, 0)
    Jump("loc_162")

    label("loc_15B")

    OP_6F(0x7, 60)

    label("loc_162")

    Return()

    # Function_1_117 end

    def Function_2_163(): pass

    label("Function_2_163")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F8, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_23C")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x5, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x145, 1)"), scpexpr(EXPR_END)), "loc_1D1")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "\x07\x05Found \x1F\x45\x01\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x27C0)
    Jump("loc_239")

    label("loc_1D1")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "\x07\x05Found \x1F\x45\x01\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\x45\x01\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x5, 60)
    OP_70(0x5, 0x0)

    label("loc_239")

    Jump("loc_30D")

    label("loc_23C")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        (
            "\x07\x05Did you know? Walter the Direwolf's original name is the Lankywolf,\x01",
            "but this isn't quite as…intimidating in English. The name change came\x01",
            "with the original team's blessing.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0x118, 0x0)

    label("loc_30D")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_163 end

    def Function_3_31B(): pass

    label("Function_3_31B")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F8, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F4")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x6, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1F9, 1)"), scpexpr(EXPR_END)), "loc_389")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #3
        "\x07\x05Found \x1F\xF9\x01\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x27C1)
    Jump("loc_3F1")

    label("loc_389")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #4
        (
            "\x07\x05Found \x1F\xF9\x01\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\xF9\x01\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x6, 60)
    OP_70(0x6, 0x0)

    label("loc_3F1")

    Jump("loc_4C3")

    label("loc_3F4")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #5
        (
            "\x07\x05[20/36] Clack, clack, clack! Their silverware played an awful musical\x01",
            "number with every smack on their plates, each note ringing with a hint\x01",
            "more irritation than the last.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0x119, 0x0)

    label("loc_4C3")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_31B end

    def Function_4_4D1(): pass

    label("Function_4_4D1")

    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F8, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5AF")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x7, 0x1E)
    OP_73(0x7)
    OP_6F(0x7, 30)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    OP_3E(0x1E3, 1)

    AnonymousTalk(    #6
        "\x07\x05Found \x1F\xE3\x01\x07\x05.\x02",
    )

    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x20D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_59D")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_AC(0x30)"), scpexpr(EXPR_END)), "loc_53C")
    Jump("loc_59D")

    label("loc_53C")

    CloseMessageWindow()

    AnonymousTalk(    #7
        "\x07\x05Found a scrap of paper with a recipe written on it.\x02",
    )

    CloseMessageWindow()
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #8
        "\x07\x05Learned the recipe for \x1F\xE3\x01\x07\x05.\x02",
    )


    label("loc_59D")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x27C2)
    Jump("loc_5FA")

    label("loc_5AF")


    AnonymousTalk(    #9
        "\x07\x05Forgive this sinful chest, Father, for I have nothing more to give.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_5FA")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    OP_F7(0x19, 0x11A, 0x0)
    Return()

    # Function_4_4D1 end

    SaveToFile()

Try(main)
