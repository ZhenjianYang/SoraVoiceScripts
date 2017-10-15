from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 洛连特

    CreateScenaFile(
        FileName            = 'T2130_1 ._SN',
        MapName             = 'Rolent',
        Location            = 'C0403.x',
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


    ScpFunction(
        "Function_0_AA",           # 00, 0
        "Function_1_D15",          # 01, 1
        "Function_2_6A83",         # 02, 2
        "Function_3_6A95",         # 03, 3
        "Function_4_6A9F",         # 04, 4
        "Function_5_6AB8",         # 05, 5
        "Function_6_6B74",         # 06, 6
        "Function_7_6B90",         # 07, 7
        "Function_8_6BD4",         # 08, 8
        "Function_9_6BF5",         # 09, 9
        "Function_10_6C11",        # 0A, 10
        "Function_11_6C6B",        # 0B, 11
        "Function_12_6CD2",        # 0C, 12
        "Function_13_6CF2",        # 0D, 13
        "Function_14_6D1C",        # 0E, 14
        "Function_15_6DCE",        # 0F, 15
        "Function_16_6E03",        # 10, 16
        "Function_17_6E46",        # 11, 17
        "Function_18_6E7B",        # 12, 18
    )


    def Function_0_AA(): pass

    label("Function_0_AA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_233")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19F")

    ChrTalk(    #0
        0xFE,
        (
            "The reformation of the youths in the\x01",
            "warehouse district is one of the few\x01",
            "bright pieces of news.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "I am making an effort to greet them\x01",
            "when I see them on street corners.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0xFE,
        "I hope they continue along this path.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x3)
    Jump("loc_230")

    label("loc_19F")


    ChrTalk(    #3
        0xFE,
        (
            "The reformation of the youths in the\x01",
            "warehouse district is one of the few\x01",
            "bright pieces of news.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xFE,
        "I hope they continue along this path.\x02",
    )

    CloseMessageWindow()

    label("loc_230")

    Jump("loc_D11")

    label("loc_233")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_3DD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_347")

    ChrTalk(    #5
        0xFE,
        (
            "The moment orbments became unusable,\x01",
            "the city all but erupted...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xFE,
        (
            "Enraged mobs of citizens pushed into\x01",
            "the guildhouse and mayoral mansion...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        (
            "Thankfully, Father Theodore was able\x01",
            "to persuade them somehow, but things\x01",
            "were moments from a riot.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)
    Jump("loc_3DA")

    label("loc_347")


    ChrTalk(    #8
        0xFE,
        (
            "The moment orbments became unusable,\x01",
            "the city all but erupted...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xFE,
        (
            "It was almost as if people's rationality\x01",
            "lost power at the same moment.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3DA")

    Jump("loc_D11")

    label("loc_3DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_663")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x67, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_29(0x67, 0x1, 0x4000)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4B8")

    ChrTalk(    #10
        0xFE,
        (
            "I invited an apprentice bracer as a\x01",
            "guest teacher, but it was...interesting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xFE,
        (
            "They couldn't even remember the\x01",
            "bracer code.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xFE,
        (
            "*siiigh* I wish they would have\x01",
            "studied a bit more.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_660")

    label("loc_4B8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x67, 0x1, 0x4000)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_576")

    ChrTalk(    #13
        0xFE,
        (
            "Oh, if it isn't the bracers!\x01",
            "Thank you for the other day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        "All the children enjoyed your class.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xFE,
        (
            "I hope you will continue to strive\x01",
            "for the peace of the kingdom.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_660")

    label("loc_576")


    ChrTalk(    #16
        0xFE,
        (
            "Oh, if it isn't the bracers!\x01",
            "Thank you for the other day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0xFE,
        (
            "I do wish you would have studied\x01",
            "a little more in preparation for it, though...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xFE,
        (
            "It's hard to gain the trust of the children\x01",
            "if you can't answer their questions.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_660")

    Jump("loc_D11")

    label("loc_663")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_A3D")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x67, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x67, 0x1, 0x4000)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9B9")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x67, 0x1, 0x4000)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7E7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_6F0")

    ChrTalk(    #19
        0xFE,
        "You did very well today.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xFE,
        (
            "The children had a great time,\x01",
            "and it's all thanks to you.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7E4")

    label("loc_6F0")

    OP_A2(0x3)

    ChrTalk(    #21
        0xFE,
        "That couldn't have gone better!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xFE,
        "The children had a wonderful time.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xFE,
        (
            "I am aware you bracers are\x01",
            "very busy, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0xFE,
        (
            "I hope you will continue to value these\x01",
            "chances to speak with the citizens as\x01",
            "you travel across the country.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7E4")

    Jump("loc_9B6")

    label("loc_7E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_883")

    ChrTalk(    #25
        0xFE,
        (
            "Thank you so much for your help\x01",
            "today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0xFE,
        (
            "...Though you might want to give\x01",
            "yourself a little refresher before\x01",
            "giving another lecture, hmm?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9B6")

    label("loc_883")

    OP_A2(0x3)

    ChrTalk(    #27
        0xFE,
        "That was an...interesting lecture.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0xFE,
        (
            "I am aware you bracers are very\x01",
            "busy, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xFE,
        (
            "I do hope that you'll do a little more\x01",
            "studying yourself before helping\x01",
            "others.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0xFE,
        (
            "You all, who are in charge of the peace\x01",
            "throughout the regions, are the heroes\x01",
            "to many children. Please do not forget that.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9B6")

    Jump("loc_A3A")

    label("loc_9B9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x67, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_9CA")
    Call(1, 1)
    Jump("loc_A3A")

    label("loc_9CA")


    ChrTalk(    #31
        0xFE,
        "*sigh* Isn't the guest teacher here yet?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xFE,
        (
            "At this rate, class will be over before\x01",
            "they even show up...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A3A")

    Jump("loc_D11")

    label("loc_A3D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 4)), scpexpr(EXPR_END)), "loc_AA9")

    ChrTalk(    #33
        0xFE,
        (
            "It's been rather noisy outside for\x01",
            "some time now...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xFE,
        "Perhaps it's just my imagination...\x02",
    )

    CloseMessageWindow()
    Jump("loc_D11")

    label("loc_AA9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_C72")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_B4F")

    ChrTalk(    #35
        0xFE,
        (
            "The bracer we were going to have present\x01",
            "as a guest teacher is absent, apparently.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0xFE,
        (
            "I must ask the guild for a\x01",
            "replacement immediately!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C6F")

    label("loc_B4F")

    OP_A2(0x3)

    ChrTalk(    #37
        0xFE,
        "*siiigh* We're in quite the predicament...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xFE,
        (
            "I had intended for a bracer to come and\x01",
            "be a guest speaker for Sunday School.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xFE,
        (
            "Unfortunately, that person is absent\x01",
            "because guild work came up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0xFE,
        (
            "*sigh* I'll have to make a request to\x01",
            "the guild for a replacement immediately!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C6F")

    Jump("loc_D11")

    label("loc_C72")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_END)), "loc_D11")

    ChrTalk(    #41
        0xFE,
        (
            "The election activities can be heard\x01",
            "even from here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0xFE,
        (
            "It is frustrating, I admit. Almost seems\x01",
            "to disrupt the peace of those who come\x01",
            "to pray.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D11")

    TalkEnd(0xFE)
    Return()

    # Function_0_AA end

    def Function_1_D15(): pass

    label("Function_1_D15")

    EventBegin(0x0)
    OP_4A(0xD, 255)
    Fade(1000)
    SetChrPos(0xF7, 54000, 0, 50610, 0)
    SetChrPos(0x101, 53000, 0, 50800, 0)
    SetChrPos(0x104, 52900, 0, 49660, 0)
    SetChrPos(0x127, 54100, 0, 49500, 0)
    OP_8C(0xD, 180, 0)
    OP_69(0x101, 0x0)
    OP_0D()
    Sleep(1000)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x67, 0x1, 0x8000)"), scpexpr(EXPR_END)), "loc_DCB")

    ChrTalk(    #43
        0xD,
        "Oh, my...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0xD,
        (
            "Are you able to help out as a guest\x01",
            "teacher yet?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EBC")

    label("loc_DCB")


    ChrTalk(    #45
        0xD,
        "Oh, my...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0xD,
        "Are you here because you saw my request?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x101,
        (
            "#1000FYes, ma'am! Sure did.\x02\x03",

            "It's pretty urgent, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0xD,
        (
            "Yes. Today, I'd like to ask you to act\x01",
            "as a guest teacher at Sunday School.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0xD,
        "How about it? Are you available?\x02",
    )

    CloseMessageWindow()

    label("loc_EBC")

    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Hear an Explanation of the Job\x01",      # 0
            "Leave\x01",                               # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FE8")

    ChrTalk(    #50
        0x101,
        "#1007FSorry, I can't right now.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0xD,
        "That's too bad...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0xD,
        "Still, I suppose there's no helping it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0xD,
        (
            "All right, once you have finished your\x01",
            "business, please come by immediately.\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x67, 0x1, 0x8000)
    OP_30(0x0)
    EventEnd(0x0)
    Return()

    label("loc_FE8")


    ChrTalk(    #54
        0x101,
        (
            "#1000FYeah, I can do it.\x02\x03",

            "#1015FI'm not super confident, but\x01",
            "I'll give it my best shot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0xD,
        (
            "Thank you very much.\x01",
            "I really appreciate it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0xD,
        (
            "I had asked a bracer named Carna to be\x01",
            "the guest lecturer, but she suddenly had\x01",
            "to leave on guild business.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0xD,
        (
            "It put the church in a fix, and I was\x01",
            "very disheartened.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_1161")

    ChrTalk(    #58
        0x106,
        "#050FI see... So that's why it's so sudden.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1192")

    label("loc_1161")


    ChrTalk(    #59
        0x103,
        "#020FI see... So that's why it's so sudden.\x02",
    )

    CloseMessageWindow()

    label("loc_1192")


    ChrTalk(    #60
        0x101,
        "#1011F...So, what should I do? \x02",
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0xD,
        "First, come into the side room.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0xD,
        "I'll explain what I'd like for the class there.\x02",
    )

    CloseMessageWindow()
    OP_28(0x67, 0x4, 0x4)
    OP_28(0x67, 0x4, 0x8)
    OP_28(0x67, 0x1, 0x1)
    OP_28(0x67, 0x1, 0x2)
    FadeToDark(1500, 0, -1)
    OP_0D()
    Sleep(1000)
    SetChrPos(0x101, -15920, 0, 42640, 0)
    SetChrPos(0xD, -15920, 0, 43790, 180)
    SetChrPos(0xF7, -16200, 0, 45190, 180)
    SetChrPos(0x104, -17400, 0, 44260, 135)
    SetChrPos(0x127, -17380, 0, 42570, 90)
    OP_6D(-11190, 0, 49840, 0)
    OP_51(0x1A, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x104, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1A, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x104, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1A, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x104, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_12E2():
        OP_69(0x1A, 0xBB8)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_12E2)
    FadeToBright(1500, 0)
    OP_0D()
    Sleep(1000)
    WaitChrThread(0xD, 0x1)
    Sleep(400)

    ChrTalk(    #63
        0x101,
        (
            "#1012F...I see. \x02\x03",

            "#1006FOkay. Yeah, I think I get the gist.\x02\x03",

            "Start with an explanation of the guild,\x01",
            "move on to an overview of a bracer's\x01",
            "job...\x02\x03",

            "And then last but not least, answer the\x01",
            "kids' questions correctly, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0xD,
        "Yes, that will be plenty.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0xD,
        (
            "If you'll excuse me, I'll be going back\x01",
            "to class.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0xD,
        (
            "I'll call you momentarily, so please\x01",
            "wait here until then.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1480():

        label("loc_1480")

        TurnDirection(0xFE, 0xD, 400)
        OP_48()
        Jump("loc_1480")

    QueueWorkItem2(0xF7, 1, lambda_1480)

    def lambda_1491():

        label("loc_1491")

        TurnDirection(0xFE, 0xD, 400)
        OP_48()
        Jump("loc_1491")

    QueueWorkItem2(0x104, 1, lambda_1491)

    def lambda_14A2():

        label("loc_14A2")

        TurnDirection(0xFE, 0xD, 400)
        OP_48()
        Jump("loc_14A2")

    QueueWorkItem2(0x127, 1, lambda_14A2)
    OP_8B(0xD, 0xFFFFC7CA, 0xB7F2, 0x190)

    def lambda_14C0():
        OP_6D(-14950, 0, 45890, 2000)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_14C0)
    OP_8E(0xD, 0xFFFFC7C0, 0x0, 0xB0FE, 0x7D0, 0x0)
    OP_44(0xF7, 0x1)
    OP_44(0x104, 0x1)
    OP_44(0x127, 0x1)
    OP_8E(0xD, 0xFFFFCC48, 0x0, 0xB798, 0x7D0, 0x1)
    OP_9F(0xD, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    def lambda_1517():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_1517)
    OP_8E(0xD, 0xFFFFD404, 0x0, 0xB798, 0x7D0, 0x0)
    SetChrPos(0xD, 48141, 1000, 50075, 180)
    OP_9F(0xD, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    WaitChrThread(0xD, 0x2)
    Sleep(800)

    def lambda_1563():
        TurnDirection(0x104, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1563)

    def lambda_1571():
        TurnDirection(0x127, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x127, 1, lambda_1571)
    OP_43(0xF7, 0x1, 0x1, 0x6)
    OP_6D(-16500, 0, 44400, 2000)
    Sleep(400)

    ChrTalk(    #67
        0x104,
        (
            "#030FStill...\x02\x03",

            "Truly, the world is a strange place.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_161C")

    ChrTalk(    #68
        0x106,
        (
            "#050FOh, for once we agree.\x02\x03",

            "I was just thinking that myself.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_165F")

    label("loc_161C")


    ChrTalk(    #69
        0x103,
        (
            "#027FOh, for once we agree.\x02\x03",

            "I was just thinking that myself.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_165F")

    OP_62(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    TurnDirection(0x101, 0x104, 400)
    Sleep(1000)

    ChrTalk(    #70
        0x101,
        (
            "#1011F#6PHmm? What's up?\x02\x03",

            "Is there something on my face?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x104,
        (
            "#031FNo, but not even I could have predicted\x01",
            "this.\x02\x03",

            "To think the day would come when\x01",
            "Estelle would take the altar.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x127,
        "#151FSure is a big surprise, isn't it?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_17C8")

    ChrTalk(    #73
        0x106,
        (
            "#051FYeah, seriously.\x02\x03",

            "This one's more the bein' taught\x01",
            "type than the teachin' type.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1859")

    label("loc_17C8")


    ChrTalk(    #74
        0x103,
        (
            "#021FIt just means that a certain girl famous\x01",
            "for skipping Sunday School has grown\x01",
            "up well, I guess.\x02\x03",

            "Oh, Estelle, your mentor is so proud!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1859")

    OP_62(0x101, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    TurnDirection(0x101, 0xF7, 400)
    Sleep(1000)

    ChrTalk(    #75
        0x101,
        (
            "#1009F#6PW-Well, that's sure nice to say.\x01",
            "I think.\x02\x03",

            "True, I'm not super confident, but\x01",
            "I should be fine teaching some kids.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_195F")

    ChrTalk(    #76
        0x106,
        (
            "#053FThat's nice and all, but...\x02\x03",

            "#050F...Whatever. I'm gonna nap until it's over.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_19A9")

    label("loc_195F")


    ChrTalk(    #77
        0x103,
        (
            "#026FI hope so, but...\x02\x03",

            "#020FWell, I'll be relaxing until it's over.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_19A9")

    TurnDirection(0x101, 0x104, 400)

    ChrTalk(    #78
        0x101,
        "#1000F#6PWhat are you gonna do, Olivier?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x104,
        (
            "#031FWhile I have little to offer, you have my\x01",
            "full attention and support.\x02\x03",

            "The class should be well visible from\x01",
            "the second floor here, so I'd like to watch\x01",
            "from there.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x127, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(400)

    ChrTalk(    #80
        0x127,
        (
            "#153FOhh, nice idea.\x02\x03",

            "#151FI should take tons of pictures!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    TurnDirection(0x101, 0x127, 400)
    Sleep(1000)

    ChrTalk(    #81
        0x101,
        (
            "#1019F#6P...Please don't screw anything up,\x01",
            "you two.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1500, 0, -1)
    OP_0D()
    Sleep(1000)
    SetMapFlags(0x400000)
    ClearChrFlags(0x19, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_1B73")
    SetChrPos(0x103, 52248, 5000, 50355, 90)

    label("loc_1B73")

    SetChrPos(0x104, 52248, 5000, 49470, 90)
    SetChrPos(0xD, 52960, 0, 48670, 90)
    OP_4A(0xC, 255)
    OP_4A(0xF, 255)
    OP_4A(0x11, 255)
    OP_4A(0x12, 255)
    OP_4A(0x10, 255)
    OP_4A(0xB, 255)
    OP_6D(52220, 5000, 48532, 0)
    OP_6B(3789, 0)
    FadeToBright(1500, 0)
    OP_0D()
    Sleep(1000)

    def lambda_1BDC():
        OP_6D(58920, 1000, 50630, 3000)
        ExitThread()

    QueueWorkItem(0x1A, 0, lambda_1BDC)

    def lambda_1BF4():
        OP_6B(2800, 3000)
        ExitThread()

    QueueWorkItem(0x1A, 2, lambda_1BF4)
    OP_6C(320000, 3000)
    WaitChrThread(0x1A, 0x1)

    ChrTalk(    #82
        0xC,
        "Now, then--\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0xC,
        (
            "Everyone, we're going to have a guest\x01",
            "teacher for the remainder of class.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0xC,
        (
            "They've taken time out of their busy\x01",
            "schedule to come speak to us, so don't\x01",
            "be rude, okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0xF,
        "#3POkaaaaay.\x02",
    )


    ChrTalk(    #86
        0x11,
        "#2POkaaaaay.\x02",
    )


    ChrTalk(    #87
        0x12,
        "#4POkaaaaay.\x02",
    )


    ChrTalk(    #88
        0x10,
        "#1POkaaaaay.\x02",
    )

    OP_56(0x1)
    OP_59()
    OP_8C(0xC, 90, 400)
    OP_8E(0xC, 0xF050, 0x3E8, 0xCC38, 0x7D0, 0x0)
    OP_8C(0xC, 180, 400)
    OP_6D(54420, 0, 51310, 2000)
    OP_8B(0xD, 0xCA84, 0xC49A, 0x190)

    ChrTalk(    #89
        0xD,
        "All right, come on out.\x02",
    )

    CloseMessageWindow()
    OP_43(0x1A, 0x0, 0x1, 0x2)
    OP_43(0xF, 0x0, 0x1, 0x5)
    OP_43(0x11, 0x0, 0x1, 0x5)
    OP_43(0x10, 0x0, 0x1, 0x5)
    OP_43(0x12, 0x0, 0x1, 0x5)
    OP_9F(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x101, 50390, 0, 50280, 90)

    def lambda_1DB5():

        label("loc_1DB5")

        TurnDirection(0xD, 0x101, 400)
        OP_48()
        Jump("loc_1DB5")

    QueueWorkItem2(0xD, 1, lambda_1DB5)

    def lambda_1DC6():

        label("loc_1DC6")

        TurnDirection(0xC, 0x101, 400)
        OP_48()
        Jump("loc_1DC6")

    QueueWorkItem2(0xC, 1, lambda_1DC6)

    def lambda_1DD7():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1DD7)
    OP_8E(0x101, 0xDB60, 0x3E8, 0xC468, 0x7D0, 0x0)
    OP_8E(0x101, 0xE196, 0x3E8, 0xCBE8, 0x7D0, 0x0)
    OP_8E(0x101, 0xE65A, 0x3E8, 0xCBB6, 0x7D0, 0x0)
    OP_8C(0x101, 180, 400)
    Sleep(500)
    WaitChrThread(0x1A, 0x0)
    OP_44(0xF, 0x0)
    OP_44(0x11, 0x0)
    OP_44(0x10, 0x0)
    OP_44(0x12, 0x0)

    def lambda_1E46():
        OP_8C(0xF, 0, 400)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_1E46)

    def lambda_1E54():
        OP_8C(0x11, 0, 400)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_1E54)

    def lambda_1E62():
        OP_8C(0x10, 0, 400)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_1E62)
    OP_8C(0x12, 315, 400)

    ChrTalk(    #90
        0x12,
        "#2PMiss, who are you?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x12, 400)
    Sleep(250)

    ChrTalk(    #91
        0x101,
        (
            "#1016FI-I was just about to introduce myself!\x01",
            "Gimme a sec...\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    OP_44(0xD, 0x1)
    OP_44(0xC, 0x1)
    OP_8C(0x101, 180, 400)
    Sleep(1000)

    ChrTalk(    #92
        0x101,
        (
            "#1018F...All right, well, hello!\x02\x03",

            "I'm Estelle Bright.\x02\x03",

            "I'm still pretty new to the job,\x01",
            "but I'm what we call a bracer.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x12, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x11, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x10, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #93
        0xF,
        "#5PWhaaa...? You're a BRACER?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0x12,
        "#2PNo way! That's so cool!!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0x11,
        "#5PHow old are you, miss?!\x02",
    )

    CloseMessageWindow()
    OP_8C(0xC, 180, 400)

    ChrTalk(    #96
        0xC,
        "Now, now, we'll have time for questions after.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0xC,
        (
            "First, let's have our guest review\x01",
            "what we've already gone over.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x101, 400)

    ChrTalk(    #98
        0xC,
        "If you wouldn't mind, Miss Estelle?\x02",
    )

    CloseMessageWindow()
    OP_43(0xC, 0x1, 0x1, 0x7)
    OP_43(0xD, 0x1, 0x1, 0x8)
    WaitChrThread(0xC, 0x1)
    SetChrChipByIndex(0x101, 10)
    SetChrSubChip(0x101, 1)
    Sleep(400)

    ChrTalk(    #99
        0x101,
        "#1010FAhem!...\x02",
    )

    CloseMessageWindow()
    Sleep(400)
    SetChrChipByIndex(0x101, 65535)
    Sleep(600)

    ChrTalk(    #100
        0x101,
        (
            "#1006FOkay! Is everyone ready?\x02\x03",

            "Let's go over today's class real quick.\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    Sleep(400)
    SetChrFlags(0xB, 0x80)
    OP_20(0x3E8)
    Fade(1000)
    OP_6D(59000, 1000, 53470, 0)
    OP_67(0, 3820, -10000, 0)
    OP_6B(3370, 0)
    OP_6C(0, 0)
    OP_6E(262, 0)
    SetChrSubChip(0xF, 0)
    SetChrSubChip(0x11, 0)
    SetChrSubChip(0x10, 0)
    SetChrSubChip(0x12, 0)
    OP_0D()
    Sleep(400)
    OP_1D(0x19)
    Sleep(400)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #101
        (
            "\x07\x05CLASS BEGIN!\x01",
            "～About All Bracer Activities～\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #102
        (
            "\x07\x05Choose the correct answer and guide\x01",
            "this special class to success!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Sleep(400)

    ChrTalk(    #103
        0x101,
        (
            "#1006FFirst, let's talk about my job as a bracer.\x02\x03",

            "So, a bracer is a specialist\x01",
            "at investigation and combat.\x02\x03",

            "And our main duty as bracers is...\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 16, -1, -1)

    AnonymousTalk(    #104
        "\x18What is a bracer's main duty?\x02",
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        -1,
        150,
        0,
        (
            "1) Security of nations' borders and maintaining public order\x01",      # 0
            "2) Protection of the peace and citizenry of local regions\x01",         # 1
            "3) Discovery and sealing of ruin relics\x01",                           # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2462"),
        (1, "loc_25A1"),
        (2, "loc_26B4"),
        (SWITCH_DEFAULT, "loc_27DA"),
    )


    label("loc_2462")


    ChrTalk(    #105
        0x101,
        (
            "#1006F...The security of nations' borders\x01",
            "and maintaining public order.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    SetChrChipByIndex(0x101, 10)
    SetChrSubChip(0x101, 1)
    Sleep(1000)
    OP_43(0x101, 0x1, 0x1, 0xA)

    ChrTalk(    #106
        0x101,
        (
            "#1015FUh, er, to protect public order, it's\x01",
            "necessary to, um, prevent invasion\x01",
            "from foreign enemies.\x02\x03",

            "(That seems wrong somehow...\x01",
            "Augh. I just need to get the ball\x01",
            "rolling at this point.)\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x101, 65535)
    Jump("loc_27DA")

    label("loc_25A1")


    ChrTalk(    #107
        0x101,
        (
            "#1006F...The protection of the peace and citizenry of\x01",
            "local regions.\x02\x03",

            "We don't just slay monsters and prevent crimes,\x01",
            "either. Bracers protect goods in transit and even\x01",
            "look for lost items. We help in a variety of ways.\x02\x03",

            "#1001F(All right! That was perfect!)\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_27DA")

    label("loc_26B4")


    ChrTalk(    #108
        0x101,
        "#1006F...The discovery and sealing of ruin relics.\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    SetChrChipByIndex(0x101, 10)
    SetChrSubChip(0x101, 1)
    Sleep(1000)
    OP_43(0x101, 0x1, 0x1, 0xA)

    ChrTalk(    #109
        0x101,
        (
            "#1008FW-Well, that's not all we do, but lately\x01",
            "we've found some pretty dangerous\x01",
            "stuff, you know?\x02\x03",

            "#1007F(That's SO obviously wrong, but...\x01",
            "I just need to play it cool and keep\x01",
            "going.)\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x101, 65535)
    Jump("loc_27DA")

    label("loc_27DA")

    Call(1, 12)

    ChrTalk(    #110
        0x101,
        (
            "#1000FBracers are broadly divided into two groups:\x01",
            "senior bracers and junior bracers.\x02\x03",

            "Of those, junior bracers are what you might\x01",
            "call trainees, and...\x02\x03",

            "By successfully completing missions and\x01",
            "training hard, they eventually earn a promotion\x01",
            "to become full bracers.\x02\x03",

            "#1015FBut, even once you become a full bracer,\x01",
            "you're further divided up into different classes.\x02\x03",

            "We call these ranks, and each rank is\x01",
            "assigned in accordance to your experience\x01",
            "and success...\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 16, -1, -1)

    AnonymousTalk(    #111
        "\x18How many ranks are there for senior bracers?\x02",
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        -1,
        150,
        0,
        (
            "1) Seven ranks from G to A\x01",                 # 0
            "2) Five ranks from Basic to High\x01",           # 1
            "3) Nine ranks from Class 9 to Class 1\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2A9E"),
        (1, "loc_2C3A"),
        (2, "loc_2D84"),
        (SWITCH_DEFAULT, "loc_2E4F"),
    )


    label("loc_2A9E")


    ChrTalk(    #112
        0x101,
        (
            "#1006FThere are seven ranks, from G to A.\x02\x03",

            "These are the only formal ranks, and when\x01",
            "a bracer is close to being promoted, a + is\x01",
            "added to said rank.\x02\x03",

            "#1015FFurthermore, there's also an S rank, but it's\x01",
            "kind of an unofficial honorary rank given to\x01",
            "persons who have performed exceptional deeds.\x02\x03",

            "#1006FSo, publicly, A rank bracers are the highest\x01",
            "bracers in the guild.\x02\x03",

            "(Yes! I am KILLING this.)\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_2E4F")

    label("loc_2C3A")


    ChrTalk(    #113
        0x101,
        "#1006FThere are five ranks from 'Basic' to 'High.'\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #114
        0x101,
        (
            "#1016FI-It's very easy to understand, isn't it?\x01",
            "Though it's also hard to, um, express in whole\x01",
            "lot of detail. Yeah, let's go with that...\x02\x03",

            "(This all sounds way too bogus... I can see in\x01",
            "their beady eyes that they're onto me!)\x02",
        )
    )

    CloseMessageWindow()
    OP_43(0x101, 0x1, 0x1, 0xB)
    Sleep(1000)
    Jump("loc_2E4F")

    label("loc_2D84")


    ChrTalk(    #115
        0x101,
        (
            "#1006FThere are nine ranks from Class 9 to Class 1.\x02\x03",

            "As you perform your job successfully, you\x01",
            "receive promotions and move up the ranks.\x02\x03",

            "#1015F(Huh? Wait, wasn't that for junior bracers?\x01",
            "Crap.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E4F")

    label("loc_2E4F")

    Call(1, 12)

    ChrTalk(    #116
        0x101,
        (
            "#1011FAll right, let's talk about the organization\x01",
            "that manages bracers, the Bracer Guild.\x02\x03",

            "#1000FI think you learned this in class, but the\x01",
            "guild operates not just in the Liberl Kingdom,\x01",
            "but all over.\x02\x03",

            "This global organization was established\x01",
            "about the same time as the Orbal Revolution,\x01",
            "which was...\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 16, -1, -1)

    AnonymousTalk(    #117
        "\x18When was the Bracer Guild established?\x02",
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        -1,
        150,
        0,
        (
            "1) About 10 years ago\x01",      # 0
            "2) About 30 years ago\x01",      # 1
            "3) About 50 years ago\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_304F"),
        (1, "loc_3114"),
        (2, "loc_31CA"),
        (SWITCH_DEFAULT, "loc_32BC"),
    )


    label("loc_304F")


    ChrTalk(    #118
        0x101,
        "#1000FRoughly ten years ago.\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)
    OP_43(0x101, 0x1, 0x1, 0xA)

    ChrTalk(    #119
        0x101,
        (
            "#1008F...Surprisingly recent, huh? Haha.\x02\x03",

            "(Wait. Ten years ago was the Hundred Days\x01",
            "War, wasn't it...? Curse my soft brain!)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_32BC")

    label("loc_3114")


    ChrTalk(    #120
        0x101,
        "#1000FRoughly thirty years ago.\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    SetChrChipByIndex(0x101, 10)
    SetChrSubChip(0x101, 1)
    Sleep(1000)
    OP_43(0x101, 0x1, 0x1, 0xA)

    ChrTalk(    #121
        0x101,
        (
            "#1008FM-More recent than you'd think, huh?\x01",
            "Ah...haha...ha.\x02\x03",

            "(They're so not buying this...)\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x101, 65535)
    Jump("loc_32BC")

    label("loc_31CA")


    ChrTalk(    #122
        0x101,
        (
            "#1000FRoughly fifty years ago.\x02\x03",

            "Orbal technology and the guild are deeply\x01",
            "connected. Even now we receive financial support\x01",
            "from foundations related to orbment technology.\x02\x03",

            "(Yeah, I'm pretty sure that was it. Man, I'm good!)\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_32BC")

    label("loc_32BC")

    Call(1, 13)

    ChrTalk(    #123
        0x101,
        (
            "#1015FEr, so next, we'll talk about the guild's\x01",
            "relationship with foreign countries.\x02\x03",

            "At the moment, the guild has branches across\x01",
            "the entire continent, but...\x02\x03",

            "The reason the guild has been able to expand\x01",
            "to this level is because it is a non-governmental\x01",
            "organization with no ties to a specific nation.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(400)
    SetChrChipByIndex(0x101, 65535)
    Sleep(400)

    ChrTalk(    #124
        0x101,
        (
            "#1006FBut, even within its practical activities,\x01",
            "the guild has a lot to think about.\x02\x03",

            "For example, they have to keep promises\x01",
            "to prevent them from ending up opposed\x01",
            "to nations.\x02\x03",

            "The most famous promise related to that is...\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 16, -1, -1)

    AnonymousTalk(    #125
        (
            "\x18What's the most important agreement\x01",
            "the guild has to keep with the nations\x01",
            "it works in?\x02",
        )
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        -1,
        150,
        0,
        (
            "1) Non-combat agreement with national armies\x01",      # 0
            "2) Immunity for nobility/royalty\x01",                  # 1
            "3) Non-interference with state powers\x01",             # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_3615"),
        (1, "loc_373A"),
        (2, "loc_38BC"),
        (SWITCH_DEFAULT, "loc_3A2A"),
    )


    label("loc_3615")


    ChrTalk(    #126
        0x101,
        (
            "#1000F...The non-combat agreement with\x01",
            "national armies.\x02\x03",

            "In other words, it's a promise to not\x01",
            "fight with that country's soldiers.\x02\x03",

            "After all, no one would accept an\x01",
            "organization that might at the wrong\x01",
            "time become their enemies.\x02\x03",

            "#1015F(I don't think that's wrong, exactly. Still...)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A2A")

    label("loc_373A")


    ChrTalk(    #127
        0x101,
        (
            "#1002F...An agreement to grant immunity to\x01",
            "nobility and royalty.\x02\x03",

            "In other words, it's a promise to not\x01",
            "arrest people of high status.\x02\x03",

            "If a king or queen does something wrong,\x01",
            "it's the people of the country who should\x01",
            "judge them.\x02\x03",

            "It's against international rules to comment\x01",
            "on other countries' internal problems.\x02\x03",

            "#1015F(That's not wrong, but...was that actually\x01",
            "in the code?)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A2A")

    label("loc_38BC")


    ChrTalk(    #128
        0x101,
        (
            "#1002F...The agreement of non-interference with\x01",
            "state powers.\x02\x03",

            "In other words, no sticking our noses\x01",
            "into state affairs or systems.\x02\x03",

            "Problems within national boundaries are\x01",
            "ultimately something for that country's\x01",
            "people to think about.\x02\x03",

            "Commenting on or interfering with this kind\x01",
            "of thing is against international rules.\x02\x03",

            "#1018F(YES!! Nailed it!)\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_3A2A")

    label("loc_3A2A")

    Call(1, 12)

    ChrTalk(    #129
        0x101,
        (
            "#1000FThe guild uses lots of methods like this\x01",
            "to separate its duties from a nation's.\x02\x03",

            "#1015FOf course, not everything is always solved\x01",
            "so simply according to the codes, so...\x02\x03",

            "Sometimes, in emergencies, you can\x01",
            "end up in situations that are contradictory\x01",
            "to the code.\x02\x03",

            "#1002FBut, in times like that, bracers are asked\x01",
            "to put one basic principle above all else.\x02\x03",

            "In other words, we bracers, in all situations,\x01",
            "should...\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 16, -1, -1)

    AnonymousTalk(    #130
        "\x18Bracers, in all situations, should...\x02",
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        -1,
        150,
        0,
        (
            "1) Prioritize the decisions of the government\x01",      # 0
            "2) Prioritize the safety of civilians\x01",              # 1
            "3) Prioritize cooperation with the army\x01",            # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_3CDA"),
        (1, "loc_3E10"),
        (2, "loc_3F6F"),
        (SWITCH_DEFAULT, "loc_4075"),
    )


    label("loc_3CDA")


    ChrTalk(    #131
        0x101,
        (
            "#1002F...Prioritize the decisions of the government.\x02\x03",

            "#1015FAfter all, we need to avoid opposing the\x01",
            "nations that govern our regions of operation.\x02\x03",

            "If some important case occurred, then it's\x01",
            "even more important.\x02\x03",

            "#1019F(That seems like it makes sense, but...\x01",
            "There was nothing about that in the code.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4075")

    label("loc_3E10")


    ChrTalk(    #132
        0x101,
        (
            "#1002F...Prioritize the safety of civilians.\x02\x03",

            "If you think about this first and foremost, then\x01",
            "you'll naturally be guided to the correct action.\x02\x03",

            "Well, sometimes when you try taking action you'll\x01",
            "end up with a whole bunch'a other problems, but\x01",
            "overcoming stuff like that is part of the job too.\x02\x03",

            "#1006F(Yeah, that's a good summary!)\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_4075")

    label("loc_3F6F")


    ChrTalk(    #133
        0x101,
        (
            "#1002F...Prioritize cooperation with the army.\x02\x03",

            "Cooperating with a nation's army is\x01",
            "critical to a bracer's job.\x02\x03",

            "With both overcoming each other's\x01",
            "weaknesses, any case can be solved.\x02\x03",

            "#1019F(...Well, that's true, but I don't think this\x01",
            "was in the code.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4075")

    label("loc_4075")

    Call(1, 12)
    Sleep(1000)

    ChrTalk(    #134
        0x101,
        (
            "#1000FAaaaaand that pretty much sums us up.\x02\x03",

            "#1001FHow was it? Did everyone understand?\x02",
        )
    )

    CloseMessageWindow()
    Sleep(1000)
    Fade(1000)
    OP_6D(51560, 5000, 50610, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_0D()
    Sleep(400)
    OP_43(0x19, 0x1, 0x1, 0xE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_4350")
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_41E6")

    ChrTalk(    #135
        0x104,
        (
            "#030F#3PThat ends the first half of the class.\x02\x03",

            "#031FVery impressive, Estelle.\x02\x03",

            "You're performing wonderfully as\x01",
            "a teacher. Such fearlessness! Such\x01",
            "verve!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_434D")

    label("loc_41E6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_429D")

    ChrTalk(    #136
        0x104,
        (
            "#030F#3PThat ends the first half of the class.\x02\x03",

            "Estelle appears to be having a hard\x01",
            "time of this battle.\x02\x03",

            "Now, how well will she be able to\x01",
            "recover from this...?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_434D")

    label("loc_429D")


    ChrTalk(    #137
        0x104,
        (
            "#030F#3PThat ends the first half of the class.\x02\x03",

            "#031FVery impressive, Estelle.\x02\x03",

            "Not a hint of shame on your face after\x01",
            "all the complete nonsense you just said.\x01",
            "Marvelous!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_434D")

    Jump("loc_4556")

    label("loc_4350")


    ChrTalk(    #138
        0x104,
        "#030F#3PThat ends the first half of the class.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_4405")

    ChrTalk(    #139
        0x103,
        (
            "#021FYep. She's working hard.\x02\x03",

            "Just when did that girl actually sit down\x01",
            "and study all this? I'm impressed.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4556")

    label("loc_4405")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_44C3")

    ChrTalk(    #140
        0x103,
        (
            "#025FStill, though, this is close.\x02\x03",

            "She has no problem blurting out any old answer\x01",
            "whenever something comes up she doesn't know,\x01",
            "but I wonder if they haven't noticed...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4556")

    label("loc_44C3")


    ChrTalk(    #141
        0x103,
        (
            "#025FAhhh, I can't stand to watch anymore!\x02\x03",

            "It's all nonsense! I'm so embarrassed...\x02\x03",

            "I'm amazed Father Theodore is able to\x01",
            "just stand there.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4556")

    OP_59()
    Sleep(400)
    Fade(1000)
    SetChrPos(0xC, 61337, 1000, 50629, 180)
    ClearChrFlags(0xB, 0x80)
    OP_6D(60430, 1000, 50280, 0)
    OP_44(0x19, 0x1)
    SetChrChipByIndex(0x19, 22)
    OP_0D()
    Sleep(1000)

    ChrTalk(    #142
        0xC,
        (
            "All right, it's the time you've all\x01",
            "been waiting for.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0xC,
        (
            "If you've got anything you want to\x01",
            "ask our guest, go ahead and raise\x01",
            "your hand.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x101, 400)

    ChrTalk(    #144
        0xC,
        "Please, Miss Estelle, carry on.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xC, 400)
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_4691")

    ChrTalk(    #145
        0x101,
        "#1006FSure thing! Leave it to me.\x02",
    )

    CloseMessageWindow()
    Jump("loc_46EB")

    label("loc_4691")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_46CC")

    ChrTalk(    #146
        0x101,
        "#1002FSure thing. I'll certainly try.\x02",
    )

    CloseMessageWindow()
    Jump("loc_46EB")

    label("loc_46CC")


    ChrTalk(    #147
        0x101,
        "#1016FY-Yeah... I'll try.\x02",
    )

    CloseMessageWindow()

    label("loc_46EB")

    OP_43(0xC, 0x1, 0x1, 0x9)
    Sleep(400)
    OP_8C(0x101, 180, 400)

    ChrTalk(    #148
        0x101,
        (
            "#1018FWho's ready to get their questions\x01",
            "answered?\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    Sleep(400)
    SetChrFlags(0xB, 0x80)
    Fade(1000)
    OP_6D(59000, 1000, 53470, 0)
    OP_67(0, 3820, -10000, 0)
    OP_6B(3370, 0)
    OP_6C(0, 0)
    OP_6E(262, 0)
    SetChrSubChip(0xF, 0)
    SetChrSubChip(0x11, 0)
    SetChrSubChip(0x10, 0)
    SetChrSubChip(0x12, 0)
    OP_0D()
    Sleep(1000)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #149
        (
            "\x07\x05Q&A TIME!\x01",
            "～Any Question Goes～\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #150
        (
            "\x07\x05Select the correct answer and overcome\x01",
            "any risky or questionable questions!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_62(0x12, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_95(0x12, 0x0, 0x0, 0x0, 0x320, 0x2EE0)

    ChrTalk(    #151
        0x12,
        "Oh, oh! Pick me! Pick me!\x02",
    )

    CloseMessageWindow()
    OP_8C(0x101, 135, 400)
    OP_43(0x101, 0x1, 0x1, 0xF)
    OP_6D(61300, 1000, 53470, 1500)

    ChrTalk(    #152
        0x101,
        (
            "#1018FWow, you've sure got a lot of energy.\x02\x03",

            "What's your question?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0x12,
        "Umm, um...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #154
        0x12,
        "When can you become a bray-ser?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #155
        0x101,
        (
            "#1006FWhat age can you become a bracer?\x02\x03",

            "#1011FWell, to become a bracer, you first\x01",
            "need to become a junior bracer.\x02\x03",

            "You can become one if you pass the test,\x01",
            "but to take the test...\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMessageWindowPos(-1, 16, -1, -1)

    AnonymousTalk(    #156
        (
            "\x18What is the age restriction on the\x01",
            "Bracer Qualification Examination?\x02",
        )
    )


    Menu(
        0,
        -1,
        150,
        0,
        (
            "1) No particular age restrictions exist\x01",                 # 0
            "2) You are required to be at least 16 years of age\x01",      # 1
            "3) You are required to be at least 18 years of age\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_4B1A"),
        (1, "loc_4BEF"),
        (2, "loc_4D2A"),
        (SWITCH_DEFAULT, "loc_4E49"),
    )


    label("loc_4B1A")


    ChrTalk(    #157
        0x101,
        "#1000F...There's no particular age restriction.\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #158
        0x101,
        (
            "#1008FS-Still, you need ability, so it's normal\x01",
            "to take the test after you reach sixteen.\x02\x03",

            "#1007F(Aww... What am I even saying?)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4E49")

    label("loc_4BEF")


    ChrTalk(    #159
        0x101,
        (
            "#1006F...You're required to be sixteen or older.\x02\x03",

            "Of course, even if you pass the exam,\x01",
            "you don't instantly become one.\x02\x03",

            "For a while, you'll receive training under\x01",
            "the guidance of an older bracer.\x02\x03",

            "Once you've gained enough experience\x01",
            "there, you finally become a junior bracer.\x02\x03",

            "(Perfect answer!)\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_4E49")

    label("loc_4D2A")


    ChrTalk(    #160
        0x101,
        "#1000F...You're required to be eighteen or older.\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #161
        0x101,
        (
            "#1008FS-Still, uh, if you're good enough, you\x01",
            "might be able to take the test earlier.\x02\x03",

            "Errr, if I recall, sixteen is considered good\x01",
            "enough, maybe?\x02\x03",

            "#1013F(Whoops. That was close. I almost lied.)\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x101, 65535)
    Jump("loc_4E49")

    label("loc_4E49")


    ChrTalk(    #162
        0x12,
        "...Okay. So you gotta be sixteen.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #163
        0x12,
        "Okay, got it. Thanks, miss.\x02",
    )

    CloseMessageWindow()
    Call(1, 16)
    OP_6D(59000, 1000, 53470, 1500)
    OP_62(0x11, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)

    ChrTalk(    #164
        0x11,
        "Excuse me, teacher! May I ask a question?\x02",
    )

    CloseMessageWindow()
    OP_8C(0x101, 180, 400)

    ChrTalk(    #165
        0x101,
        "#1000FFire away.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #166
        0x11,
        (
            "Do you gotta beat up monsters\x01",
            "no matter what?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #167
        0x11,
        "Some of them are really cute...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #168
        0x101,
        (
            "#1011FThat's a good question! How to respond\x01",
            "to monsters is tough.\x02\x03",

            "#1010FBut, in general...\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMessageWindowPos(-1, 16, -1, -1)

    AnonymousTalk(    #169
        "\x18How do you decide how to respond to monsters?\x02",
    )


    Menu(
        0,
        -1,
        150,
        0,
        (
            "1) Judge based on appearance\x01",       # 0
            "2) Defeat them, obviously\x01",          # 1
            "3) Prioritize client's intent\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_50A1"),
        (1, "loc_51DB"),
        (2, "loc_532F"),
        (SWITCH_DEFAULT, "loc_5484"),
    )


    label("loc_50A1")


    ChrTalk(    #170
        0x101,
        "#1010F...We judge based on appearance.\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #171
        0x101,
        (
            "#1008FBut there are also some preeetty\x01",
            "adorable monsters that are both strong\x01",
            "and aggressive...\x02\x03",

            "That's why appearances aren't, um,\x01",
            "very reliable. Aha...ha...\x02\x03",

            "A-Anyway, you have to be able to make\x01",
            "decisions on the fly.\x02\x03",

            "#1007F(I suck...)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5484")

    label("loc_51DB")


    ChrTalk(    #172
        0x101,
        (
            "#1002F...Obviously, we defeat them.\x02\x03",

            "The danger posed by monsters has nothing\x01",
            "to do with their appearance. I mean, have you\x01",
            "seen what a pom can do? They're DIABOLICAL.\x02\x03",

            "#1015FHowever, if the client doesn't request an\x01",
            "outright extermination, we may also sometimes\x01",
            "let them go.\x02\x03",

            "(I feel like there was a better way to answer\x01",
            "that...)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5484")

    label("loc_532F")


    ChrTalk(    #173
        0x101,
        (
            "#1000F...We prioritize the client's intent.\x02\x03",

            "There's no absolute right answer when\x01",
            "dealing with monsters. It really depends\x01",
            "on the situation.\x02\x03",

            "So, if the client doesn't demand their\x01",
            "extermination, we may sometimes let\x01",
            "them go.\x02\x03",

            "#1006F(It was kind of a tricky question, but looks\x01",
            "like I was able to answer perfectly! Phew!)\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_5484")

    label("loc_5484")


    ChrTalk(    #174
        0x11,
        "Oh! Okay.\x02",
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)

    ChrTalk(    #175
        0x10,
        "May I ask a question, too?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #176
        0x101,
        "#1000FSure. Go for it.\x02",
    )

    CloseMessageWindow()
    OP_43(0x101, 0x1, 0x1, 0x11)
    OP_6D(57600, 1000, 53470, 1500)

    ChrTalk(    #177
        0x10,
        (
            "There was a case a while back where the\x01",
            "sky bandits attacked an airliner.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #178
        0x10,
        (
            "Was it the Royal Army who arrested\x01",
            "the sky bandits then? Or was it bracers?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #179
        0x101,
        (
            "#1011FYou mean the disappearance of the Linde?\x02\x03",

            "#1015FThe ones who finally arrested the sky\x01",
            "bandits were...\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMessageWindowPos(-1, 16, -1, -1)

    AnonymousTalk(    #180
        "\x18Who arrested the Capua gang?\x02",
    )


    Menu(
        0,
        -1,
        150,
        0,
        (
            "1) Bracers, of course\x01",          # 0
            "2) The Royal Army forces\x01",       # 1
            "3) The Royal Guard troops\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_56D0"),
        (1, "loc_581D"),
        (2, "loc_597D"),
        (SWITCH_DEFAULT, "loc_5AFC"),
    )


    label("loc_56D0")


    ChrTalk(    #181
        0x101,
        "#1012FThe bracers, of course.\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #182
        0x101,
        (
            "#1008FOh, but now that I think about it, we met up\x01",
            "with the army on the entry mission, huh?\x02\x03",

            "...S-Sorry, my memory's kinda vague on that.\x02\x03",

            "#1015FUm, anyway, the bracers and the Royal Army\x01",
            "cooperated to sniff them out in the end.\x02\x03",

            "(Uuuuugh, why is my brain so bad...)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5AFC")

    label("loc_581D")


    ChrTalk(    #183
        0x101,
        (
            "#1000F...The Royal Army forces.\x02\x03",

            "In the final entry mission, the bracers\x01",
            "and Royal Army worked together using\x01",
            "a pincer move to corner them.\x02\x03",

            "When the sky bandits tried to flee, the\x01",
            "Royal Army caught and arrested them.\x02\x03",

            "In other words, the bracers and the Royal\x01",
            "Army cooperated to flush them out.\x02\x03",

            "#1006F(All right, no problems here.)\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_5AFC")

    label("loc_597D")


    ChrTalk(    #184
        0x101,
        "#1000F...The Royal Guard troops.\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #185
        0x101,
        (
            "#1015FActually, you know... I don't think there\x01",
            "were any of the Royal Guard there...\x02\x03",

            "#1013F...S-Sorry, my memory's kinda vague on that.\x02\x03",

            "Umm, anyway, the bracers and the Royal Army\x01",
            "cooperated to sniff them out in the end.\x02\x03",

            "#1007F(That's right, the Royal Guard came for\x01",
            "Mayor Dalmore, not the sky bandits...)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5AFC")

    label("loc_5AFC")


    ChrTalk(    #186
        0x10,
        (
            "Okay! So the Royal Army and the\x01",
            "bracers worked together?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #187
        0x10,
        "That's so cool!\x02",
    )

    CloseMessageWindow()
    Call(1, 16)
    ClearChrFlags(0x1B, 0x80)

    def lambda_5B5E():
        OP_8F(0x1B, 0xDC1E, 0x0, 0xAEBA, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_5B5E)
    OP_6D(59000, 1000, 53470, 1500)

    ChrTalk(    #188
        0x1B,
        "#1PUmmmmm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #189
        0x1B,
        "#1PCan I ask something?\x02",
    )

    CloseMessageWindow()
    OP_43(0x101, 0x1, 0x1, 0x12)
    OP_6D(57260, 1000, 50270, 1500)
    TurnDirection(0x101, 0x1B, 400)

    ChrTalk(    #190
        0x101,
        "#1000FSure, go ahead.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #191
        0x1B,
        (
            "#1PI'm actually studying for entrance\x01",
            "exams and just forgot this, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #192
        0x1B,
        (
            "#1PWhich of the three principles in the code\x01",
            "is the protective duty to civilians?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #193
        0x101,
        (
            "#1004F(G-Ghhh...!)\x02\x03",

            "(H-How the heck am I supposed to\x01",
            "remember something like that?!)\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    SetChrChipByIndex(0x101, 10)
    SetChrSubChip(0x101, 1)
    Sleep(600)

    ChrTalk(    #194
        0x101,
        (
            "#1015FW-Wait a second, the protective duty\x01",
            "to civilians principle?\x02\x03",

            "Errr, ummmmm, that is...\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMessageWindowPos(-1, 16, -1, -1)

    AnonymousTalk(    #195
        "\x18Which principle is the protective duty to civilians?\x02",
    )


    Menu(
        0,
        -1,
        150,
        0,
        (
            "1) Guild Code, Principle 1\x01",      # 0
            "2) Guild Code, Principle 2\x01",      # 1
            "3) Guild Code, Principle 3\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Sleep(400)
    SetChrChipByIndex(0x101, 65535)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_5E7B"),
        (1, "loc_5FFF"),
        (2, "loc_60A8"),
        (SWITCH_DEFAULT, "loc_623B"),
    )


    label("loc_5E7B")


    ChrTalk(    #196
        0x101,
        "#1015FGuild Code, Principle 1, I think? \x02",
    )

    CloseMessageWindow()

    ChrTalk(    #197
        0x1B,
        "#1PHuh... Was it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #198
        0x1B,
        (
            "#1PI thought the first principle was\x01",
            "basic ideology...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #199
        0x101,
        "#1008FOh, r-really...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #200
        0x1B,
        "#1PI'm sorry. I already knew the answer.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #201
        0x1B,
        (
            "#1PThe 'protective duty' to civilians is\x01",
            "the second principle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #202
        0x101,
        (
            "#1016FW-Well, I'm sure glad you know!\x02\x03",

            "#1007F(Aaaah, this is so embarrassing...)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_623B")

    label("loc_5FFF")


    ChrTalk(    #203
        0x101,
        "#1015F...Guild Code, Principle 2, I think?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #204
        0x1B,
        "#1POh, yeah. I knew that!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #205
        0x1B,
        "#1PSorry...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #206
        0x101,
        (
            "#1016FNo, it's fine.\x02\x03",

            "(I managed to survive that one.)\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_623B")

    label("loc_60A8")


    ChrTalk(    #207
        0x101,
        "#1000F...Guild Code, Principle 3, I think?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #208
        0x1B,
        "#1PHuh... Was it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #209
        0x1B,
        (
            "#1PI thought the third principle was\x01",
            "non-interference with nations.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #210
        0x101,
        "#1008FOh, r-really...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #211
        0x1B,
        "#1PI'm sorry. I already knew the answer.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #212
        0x1B,
        (
            "#1PThe 'protective duty' to civilians is\x01",
            "the second principle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #213
        0x101,
        (
            "#1016FW-Well, I'm sure glad you know!\x02\x03",

            "#1007F(Aaaah, this is so embarrassing...)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_623B")

    label("loc_623B")

    OP_43(0x101, 0x1, 0x1, 0x10)
    OP_6D(59000, 1000, 53470, 1500)

    def lambda_6259():
        OP_8F(0x1B, 0xDC1E, 0xFFFFFDA8, 0xAEBA, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_6259)

    ChrTalk(    #214
        0x101,
        "#1000FErr, so...no more questions?\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x1B, 0x1)
    SetChrFlags(0x1B, 0x80)

    ChrTalk(    #215
        0xF,
        "#2POkay, I've got a question, then!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #216
        0x101,
        "#1000FGo ahead.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #217
        0xF,
        (
            "#2PUm, um, so it doesn't have much\x01",
            "to do with the class, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #218
        0xF,
        (
            "#2PWhen the mayor was arrested, the\x01",
            "queen's airship came, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #219
        0xF,
        "#2PHow big was the airship?\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #220
        0x101,
        (
            "#1019F(I-I knew there'd be one... There's always\x01",
            "one with some weirdo question that has\x01",
            "nothing to do with anything.)\x02\x03",

            "#1016F...By the queen's ship, do you mean the\x01",
            "Arseille?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #221
        0xF,
        "#2PYeah, that, that!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #222
        0xF,
        (
            "#2PIt looked REAL big, but I wonder\x01",
            "how big it really was.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #223
        0x101,
        (
            "#1015FThe Arseille's size?\x02\x03",

            "I think I've read about that in a book before...\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMessageWindowPos(-1, 16, -1, -1)

    AnonymousTalk(    #224
        "\x18What's the overall length of the Arseille?\x02",
    )


    Menu(
        0,
        -1,
        150,
        0,
        (
            "1) 22 arge\x01",      # 0
            "2) 32 arge\x01",      # 1
            "3) 42 arge\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_65B2"),
        (1, "loc_66AC"),
        (2, "loc_67A5"),
        (SWITCH_DEFAULT, "loc_6851"),
    )


    label("loc_65B2")


    ChrTalk(    #225
        0x101,
        "#1015FI think it had an overall length of 22 arge.\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    SetChrChipByIndex(0x101, 10)
    SetChrSubChip(0x101, 1)
    Sleep(1000)

    ChrTalk(    #226
        0x101,
        (
            "#1007FS-Sorry... To be honest, I'm not too sure.\x02\x03",

            "I might be wrong, so you should\x01",
            "probably look it up in a book.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #227
        0xF,
        "Okaaaay...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #228
        0xF,
        "I'll check a book.\x02",
    )

    CloseMessageWindow()
    Jump("loc_6851")

    label("loc_66AC")


    ChrTalk(    #229
        0x101,
        "#1015FI think it had an overall length of 32 arge.\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    SetChrChipByIndex(0x101, 10)
    SetChrSubChip(0x101, 1)
    Sleep(1000)

    ChrTalk(    #230
        0x101,
        (
            "#1007FS-Sorry... To be honest I'm not too sure.\x02\x03",

            "I might be wrong, so you should\x01",
            "probably look it up in a book.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #231
        0xF,
        "Okaaaay...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #232
        0xF,
        "I'll check a book.\x02",
    )

    CloseMessageWindow()
    Jump("loc_6851")

    label("loc_67A5")


    ChrTalk(    #233
        0x101,
        (
            "#1015FI think...it had an overall length of\x01",
            "42 arge, if I remember right.\x02\x03",

            "That might not be exactly precise,\x01",
            "but should be close!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #234
        0xF,
        "Wow, that's HUGE!\x02",
    )

    CloseMessageWindow()
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_6851")

    label("loc_6851")


    ChrTalk(    #235
        0xF,
        "Thanks, Miss Estelle!\x02",
    )

    CloseMessageWindow()
    FadeToDark(1500, 0, -1)
    OP_0D()
    SetChrPos(0xC, 61337, 1000, 50629, 180)
    OP_6D(58920, 1000, 50630, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(320000, 0)
    OP_6E(262, 0)
    SetChrChipByIndex(0x101, 65535)
    ClearChrFlags(0xB, 0x80)
    FadeToBright(1500, 0)
    OP_0D()
    Sleep(1000)

    ChrTalk(    #236
        0xC,
        "Any more questions, children?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #237
        0xC,
        (
            "If not, then I believe that's all for\x01",
            "our guest speaker today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #238
        0xC,
        "Everyone, say thank you to Miss Estelle.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #239
        0xF,
        "#5PThank you very muuuuuch!\x02",
    )


    ChrTalk(    #240
        0x11,
        "#2PThank you very muuuuuch!\x02",
    )


    ChrTalk(    #241
        0x12,
        "#2PThank you very muuuuuch!\x02",
    )


    ChrTalk(    #242
        0x10,
        "#1PThank you very muuuuuch!\x02",
    )

    OP_56(0x1)
    OP_59()

    ChrTalk(    #243
        0x101,
        "#1001FBye, kids! ♪\x02",
    )

    CloseMessageWindow()
    FadeToDark(1500, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_6A5B")
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6A4D")
    OP_2B(0x67, 0x2)
    OP_2C(0x67, 0x3E8)
    OP_28(0x67, 0x1, 0x2000)
    OP_28(0x67, 0x1, 0x4)
    Jump("loc_6A53")

    label("loc_6A4D")

    OP_28(0x67, 0x1, 0x8)

    label("loc_6A53")

    OP_28(0x67, 0x4, 0x10)
    Jump("loc_6A71")

    label("loc_6A5B")

    OP_28(0x67, 0x1, 0x4000)
    OP_28(0x67, 0x1, 0x10)
    OP_28(0x67, 0x4, 0x40)
    OP_28(0x67, 0x4, 0x80)

    label("loc_6A71")

    ClearMapFlags(0x400000)
    OP_A2(0x10F2)
    NewScene("ED6_DT21/T2100   ._SN", 105, 0, 0)
    IdleLoop()
    Return()

    # Function_1_D15 end

    def Function_2_6A83(): pass

    label("Function_2_6A83")

    OP_6D(58920, 1000, 50630, 3000)
    Return()

    # Function_2_6A83 end

    def Function_3_6A95(): pass

    label("Function_3_6A95")

    OP_6B(2800, 4000)
    Return()

    # Function_3_6A95 end

    def Function_4_6A9F(): pass

    label("Function_4_6A9F")

    SetChrPos(0x1A, 57760, 0, 48830, 0)
    OP_69(0x1A, 0xFA0)
    Return()

    # Function_4_6A9F end

    def Function_5_6AB8(): pass

    label("Function_5_6AB8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6B73")
    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_6ADE"),
        (1, "loc_6AE6"),
        (2, "loc_6AEE"),
        (3, "loc_6AF6"),
        (SWITCH_DEFAULT, "loc_6AFE"),
    )


    label("loc_6ADE")

    Sleep(200)
    Jump("loc_6AFE")

    label("loc_6AE6")

    Sleep(300)
    Jump("loc_6AFE")

    label("loc_6AEE")

    Sleep(400)
    Jump("loc_6AFE")

    label("loc_6AF6")

    Sleep(500)
    Jump("loc_6AFE")

    label("loc_6AFE")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6B21")
    OP_62(0xFE, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)

    label("loc_6B21")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_6B3E"),
        (1, "loc_6B48"),
        (2, "loc_6B52"),
        (3, "loc_6B5C"),
        (SWITCH_DEFAULT, "loc_6B66"),
    )


    label("loc_6B3E")

    OP_8C(0xFE, 45, 400)
    Jump("loc_6B70")

    label("loc_6B48")

    OP_8C(0xFE, 90, 400)
    Jump("loc_6B70")

    label("loc_6B52")

    OP_8C(0xFE, 315, 400)
    Jump("loc_6B70")

    label("loc_6B5C")

    OP_8C(0xFE, 270, 400)
    Jump("loc_6B70")

    label("loc_6B66")

    OP_8C(0xFE, 0, 400)
    Jump("loc_6B70")

    label("loc_6B70")

    Jump("Function_5_6AB8")

    label("loc_6B73")

    Return()

    # Function_5_6AB8 end

    def Function_6_6B74(): pass

    label("Function_6_6B74")

    OP_8E(0xF7, 0xFFFFC1D0, 0x0, 0xAEEC, 0x3E8, 0x0)
    TurnDirection(0xF7, 0x101, 400)
    Return()

    # Function_6_6B74 end

    def Function_7_6B90(): pass

    label("Function_7_6B90")

    OP_8E(0xC, 0xF848, 0x0, 0xCB98, 0x7D0, 0x0)
    OP_8E(0xC, 0xF88E, 0x0, 0xC4AE, 0x7D0, 0x0)
    OP_8E(0xC, 0xFFDC, 0x0, 0xC4A4, 0x7D0, 0x0)
    OP_8C(0xC, 270, 400)
    Return()

    # Function_7_6B90 end

    def Function_8_6BD4(): pass

    label("Function_8_6BD4")

    Sleep(800)
    OP_8E(0xD, 0xCF26, 0x0, 0xB446, 0x7D0, 0x0)
    OP_8C(0xD, 90, 400)
    Return()

    # Function_8_6BD4 end

    def Function_9_6BF5(): pass

    label("Function_9_6BF5")

    OP_8E(0xC, 0xFFDC, 0x0, 0xC4A4, 0x7D0, 0x0)
    OP_8C(0xC, 270, 400)
    Return()

    # Function_9_6BF5 end

    def Function_10_6C11(): pass

    label("Function_10_6C11")

    OP_62(0x10, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0x11, 0xF, 400)
    Sleep(400)
    OP_62(0x11, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    TurnDirection(0xF, 0x11, 400)
    Sleep(2000)
    OP_8C(0x11, 0, 400)
    OP_8C(0xF, 0, 400)
    Return()

    # Function_10_6C11 end

    def Function_11_6C6B(): pass

    label("Function_11_6C6B")

    OP_62(0x10, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(100)
    OP_62(0x11, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0xF, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(50)
    OP_62(0x12, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Return()

    # Function_11_6C6B end

    def Function_12_6CD2(): pass

    label("Function_12_6CD2")

    Sleep(400)
    FadeToDark(600, 0, -1)
    OP_0D()
    Sleep(800)
    FadeToBright(600, 0)
    OP_0D()
    Return()

    # Function_12_6CD2 end

    def Function_13_6CF2(): pass

    label("Function_13_6CF2")

    Sleep(400)
    FadeToDark(600, 0, -1)
    OP_0D()
    Sleep(800)
    SetChrChipByIndex(0x101, 10)
    SetChrSubChip(0x101, 1)
    FadeToBright(600, 0)
    OP_0D()
    Return()

    # Function_13_6CF2 end

    def Function_14_6D1C(): pass

    label("Function_14_6D1C")

    LoadEffect(0x0, "map\\\\mp032_00.eff")

    label("loc_6D30")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6DCD")
    Sleep(600)
    SetChrChipByIndex(0x19, 25)
    Sleep(600)

    label("loc_6D48")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6DBB")
    LoadEffect(0x0, "map\\\\mp032_00.eff")
    OP_22(0x7C, 0x0, 0x64)
    PlayEffect(0x0, 0xFF, 0x19, 0, 1200, 500, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6DB8")
    Jump("loc_6DBB")

    label("loc_6DB8")

    Jump("loc_6D48")

    label("loc_6DBB")

    Sleep(1000)
    SetChrChipByIndex(0x19, 22)
    Sleep(1000)
    Jump("loc_6D30")

    label("loc_6DCD")

    Return()

    # Function_14_6D1C end

    def Function_15_6DCE(): pass

    label("Function_15_6DCE")


    def lambda_6DD4():
        TurnDirection(0x10, 0x12, 400)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_6DD4)
    Sleep(100)

    def lambda_6DE7():
        TurnDirection(0x11, 0x12, 400)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_6DE7)
    Sleep(50)

    def lambda_6DFA():
        TurnDirection(0xF, 0x12, 400)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_6DFA)
    Return()

    # Function_15_6DCE end

    def Function_16_6E03(): pass

    label("Function_16_6E03")


    def lambda_6E09():
        OP_8C(0x10, 0, 400)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_6E09)
    Sleep(100)

    def lambda_6E1C():
        OP_8C(0x11, 0, 400)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_6E1C)

    def lambda_6E2A():
        OP_8C(0x12, 315, 400)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_6E2A)
    Sleep(50)

    def lambda_6E3D():
        OP_8C(0xF, 0, 400)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_6E3D)
    Return()

    # Function_16_6E03 end

    def Function_17_6E46(): pass

    label("Function_17_6E46")


    def lambda_6E4C():
        TurnDirection(0x12, 0x10, 400)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_6E4C)
    Sleep(100)

    def lambda_6E5F():
        TurnDirection(0x11, 0x10, 400)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_6E5F)
    Sleep(50)

    def lambda_6E72():
        TurnDirection(0xF, 0x10, 400)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_6E72)
    Return()

    # Function_17_6E46 end

    def Function_18_6E7B(): pass

    label("Function_18_6E7B")


    def lambda_6E81():
        TurnDirection(0x12, 0x1B, 400)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_6E81)
    Sleep(100)

    def lambda_6E94():
        TurnDirection(0x11, 0x1B, 400)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_6E94)
    Sleep(50)

    def lambda_6EA7():
        TurnDirection(0xF, 0x1B, 400)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_6EA7)

    def lambda_6EB5():
        TurnDirection(0x10, 0x1B, 400)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_6EB5)
    Return()

    # Function_18_6E7B end

    SaveToFile()

Try(main)
