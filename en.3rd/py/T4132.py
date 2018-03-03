from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4132   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4132.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60014",
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
            'ED6_DT21/SUB000  ._SN',
            ''
        ],
    )

    BuildStringList(
        '@FileName',                            # 8
        'Fritz',                                # 9
        'Nielsen',                              # 10
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
        'ED6_DT07/CH01220 ._CH',             # 00
        'ED6_DT07/CH01660 ._CH',             # 01
    )

    AddCharChipPat(
        'ED6_DT07/CH01220P._CP',             # 00
        'ED6_DT07/CH01660P._CP',             # 01
    )

    DeclNpc(
        X                   = 6940,
        Z                   = 0,
        Y                   = 3300,
        Direction           = 166,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = -24500,
        Z                   = 0,
        Y                   = 113310,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )


    DeclActor(
        TriggerX            = 7060,
        TriggerZ            = 0,
        TriggerY            = 1700,
        TriggerRange        = 800,
        ActorX              = 6940,
        ActorZ              = 1500,
        ActorY              = 3300,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 7000,
        TriggerZ            = 0,
        TriggerY            = 4890,
        TriggerRange        = 800,
        ActorX              = 7000,
        ActorZ              = 1000,
        ActorY              = 4890,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_142",          # 00, 0
        "Function_1_143",          # 01, 1
        "Function_2_14D",          # 02, 2
        "Function_3_152",          # 03, 3
        "Function_4_335",          # 04, 4
        "Function_5_8C5",          # 05, 5
    )


    def Function_0_142(): pass

    label("Function_0_142")

    Return()

    # Function_0_142 end

    def Function_1_143(): pass

    label("Function_1_143")

    OP_B1("t4132_n")
    Return()

    # Function_1_143 end

    def Function_2_14D(): pass

    label("Function_2_14D")

    Call(0, 3)
    Return()

    # Function_2_14D end

    def Function_3_152(): pass

    label("Function_3_152")

    TalkBegin(0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 0)), scpexpr(EXPR_END)), "loc_316")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_25B")

    ChrTalk(    #0
        0x10,
        (
            "A number of men in black suits came in here\x01",
            "the other day, as truth would have it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x10,
        (
            "From what I could tell, they were on the hunt\x01",
            "for someone, but I don't know much more than\x01",
            "that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x10,
        "The whole story was a little fishy if you ask me.\x02",
    )

    CloseMessageWindow()
    Jump("loc_313")

    label("loc_25B")


    ChrTalk(    #3
        0x10,
        (
            "Have you come to stay at our hotel,\x01",
            "perchance?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x10,
        (
            "I'm terribly sorry, but guests are only able to\x01",
            "check in from three o'clock onward.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x10,
        "Could I ask you to come back then?\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_313")

    Jump("loc_331")

    label("loc_316")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 4)), scpexpr(EXPR_END)), "loc_320")
    Jump("loc_331")

    label("loc_320")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 3)), scpexpr(EXPR_END)), "loc_32A")
    Jump("loc_331")

    label("loc_32A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 2)), scpexpr(EXPR_END)), "loc_331")

    label("loc_331")

    TalkEnd(0x10)
    Return()

    # Function_3_152 end

    def Function_4_335(): pass

    label("Function_4_335")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 0)), scpexpr(EXPR_END)), "loc_8A6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EB, 1)), scpexpr(EXPR_END)), "loc_57A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_3F8")

    ChrTalk(    #6
        0xFE,
        "A couple of strange men came in here earlier.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        (
            "They had a truly murderous aura about them\x01",
            "that felt eerily familiar...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xFE,
        "But they couldn't be...could they?\x02",
    )

    CloseMessageWindow()
    Jump("loc_577")

    label("loc_3F8")


    ChrTalk(    #9
        0xFE,
        (
            "I'm due to meet someone here. I'm just waiting\x01",
            "for them to arrive.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xFE,
        (
            "I'm planning on doing some research on Liberl\x01",
            "while I'm here, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xFE,
        (
            "After all, this is the nation now known for\x01",
            "repelling the mighty Erebonian Empire.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xFE,
        (
            "I'm fascinated to see if I can find exactly\x01",
            "where that strength came from.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xFE,
        (
            "Haha. This should prove to be some very \x01",
            "interesting research.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_577")

    Jump("loc_8A3")

    label("loc_57A")

    OP_8C(0xFE, 0, 0)

    ChrTalk(    #14
        0xFE,
        "Oh? Who might the two of you be?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x103, 500)
    Sleep(300)

    ChrTalk(    #15
        0xFE,
        (
            "The sound of your footsteps is unfamiliar to me...\x01",
            "I presume this must be the first time we've met?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x103,
        "#1643FY-Yes. It certainly is...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x151,
        (
            "#1653FUmm...\x02\x03",

            "#1650FAm I right in assuming that you must be\x01",
            "visually impaired, sir?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xFE,
        (
            "Yes, that's right. I'm completely blind in\x01",
            "both eyes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0xFE,
        (
            "Still, if you'll forgive me for saying so,\x01",
            "you're rather an unusual pair, aren't you?\x01",
            "And one of you is a bracer, I believe?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x151, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #20
        0xFE,
        (
            "Haha. There's no need to be so surprised. The air\x01",
            "you have about you reminds me of other bracers\x01",
            "I know, that's all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0xFE,
        (
            "I may have lost my vision, but that has allowed me\x01",
            "to see new things I couldn't before, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x103,
        "#1643FR-Really?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x151,
        "#1650FThat's incredible...\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2F59)

    label("loc_8A3")

    Jump("loc_8C1")

    label("loc_8A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 4)), scpexpr(EXPR_END)), "loc_8B0")
    Jump("loc_8C1")

    label("loc_8B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 3)), scpexpr(EXPR_END)), "loc_8BA")
    Jump("loc_8C1")

    label("loc_8BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 2)), scpexpr(EXPR_END)), "loc_8C1")

    label("loc_8C1")

    TalkEnd(0xFE)
    Return()

    # Function_4_335 end

    def Function_5_8C5(): pass

    label("Function_5_8C5")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #24
        (
            "\x07\x05Office\x01",
            "※Authorized Personnel Only\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_5_8C5 end

    SaveToFile()

Try(main)
