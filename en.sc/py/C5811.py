from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'C5811   ._SN',
        MapName             = 'Other',
        Location            = 'C5811.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60062",
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


    DeclActor(
        TriggerX            = -11900,
        TriggerZ            = 0,
        TriggerY            = -5480,
        TriggerRange        = 1500,
        ActorX              = -11900,
        ActorZ              = 1000,
        ActorY              = -5480,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 4730,
        TriggerZ            = 0,
        TriggerY            = 12330,
        TriggerRange        = 1000,
        ActorX              = 5090,
        ActorZ              = 1000,
        ActorY              = 12940,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -5410,
        TriggerZ            = 0,
        TriggerY            = 12060,
        TriggerRange        = 1000,
        ActorX              = -5740,
        ActorZ              = 1000,
        ActorY              = 12680,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 5160,
        TriggerZ            = 0,
        TriggerY            = -11960,
        TriggerRange        = 1000,
        ActorX              = 5370,
        ActorZ              = 1000,
        ActorY              = -12630,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_13A",          # 00, 0
        "Function_1_13B",          # 01, 1
        "Function_2_187",          # 02, 2
        "Function_3_2B6",          # 03, 3
        "Function_4_3F7",          # 04, 4
        "Function_5_505",          # 05, 5
    )


    def Function_0_13A(): pass

    label("Function_0_13A")

    Return()

    # Function_0_13A end

    def Function_1_13B(): pass

    label("Function_1_13B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x474, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14D")
    OP_6F(0x2, 0)
    Jump("loc_154")

    label("loc_14D")

    OP_6F(0x2, 60)

    label("loc_154")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x474, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_166")
    OP_6F(0x3, 0)
    Jump("loc_16D")

    label("loc_166")

    OP_6F(0x3, 60)

    label("loc_16D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x474, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17F")
    OP_6F(0x4, 0)
    Jump("loc_186")

    label("loc_17F")

    OP_6F(0x4, 60)

    label("loc_186")

    Return()

    # Function_1_13B end

    def Function_2_187(): pass

    label("Function_2_187")

    OP_EA(0x2, 0xBA, 0x1, 0x0)
    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x474, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_26D")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2, 0x1E)
    OP_73(0x2)
    OP_6F(0x2, 30)
    OP_3E(0x39F, 10)
    OP_3E(0x3A1, 10)
    OP_3E(0x3A7, 10)
    OP_3E(0x3A9, 10)
    OP_3E(0x3AB, 10)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #0
        (
            "Found\x01",
            "#2C#20ISavory Pinion x10\x01",
            "#20IJuicy Bone x10\x01",
            "#20IMonster Fowl x10\x01",
            "#20IMonster Bird Egg x10\x01",
            "#20IPrickly Seed x10#0C.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x23A0)
    Jump("loc_2A4")

    label("loc_26D")


    AnonymousTalk(    #1
        "\x07\x05The looters in Calvard aren't this desperate...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_2A4")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_187 end

    def Function_3_2B6(): pass

    label("Function_3_2B6")

    OP_EA(0x2, 0xBB, 0x1, 0x0)
    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x474, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_39C")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x3, 0x1E)
    OP_73(0x3)
    OP_6F(0x3, 30)
    OP_3E(0x39E, 10)
    OP_3E(0x3A0, 10)
    OP_3E(0x3A3, 10)
    OP_3E(0x3A4, 10)
    OP_3E(0x3A5, 10)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #2
        (
            "Found\x01",
            "#2C#20ICurative Horn x10\x01",
            "#20ILeathery Tail x10\x01",
            "#20ILucky Fang x10\x01",
            "#20IMonster Carapace x10\x01",
            "#20IBeast Flesh x10#0C.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x23A1)
    Jump("loc_3E5")

    label("loc_39C")


    AnonymousTalk(    #3
        (
            "\x07\x05The chest wants to know what it's done\x01",
            "to deserve such treatment.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_3E5")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_2B6 end

    def Function_4_3F7(): pass

    label("Function_4_3F7")

    OP_EA(0x2, 0xBC, 0x1, 0x0)
    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x474, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4BD")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x4, 0x1E)
    OP_73(0x4)
    OP_6F(0x4, 30)
    OP_3E(0x3A2, 10)
    OP_3E(0x3A6, 10)
    OP_3E(0x3A8, 10)
    OP_3E(0x3AA, 10)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #4
        (
            "Found\x01",
            "#2C#20IGummy Eyeball x10\x01",
            "#20IFish Fillet x10\x01",
            "#20IClear Gelatin x10\x01",
            "#20IFish Egg x10#0C.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x23A2)
    Jump("loc_4F3")

    label("loc_4BD")


    AnonymousTalk(    #5
        "\x07\x05The chest applauds your dedication to larceny.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_4F3")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_3F7 end

    def Function_5_505(): pass

    label("Function_5_505")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(330, 68, 34, 12)
    SetChrName("")

    AnonymousTalk(    #6
        "\x07\x05#1SThank you for your patronage.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #7
        (
            "\x07\x05#1SCurrently, due to system errors, items that can be\x01",
            "selected are limited.\x02",
        )
    )

    CloseMessageWindow()
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        40,
        90,
        1,
        (
            "Accept Package\x01",      # 0
            "Stop Use\x01",            # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_5DA"),
        (1, "loc_8E2"),
        (SWITCH_DEFAULT, "loc_8E5"),
    )


    label("loc_5DA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x417, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x456, 0)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_672")

    AnonymousTalk(    #8
        "\x07\x05#1SBeginning lookup...\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(    #9
        "\x07\x05#1S...\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(    #10
        "\x07\x05#1S...Unable to find data.\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(    #11
        "\x07\x05#1SThere are no packages for this user at this time.\x02",
    )

    CloseMessageWindow()
    Jump("loc_8DF")

    label("loc_672")


    AnonymousTalk(    #12
        "\x07\x05#1SBeginning lookup...\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(    #13
        "\x07\x05#1S...\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(    #14
        "\x07\x05#1S...Specified wavelength pattern found.\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(    #15
        "\x07\x05#1SUser is authenticated as recorded recipient of a package.\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(    #16
        "\x07\x05#1SBeginning transfer of stored item #\\R-8834-0033.\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(    #17
        "\x07\x05#1SDownloading data... 20%...\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(    #18
        "\x07\x05#1S...40%...60%...\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(    #19
        "\x07\x05#1S...80%... Transfer complete!\x02",
    )

    CloseMessageWindow()
    OP_5F(0x0)
    Sleep(200)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #20
        "\x07\x00Received #1048i.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x418, 1)

    ChrTalk(    #21
        0x101,
        (
            "#1004FTh-This is a data crystal, right?\x02\x03",

            "Seems like it was sent from somewhere...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x102,
        (
            "#1042FSeems like it responded to something in\x01",
            "our possessions.\x02\x03",

            "#1040FWe might be able to view the contents if we hand\x01",
            "it over to Professor Russell.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x22B0)

    label("loc_8DF")

    Jump("loc_8E5")

    label("loc_8E2")

    Jump("loc_8E5")

    label("loc_8E5")

    OP_5F(0x0)
    OP_56(0x0)
    Sleep(200)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(100)
    TalkEnd(0xFF)
    Return()

    # Function_5_505 end

    SaveToFile()

Try(main)
