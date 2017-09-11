from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 洛连特

    CreateScenaFile(
        FileName            = 'T0121_1 ._SN',
        MapName             = 'Rolent',
        Location            = 'T0121.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60010",
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

    ScpFunction(
        "Function_0_66",           # 00, 0
        "Function_1_197",          # 01, 1
        "Function_2_2EE",          # 02, 2
    )


    def Function_0_66(): pass

    label("Function_0_66")

    TalkBegin(0xE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12E")
    OP_A2(0x9)

    ChrTalk(    #0
        0xFE,
        (
            "What's the deal with everything being\x01",
            "in short supply around here?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "Damn it! Somehow I'm going to have\x01",
            "to dig up a Grade-A product before\x01",
            "I head to my next business deal...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_193")

    label("loc_12E")


    ChrTalk(    #2
        0xFE,
        (
            "Somehow I'm going to have to\x01",
            "dig up a Grade-A product before\x01",
            "I head to my next business deal...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_193")

    TalkEnd(0xE)
    Return()

    # Function_0_66 end

    def Function_1_197(): pass

    label("Function_1_197")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D, 0)), scpexpr(EXPR_END)), "loc_1B6")
    OP_2A(0x4, 0x5, 0x6, 0x7, 0x8, 0x9, 0xB, 0xC, 0xD, 0xFFFF)
    Jump("loc_2EA")

    label("loc_1B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 1)), scpexpr(EXPR_END)), "loc_1D3")
    OP_2A(0x4, 0x5, 0x6, 0x7, 0x8, 0x9, 0xB, 0xC, 0xFFFF)
    Jump("loc_2EA")

    label("loc_1D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A, 2)), scpexpr(EXPR_END)), "loc_1F0")
    OP_2A(0x4, 0x5, 0x6, 0x7, 0x8, 0x9, 0xB, 0xC, 0xFFFF)
    Jump("loc_2EA")

    label("loc_1F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 7)), scpexpr(EXPR_END)), "loc_20D")
    OP_2A(0x4, 0x5, 0x6, 0x7, 0x8, 0x9, 0xB, 0xC, 0xFFFF)
    Jump("loc_2EA")

    label("loc_20D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 2)), scpexpr(EXPR_END)), "loc_226")
    OP_2A(0x4, 0x5, 0x6, 0x7, 0x8, 0xB, 0xFFFF)
    Jump("loc_2EA")

    label("loc_226")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 1)), scpexpr(EXPR_END)), "loc_23F")
    OP_2A(0x4, 0x5, 0x6, 0x7, 0x8, 0xB, 0xFFFF)
    Jump("loc_2EA")

    label("loc_23F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_END)), "loc_250")
    OP_2A(0x4, 0xB, 0xFFFF)
    Jump("loc_2EA")

    label("loc_250")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 4)), scpexpr(EXPR_END)), "loc_2A2")
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(72, 320, 56, 3)

    AnonymousTalk(    #3
        "\x07\x05There are no current job listings.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    Jump("loc_2EA")

    label("loc_2A2")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(72, 320, 56, 3)

    AnonymousTalk(    #4
        "\x07\x05There are no current job listings.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_2EA")

    TalkEnd(0xFF)
    Return()

    # Function_1_197 end

    def Function_2_2EE(): pass

    label("Function_2_2EE")

    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_87E")
    Sleep(100)
    OP_AF(0x4, 0xA)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    EventBegin(0x0)
    Sleep(500)

    ChrTalk(    #5
        0x8,
        (
            "#741FGood job, you two. It seems like you\x01",
            "were able to complete your objective\x01",
            "without running into any major problems.\x02\x03",

            "#741FAnother thing to take note of is that depending\x01",
            "on how you handle a job, you may see an increase\x01",
            "or decrease in the amount of pay you receive.\x02\x03",

            "#740FWhen you report the results of your work\x01",
            "to the guild, pay in the form of mira\x01",
            "isn't the only thing you will receive.\x02\x03",

            "You will also accumulate points which are\x01",
            "known as BP (bracer points). BP are an\x01",
            "indication of your achievements as a bracer.\x02\x03",

            "When these points exceed a certain value, you\x01",
            "will advance in rank as a bracer and be awarded\x01",
            "with a piece of special equipment by the guild.\x02\x03",

            "The ranks of a junior bracer start at 9 and\x01",
            "go all the way up to 1. Please set your\x01",
            "sights on making first-rank and work hard.\x02\x03",

            "#740FThe amount of mira and BP you receive will\x01",
            "also be recorded in your Bracer Notebooks,\x01",
            "so please have a look sometime later on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x9,
        (
            "#020FAll that's left to do now is finalize\x01",
            "your training.\x02\x03",

            "Let's head back upstairs, shall we?\x02\x03",

            "I'll talk to you later, Aina.\x01",
            "And sorry about putting more work\x01",
            "on your plate today than usual.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x8,
        (
            "#741FDon't worry about it. Training new\x01",
            "bracers is important for the future\x01",
            "of the guild.\x02\x03",

            "I fully intend to work these two\x01",
            "to the bone in any case.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x101,
        "#008FTo the b-bone...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x102,
        (
            "#019FAnd knowing Schera it'll involve\x01",
            "the whip...\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(500, 0, -1)
    OP_0D()
    Call(0, 23)
    Jump("loc_9AB")

    label("loc_87E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_A9(0x4)"), scpexpr(EXPR_END)), "loc_924")
    Sleep(200)

    ChrTalk(    #10
        0x8,
        (
            "#740FGood work. It seems like you completed\x01",
            "your objective without any trouble.\x02\x03",

            "If you finish any other jobs, please\x01",
            "come back and report again.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9AB")

    label("loc_924")

    Sleep(200)

    ChrTalk(    #11
        0x8,
        (
            "#740FIt looks like there's nothing to\x01",
            "report at this time.\x02\x03",

            "If you finish any other jobs, please\x01",
            "come back and report again.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9AB")

    Return()

    # Function_2_2EE end

    SaveToFile()

Try(main)
