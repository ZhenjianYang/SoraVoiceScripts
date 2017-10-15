from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 卢安

    CreateScenaFile(
        FileName            = 'T2611   ._SN',
        MapName             = 'Ruan',
        Location            = 'T2611.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60032",
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
        'Candlestick',                          # 9
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
        'ED6_DT06/CH20021 ._CH',             # 00
        'ED6_DT07/CH00024 ._CH',             # 01
        'ED6_DT07/CH00054 ._CH',             # 02
        'ED6_DT26/CH20311 ._CH',             # 03
    )

    AddCharChipPat(
        'ED6_DT06/CH20021P._CP',             # 00
        'ED6_DT07/CH00024P._CP',             # 01
        'ED6_DT07/CH00054P._CP',             # 02
        'ED6_DT26/CH20311P._CP',             # 03
    )

    DeclNpc(
        X                   = 8920,
        Z                   = 6000,
        Y                   = 27470,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1245184,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1E2,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclActor(
        TriggerX            = 9080,
        TriggerZ            = 4000,
        TriggerY            = 28080,
        TriggerRange        = 1300,
        ActorX              = 8920,
        ActorZ              = 6000,
        ActorY              = 27470,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -39000,
        TriggerZ            = 0,
        TriggerY            = 30250,
        TriggerRange        = 1300,
        ActorX              = -39000,
        ActorZ              = 1000,
        ActorY              = 30250,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 44990,
        TriggerZ            = 0,
        TriggerY            = 3460,
        TriggerRange        = 800,
        ActorX              = 44990,
        ActorZ              = 1000,
        ActorY              = 3460,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 43000,
        TriggerZ            = 0,
        TriggerY            = 25500,
        TriggerRange        = 1500,
        ActorX              = 42980,
        ActorZ              = 1000,
        ActorY              = 25500,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -80200,
        TriggerZ            = 250,
        TriggerY            = 31450,
        TriggerRange        = 1000,
        ActorX              = -80240,
        ActorZ              = 250,
        ActorY              = 32100,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_19E",          # 00, 0
        "Function_1_19F",          # 01, 1
        "Function_2_20A",          # 02, 2
        "Function_3_363",          # 03, 3
        "Function_4_852",          # 04, 4
        "Function_5_D48",          # 05, 5
        "Function_6_F85",          # 06, 6
        "Function_7_1954",         # 07, 7
    )


    def Function_0_19E(): pass

    label("Function_0_19E")

    Return()

    # Function_0_19E end

    def Function_1_19F(): pass

    label("Function_1_19F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x245, 1)), scpexpr(EXPR_END)), "loc_1AF")
    OP_10(0x5, 0x0)
    OP_10(0x17, 0x1)
    Jump("loc_1B5")

    label("loc_1AF")

    OP_10(0x5, 0x1)
    OP_10(0x17, 0x0)

    label("loc_1B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x268, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C7")
    OP_6F(0xB, 0)
    Jump("loc_1CE")

    label("loc_1C7")

    OP_6F(0xB, 60)

    label("loc_1CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x244, 5)), scpexpr(EXPR_END)), "loc_1D9")
    OP_64(0x0, 0x1)

    label("loc_1D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x244, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x244, 6)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1E9")
    OP_64(0x1, 0x1)

    label("loc_1E9")

    OP_72(0x1, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x245, 0)), scpexpr(EXPR_END)), "loc_1FE")
    OP_64(0x2, 0x1)
    OP_71(0x1, 0x10)

    label("loc_1FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x245, 1)), scpexpr(EXPR_END)), "loc_209")
    OP_64(0x3, 0x1)

    label("loc_209")

    Return()

    # Function_1_19F end

    def Function_2_20A(): pass

    label("Function_2_20A")

    OP_EA(0x2, 0xFE, 0x1, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x268, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E2")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0xB, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1F5, 1)"), scpexpr(EXPR_END)), "loc_27B")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "Found \x1F\xF5\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1341)
    Jump("loc_2DF")

    label("loc_27B")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "Found \x1F\xF5\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\xF5\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0xB, 60)
    OP_70(0xB, 0x0)

    label("loc_2DF")

    Jump("loc_355")

    label("loc_2E2")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        (
            "\x07\x05This chest is as empty as my well of creativity\x01",
            "after writing all of these messages.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_355")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_20A end

    def Function_3_363(): pass

    label("Function_3_363")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_37D")
    Call(0, 7)
    FadeToBright(0, 0)

    label("loc_37D")

    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x101, 9240, 4000, 27500, 8)
    SetChrPos(0x105, 10120, 4000, 27470, 313)
    SetChrPos(0xF7, 7810, 4000, 27040, 39)
    SetChrPos(0x104, 9270, 4000, 26150, 7)
    SetChrPos(0x127, 8070, 4000, 26100, 36)
    OP_6D(9230, 4000, 27500, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()

    ChrTalk(    #3
        0x105,
        (
            "#042F#4PA 'hollow flame'...\x01",
            "I guess you could think of\x01",
            "a candlestick that way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x101,
        (
            "#1006F#6PThis is the only one that isn't lit...\x02\x03",

            "Let me take a look.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #5
        "\x07\x05There was a card within the candlestick.\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Sleep(300)
    Fade(250)
    SetChrChipByIndex(0x101, 3)
    SetChrSubChip(0x101, 0)
    OP_0D()
    Sleep(500)
    FadeToDark(300, 0, 100)
    OP_AD(0x240094, 0xBE, 0x64, 0x1F4)
    Sleep(1000)
    SetMessageWindowPos(-1, 300, -1, 3)
    SetChrName("")

    AnonymousTalk(    #6
        (
            "\x07\x05The second curse is within the classroom.\x01",
            "Seek the south-facing student.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_AE(0x1F4)
    Sleep(1000)
    LoadEffect(0x0, "map\\\\mpfire6.eff")
    PlayEffect(0x0, 0xFF, 0x101, 0, 600, 400, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)
    OP_22(0x86, 0x0, 0x64)
    SetChrChipByIndex(0x101, 65535)
    SetChrSubChip(0x101, 0)
    Sleep(1000)
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_8F(0x101, 0x240E, 0xFA0, 0x69FA, 0x7D0, 0x0)
    Sleep(500)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)

    AnonymousTalk(    #7
        "\x07\x05The card burst into flames.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #8
        0x101,
        (
            "#1020F#6PWaaaa-aaaah!\x02\x03",

            "#1007FW-Well, at least the answer was right.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x104,
        (
            "#030FSo, a classroom this time?\x02\x03",

            "#035FAnd a 'south-facing student' in an empty school...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 400)
    Sleep(400)

    ChrTalk(    #10
        0x105,
        (
            "#042FIf I remember correctly, there are\x01",
            "four classrooms total in the left wing--\x01",
            "two on each floor.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_7F9")

    ChrTalk(    #11
        0x106,
        (
            "#051FAll right, then. Let's check them\x01",
            "out and watch our compass.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_83E")

    label("loc_7F9")


    ChrTalk(    #12
        0x103,
        (
            "#020FWell, let's check them all and\x01",
            "keep an eye on our compass.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_83E")

    OP_64(0x0, 0x1)
    OP_65(0x1, 0x1)
    OP_A2(0x1225)
    OP_28(0x84, 0x1, 0x4)
    EventEnd(0x0)
    Return()

    # Function_3_363 end

    def Function_4_852(): pass

    label("Function_4_852")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_86C")
    Call(0, 7)
    FadeToBright(0, 0)

    label("loc_86C")

    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x101, -37320, 0, 30250, 270)
    SetChrPos(0xF7, -37650, 0, 31430, 225)
    SetChrPos(0x105, -37880, 0, 29190, 315)
    SetChrPos(0x104, -39220, 0, 28840, 360)
    SetChrPos(0x127, -38860, 0, 31650, 180)
    OP_6D(-38470, 0, 30820, 0)
    OP_67(0, 6150, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #13
        0x127,
        (
            "#153FAll the other desks are messed up,\x01",
            "but this one looks okay!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_99B")

    ChrTalk(    #14
        0x106,
        (
            "#050FAnd it's pointing exactly south.\x01",
            "This is probably it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9F1")

    label("loc_99B")


    ChrTalk(    #15
        0x103,
        (
            "#022FAnd it is facing south precisely.\x01",
            "I suspect this is what we're looking for.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9F1")


    ChrTalk(    #16
        0x101,
        "#1002FLemme take a look...\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #17
        "\x07\x05There was a card in the desk's cavity.\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Sleep(300)
    Fade(250)
    SetChrChipByIndex(0x101, 3)
    SetChrSubChip(0x101, 0)
    OP_0D()
    Sleep(500)
    FadeToDark(300, 0, 100)
    OP_AD(0x240095, 0xBE, 0x64, 0x1F4)
    Sleep(1000)
    SetMessageWindowPos(-1, 300, -1, 3)
    SetChrName("")

    AnonymousTalk(    #18
        (
            "\x07\x05The third curse lies within the garden.\x01",
            "Seek ye the fallen neck.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_AE(0x1F4)
    Sleep(1000)
    LoadEffect(0x0, "map\\\\mpfire6.eff")
    PlayEffect(0x0, 0xFF, 0x101, 0, 600, 400, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)
    OP_22(0x86, 0x0, 0x64)
    SetChrChipByIndex(0x101, 65535)
    SetChrSubChip(0x101, 0)
    Sleep(1000)
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)

    AnonymousTalk(    #19
        "\x07\x05The card burst into flames.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #20
        0x101,
        (
            "#1004FYeow-owww!\x02\x03",

            "#1006FWell, that was right, at least,\x01",
            "but where's the next one?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x104,
        (
            "#035FThe fallen neck in the garden...\x02\x03",

            "#030FA metaphor, clearly, but for what?\x01",
            "What marvelous mystery!\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_64(0x1, 0x1)
    OP_A2(0x1226)
    OP_28(0x84, 0x1, 0x8)
    SetChrPos(0x101, -37320, 0, 30250, 270)
    SetChrPos(0xF7, -37320, 0, 30250, 270)
    SetChrPos(0x105, -37320, 0, 30250, 270)
    SetChrPos(0x104, -37320, 0, 30250, 270)
    SetChrPos(0x127, -37320, 0, 30250, 270)
    OP_6D(-37320, 0, 30250, 0)
    OP_67(0, 6150, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_4_852 end

    def Function_5_D48(): pass

    label("Function_5_D48")

    EventBegin(0x0)
    Fade(1000)
    OP_6D(44710, 0, 3440, 0)
    OP_67(0, 6150, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    SetChrPos(0x101, 44390, 0, 2910, 0)
    SetChrPos(0xF7, 43210, 0, 2890, 45)
    SetChrPos(0x105, 45590, 0, 2820, 315)
    SetChrPos(0x104, 45160, 0, 1650, 0)
    SetChrPos(0x127, 43950, 0, 1770, 0)
    OP_0D()
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #22
        "\x07\x05The door is locked.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x244, 7)), scpexpr(EXPR_END)), "loc_EFB")
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "[Use Back Gate Key]\x01",       # 0
            "[Use Rusted Key]\x01",          # 1
            "[Don't Use Anything]\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_E9D"),
        (1, "loc_EC5"),
        (2, "loc_EEC"),
        (SWITCH_DEFAULT, "loc_EF8"),
    )


    label("loc_E9D")


    AnonymousTalk(    #23
        "\x07\x05The key doesn't fit.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    Jump("loc_EF8")

    label("loc_EC5")

    FadeToBright(300, 0)
    Sleep(500)
    OP_22(0x73, 0x0, 0x64)
    Sleep(1000)
    OP_64(0x2, 0x1)
    OP_71(0x1, 0x10)
    OP_A2(0x1228)
    Jump("loc_EF8")

    label("loc_EEC")

    FadeToBright(300, 0)
    Jump("loc_EF8")

    label("loc_EF8")

    Jump("loc_F79")

    label("loc_EFB")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "[Use Back Gate Key]\x01",       # 0
            "[Don't Use Anything]\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_F54"),
        (SWITCH_DEFAULT, "loc_F70"),
    )


    label("loc_F54")


    AnonymousTalk(    #24
        "\x07\x05The key doesn't fit.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_F70")

    FadeToBright(300, 0)

    label("loc_F79")

    SetMessageWindowPos(72, 320, 56, 3)
    EventEnd(0x0)
    Return()

    # Function_5_D48 end

    def Function_6_F85(): pass

    label("Function_6_F85")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F9F")
    Call(0, 7)
    FadeToBright(0, 0)

    label("loc_F9F")

    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x101, 43100, 0, 22930, 0)
    SetChrPos(0xF7, 41900, 0, 23180, 0)
    SetChrPos(0x105, 44610, 0, 23420, 315)
    SetChrPos(0x104, 43520, 0, 21510, 8)
    SetChrPos(0x127, 41550, 0, 21200, 17)
    OP_6D(43080, 0, 25000, 0)
    OP_67(0, 7280, -10000, 0)
    OP_6B(1180, 0)
    OP_6C(35000, 0)
    OP_6E(688, 0)
    OP_0D()
    Sleep(1000)

    ChrTalk(    #25
        0x101,
        "#1004FIs this...a statue of a dragon?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x105,
        (
            "#040F#4PThis statue's been here for as \x01",
            "long as I can remember.\x02\x03",

            "Apparently it's carved in the image of a\x01",
            "dragon who used to reside in Liberl.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_11F1")

    ChrTalk(    #27
        0x106,
        (
            "#053FHmm. Something's off about this.\x02\x03",

            "#050FLesse if there's any kind of trick here...\x02",
        )
    )

    CloseMessageWindow()
    OP_8E(0x106, 0xA85C, 0x0, 0x5DC0, 0x7D0, 0x0)
    OP_8C(0x106, 0, 400)
    Sleep(1000)
    OP_8C(0x106, 45, 400)
    Sleep(1000)
    OP_8C(0x106, 315, 400)
    Sleep(1000)
    OP_8C(0x106, 0, 400)
    Sleep(1000)
    Fade(500)
    SetChrFlags(0x106, 0x2)
    SetChrChipByIndex(0x106, 2)
    SetChrSubChip(0x106, 1)
    OP_0D()
    Sleep(1000)
    OP_62(0x106, 0xFFFFFED4, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #28
        0x106,
        "#051F#6PBingo.\x02",
    )

    CloseMessageWindow()
    Jump("loc_12FB")

    label("loc_11F1")


    ChrTalk(    #29
        0x103,
        (
            "#026FHmmm... There's something off here.\x02\x03",

            "#020FLet me take a look at this fine\x01",
            "dragon, see if there's anything...\x02",
        )
    )

    CloseMessageWindow()
    OP_8E(0x103, 0xA85C, 0x0, 0x5DC0, 0x7D0, 0x0)
    OP_8C(0x103, 0, 400)
    Sleep(1000)
    OP_8C(0x103, 45, 400)
    Sleep(1000)
    OP_8C(0x103, 315, 400)
    Sleep(1000)
    OP_8C(0x103, 0, 400)
    Sleep(1000)
    Fade(500)
    SetChrFlags(0x103, 0x2)
    SetChrChipByIndex(0x103, 1)
    SetChrSubChip(0x103, 1)
    OP_0D()
    Sleep(1000)
    OP_62(0x103, 0xFFFFFED4, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #30
        0x103,
        "#027F#6PVictory! ㈱\x02",
    )

    CloseMessageWindow()

    label("loc_12FB")

    OP_22(0x82, 0x0, 0x64)
    Sleep(1000)
    FadeToDark(300, 0, -1)
    OP_0D()
    OP_22(0x70, 0x0, 0x64)
    Sleep(4000)
    FadeToBright(300, 0)
    ClearChrFlags(0x106, 0x2)
    ClearChrFlags(0x103, 0x2)
    SetChrChipByIndex(0x103, 65535)
    SetChrChipByIndex(0x106, 65535)
    SetChrSubChip(0x103, 0)
    SetChrSubChip(0x106, 0)
    SetChrPos(0x101, 43100, 0, 47930, 0)
    SetChrPos(0xF7, 41900, 0, 48180, 0)
    SetChrPos(0x105, 44610, 0, 48420, 315)
    SetChrPos(0x104, 43380, 0, 46320, 0)
    SetChrPos(0x127, 41690, 0, 46310, 0)
    OP_6D(43080, 0, 48770, 0)
    OP_67(0, 7280, -10000, 0)
    OP_6B(1180, 0)
    OP_6C(35000, 0)
    OP_6E(688, 0)
    OP_0D()
    Sleep(1000)

    ChrTalk(    #31
        0x105,
        (
            "#044FFor something like this to be\x01",
            "beneath the statue...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x104,
        (
            "#030FHeh... Not a bad little plan.\x02\x03",

            "This is getting quite exhilarating.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x127,
        (
            "#151FYeah! Someone's really trying to make this fun!\x02\x03",

            "If this was a touristy-trap place,\x01",
            "I bet it'd get a looootta guests!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x101,
        (
            "#1015FBut...you know, something about\x01",
            "all this seems weird. Like, beyond\x01",
            "what you'd expect.\x02\x03",

            "Like, those cards.\x01",
            "Doesn't that seem weird for a ghost?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_161D")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Set Candelabrum Quest to Not Done\x01",      # 0
            "Set Candelabrum Quest to Done\x01",          # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1604"),
        (1, "loc_160C"),
        (SWITCH_DEFAULT, "loc_1614"),
    )


    label("loc_1604")

    OP_28(0x57, 0x3, 0x10)
    Jump("loc_1614")

    label("loc_160C")

    OP_28(0x57, 0x4, 0x10)
    Jump("loc_1614")

    label("loc_1614")

    FadeToBright(300, 0)

    label("loc_161D")

    TurnDirection(0x105, 0x101, 400)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x57, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_172D")

    ChrTalk(    #35
        0x105,
        (
            "#047FYes, it would seem difficult for an\x01",
            "incorporeal spirit to do all this.\x02\x03",

            "#049FAnd...these riddles.\x01",
            "I swear I've...somewhere...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 400)

    ChrTalk(    #36
        0x101,
        (
            "#1004F#6PYou too, Kloe?\x02\x03",

            "#1007FYeah, I was just thinking, I remember\x01",
            "these from somewhere, but where...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1785")

    label("loc_172D")

    TurnDirection(0x105, 0x101, 400)

    ChrTalk(    #37
        0x105,
        (
            "#043FYes, it would seem difficult for an\x01",
            "incorporeal spirit to do all this.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1785")

    TurnDirection(0xF7, 0x101, 400)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_180C")

    ChrTalk(    #38
        0x106,
        (
            "#057FEither way, we're up against something\x01",
            "that isn't gonna go easy on us.\x02\x03",

            "Keep it together. We're going down.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_189D")

    label("loc_180C")


    ChrTalk(    #39
        0x103,
        (
            "#022FOne way or another, we're matching wits\x01",
            "with something which clearly intends to\x01",
            "challenge us.\x02\x03",

            "Stay sharp. We need to head down there.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_189D")

    OP_A2(0x1229)
    OP_28(0x84, 0x1, 0x20)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6D(44540, 0, 50140, 0)
    OP_67(0, 6150, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    SetChrPos(0x101, 44540, 0, 50140, 0)
    SetChrPos(0xF7, 44540, 0, 50140, 0)
    SetChrPos(0x105, 44540, 0, 50140, 0)
    SetChrPos(0x104, 44540, 0, 50140, 0)
    SetChrPos(0x127, 44540, 0, 50140, 0)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_6_F85 end

    def Function_7_1954(): pass

    label("Function_7_1954")

    FadeToDark(0, 0, -1)
    OP_A3(0x1200)
    OP_A3(0x1201)
    RemoveParty(0x2, 0xFF)
    RemoveParty(0x5, 0xFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Set Scherazard as Partner\x01",      # 0
            "Set Agate as Partner\x01",           # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_19CD"),
        (1, "loc_19D3"),
        (SWITCH_DEFAULT, "loc_19D9"),
    )


    label("loc_19CD")

    OP_A2(0x1200)
    Jump("loc_19D9")

    label("loc_19D3")

    OP_A2(0x1201)
    Jump("loc_19D9")

    label("loc_19D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_19E7")
    AddParty(0x2, 0xF7, 0xFF)
    Jump("loc_19EB")

    label("loc_19E7")

    AddParty(0x5, 0xF7, 0xFF)

    label("loc_19EB")

    Return()

    # Function_7_1954 end

    SaveToFile()

Try(main)
