from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'T0510_1 ._SN',
        MapName             = 'Rolent',
        Location            = 'T0510.x',
        MapIndex            = 18,
        MapDefaultBGM       = "ed60016",
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
        "Function_1_9D8",          # 01, 1
    )


    def Function_0_66(): pass

    label("Function_0_66")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x50, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_415")
    OP_A2(0x281)

    ChrTalk(    #0
        0x8,
        (
            "Well, if it isn't Estelle...\x01",
            "and Joshua, too.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x8, 0)

    ChrTalk(    #1
        0x101,
        "#000FHello, Mr. Ashton.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x8, 0)

    ChrTalk(    #2
        0x102,
        "#010FIt's been a while since we last met.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x8,
        "Yes, it has.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x8,
        (
            "So I've heard my boy, Luke, caused\x01",
            "you a lot of trouble, did he?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x8,
        "I'm absolutely ashamed as a father.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x101,
        (
            "#001FI'm sure it's perfectly normal for a\x01",
            "boy his age to be naughty like that.\x02\x03",

            "I mean, even I ran around outside\x01",
            "of town when I was young.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #7
        0x102,
        (
            "#017FYeah, and you're supposed to\x01",
            "be a girl...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x8,
        (
            "Ha ha, you're certainly full of\x01",
            "energy as usual.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x8,
        (
            "I'd love to get you to share some\x01",
            "of that vigor with my new recruits.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x8,
        (
            "I've been thinking recently about\x01",
            "doing a simulated battle to whip\x01",
            "my men into shape.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x8,
        (
            "So I put in a request at the guild\x01",
            "for a few good men or women to\x01",
            "play the part of enemy soldiers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x8,
        (
            "I think the pair of you would be the\x01",
            "perfect fit for the job, so how about\x01",
            "it? Can you do this for me?\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x8, 0x4, 0x4)
    OP_28(0x8, 0x1, 0x1)
    OP_28(0x8, 0x4, 0x2)
    TurnDirection(0x102, 0x8, 400)
    Jump("loc_65A")

    label("loc_415")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x8, 0x1, 0x8000)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5E4")

    ChrTalk(    #13
        0x8,
        (
            "Well, if it isn't Estelle...\x01",
            "and Joshua, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x8,
        (
            "Did you come here after seeing\x01",
            "the bulletin board at the guild?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x8,
        (
            "I've actually been thinking recently\x01",
            "about doing a simulated battle to\x01",
            "whip my men into shape.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x8,
        (
            "So I put in a request at the guild\x01",
            "for a few good men or women to\x01",
            "play the part of enemy soldiers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x8,
        (
            "I think the pair of you would be the\x01",
            "perfect fit for the job, so how about\x01",
            "it? Can you do this for me?\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x8, 0x4, 0x4)
    OP_28(0x8, 0x1, 0x1)
    OP_28(0x8, 0x4, 0x2)
    Jump("loc_65A")

    label("loc_5E4")


    ChrTalk(    #18
        0x8,
        (
            "Have you finished with your\x01",
            "errands?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x8,
        (
            "Will you accept the part of the\x01",
            "enemy soldiers for a simulated\x01",
            "battle?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_65A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9CD")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        0,
        (
            "[Accept]\x01",       # 0
            "[Decline]\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (1, "loc_6BF"),
        (0, "loc_7E8"),
        (SWITCH_DEFAULT, "loc_6BF"),
    )


    label("loc_6BF")

    OP_28(0x8, 0x1, 0x8000)

    ChrTalk(    #20
        0x101,
        (
            "#505FI'm sorry, sir, but\x01",
            "we've got a few errands at the\x01",
            "moment...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x8,
        (
            "I see. That's too bad. I won't try\x01",
            "to force you to take part if you're\x01",
            "busy with other work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x8,
        (
            "If you decide later on that you can\x01",
            "do it, come as soon as possible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x101,
        "#000FAll right, we'll try.\x02",
    )

    CloseMessageWindow()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    Jump("loc_9CA")

    label("loc_7E8")

    OP_28(0x8, 0x4, 0x8)

    ChrTalk(    #24
        0x101,
        "#006FSure, we'll do it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x102,
        "#010FWe'll gladly accept.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x8,
        "Thanks. I really appreciate this.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x8,
        (
            "Go ahead and take a break until\x01",
            "the preparations are ready.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x8,
        (
            "If I don't have you in tip-top\x01",
            "condition then there's no point\x01",
            "in doing the training.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(400)

    ChrTalk(    #29
        0x101,
        (
            "#001FHeh heh, then I'm ready for an\x01",
            "afternoon nap.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x102,
        (
            "#010FAll right then, we'll get ourselves\x01",
            "ready.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x8,
        "Sure, please do what you need to.\x02",
    )

    CloseMessageWindow()
    FadeToDark(3000, 0, -1)
    OP_0D()
    OP_31(0x0, 0xFE, 0x0)
    OP_31(0x1, 0xFE, 0x0)
    NewScene("ED6_DT01/T0500   ._SN", 1, 0, 0)
    IdleLoop()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    Jump("loc_9CA")

    label("loc_9CA")

    Jump("loc_65A")

    label("loc_9CD")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_0_66 end

    def Function_1_9D8(): pass

    label("Function_1_9D8")

    TalkBegin(0x8)
    EventBegin(0x0)
    OP_6D(28890, 0, -73240, 0)
    OP_8C(0x8, 270, 0)
    SetChrPos(0x101, 27710, 0, -72870, 90)
    SetChrPos(0x102, 27790, 0, -73700, 90)
    OP_31(0x0, 0xFE, 0x0)
    OP_31(0x1, 0xFE, 0x0)
    Sleep(2000)

    ChrTalk(    #32
        0x8,
        (
            "Estelle and Joshua. Thanks for\x01",
            "your hard work today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x8,
        (
            "Thanks to you, I think my soldiers\x01",
            "have gotten the wake up call they\x01",
            "needed.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x8, 0)

    ChrTalk(    #34
        0x101,
        (
            "#000FThere's no need to thank us.\x01",
            "It's us who should be thanking you.\x02\x03",

            "This was excellent training.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x8, 0)

    ChrTalk(    #35
        0x102,
        (
            "#010FI agree. This was a good learning\x01",
            "experience.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x8,
        (
            "Ha ha, if you think so then you're\x01",
            "set for life as bracers. \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x8,
        (
            "Though our positions may be\x01",
            "different, we are both here to\x01",
            "serve the public.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x8,
        (
            "Although I can't do much else,\x01",
            "I'll pray for success for the both\x01",
            "of you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x101,
        "#001FSure. And thanks again.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x102,
        "#010FTake care of yourself.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x8,
        (
            "I will. And I hope to be seeing\x01",
            "you again, sometime.\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x17, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #42
        "\x07\x00Quest \x07\x02[Soldier Training] \x07\x00completed!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x1)
    OP_28(0x8, 0x4, 0x10)
    OP_28(0x8, 0x1, 0x8)
    OP_31(0x0, 0xFE, 0x0)
    OP_31(0x1, 0xFE, 0x0)
    EventEnd(0x0)
    ClearMapFlags(0x400000)
    TalkEnd(0x8)
    Return()

    # Function_1_9D8 end

    SaveToFile()

Try(main)
