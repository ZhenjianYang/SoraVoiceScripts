from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'C4203   ._SN',
        MapName             = 'Grancel',
        Location            = 'C4203.x',
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
        'ED6_DT09/CH10490 ._CH',             # 00
        'ED6_DT09/CH10491 ._CH',             # 01
        'ED6_DT09/CH10500 ._CH',             # 02
        'ED6_DT09/CH10501 ._CH',             # 03
        'ED6_DT09/CH10510 ._CH',             # 04
        'ED6_DT09/CH10511 ._CH',             # 05
        'ED6_DT09/CH11110 ._CH',             # 06
        'ED6_DT09/CH11111 ._CH',             # 07
        'ED6_DT09/CH11120 ._CH',             # 08
        'ED6_DT09/CH11121 ._CH',             # 09
        'ED6_DT09/CH11130 ._CH',             # 0A
        'ED6_DT09/CH11131 ._CH',             # 0B
        'ED6_DT09/CH11140 ._CH',             # 0C
        'ED6_DT09/CH11141 ._CH',             # 0D
        'ED6_DT09/CH11150 ._CH',             # 0E
        'ED6_DT09/CH11151 ._CH',             # 0F
    )

    AddCharChipPat(
        'ED6_DT09/CH10490P._CP',             # 00
        'ED6_DT09/CH10491P._CP',             # 01
        'ED6_DT09/CH10500P._CP',             # 02
        'ED6_DT09/CH10501P._CP',             # 03
        'ED6_DT09/CH10510P._CP',             # 04
        'ED6_DT09/CH10511P._CP',             # 05
        'ED6_DT09/CH11110P._CP',             # 06
        'ED6_DT09/CH11111P._CP',             # 07
        'ED6_DT09/CH11120P._CP',             # 08
        'ED6_DT09/CH11121P._CP',             # 09
        'ED6_DT09/CH11130P._CP',             # 0A
        'ED6_DT09/CH11131P._CP',             # 0B
        'ED6_DT09/CH11140P._CP',             # 0C
        'ED6_DT09/CH11141P._CP',             # 0D
        'ED6_DT09/CH11150P._CP',             # 0E
        'ED6_DT09/CH11151P._CP',             # 0F
    )

    DeclMonster(
        X                   = -47360,
        Z                   = 0,
        Y                   = 42620,
        Unknown_0C          = 180,
        Unknown_0E          = 10,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x27C,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -121330,
        Z                   = 0,
        Y                   = 50600,
        Unknown_0C          = 180,
        Unknown_0E          = 8,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x277,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -88180,
        Z                   = 0,
        Y                   = 51510,
        Unknown_0C          = 180,
        Unknown_0E          = 8,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x27F,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclActor(
        TriggerX            = -101030,
        TriggerZ            = 0,
        TriggerY            = 62030,
        TriggerRange        = 800,
        ActorX              = -101030,
        ActorZ              = 500,
        ActorY              = 62030,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -91330,
        TriggerZ            = 0,
        TriggerY            = 60050,
        TriggerRange        = 1000,
        ActorX              = -91210,
        ActorZ              = 1500,
        ActorY              = 60790,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_1C6",          # 00, 0
        "Function_1_1C7",          # 01, 1
        "Function_2_209",          # 02, 2
        "Function_3_5F9",          # 03, 3
    )


    def Function_0_1C6(): pass

    label("Function_0_1C6")

    Return()

    # Function_0_1C6 end

    def Function_1_1C7(): pass

    label("Function_1_1C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 5)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1D7")
    OP_64(0x0, 0x1)

    label("loc_1D7")

    OP_72(0x0, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 5)), scpexpr(EXPR_END)), "loc_1EA")
    OP_6F(0x0, 240)

    label("loc_1EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xDB, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1FC")
    OP_6F(0x1, 0)
    Jump("loc_203")

    label("loc_1FC")

    OP_6F(0x1, 60)

    label("loc_203")

    OP_22(0x1CD, 0x1, 0x64)
    Return()

    # Function_1_1C7 end

    def Function_2_209(): pass

    label("Function_2_209")

    EventBegin(0x0)
    OP_6D(-100990, 0, 62230, 1000)

    ChrTalk(    #0
        0x102,
        (
            "#010FThe map has this area\x01",
            "marked with '='.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x108,
        (
            "#073FHmm...\x01",
            "I don't see anything special...\x02\x03",

            "Those royal family sneaks sure\x01",
            "know how to hide things!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x104,
        (
            "#035FI suppose this will require a\x01",
            "hefty amount of searching.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x102,
        "#012F...I'll go first.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x102, -101200, 0, 61500, 0)
    SetChrPos(0x108, -100610, 0, 59330, 0)
    SetChrPos(0x104, -101480, 0, 59880, 0)
    Sleep(500)
    FadeToBright(1000, 0)
    OP_0D()
    OP_8F(0x102, 0xFFFE774E, 0x0, 0xF00A, 0x2BC, 0x0)
    Sleep(500)
    OP_8F(0x102, 0xFFFE738E, 0x0, 0xEFBA, 0x1F4, 0x0)
    Sleep(1000)

    ChrTalk(    #4
        0x102,
        "#015FAh...here it is.\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    OP_22(0x64, 0x0, 0x64)
    Sleep(500)
    OP_71(0x0, 0x10)
    OP_6F(0x0, 0)
    OP_70(0x0, 0x78)
    OP_22(0x70, 0x0, 0x64)
    OP_73(0x0)
    OP_6F(0x0, 120)
    OP_70(0x0, 0xF0)
    OP_22(0x70, 0x0, 0x64)

    ChrTalk(    #5
        0x108,
        "#071FNice work.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x104,
        (
            "#033FHmmm... Impressive.\x02\x03",

            "Have you some particular knack\x01",
            "for finding hidden switches?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x104, 400)

    ChrTalk(    #7
        0x102,
        (
            "#013F#5PA knack...?\x01",
            "It's just practice.\x02\x03",

            "#010FYou just naturally learn\x01",
            "what to feel for.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x104,
        (
            "#030FNaturally, eh?\x02\x03",

            "#031FTell me, you weren't a phantom thief of some\x01",
            "kind in your childhood, were you?\x02\x03",

            "You know, the kind that shows up in plays and\x01",
            "the like.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x102,
        "#018F#5POh, please...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x108,
        (
            "#070FTime isn't on our side, guys.\x01",
            "Let's get moving.\x02\x03",

            "This is the real deal.\x02",
        )
    )

    CloseMessageWindow()
    OP_73(0x0)
    OP_72(0x0, 0x10)
    OP_71(0x0, 0x2)
    OP_64(0x0, 0x1)
    OP_A2(0x65D)
    OP_28(0x4D, 0x1, 0x8)
    OP_28(0x4D, 0x1, 0x10)
    EventEnd(0x0)
    Return()

    # Function_2_209 end

    def Function_3_5F9(): pass

    label("Function_3_5F9")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xDB, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6EB")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1F6, 1)"), scpexpr(EXPR_END)), "loc_670")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #11
        "\x07\x00Found \x07\x02Teara Balm\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x6DD)
    Jump("loc_6E8")

    label("loc_670")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #12
        (
            "\x07\x00Found \x07\x02Teara Balm\x07\x00 in chest.\x01",
            "Inventory full so gave up \x07\x02Teara Balm\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x1, 60)
    OP_70(0x1, 0x0)

    label("loc_6E8")

    Jump("loc_732")

    label("loc_6EB")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #13
        "\x07\x05The chest is so very, very, very empty.\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_83(0xF, 0x4A)

    label("loc_732")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_5F9 end

    SaveToFile()

Try(main)
