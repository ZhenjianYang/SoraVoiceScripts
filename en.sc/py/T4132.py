from ED6SCScenarioHelper import *

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
        'Agate',                                # 10
        'Scherazard',                           # 11
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
        'ED6_DT07/CH00050 ._CH',             # 01
        'ED6_DT07/CH00020 ._CH',             # 02
    )

    AddCharChipPat(
        'ED6_DT07/CH01220P._CP',             # 00
        'ED6_DT07/CH00050P._CP',             # 01
        'ED6_DT07/CH00020P._CP',             # 02
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
        X                   = 6100,
        Z                   = 0,
        Y                   = 1700,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 6100,
        Z                   = 0,
        Y                   = 1700,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
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
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_16A",          # 00, 0
        "Function_1_198",          # 01, 1
        "Function_2_1BE",          # 02, 2
        "Function_3_1C3",          # 03, 3
        "Function_4_955",          # 04, 4
        "Function_5_9B9",          # 05, 5
        "Function_6_A21",          # 06, 6
    )


    def Function_0_16A(): pass

    label("Function_0_16A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_178")
    Jump("loc_197")

    label("loc_178")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_197")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_192")
    ClearChrFlags(0x9, 0x80)
    Jump("loc_197")

    label("loc_192")

    ClearChrFlags(0xA, 0x80)

    label("loc_197")

    Return()

    # Function_0_16A end

    def Function_1_198(): pass

    label("Function_1_198")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1B4")
    OP_B1("t4132_y")
    Jump("loc_1BD")

    label("loc_1B4")

    OP_B1("t4132_n")

    label("loc_1BD")

    Return()

    # Function_1_198 end

    def Function_2_1BE(): pass

    label("Function_2_1BE")

    Call(0, 3)
    Return()

    # Function_2_1BE end

    def Function_3_1C3(): pass

    label("Function_3_1C3")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C8, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1D6")
    Jump("loc_201")

    label("loc_1D6")

    Call(6, 6)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1F0")
    OP_A9(0xCC)
    TalkEnd(0x8)
    Return()

    label("loc_1F0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_201")
    TalkEnd(0x8)
    Return()

    label("loc_201")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_321")

    ChrTalk(    #0
        0x8,
        (
            "Thanks to the queen, I'm still somehow\x01",
            "able to keep up with my business.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x8,
        (
            "Even without orbments, I'm striving\x01",
            "to maintain the same level of service\x01",
            "I always offer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x8,
        (
            "Sadly, there's not much I can\x01",
            "do about light or heat.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x8,
        "I hope the orbments are restored soon...\x02",
    )

    CloseMessageWindow()
    Jump("loc_951")

    label("loc_321")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_3EE")

    ChrTalk(    #4
        0x8,
        "Miss Estelle, will you be departing?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x8,
        (
            "We sincerely hope you will make use of our\x01",
            "hotel upon your next visit to Grancel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x8,
        (
            "Our entire staff will be eagerly waiting\x01",
            "to greet you again!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_951")

    label("loc_3EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_574")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2CC, 5)), scpexpr(EXPR_END)), "loc_481")

    ChrTalk(    #7
        0x8,
        (
            "Miss Renne, the young lady who was\x01",
            "staying with you last night, yes?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x8,
        (
            "If I see her, I'll make sure to\x01",
            "contact the guild.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_571")

    label("loc_481")


    ChrTalk(    #9
        0x101,
        "#1011FFritz, have you seen Renne?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x8,
        (
            "...Miss Renne, the young lady who was\x01",
            "staying with you last night, yes?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x8,
        "No, I'm afraid she has not come here.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x101,
        "#1015FAw, man...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x8,
        (
            "If I see her, I'll make sure to\x01",
            "contact the guild.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1665)

    label("loc_571")

    Jump("loc_951")

    label("loc_574")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_603")

    ChrTalk(    #14
        0x8,
        (
            "It's just about time for our guests\x01",
            "who went out to be returning...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x8,
        (
            "Haha, the day just flies by when\x01",
            "I'm hard at work!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_951")

    label("loc_603")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_776")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_756")

    ChrTalk(    #16
        0x8,
        (
            "I was trying not to worry about the\x01",
            "threatening letter, given how vague\x01",
            "its contents were...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x8,
        (
            "But I must admit, having the Bracer Guild\x01",
            "investigate the matter is quite a relief.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x8,
        (
            "I suppose somewhere deep within me,\x01",
            "I was still worried as can be.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x8,
        (
            "If there's anything I can do,\x01",
            "I'd be happy to assist.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_773")

    label("loc_756")


    ChrTalk(    #20
        0x8,
        "*sigh* How worrisome...\x02",
    )

    CloseMessageWindow()

    label("loc_773")

    Jump("loc_951")

    label("loc_776")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_951")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C8, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_883")

    ChrTalk(    #21
        0x101,
        "#1001FHeya, Fritz!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x8,
        (
            "Oh, Estelle... I haven't seen you since\x01",
            "the birthday celebrations, I believe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x8,
        (
            "Are you here on business today?\x01",
            "Please, enjoy your stay.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x101,
        (
            "#1015F(Huh...?)\x02\x03",

            "(Is it just my imagination?\x01",
            "He doesn't look too well...)\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1644)
    Jump("loc_951")

    label("loc_883")


    ChrTalk(    #25
        0x8,
        (
            "Perhaps it's because the non-aggression\x01",
            "pact signing is drawing near...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x8,
        (
            "But lately, I've received countless\x01",
            "more inquiries about stays from\x01",
            "foreign guests.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x8,
        "Haha. Busy times are on their way!\x02",
    )

    CloseMessageWindow()

    label("loc_951")

    TalkEnd(0x8)
    Return()

    # Function_3_1C3 end

    def Function_4_955(): pass

    label("Function_4_955")

    TalkBegin(0xFE)

    ChrTalk(    #28
        0xFE,
        (
            "#050FEstelle, what're you here for?\x02\x03",

            "This is my area, ain't it?\x01",
            "You go check elsewhere.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_4_955 end

    def Function_5_9B9(): pass

    label("Function_5_9B9")

    TalkBegin(0xFE)

    ChrTalk(    #29
        0xFE,
        (
            "#020FEstelle, what is it?\x02\x03",

            "The hotel is my job today.\x01",
            "You should get to your assigned area.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_5_9B9 end

    def Function_6_A21(): pass

    label("Function_6_A21")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #30
        (
            "\x07\x05Office\x01",
            "※Employees Only\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_6_A21 end

    SaveToFile()

Try(main)
