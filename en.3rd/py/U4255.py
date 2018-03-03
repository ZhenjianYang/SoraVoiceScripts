from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'U4255   ._SN',
        MapName             = 'Gaiden2',
        Location            = 'U4255.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60230",
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
        TriggerX            = -65370,
        TriggerZ            = 0,
        TriggerY            = 76630,
        TriggerRange        = 1000,
        ActorX              = -65370,
        ActorZ              = 1000,
        ActorY              = 76630,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -63850,
        TriggerZ            = 0,
        TriggerY            = 76630,
        TriggerRange        = 1000,
        ActorX              = -63850,
        ActorZ              = 1000,
        ActorY              = 76630,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_F2",           # 00, 0
        "Function_1_F3",           # 01, 1
        "Function_2_126",          # 02, 2
        "Function_3_26A",          # 03, 3
    )


    def Function_0_F2(): pass

    label("Function_0_F2")

    Return()

    # Function_0_F2 end

    def Function_1_F3(): pass

    label("Function_1_F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F4, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_105")
    OP_6F(0x5, 0)
    Jump("loc_10C")

    label("loc_105")

    OP_6F(0x5, 60)

    label("loc_10C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F4, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11E")
    OP_6F(0x6, 0)
    Jump("loc_125")

    label("loc_11E")

    OP_6F(0x6, 60)

    label("loc_125")

    Return()

    # Function_1_F3 end

    def Function_2_126(): pass

    label("Function_2_126")

    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F4, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_204")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x5, 0x1E)
    OP_73(0x5)
    OP_6F(0x5, 30)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    OP_3E(0x1E0, 1)

    AnonymousTalk(    #0
        "\x07\x05Found \x1F\xE0\x01\x07\x05.\x02",
    )

    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x20D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1F2")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_AC(0x14)"), scpexpr(EXPR_END)), "loc_191")
    Jump("loc_1F2")

    label("loc_191")

    CloseMessageWindow()

    AnonymousTalk(    #1
        "\x07\x05Found a scrap of paper with a recipe written on it.\x02",
    )

    CloseMessageWindow()
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #2
        "\x07\x05Learned the recipe for \x1F\xE0\x01\x07\x05.\x02",
    )


    label("loc_1F2")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x27A1)
    Jump("loc_253")

    label("loc_204")


    AnonymousTalk(    #3
        (
            "\x07\x05This is a nice chest\x01",
            "This is also a haiku\x01",
            "Chest chest chest chest chest\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_253")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    OP_F7(0x19, 0x129, 0x0)
    Return()

    # Function_2_126 end

    def Function_3_26A(): pass

    label("Function_3_26A")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F4, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_343")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x6, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1BC, 1)"), scpexpr(EXPR_END)), "loc_2D8")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #4
        "\x07\x05Found \x1F\xBC\x01\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x27A2)
    Jump("loc_340")

    label("loc_2D8")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #5
        (
            "\x07\x05Found \x1F\xBC\x01\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\xBC\x01\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x6, 60)
    OP_70(0x6, 0x0)

    label("loc_340")

    Jump("loc_42D")

    label("loc_343")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #6
        (
            "\x07\x05[8/36] 'I shall await your answer at midnight.\x01",
            "                                                    From my heart to yours,\x01",
            "                                                                  -Jubilee'\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0x12A, 0x0)

    label("loc_42D")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_26A end

    SaveToFile()

Try(main)
