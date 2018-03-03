from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'U4122   ._SN',
        MapName             = 'Gaiden2',
        Location            = 'U4122.x',
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
        "Function_2_17F",          # 02, 2
        "Function_3_2BB",          # 03, 3
        "Function_4_448",          # 04, 4
    )


    def Function_0_116(): pass

    label("Function_0_116")

    Return()

    # Function_0_116 end

    def Function_1_117(): pass

    label("Function_1_117")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E4, 1)), scpexpr(EXPR_END)), "loc_12A")
    OP_B1("U4122_y")
    Jump("loc_133")

    label("loc_12A")

    OP_B1("U4122_n")

    label("loc_133")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F8, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_145")
    OP_6F(0x2, 0)
    Jump("loc_14C")

    label("loc_145")

    OP_6F(0x2, 60)

    label("loc_14C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F8, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15E")
    OP_6F(0x3, 0)
    Jump("loc_165")

    label("loc_15E")

    OP_6F(0x3, 60)

    label("loc_165")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F8, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_177")
    OP_6F(0x4, 0)
    Jump("loc_17E")

    label("loc_177")

    OP_6F(0x4, 60)

    label("loc_17E")

    Return()

    # Function_1_117 end

    def Function_2_17F(): pass

    label("Function_2_17F")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F8, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_258")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x145, 1)"), scpexpr(EXPR_END)), "loc_1ED")
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
    Jump("loc_255")

    label("loc_1ED")

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
    OP_6F(0x2, 60)
    OP_70(0x2, 0x0)

    label("loc_255")

    Jump("loc_2AD")

    label("loc_258")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        "\x07\x05I'M NOT CLEVER ENOUGH FOR ALL THESE CHEST PHRASES\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0xFD, 0x0)

    label("loc_2AD")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_17F end

    def Function_3_2BB(): pass

    label("Function_3_2BB")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F8, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_394")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x3, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1F9, 1)"), scpexpr(EXPR_END)), "loc_329")
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
    Jump("loc_391")

    label("loc_329")

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
    OP_6F(0x3, 60)
    OP_70(0x3, 0x0)

    label("loc_391")

    Jump("loc_43A")

    label("loc_394")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #5
        (
            "\x07\x05(12/12) Hideko didn't even wait for an answer; she just flung open the\x01",
            "door without a care. And there, standing before her, was...\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0xFE, 0x0)

    label("loc_43A")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_2BB end

    def Function_4_448(): pass

    label("Function_4_448")

    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F8, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_524")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x4, 0x1E)
    OP_73(0x4)
    OP_6F(0x4, 30)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    OP_3E(0x1E3, 1)

    AnonymousTalk(    #6
        "\x07\x05Found \x1F\xE3\x01\x07\x05.\x02",
    )

    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x20D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_512")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_AC(0x30)"), scpexpr(EXPR_END)), "loc_4B3")
    Jump("loc_512")

    label("loc_4B3")

    CloseMessageWindow()

    AnonymousTalk(    #7
        "Found a scrap of paper with a recipe written on it.\x02",
    )

    CloseMessageWindow()
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #8
        "\x07\x05Learned the recipe for \x1F\xE3\x01\x07\x05.\x02",
    )


    label("loc_512")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x27C2)
    Jump("loc_590")

    label("loc_524")


    AnonymousTalk(    #9
        (
            "\x07\x05There's some green hair inside. The chest prays to Aidios this sinful\x01",
            "priest gets his just desserts.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_590")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    OP_F7(0x19, 0xFF, 0x0)
    Return()

    # Function_4_448 end

    SaveToFile()

Try(main)
