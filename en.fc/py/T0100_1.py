from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 洛连特

    CreateScenaFile(
        FileName            = 'T0100_1 ._SN',
        MapName             = 'Rolent',
        Location            = 'T0100.x',
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
        "Function_1_142B",         # 01, 1
        "Function_2_1FB0",         # 02, 2
        "Function_3_287C",         # 03, 3
        "Function_4_3B2A",         # 04, 4
        "Function_5_4261",         # 05, 5
        "Function_6_4286",         # 06, 6
        "Function_7_429F",         # 07, 7
        "Function_8_42B8",         # 08, 8
        "Function_9_4319",         # 09, 9
        "Function_10_4363",        # 0A, 10
        "Function_11_467A",        # 0B, 11
        "Function_12_4914",        # 0C, 12
        "Function_13_493C",        # 0D, 13
        "Function_14_4946",        # 0E, 14
        "Function_15_496B",        # 0F, 15
        "Function_16_4997",        # 10, 16
        "Function_17_49C3",        # 11, 17
        "Function_18_49DF",        # 12, 18
        "Function_19_49FB",        # 13, 19
        "Function_20_4C46",        # 14, 20
        "Function_21_4C58",        # 15, 21
        "Function_22_4CA4",        # 16, 22
        "Function_23_4CC9",        # 17, 23
        "Function_24_4CF5",        # 18, 24
        "Function_25_4D21",        # 19, 25
        "Function_26_4F88",        # 1A, 26
        "Function_27_4F9A",        # 1B, 27
        "Function_28_4FE6",        # 1C, 28
        "Function_29_501D",        # 1D, 29
        "Function_30_5036",        # 1E, 30
        "Function_31_5045",        # 1F, 31
        "Function_32_52E9",        # 20, 32
        "Function_33_52FB",        # 21, 33
        "Function_34_5326",        # 22, 34
        "Function_35_5348",        # 23, 35
    )


    def Function_0_66(): pass

    label("Function_0_66")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x4, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_22A")
    TalkBegin(0x12)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17C")
    OP_A2(0x10)

    ChrTalk(    #0
        0xFE,
        (
            "Thanks for finding my rock earlier.\x01",
            "You really helped me out a ton.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "That said, I can't believe my mom\x01",
            "is trying to sell folk crafts in a city\x01",
            "that has ships that can fly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0xFE,
        (
            "I am just amazed at how brazen\x01",
            "she is when it comes to business.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_224")

    label("loc_17C")


    ChrTalk(    #3
        0xFE,
        (
            "I cannot believe my mom is\x01",
            "trying to sell folk crafts in a\x01",
            "city that has ships that can fly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xFE,
        (
            "I am just amazed at how brazen\x01",
            "she is when it comes to business.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_224")

    TalkEnd(0x12)
    Jump("loc_142A")

    label("loc_22A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x4, 0x1, 0x20)"), scpexpr(EXPR_EXEC_OP, "OP_40(0x325)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D1F")
    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x101, 31400, 0, 29390, 120)
    SetChrPos(0x102, 30330, 0, 28560, 120)
    OP_4A(0x12, 255)
    OP_6D(31410, 0, 29350, 0)
    OP_6C(0, 0)
    OP_0D()
    Sleep(400)
    OP_62(0x12, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(400)
    TurnDirection(0x12, 0x101, 400)
    Sleep(400)

    ChrTalk(    #5
        0x12,
        "Hey...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x12,
        "Is that rock...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x101,
        (
            "#000FCould it be that...\x02\x03",

            "...this is the rock you've been\x01",
            "looking for?\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #8
        "\x07\x00Handed over \x07\x02Quartz Fragment\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(    #9
        0x12,
        (
            "Yep, this is the one.\x01",
            "My shiny rock.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x12, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(400)

    ChrTalk(    #10
        0x12,
        "...\x02",
    )

    CloseMessageWindow()
    OP_63(0x12)

    ChrTalk(    #11
        0x12,
        "...Why is it all dirty like this?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x101,
        (
            "#007FHey! Don't you have something\x01",
            "else to say before you complain?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x12,
        "You guys are bracers, right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x12,
        (
            "I've already paid your money\x01",
            "to the guild.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x12,
        (
            "Therefore, I think I have the right\x01",
            "to complain.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(400)

    ChrTalk(    #16
        0x101,
        "#005FThat's not the problem here!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #17
        0x102,
        (
            "#017FCalm down, Estelle.\x01",
            "He's just a kid.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #18
        0x101,
        "#009FI know that, but...\x02",
    )

    CloseMessageWindow()

    def lambda_54C():
        TurnDirection(0x102, 0x12, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_54C)
    Sleep(200)
    TurnDirection(0x101, 0x12, 400)

    ChrTalk(    #19
        0x102,
        (
            "#010FThis quartz is what you were\x01",
            "looking for, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x12,
        "Yeah, that's the one...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x12,
        "...This rock is really quartz?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x12,
        (
            "You mean the same kind of\x01",
            "quartz that's in an orbment?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x102,
        (
            "#019FYep, it's the same kind of\x01",
            "quartz made of sepith.\x02\x03",

            "It's chipped, so it doesn't\x01",
            "function anymore.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x12,
        "I see...\x02",
    )

    CloseMessageWindow()
    OP_8C(0x12, 45, 400)
    OP_62(0x12, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(400)

    ChrTalk(    #25
        0x12,
        (
            "So this rock belonged to\x01",
            "an orbment...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x12,
        "...\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(400)

    ChrTalk(    #27
        0x101,
        (
            "#000F???\x02\x03",

            "What's wrong?\x01",
            "You seem a bit out of it.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x12)
    OP_62(0x12, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(400)
    TurnDirection(0x12, 0x101, 400)

    ChrTalk(    #28
        0x12,
        "...Who? Me?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x12,
        "Oh, it's nothing.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x12,
        "I'm glad you found it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x12,
        "I guess that's about it, then.\x02",
    )

    CloseMessageWindow()

    def lambda_7C6():

        label("loc_7C6")

        TurnDirection(0x101, 0x12, 400)
        OP_48()
        Jump("loc_7C6")

    QueueWorkItem2(0x101, 1, lambda_7C6)

    def lambda_7D7():

        label("loc_7D7")

        TurnDirection(0x102, 0x12, 400)
        OP_48()
        Jump("loc_7D7")

    QueueWorkItem2(0x102, 1, lambda_7D7)
    OP_8E(0xFE, 0x7D5A, 0x0, 0x5E1A, 0x1388, 0x0)
    OP_62(0x12, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(400)

    ChrTalk(    #32
        0x12,
        "Oh, that reminds me.\x02",
    )

    CloseMessageWindow()
    OP_8C(0xFE, 0, 400)
    OP_8E(0xFE, 0x7A12, 0x0, 0x7080, 0x1388, 0x0)

    ChrTalk(    #33
        0x12,
        "I almost forgot. Here, take these.\x02",
    )

    CloseMessageWindow()
    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #34
        "\x07\x00Received \x07\x02Drill Meatball\x07\x00 x5.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_3E(0x1A5, 5)

    ChrTalk(    #35
        0x12,
        (
            "My mom gives these to me and\x01",
            "tells me they're healthy, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x12,
        (
            "They're kind of bitter,\x01",
            "so I can't stand them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xFE,
        (
            "Anyway, I appreciate what you\x01",
            "did for me today.\x02",
        )
    )

    CloseMessageWindow()
    OP_8E(0xFE, 0x7D8C, 0x0, 0x46AA, 0x1388, 0x0)
    OP_44(0x101, 0x1)
    OP_44(0x102, 0x1)

    ChrTalk(    #38
        0x101,
        "#007FSeriously, what a cheeky little kid.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x102,
        (
            "#010FI'm sure it's a difficult age for him.\x02\x03",

            "#010FBut...\x02\x03",

            "I wonder why he was searching\x01",
            "for that quartz.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #40
        0x101,
        (
            "#501FWhat do you mean?\x02\x03",

            "Now that you mention it,\x01",
            "it does seem a little strange.\x02\x03",

            "#001FBut, oh well. Everyone has something\x01",
            "they think is important.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #41
        0x102,
        (
            "#019FTruer words couldn't be spoken.\x02\x03",

            "Perhaps, that kid has an interest\x01",
            "in orbments.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x101,
        (
            "#505FI, for one, don't see what's so\x01",
            "interesting about those overly\x01",
            "complex gadgets.\x02\x03",

            "My brain goes numb just thinking\x01",
            "about them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x102,
        (
            "#010FExcept for the fact that you'll have\x01",
            "to get used to them sooner or later.\x02\x03",

            "You won't be able to fulfill your job\x01",
            "as a bracer if you can't use one.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(400)

    ChrTalk(    #44
        0x101,
        "#007FAll right, all right, I'll try and learn.\x02",
    )

    CloseMessageWindow()
    SetChrPos(0x12, 62400, 250, 22000, 270)
    OP_3F(0x325, 1)
    OP_28(0x4, 0x4, 0x10)
    OP_28(0x4, 0x1, 0x40)
    OP_44(0x12, 0xFF)
    OP_43(0x12, 0x0, 0x0, 0x8)
    OP_22(0x17, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #45
        "\x07\x00Quest \x07\x02[Find the Shiny Rock] \x07\x00completed!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    EventEnd(0x0)
    Jump("loc_142A")

    label("loc_D1F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x4, 0x0, 0x4)"), scpexpr(EXPR_END)), "loc_DDA")
    TalkBegin(0x12)

    ChrTalk(    #46
        0xFE,
        (
            "If you happen to find a shiny rock,\x01",
            "give me a holler. I'll be in the area.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0xFE,
        (
            "I've already searched around\x01",
            "the general goods store...\x01",
            "so where haven't I looked?\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x12)
    Jump("loc_142A")

    label("loc_DDA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x4, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_12E1")
    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x101, 31400, 0, 29390, 120)
    SetChrPos(0x102, 30690, 0, 29150, 133)
    OP_4A(0x12, 255)
    OP_6D(31410, 0, 29350, 0)
    OP_6C(0, 0)
    OP_0D()
    Sleep(400)

    ChrTalk(    #48
        0x12,
        "This is really weird...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x12,
        "Where could it have gone...\x02",
    )

    CloseMessageWindow()
    OP_62(0x12, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(400)
    TurnDirection(0x12, 0x101, 400)
    Sleep(400)

    ChrTalk(    #50
        0x12,
        "Oh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x12,
        (
            "Excuse me, but can I ask\x01",
            "you something?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x12,
        (
            "You didn't see a shiny rock around\x01",
            "here anywhere, did you?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)

    ChrTalk(    #53
        0x101,
        (
            "#004FHuh?\x02\x03",

            "A shiny rock?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x12,
        (
            "Yeah, that's right.\x01",
            "One that sparkles.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x12,
        (
            "You didn't see a rock like that lying\x01",
            "around anywhere, did you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x101,
        (
            "#000FAre you saying you lost something?\x02\x03",

            "#505FUm, I don't recall seeing anything\x01",
            "like that.\x02\x03",

            "Do you know where you might\x01",
            "have dropped it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x12,
        (
            "My mom was calling for me,\x01",
            "so I ran over to the general\x01",
            "goods store where she was.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x12,
        (
            "I know I had it in my hand at the\x01",
            "time, but when I came back here,\x01",
            "it was gone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x101,
        (
            "#000FWhen you say 'general goods store',\x01",
            "you mean Mr. Rinon's store, right?\x02\x03",

            "Did you look in front of his store?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x12,
        (
            "Obviously that's the first place\x01",
            "I looked. You don't need to treat\x01",
            "me like a kid, you know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x101,
        "#004FMy...aren't you a charmer.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x12,
        (
            "Well, I already asked the Bracer\x01",
            "Guild to help find it, so I'm sure\x01",
            "it'll show up sooner or later.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x12,
        (
            "If you do happen to come across\x01",
            "it, give me a holler straight away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x12,
        "I'll probably be around.\x02",
    )

    CloseMessageWindow()
    OP_28(0x4, 0x4, 0x4)
    OP_28(0x4, 0x4, 0x8)
    OP_28(0x4, 0x1, 0x1)
    OP_28(0x4, 0x1, 0x2)
    OP_65(0x1, 0x1)
    OP_4B(0x12, 255)
    OP_8C(0x12, 45, 0)
    EventEnd(0x0)
    Jump("loc_142A")

    label("loc_12E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_END)), "loc_13BD")
    SetChrFlags(0x12, 0x10)
    TalkBegin(0x12)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_135C")

    ChrTalk(    #65
        0xFE,
        (
            "Crap, I wonder where the darn\x01",
            "thing went.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0xFE,
        (
            "I've checked every place I could\x01",
            "think of...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13B5")

    label("loc_135C")


    ChrTalk(    #67
        0xFE,
        (
            "That's really strange...\x01",
            "Why can't I find it anywhere?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0xFE,
        "This is so frustrating.\x02",
    )

    CloseMessageWindow()

    label("loc_13B5")

    ClearChrFlags(0x12, 0x10)
    Jump("loc_1427")

    label("loc_13BD")

    SetChrFlags(0x12, 0x10)
    TalkBegin(0x12)

    ChrTalk(    #69
        0xFE,
        (
            "There sure is a lot of junk\x01",
            "around here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0xFE,
        (
            "I wonder if there's anything\x01",
            "interesting.\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x12, 0x10)

    label("loc_1427")

    TalkEnd(0x12)

    label("loc_142A")

    Return()

    # Function_0_66 end

    def Function_1_142B(): pass

    label("Function_1_142B")

    TalkBegin(0x12)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x4, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_14FA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14C0")
    OP_A2(0x10)

    ChrTalk(    #71
        0xFE,
        (
            "船が空飛ぶような町でさ、\x01",
            "よく小物売りなんてやってられるよな。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0xFE,
        (
            "オレ感心するよ、お袋の無神経さに。\x01",
            "いや、マジで。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14F7")

    label("loc_14C0")


    ChrTalk(    #73
        0xFE,
        (
            "オレ感心するよ、お袋の無神経さに。\x01",
            "いや、マジで。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14F7")

    Jump("loc_1FAC")

    label("loc_14FA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x4, 0x1, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_40(0x325)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1B55")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x4, 0x0, 0x4)"), scpexpr(EXPR_END)), "loc_1590")
    TurnDirection(0xFE, 0x101, 0)
    OP_62(0x12, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(500)

    ChrTalk(    #74
        0xFE,
        "あ…………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0xFE,
        "……ねえ、それ。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xFE, 0)

    ChrTalk(    #76
        0x101,
        (
            "#000Fこれでしょ？\x01",
            "君の探してた歯車って。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_16D2")

    label("loc_1590")


    ChrTalk(    #77
        0xFE,
        "ねえ、ちょっと聞きたいんだけどさ。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0xFE,
        "この辺で、歯車を見なかった？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xFE, 0)

    ChrTalk(    #79
        0x101,
        "#000Fへっ？　歯車？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(    #80
        0xFE,
        (
            "そう。\x01",
            "ギザギザで金ピカのやつ。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0xFE,
        "落ちてなかった？　どっかに。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0xFE,
        (
            "まあ、ブレイサーにも頼んだから\x01",
            "じき見つかるだろうけど……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0x101,
        (
            "#000Fあ、そういえば。\x02\x03",

            "#000Fもしかして、これ？\x01",
            "君の探してる歯車って。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16D2")

    OP_28(0x4, 0x4, 0x10)
    OP_28(0x4, 0x1, 0x4)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #84
        "\x07\x02歯車\x07\x00を渡した。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3F(0x325, 1)

    ChrTalk(    #85
        0xFE,
        "ああ、そう。オレの歯車……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0xFE,
        "……………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0xFE,
        "……なんだよ、汚れてるじゃん。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0x101,
        (
            "#000Fコラ、\x01",
            "文句の前に言うことがあるでしょ。\x02\x03",

            "#000Fわざわざ排水溝から\x01",
            "拾ってくれた人がいるんだよ？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0xFE,
        (
            "こっちだって\x01",
            "ギルドを通して金払ってんだぜ。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0xFE,
        "文句言う権利はあるとおもうけど。\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(500)

    ChrTalk(    #91
        0x101,
        "#002F#5Sそういう問題じゃないでしょ！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0xFE,
        (
            "……ま、なんでもいいさ。\x01",
            "とにかく見っけてくれて助かったぜ。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0xFE,
        "んじゃ。\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0x12, 0x40)
    OP_43(0x101, 0x0, 0x1, 0x6)
    OP_43(0x102, 0x0, 0x1, 0x7)
    OP_43(0x12, 0x0, 0x1, 0x5)
    OP_A2(0x11)
    OP_A2(0xE)
    OP_A2(0xF)
    OP_A5(0x11)
    OP_A5(0xE)
    OP_A5(0xF)
    SetChrPos(0x12, 62400, 250, 22000, 270)
    ClearChrFlags(0x12, 0x40)
    ClearChrFlags(0xFE, 0x80)
    OP_85(0x12)
    OP_62(0x101, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #94
        0x101,
        "#002Fうう～、ほんっと生意気なガキね～。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 0)

    ChrTalk(    #95
        0x102,
        (
            "#010Fエステル、落ち着いて。\x01",
            "相手は子供だよ。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 0)

    ChrTalk(    #96
        0x101,
        "#000Fわ、分かってるってば。\x02",
    )

    CloseMessageWindow()
    OP_8B(0x102, 0x10ACC, 0x9858, 0x1F4)

    ChrTalk(    #97
        0x102,
        (
            "#010Fでも、あの子……\x02\x03",

            "#010Fなんで歯車なんか探してたんだろう。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0x101,
        (
            "#000F……へ？\x02\x03",

            "#000Fうーん、\x01",
            "言われてみれば確かに不思議だけど……\x02\x03",

            "#000Fでも、いいじゃない。\x01",
            "大切なものなんて、人それぞれなんだし。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 0)

    ChrTalk(    #99
        0x102,
        (
            "#010Fはは、そうかもしれないね。\x02\x03",

            "#010F……さて、\x01",
            "それじゃあ、僕たちも行こうか。\x02\x03",

            "#010Fギルドに報告しに\x01",
            "行かないといけないし。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0x101,
        "#000Fうん、行こっ。\x02",
    )

    CloseMessageWindow()
    OP_92(0x1, 0x0, 0x0, 0xBB8, 0x0)
    OP_30(0x0)
    EventEnd(0x0)
    Jump("loc_1FAC")

    label("loc_1B55")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_END)), "loc_1E97")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x4, 0x0, 0x4)"), scpexpr(EXPR_END)), "loc_1BE1")

    ChrTalk(    #101
        0xFE,
        (
            "もし歯車を見っけたらさ、\x01",
            "オレに声かけてよ。この辺いるし。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0xFE,
        (
            "……さて、雑貨屋んトコは調べたし、\x01",
            "あとはどこだろ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E94")

    label("loc_1BE1")

    OP_28(0x4, 0x4, 0x4)
    OP_28(0x4, 0x4, 0x8)
    OP_28(0x4, 0x1, 0x1)
    OP_28(0x4, 0x4, 0x2)

    ChrTalk(    #103
        0xFE,
        (
            "ねえ、ちょっと聞きたいんだけどさ。\x01",
            "この辺で、歯車を見なかった？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xFE, 0)

    ChrTalk(    #104
        0x101,
        "#000Fへっ？　歯車？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(    #105
        0xFE,
        (
            "そう。\x01",
            "ギザギザで金ピカのやつ。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0xFE,
        "落ちてなかった？　どっかに。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0x101,
        (
            "#000F落し物？\x01",
            "うーん、ちょっと見なかったなぁ。\x02\x03",

            "#000Fどの辺りで落としたか分かる？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0xFE,
        (
            "お袋に呼ばれてさ、オレ、行ったんだ。\x01",
            "雑貨屋んトコまで。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0xFE,
        (
            "そんときは手に持ってたよ、ゼッタイ。\x01",
            "でも戻ってきたらなかった。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0x101,
        (
            "#000Fそれなら店の前があやしいじゃない。\x01",
            "もう調べたの？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0xFE,
        (
            "当然だろ？\x01",
            "ガキ扱いすんなよ。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #112
        0x101,
        "#002Fな、生意気～。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0xFE,
        (
            "まあ、ブレイサーにも頼んだから\x01",
            "じき見つかるだろうけど……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0xFE,
        (
            "もし見っけたらさ、オレに声かけて。\x01",
            "この辺いるし、たぶん。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E94")

    Jump("loc_1FAC")

    label("loc_1E97")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F49")
    OP_A2(0x10)

    ChrTalk(    #115
        0xFE,
        "……飛行船って、いいよな。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0xFE,
        (
            "来るとき乗ったんだけどさ、\x01",
            "でかくて、ゆったりしてて……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0xFE,
        (
            "オレの勘だけどさ、あれも全部\x01",
            "オーブメントで動いてんだぜ、きっと。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1FAC")

    label("loc_1F49")


    ChrTalk(    #118
        0xFE,
        "いいよな、飛行船って。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0xFE,
        (
            "オレの勘だけどさ、あれも全部\x01",
            "オーブメントで動いてんだぜ、きっと。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1FAC")

    TalkEnd(0x12)
    Return()

    # Function_1_142B end

    def Function_2_1FB0(): pass

    label("Function_2_1FB0")

    TalkBegin(0x13)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_END)), "loc_2670")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x50, 0)), scpexpr(EXPR_END)), "loc_2084")
    TurnDirection(0x13, 0x0, 0)

    ChrTalk(    #120
        0xFE,
        (
            "Oh, well, maybe I'll try heading\x01",
            "to Grancel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0xFE,
        (
            "Then again, my idiot son sure\x01",
            "hasn't been any help.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0xFE,
        (
            "Just when I think he's starting to\x01",
            "help, he disappears somewhere.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x13, 180, 0)
    Jump("loc_266D")

    label("loc_2084")

    OP_A2(0x280)

    ChrTalk(    #123
        0xFE,
        "Unbelievable...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0xFE,
        (
            "I came all the way here just to\x01",
            "find that I wasted all this time\x01",
            "for nothing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0xFE,
        (
            "I can't find any buyers and the\x01",
            "shops are bigger cheapskates\x01",
            "than I thought they'd be...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0xFE,
        (
            "I guess it's safe to say that backwater\x01",
            "places will always be backwater places.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(200)

    ChrTalk(    #127
        0x101,
        "#009F(This lady is really making me angry.)\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x13, 0x101, 0)

    ChrTalk(    #128
        0xFE,
        (
            "Huh? And who are you supposed\x01",
            "to be?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0xFE,
        (
            "Then again, I really don't care who\x01",
            "you are. I'll give you a deal, so how\x01",
            "about you buy something?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0x101,
        "#004FWhat...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0xFE,
        (
            "Will one of these wood carvings\x01",
            "work for you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0xFE,
        (
            "You won't find fine workmanship like\x01",
            "this outside the Calvard Republic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0x101,
        (
            "#501FCalvard? Sounds familiar...\x01",
            "Is that some famous store\x01",
            "or something?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #134
        0x102,
        (
            "#010FThe Calvard Republic is the country\x01",
            "to the east of the Liberl Kingdom.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #135
        0x101,
        "#008FI-I knew that.\x02",
    )

    CloseMessageWindow()

    def lambda_23E7():
        TurnDirection(0x102, 0x13, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_23E7)
    TurnDirection(0x101, 0x13, 400)

    ChrTalk(    #136
        0x102,
        (
            "#010FSo Calvard-made folk craft items\x01",
            "are what you're selling, huh?\x02\x03",

            "I'm sure you'd find a lot more people\x01",
            "willing to take them off your hands if\x01",
            "you went to the Royal City.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x13, 0x102, 400)

    ChrTalk(    #137
        0xFE,
        "*sigh* ...You think so?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0xFE,
        (
            "I really thought some place in the boonies\x01",
            "like this one would be a taker on these, but\x01",
            "maybe I was wrong.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(200)

    ChrTalk(    #139
        0x101,
        (
            "#009F(Danger. Danger.\x01",
            "Anger meter riiiiising...)\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x13, 0x0, 400)

    ChrTalk(    #140
        0xFE,
        (
            "Oh well, I guess I'll try heading to\x01",
            "Grancel sooner rather than later.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0xFE,
        (
            "Then again, what is my son,\x01",
            "Charles, up to?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0xFE,
        (
            "Just when I thought I could get some\x01",
            "help out of him, he ups and wanders\x01",
            "off.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x13, 180, 0)

    label("loc_266D")

    Jump("loc_2878")

    label("loc_2670")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_27A9")
    OP_A2(0x19)

    ChrTalk(    #143
        0xFE,
        (
            "For a backwoods town, these\x01",
            "stores do carry a pretty nice\x01",
            "selection of goods.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0xFE,
        (
            "The Liberl Kingdom definitely has\x01",
            "a different feel with all these\x01",
            "orbments everywhere.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0xFE,
        (
            "I'd better get in the mood to do business\x01",
            "starting tomorrow or I'm going to face some\x01",
            "serious financial repercussions.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2878")

    label("loc_27A9")


    ChrTalk(    #146
        0xFE,
        (
            "For a backwoods town, these\x01",
            "stores do carry a pretty nice\x01",
            "selection of goods.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0xFE,
        (
            "I'd better get in the mood to do business\x01",
            "starting tomorrow or I'm going to face some\x01",
            "serious financial repercussions.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2878")

    TalkEnd(0x13)
    Return()

    # Function_2_1FB0 end

    def Function_3_287C(): pass

    label("Function_3_287C")

    TalkBegin(0x14)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D, 0)), scpexpr(EXPR_END)), "loc_2906")

    ChrTalk(    #148
        0xFE,
        (
            "Today is another great day\x01",
            "for a cat nap.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0xFE,
        (
            "It looks like we'll be able to\x01",
            "relax this afternoon.\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x192, 0x0, 0x64)

    ChrTalk(    #150
        0x15,
        "Nyaaoo～n\x02",
    )

    CloseMessageWindow()
    Jump("loc_3B21")

    label("loc_2906")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 1)), scpexpr(EXPR_END)), "loc_2A17")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x9, 0x1, 0x8000)"), scpexpr(EXPR_END)), "loc_2960")
    OP_62(0x14, 0x0, 2000, 0x1C, 0x21, 0xFA, 0x0)
    Sleep(500)

    ChrTalk(    #151
        0xFE,
        "...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #152
        0xFE,
        "...Zzz...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0x15,
        "...Prrrrrr...\x02",
    )

    CloseMessageWindow()
    OP_63(0x14)
    Jump("loc_2A14")

    label("loc_2960")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x9, 0x0, 0x4)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x9, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_29CF")
    OP_28(0x9, 0x1, 0x8000)

    ChrTalk(    #154
        0x101,
        (
            "#004F(Look!)\x02\x03",

            "(The cat's come back.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #155
        0xFE,
        "...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #156
        0xFE,
        "...Zzz...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #157
        0xFE,
        "...Zzz...\x02",
    )

    CloseMessageWindow()
    OP_63(0x14)
    Jump("loc_2A14")

    label("loc_29CF")

    OP_62(0x14, 0x0, 2000, 0x1C, 0x21, 0xFA, 0x0)
    Sleep(500)

    ChrTalk(    #158
        0xFE,
        "...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #159
        0xFE,
        "...Zzz...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #160
        0x15,
        "...Prrrrrr...\x02",
    )

    CloseMessageWindow()
    OP_63(0x14)

    label("loc_2A14")

    Jump("loc_3B21")

    label("loc_2A17")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 1)), scpexpr(EXPR_END)), "loc_2D2C")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x9, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2B7A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B00")
    OP_A2(0x12)
    ClearChrFlags(0x14, 0x10)

    ChrTalk(    #161
        0xFE,
        (
            "What do we have here?\x01",
            "A handsome Bracer if ever\x01",
            "I've seen one.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #162
        0xFE,
        (
            "How about taking a nap with\x01",
            "li'l ol' me?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(400)

    ChrTalk(    #163
        0x102,
        (
            "#018FI'll have to take a raincheck\x01",
            "on that one...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B77")

    label("loc_2B00")

    ClearChrFlags(0x14, 0x10)

    ChrTalk(    #164
        0xFE,
        (
            "What do we have here?\x01",
            "A handsome Bracer if ever\x01",
            "I've seen one.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #165
        0xFE,
        (
            "How about taking a nap with\x01",
            "li'l ol' me?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B77")

    Jump("loc_2D29")

    label("loc_2B7A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x9, 0x1, 0x8000)"), scpexpr(EXPR_END)), "loc_2BF8")

    ChrTalk(    #166
        0xFE,
        (
            "I'm sorry for putting you through\x01",
            "all this trouble.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #167
        0xFE,
        "Aryll came back all by herself.\x02",
    )

    CloseMessageWindow()
    OP_22(0x192, 0x0, 0x64)

    ChrTalk(    #168
        0x15,
        "Nya～o.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2D29")

    label("loc_2BF8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x9, 0x0, 0x4)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x9, 0x1, 0x8000)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2CD6")
    OP_28(0x9, 0x1, 0x8000)

    ChrTalk(    #169
        0x101,
        (
            "#004FLook!\x02\x03",

            "The cat came back?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #170
        0xFE,
        (
            "What do we have here?\x01",
            "Oh, it's Mr. and Ms. Bracer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #171
        0xFE,
        "Aryll came back all by herself.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #172
        0xFE,
        (
            "What a good girl she is,\x01",
            "don't you think?\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x192, 0x0, 0x64)

    ChrTalk(    #173
        0x15,
        "Nya～o.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2D29")

    label("loc_2CD6")


    ChrTalk(    #174
        0xFE,
        "Aryll, where have you been?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #175
        0xFE,
        "I've been worried sick.\x02",
    )

    CloseMessageWindow()
    OP_22(0x192, 0x0, 0x64)

    ChrTalk(    #176
        0x15,
        "Mya～～go.\x02",
    )

    CloseMessageWindow()

    label("loc_2D29")

    Jump("loc_3B21")

    label("loc_2D2C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x9, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2DA7")

    ChrTalk(    #177
        0xFE,
        (
            "From now on, I guess I'll have to\x01",
            "cut back on my afternoon naps.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #178
        0xFE,
        "Right, Aryll?\x02",
    )

    CloseMessageWindow()
    OP_22(0x192, 0x0, 0x64)

    ChrTalk(    #179
        0x15,
        "Nyaaoo～n.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3B21")

    label("loc_2DA7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x9, 0x1, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x9, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2F58")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2EB5")
    OP_A2(0x12)
    ClearChrFlags(0x14, 0x10)
    TurnDirection(0x14, 0x101, 0)

    ChrTalk(    #180
        0xFE,
        "So did you find Aryll?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #181
        0x101,
        (
            "#000FWe sure did!\x02\x03",

            "#007FBut she ran away...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #182
        0xFE,
        "Is that so?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #183
        0xFE,
        (
            "That's quite peculiar since she's\x01",
            "not afraid of strangers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #184
        0xFE,
        (
            "Anyway, I'll be waiting here,\x01",
            "so please find my little Aryll.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2F55")

    label("loc_2EB5")

    ClearChrFlags(0x14, 0x10)
    TurnDirection(0x14, 0x0, 0)

    ChrTalk(    #185
        0xFE,
        (
            "That's so odd that she'd run away like\x01",
            "that. She's not afraid of strangers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #186
        0xFE,
        (
            "Anyway, I'll be waiting here,\x01",
            "so please find my little Aryll.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F55")

    Jump("loc_3B21")

    label("loc_2F58")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 7)), scpexpr(EXPR_END)), "loc_39F7")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x9, 0x0, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3991")
    OP_28(0x9, 0x4, 0x4)
    OP_28(0x9, 0x4, 0x8)
    OP_28(0x9, 0x4, 0x2)
    OP_28(0x9, 0x1, 0x1)
    EventBegin(0x0)
    Fade(1000)
    OP_6D(36950, 0, 57050, 0)
    OP_6C(0, 0)
    SetChrPos(0x101, 38560, 0, 57230, 270)
    SetChrPos(0x102, 37800, 0, 58080, 225)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2FF5")
    SetChrPos(0x2, 39290, 0, 58080, 211)
    SetChrPos(0x3, 40280, 0, 58050, 212)
    Jump("loc_3014")

    label("loc_2FF5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3014")
    SetChrPos(0x2, 39290, 0, 58080, 211)

    label("loc_3014")

    OP_0D()
    Sleep(100)

    ChrTalk(    #187
        0xFE,
        "#3PWhat am I ever to do?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #188
        0xFE,
        (
            "#3PI hope those Bracers will\x01",
            "show up sometime soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #189
        0x101,
        (
            "#000FDid I hear you say you're looking\x01",
            "for a couple of bracers?\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x14, 0x10)
    TurnDirection(0x14, 0x101, 0)

    ChrTalk(    #190
        0xFE,
        "#3PYes, that's right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #191
        0xFE,
        "#3PDoes this mean that you are they?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #192
        0x101,
        "#006FIt sure does.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x14, 0x102, 0)

    ChrTalk(    #193
        0xFE,
        (
            "#3PEven that handsome young man,\x01",
            "too?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x14, 0)

    ChrTalk(    #194
        0x102,
        "#010FThat's right. Myself included.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #195
        0xFE,
        (
            "#3PWell, well, what a pleasant\x01",
            "surprise this is. ☆\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #196
        0xFE,
        (
            "#3PThere certainly seem to be a lot\x01",
            "of people with the name 'Bracer'\x01",
            "these days.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(400)

    ChrTalk(    #197
        0x101,
        "#501F???\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #198
        0xFE,
        (
            "#3PDoes this mean that you are brother\x01",
            "and sister or something like that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #199
        0xFE,
        (
            "#3PYou know, that's got to be it.\x01",
            "When people have the same name\x01",
            "it usually means they're family.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #200
        0x101,
        (
            "#505FWell, I guess that's kind of\x01",
            "how it is for us...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 0)

    ChrTalk(    #201
        0x102,
        (
            "#014F(Estelle, I think this lady has\x01",
            "no idea what bracers are...)\x02\x03",

            "#014F(She seems to have mistaken the\x01",
            "word 'bracer' for somebody's name.)\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 0)
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(400)

    ChrTalk(    #202
        0x101,
        "#004F(Y-You can't be serious...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #203
        0xFE,
        (
            "#3PMay I ask what the two of you are\x01",
            "whispering to each other about?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #204
        0x102,
        (
            "#017F(It'll be a pain to explain all of this\x01",
            "to her, so let's just go along with\x01",
            "what she says.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #205
        0x101,
        "#506F(...I'll try.)\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x14, 400)
    Sleep(200)
    TurnDirection(0x101, 0x14, 400)

    ChrTalk(    #206
        0x102,
        (
            "#010FYou seem to be troubled over\x01",
            "something, ma'am...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x14, 0x102, 0)

    ChrTalk(    #207
        0xFE,
        (
            "#3PMy goodness. For such a cute little\x01",
            "dumpling you catch on quick.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #208
        0xFE,
        "#3PYoung boys are sooo considerate.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #209
        0x101,
        (
            "#509FHey. Are you really distressed or are\x01",
            "you just trying to flirt with someone\x01",
            "who's way too young for you?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x14, 0x101, 0)

    ChrTalk(    #210
        0xFE,
        (
            "#3POh, that's right. I am, I am.\x01",
            "I am sooo distressed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #211
        0xFE,
        "#3PMy little Aryll hasn't come home.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #212
        0xFE,
        (
            "#3PI carelessly dozed off here at\x01",
            "the cafe and she vanished.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #213
        0x101,
        "#000FAnd who is 'Aryll,' exactly?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #214
        0xFE,
        (
            "#3PMy little kitten.\x01",
            "She's so snuggly-wuggly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #215
        0xFE,
        (
            "#3POh, and if I might add, it's not\x01",
            "just her face that's so cute,\x01",
            "it's her personality as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #216
        0x102,
        (
            "#010FWhat's the color of your\x01",
            "kitten's fur?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #217
        0xFE,
        "#3PUmm, let me think for a moment...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #218
        0xFE,
        (
            "#3PMaybe it's like the color of the\x01",
            "evening sun in autumn shining\x01",
            "down upon a field of wheat.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #219
        0x102,
        "#010FSo, it's...tan-ish?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #220
        0xFE,
        (
            "#3PI think she's just out running\x01",
            "around somewhere, so if you\x01",
            "find her, please bring her back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #221
        0x102,
        (
            "#010FUnderstood. We'll start by looking\x01",
            "for her outdoors.\x02\x03",

            "#010FIf we find her we'll come back\x01",
            "and report to you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #222
        0xFE,
        "#3PI'll be waiting right here for you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #223
        0xFE,
        "#3PGood luck, Mr. and Ms. Bracer.\x02",
    )

    CloseMessageWindow()
    Sleep(50)
    EventEnd(0x4)
    Jump("loc_39F4")

    label("loc_3991")

    ClearChrFlags(0x14, 0x10)
    TurnDirection(0x14, 0x0, 0)

    ChrTalk(    #224
        0xFE,
        "I'll be waiting right here.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #225
        0xFE,
        (
            "Please find my little Aryll,\x01",
            "Mr. and Ms. Bracer.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_39F4")

    Jump("loc_3B21")

    label("loc_39F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 1)), scpexpr(EXPR_END)), "loc_3A56")

    ChrTalk(    #226
        0xFE,
        "Oh, what a troublesome little kitten.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #227
        0xFE,
        "Could she be taking a nap somewhere?\x02",
    )

    CloseMessageWindow()
    Jump("loc_3B21")

    label("loc_3A56")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 2)), scpexpr(EXPR_END)), "loc_3AA1")
    OP_62(0x14, 0x0, 2000, 0x1C, 0x21, 0xFA, 0x0)
    Sleep(500)

    ChrTalk(    #228
        0xFE,
        "...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #229
        0xFE,
        "...Zzz...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #230
        0x15,
        "...Zzz...\x02",
    )

    CloseMessageWindow()
    OP_63(0x14)
    Jump("loc_3B21")

    label("loc_3AA1")


    ChrTalk(    #231
        0xFE,
        (
            "It's such a warm day today,\x01",
            "isn't it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #232
        0xFE,
        (
            "It looks like we'll be able to\x01",
            "take a nice afternoon nap.\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x192, 0x0, 0x64)

    ChrTalk(    #233
        0x15,
        "Nyayayaa～.\x02",
    )

    CloseMessageWindow()

    label("loc_3B21")

    TalkEnd(0x14)
    SetChrFlags(0x14, 0x10)
    Return()

    # Function_3_287C end

    def Function_4_3B2A(): pass

    label("Function_4_3B2A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x4, 0x1, 0x20)"), scpexpr(EXPR_END)), "loc_3B39")
    Return()

    label("loc_3B39")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x4, 0x1, 0x4)"), scpexpr(EXPR_END)), "loc_3CC1")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3BFF")
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #234
        0x102,
        (
            "#010FIf you're so interested in seeing\x01",
            "what's down there, then how\x01",
            "about checking out the sewers?\x02\x03",

            "The entrance to the sewers should\x01",
            "be just behind the chapel.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3CBB")

    label("loc_3BFF")


    ChrTalk(    #235
        0x101,
        "#505FHmm...I wonder what's down there.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #236
        0x102,
        (
            "#010FIf you're so interested, then how\x01",
            "about checking out the sewers?\x02\x03",

            "The entrance to the sewers should\x01",
            "be just behind the chapel.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3CBB")

    TalkEnd(0xFF)
    Jump("loc_4260")

    label("loc_3CC1")

    OP_28(0x4, 0x1, 0x4)
    OP_28(0x4, 0x1, 0x8)
    OP_28(0x4, 0x1, 0x10)
    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x0, 46120, 0, 26090, 225)
    SetChrPos(0x1, 45540, 0, 27200, 180)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x64), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x64), scpexpr(EXPR_PUSH_LONG, 0x5A), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3D1D")
    OP_6C(350000, 0)
    Jump("loc_3D3E")

    label("loc_3D1D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x64), scpexpr(EXPR_PUSH_LONG, 0x5A), scpexpr(EXPR_GTR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x64), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3D3E")
    OP_6C(350000, 0)
    Jump("loc_3D3E")

    label("loc_3D3E")

    OP_0D()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3EB1")
    Sleep(400)
    OP_62(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(400)

    ChrTalk(    #237
        0x101,
        "#004FHuh...?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #238
        0x102,
        "#010FWhat's the matter?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #239
        0x101,
        (
            "#002FI wonder what that is...\x01",
            "There's something shining down\x01",
            "there through the sewer grate.\x02",
        )
    )

    CloseMessageWindow()
    OP_8E(0x102, 0xB176, 0x0, 0x67AC, 0x7D0, 0x0)
    LoadEffect(0x0, "map\\\\evsepith.eff")
    PlayEffect(0x0, 0xFF, 0xFF, 45050, 200, 25150, 0, 0, 0, 200, 400, 200, 0xFF, 0, 0, 0, 0)
    Sleep(1000)

    ChrTalk(    #240
        0x102,
        (
            "#014F...You're right.\x02\x03",

            "It looks like something must have\x01",
            "fallen through.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4085")

    label("loc_3EB1")

    Sleep(400)
    OP_62(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(400)

    ChrTalk(    #241
        0x102,
        "#014FHold up a second.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x1, 0x0, 0)

    ChrTalk(    #242
        0x101,
        "#000FWhat is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #243
        0x102,
        (
            "#014FI can see something shining down\x01",
            "there through the sewer grate.\x02",
        )
    )

    CloseMessageWindow()
    OP_8B(0x101, 0xB176, 0x67AC, 0x190)

    ChrTalk(    #244
        0x101,
        (
            "#000FWhere? Where?\x01",
            "Let me have a peek.\x02",
        )
    )

    CloseMessageWindow()
    OP_8E(0x101, 0xB176, 0x0, 0x67AC, 0x7D0, 0x0)
    LoadEffect(0x0, "map\\\\evsepith.eff")
    PlayEffect(0x0, 0xFF, 0xFF, 45050, 200, 25150, 0, 0, 0, 200, 400, 200, 0xFF, 0, 0, 0, 0)
    Sleep(800)

    ChrTalk(    #245
        0x101,
        (
            "#004FOh, you're right. I can see something\x01",
            "sparkling down there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #246
        0x102,
        (
            "#010FIt looks like it must have fallen down\x01",
            "into the sewers through the grate.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4085")

    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #247
        0x101,
        "#505FThe sewers?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #248
        0x102,
        (
            "#015FDon't tell me you forgot about\x01",
            "the sewers already...\x02\x03",

            "You know...that smelly, monster-\x01",
            "infested place we were in not that\x01",
            "long ago...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #249
        0x101,
        "#508FOh, right! Those sewers.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #250
        0x102,
        (
            "#010FWe went there during our\x01",
            "practical training, right?\x02\x03",

            "The entrance to the sewers should\x01",
            "be just behind the chapel.\x02\x03",

            "If you're so interested in what's\x01",
            "down there, then how about we\x01",
            "check it out a little later.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #251
        0x101,
        "#006FSure, let's do that.\x02",
    )

    CloseMessageWindow()
    OP_65(0x2, 0x1)
    OP_82(0x0, 0x0)
    OP_84(0x0)
    EventEnd(0x0)

    label("loc_4260")

    Return()

    # Function_4_3B2A end

    def Function_5_4261(): pass

    label("Function_5_4261")

    SetChrFlags(0x12, 0x40)
    OP_A6(0x11)
    OP_8E(0xFE, 0x10ACC, 0x0, 0x9858, 0x1B58, 0x0)
    SetChrFlags(0xFE, 0x80)
    OP_A3(0x11)
    Return()

    # Function_5_4261 end

    def Function_6_4286(): pass

    label("Function_6_4286")

    OP_A6(0xE)

    label("loc_4289")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_END)), "loc_429B")
    TurnDirection(0xFE, 0x12, 0)
    OP_48()
    Jump("loc_4289")

    label("loc_429B")

    OP_A3(0xE)
    Return()

    # Function_6_4286 end

    def Function_7_429F(): pass

    label("Function_7_429F")

    OP_A6(0xF)

    label("loc_42A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_END)), "loc_42B4")
    TurnDirection(0xFE, 0x12, 0)
    OP_48()
    Jump("loc_42A2")

    label("loc_42B4")

    OP_A3(0xF)
    Return()

    # Function_7_429F end

    def Function_8_42B8(): pass

    label("Function_8_42B8")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        32,
        0,
        (
            "Enter the sewers\x01",      # 0
            "Leave\x01",                 # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_4301"),
        (1, "loc_430D"),
        (SWITCH_DEFAULT, "loc_4313"),
    )


    label("loc_4301")

    NewScene("ED6_DT01/C0500   ._SN", 0, 0, 0)
    IdleLoop()
    Jump("loc_4313")

    label("loc_430D")

    TalkEnd(0xFF)
    Jump("loc_4313")

    label("loc_4313")

    Sleep(30)
    Return()

    # Function_8_42B8 end

    def Function_9_4319(): pass

    label("Function_9_4319")

    FadeToBright(500, 0)
    OP_6D(76970, 0, 20370, 0)
    SetChrPos(0x101, 76970, 0, 20370, 180)
    SetChrPos(0x102, 76970, 0, 20370, 0)
    OP_30(0x0)
    OP_0D()
    SetMapFlags(0x1)
    ClearMapFlags(0x80)
    Return()

    # Function_9_4319 end

    def Function_10_4363(): pass

    label("Function_10_4363")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x9, 0x0, 0x40)"), scpexpr(EXPR_END)), "loc_4370")
    Jump("loc_4679")

    label("loc_4370")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x9, 0x1, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_29(0x9, 0x0, 0x4)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4679")
    OP_28(0x9, 0x1, 0x2)
    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x16, 58830, 0, 40470, 165)
    ClearChrFlags(0x16, 0x80)
    SetChrFlags(0x16, 0x40)
    OP_6D(59150, 0, 42330, 0)
    OP_6C(135000, 0)
    SetChrPos(0x101, 59390, 0, 55350, 176)
    SetChrPos(0x102, 57010, 0, 55120, 164)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_441A")
    SetChrPos(0x2, 59390, 0, 57350, 176)
    SetChrPos(0x3, 57010, 0, 57120, 164)
    Jump("loc_4439")

    label("loc_441A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4439")
    SetChrPos(0x2, 59390, 0, 57350, 176)

    label("loc_4439")

    OP_0D()

    def lambda_4440():
        OP_6C(180000, 3000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_4440)

    def lambda_4450():
        OP_6D(58950, 0, 46580, 3000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_4450)
    OP_8E(0x16, 0xE63C, 0x0, 0xB63A, 0x7D0, 0x0)
    OP_8E(0x101, 0xE61E, 0x0, 0xCC6A, 0x1770, 0x0)

    ChrTalk(    #252
        0x101,
        "#004FLook!\x02",
    )

    CloseMessageWindow()
    OP_62(0x16, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(400)
    OP_63(0x16)
    OP_62(0x16, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(600)

    def lambda_44D6():
        OP_8E(0x101, 0xE95C, 0x0, 0xAB18, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_44D6)

    def lambda_44F1():
        OP_8E(0x102, 0xE48E, 0x0, 0xB450, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_44F1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_454D")

    def lambda_451A():
        OP_8E(0x2, 0xE75E, 0x0, 0xBF5E, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_451A)

    def lambda_4535():
        OP_8E(0x3, 0xE394, 0x0, 0xBD56, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_4535)
    Jump("loc_4576")

    label("loc_454D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4576")

    def lambda_4561():
        OP_8E(0x2, 0xE75E, 0x0, 0xBF5E, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_4561)

    label("loc_4576")

    OP_8E(0x16, 0xE6C8, 0x0, 0xAD16, 0x1770, 0x0)

    def lambda_4590():
        OP_6D(59770, 0, 44910, 2000)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_4590)
    OP_8E(0x16, 0xF082, 0x0, 0x95BA, 0x1770, 0x0)
    SetChrFlags(0x16, 0x80)
    ClearChrFlags(0x16, 0x40)
    WaitChrThread(0x0, 0x3)
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #253
        0x101,
        "#002FJoshua, is that cat...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #254
        0x102,
        (
            "#010FIt looks like the one that lady\x01",
            "was looking for.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #255
        0x101,
        (
            "#002FI'm certain that's the one.\x01",
            "We'd better hurry and catch it!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    EventEnd(0x4)
    Jump("loc_4679")

    label("loc_4679")

    Return()

    # Function_10_4363 end

    def Function_11_467A(): pass

    label("Function_11_467A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x9, 0x0, 0x40)"), scpexpr(EXPR_END)), "loc_4687")
    Jump("loc_4913")

    label("loc_4687")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x9, 0x1, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_29(0x9, 0x0, 0x4)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4913")
    OP_28(0x9, 0x1, 0x2)
    EventBegin(0x0)
    ClearMapFlags(0x1)
    SetChrPos(0x16, 48900, 0, 84200, 180)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x16, 0x8)
    SetChrFlags(0x16, 0x40)
    OP_43(0x16, 0x0, 0x1, 0xC)
    OP_43(0x16, 0x1, 0x1, 0xD)
    Fade(1000)
    SetChrPos(0x2, 47800, 0, 50200, 0)
    SetChrPos(0x3, 46800, 0, 50200, 0)
    Sleep(2000)
    SetChrPos(0x0, 48800, 0, 50200, 0)
    SetChrPos(0x1, 48800, 0, 50200, 0)
    OP_62(0x16, 0x0, 1700, 0x8, 0x9, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    OP_8E(0x16, 0xBFCC, 0x0, 0x116E8, 0xBB8, 0x0)
    OP_63(0x16)
    Sleep(500)
    SetChrPos(0x0, 48800, 0, 59200, 0)
    SetChrPos(0x1, 48800, 0, 59200, 0)

    ChrTalk(    #256
        0x101,
        "#004Fあっ！\x02",
    )

    CloseMessageWindow()
    OP_62(0x16, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(500)
    OP_63(0x16)
    OP_62(0x16, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(600)
    OP_43(0x101, 0x0, 0x1, 0xF)
    OP_43(0x102, 0x0, 0x1, 0x10)
    OP_43(0x16, 0x0, 0x1, 0xE)
    OP_A2(0x15)
    OP_A2(0x13)
    OP_A2(0x14)
    OP_A5(0x15)
    OP_A5(0x13)
    OP_A5(0x14)
    SetChrPos(0x16, 5488, 0, 16806, 0)
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x16, 0x8)

    ChrTalk(    #257
        0x101,
        "#002Fヨシュア、今のネコ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #258
        0x102,
        "#010Fさっき聞いたネコみたいだね。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #259
        0x101,
        (
            "#002F間違いないわ。\x01",
            "早く追いかけなきゃ！\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x2, 48800, 0, 62200, 0)
    SetChrPos(0x3, 48800, 0, 61200, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_48CF")
    OP_43(0x10F, 0x0, 0x1, 0x11)
    OP_43(0x110, 0x0, 0x1, 0x12)
    OP_A2(0x17)
    OP_A2(0x16)
    OP_92(0x1, 0x0, 0x0, 0xBB8, 0x0)
    OP_A5(0x16)
    OP_A5(0x17)
    Jump("loc_4902")

    label("loc_48CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A, 2)), scpexpr(EXPR_END)), "loc_48F4")
    OP_43(0x10F, 0x0, 0x1, 0x11)
    OP_A2(0x16)
    OP_92(0x1, 0x0, 0x0, 0xBB8, 0x0)
    OP_A5(0x16)
    Jump("loc_4902")

    label("loc_48F4")

    OP_92(0x1, 0x0, 0x0, 0xBB8, 0x0)

    label("loc_4902")

    OP_30(0x0)
    Sleep(50)
    EventEnd(0x4)
    SetMapFlags(0x1)
    Jump("loc_4913")

    label("loc_4913")

    Return()

    # Function_11_467A end

    def Function_12_4914(): pass

    label("Function_12_4914")

    OP_6D(49100, 0, 76400, 3000)
    Sleep(500)
    OP_6D(49100, 0, 70400, 2500)
    Return()

    # Function_12_4914 end

    def Function_13_493C(): pass

    label("Function_13_493C")

    OP_6C(0, 3000)
    Return()

    # Function_13_493C end

    def Function_14_4946(): pass

    label("Function_14_4946")

    SetChrFlags(0x16, 0x40)
    OP_A6(0x15)
    OP_8E(0x16, 0xE420, 0x0, 0x11170, 0x1B58, 0x0)
    SetChrFlags(0x16, 0x80)
    OP_A3(0x15)
    Return()

    # Function_14_4946 end

    def Function_15_496B(): pass

    label("Function_15_496B")

    OP_A6(0x13)
    SetChrFlags(0x101, 0x40)
    OP_8E(0x101, 0xC094, 0x0, 0x10108, 0x1B58, 0x0)
    OP_8C(0x101, 45, 0)
    ClearChrFlags(0x101, 0x40)
    OP_A3(0x13)
    Return()

    # Function_15_496B end

    def Function_16_4997(): pass

    label("Function_16_4997")

    OP_A6(0x14)
    SetChrFlags(0x102, 0x40)
    OP_8E(0x102, 0xBBE4, 0x0, 0xFE4B, 0xBB8, 0x0)
    OP_8C(0x102, 45, 0)
    ClearChrFlags(0x102, 0x40)
    OP_A3(0x14)
    Return()

    # Function_16_4997 end

    def Function_17_49C3(): pass

    label("Function_17_49C3")

    SetChrFlags(0x10F, 0x40)
    OP_92(0x10F, 0x0, 0x0, 0xBB8, 0x0)
    ClearChrFlags(0x10F, 0x40)
    OP_A3(0x16)
    Return()

    # Function_17_49C3 end

    def Function_18_49DF(): pass

    label("Function_18_49DF")

    SetChrFlags(0x110, 0x40)
    OP_92(0x110, 0x0, 0x0, 0xBB8, 0x0)
    ClearChrFlags(0x110, 0x40)
    OP_A3(0x17)
    Return()

    # Function_18_49DF end

    def Function_19_49FB(): pass

    label("Function_19_49FB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x9, 0x0, 0x40)"), scpexpr(EXPR_END)), "loc_4A08")
    Jump("loc_4C45")

    label("loc_4A08")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x9, 0x1, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_29(0x9, 0x1, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4C45")
    OP_28(0x9, 0x1, 0x4)
    EventBegin(0x0)
    ClearMapFlags(0x1)
    SetChrPos(0x16, 60700, 0, 14400, 270)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x16, 0x8)
    SetChrFlags(0x16, 0x40)
    Fade(1000)
    OP_43(0x16, 0x0, 0x1, 0x14)
    OP_43(0x16, 0x1, 0x1, 0x15)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4A8F")
    SetChrPos(0x2, 47400, 0, 50200, 0)
    SetChrPos(0x3, 46400, 0, 50200, 0)
    Jump("loc_4AAE")

    label("loc_4A8F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4AAE")
    SetChrPos(0x2, 47400, 0, 50200, 0)

    label("loc_4AAE")

    OP_8E(0x16, 0xC5A8, 0x0, 0x3840, 0xBB8, 0x0)
    OP_8E(0x16, 0xBDD8, 0x0, 0x3DB8, 0xBB8, 0x0)
    SetChrPos(0x0, 48800, 0, 29600, 0)
    SetChrPos(0x1, 48800, 0, 29600, 0)

    ChrTalk(    #260
        0x101,
        "#004FLook! It's that cat again!\x02",
    )

    CloseMessageWindow()
    OP_62(0x16, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_8E(0x16, 0xBDD8, 0x0, 0x3E80, 0xBB8, 0x0)
    Sleep(500)
    OP_63(0x16)
    OP_62(0x16, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(600)

    ChrTalk(    #261
        0x101,
        "#005FGet back here!\x02",
    )

    CloseMessageWindow()
    OP_43(0x101, 0x0, 0x1, 0x17)
    OP_43(0x102, 0x0, 0x1, 0x18)
    OP_43(0x16, 0x0, 0x1, 0x16)
    OP_A2(0x15)
    OP_A2(0x13)
    OP_A2(0x14)
    OP_A5(0x15)
    OP_A5(0x13)
    OP_A5(0x14)
    SetChrPos(0x16, 5488, 0, 16806, 0)
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x16, 0x8)

    ChrTalk(    #262
        0x102,
        (
            "#017FThis is just like back at the\x01",
            "Perzel Farm...\x02\x03",

            "#017FIt seems like we're doing a\x01",
            "lot of chasing these days.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    EventEnd(0x4)
    SetMapFlags(0x1)
    Jump("loc_4C45")

    label("loc_4C45")

    Return()

    # Function_19_49FB end

    def Function_20_4C46(): pass

    label("Function_20_4C46")

    OP_6D(48800, 0, 16800, 3000)
    Return()

    # Function_20_4C46 end

    def Function_21_4C58(): pass

    label("Function_21_4C58")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x64), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x64), scpexpr(EXPR_PUSH_LONG, 0x5A), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4C79")
    OP_6C(0, 3000)
    Jump("loc_4CA3")

    label("loc_4C79")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x64), scpexpr(EXPR_PUSH_LONG, 0x10E), scpexpr(EXPR_GTR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x64), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4C9A")
    OP_6C(0, 3000)
    Jump("loc_4CA3")

    label("loc_4C9A")

    OP_6C(180000, 3000)

    label("loc_4CA3")

    Return()

    # Function_21_4C58 end

    def Function_22_4CA4(): pass

    label("Function_22_4CA4")

    SetChrFlags(0x16, 0x40)
    OP_A6(0x15)
    OP_8E(0x16, 0xD994, 0x0, 0x3840, 0x1B58, 0x0)
    SetChrFlags(0x16, 0x80)
    OP_A3(0x15)
    Return()

    # Function_22_4CA4 end

    def Function_23_4CC9(): pass

    label("Function_23_4CC9")

    OP_A6(0x13)
    SetChrFlags(0x101, 0x40)
    OP_8E(0x101, 0xBC48, 0x0, 0x4E84, 0x1B58, 0x0)
    OP_8C(0x101, 135, 0)
    ClearChrFlags(0x101, 0x40)
    OP_A3(0x13)
    Return()

    # Function_23_4CC9 end

    def Function_24_4CF5(): pass

    label("Function_24_4CF5")

    OP_A6(0x14)
    SetChrFlags(0x102, 0x40)
    OP_8E(0x102, 0xC0F8, 0x0, 0x558C, 0xBB8, 0x0)
    OP_8C(0x102, 135, 0)
    ClearChrFlags(0x102, 0x40)
    OP_A3(0x14)
    Return()

    # Function_24_4CF5 end

    def Function_25_4D21(): pass

    label("Function_25_4D21")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x9, 0x0, 0x40)"), scpexpr(EXPR_END)), "loc_4D2E")
    Jump("loc_4F87")

    label("loc_4D2E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x9, 0x1, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_29(0x9, 0x1, 0x4)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4F87")
    OP_28(0x9, 0x1, 0x8)
    EventBegin(0x0)
    ClearMapFlags(0x1)
    Fade(1000)
    OP_6C(180000, 0)
    OP_6D(64629, 0, 38310, 0)
    SetChrPos(0x16, 75500, 0, 40200, 270)
    SetChrFlags(0x101, 0x40)
    SetChrFlags(0x102, 0x40)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x16, 0x8)
    SetChrFlags(0x16, 0x40)
    OP_0D()
    OP_62(0x16, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    OP_8E(0x16, 0xFD84, 0x0, 0x9DD0, 0xBB8, 0x0)
    TurnDirection(0x101, 0x16, 0)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(500)

    ChrTalk(    #263
        0x101,
        "#004FThere's that cat again!\x02",
    )

    CloseMessageWindow()
    OP_8E(0x101, 0xFBF4, 0x0, 0x8BD8, 0x1770, 0x0)
    TurnDirection(0x101, 0x16, 0)
    TurnDirection(0x16, 0x101, 0)

    def lambda_4E2C():
        OP_92(0x102, 0x101, 0x5DC, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4E2C)
    OP_62(0x16, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_95(0x16, 0x0, 0x0, 0x0, 0x320, 0x2EE0)
    Sleep(500)
    WaitChrThread(0x102, 0x1)
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #264
        0x102,
        (
            "#014FEstelle, wait a minute.\x02\x03",

            "#014FMaybe that kitten is trying to...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #265
        0x101,
        "#004FOh no, it's getting away!\x02",
    )

    CloseMessageWindow()
    OP_90(0x101, 0x0, 0x0, 0x3E8, 0x1B58, 0x0)
    OP_43(0x101, 0x0, 0x1, 0x1D)
    OP_43(0x16, 0x0, 0x1, 0x1C)
    OP_A2(0x15)
    OP_A2(0x13)
    OP_A5(0x15)
    OP_A5(0x13)

    ChrTalk(    #266
        0x101,
        (
            "#005FIt went toward the chapel!\x01",
            "Let's hurry and catch it!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #267
        0x102,
        "#017FHere we go again...\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x101, 0x40)
    ClearChrFlags(0x102, 0x40)
    Sleep(50)
    EventEnd(0x4)
    Jump("loc_4F87")

    label("loc_4F87")

    Return()

    # Function_25_4D21 end

    def Function_26_4F88(): pass

    label("Function_26_4F88")

    OP_6D(64300, 0, 38200, 3000)
    Return()

    # Function_26_4F88 end

    def Function_27_4F9A(): pass

    label("Function_27_4F9A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x64), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x64), scpexpr(EXPR_PUSH_LONG, 0x5A), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4FBB")
    OP_6C(0, 3000)
    Jump("loc_4FE5")

    label("loc_4FBB")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x64), scpexpr(EXPR_PUSH_LONG, 0x10E), scpexpr(EXPR_GTR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x64), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4FDC")
    OP_6C(0, 3000)
    Jump("loc_4FE5")

    label("loc_4FDC")

    OP_6C(180000, 3000)

    label("loc_4FE5")

    Return()

    # Function_27_4F9A end

    def Function_28_4FE6(): pass

    label("Function_28_4FE6")

    SetChrFlags(0x16, 0x40)
    OP_A6(0x15)
    OP_62(0x16, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    OP_8E(0x16, 0x11BFC, 0x1F4, 0x87F0, 0x1B58, 0x0)
    SetChrFlags(0xFE, 0x80)
    OP_A3(0x15)
    Return()

    # Function_28_4FE6 end

    def Function_29_501D(): pass

    label("Function_29_501D")

    OP_A6(0x13)

    label("loc_5020")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 5)), scpexpr(EXPR_END)), "loc_5032")
    TurnDirection(0x101, 0x16, 0)
    OP_48()
    Jump("loc_5020")

    label("loc_5032")

    OP_A3(0x13)
    Return()

    # Function_29_501D end

    def Function_30_5036(): pass

    label("Function_30_5036")

    OP_92(0x102, 0x101, 0x5DC, 0xBB8, 0x0)
    Return()

    # Function_30_5036 end

    def Function_31_5045(): pass

    label("Function_31_5045")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x9, 0x0, 0x40)"), scpexpr(EXPR_END)), "loc_5052")
    Jump("loc_52E8")

    label("loc_5052")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x9, 0x1, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_29(0x9, 0x1, 0x4)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_52E8")
    OP_28(0x9, 0x1, 0x8)
    EventBegin(0x0)
    ClearMapFlags(0x1)
    Fade(1000)
    OP_6C(90000, 0)
    OP_6D(64500, 0, 40400, 0)
    SetChrPos(0x16, 75500, 0, 40200, 270)
    SetChrFlags(0x101, 0x40)
    SetChrFlags(0x102, 0x40)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x16, 0x8)
    SetChrFlags(0x16, 0x40)
    SetChrPos(0x101, 61000, 0, 40300, 90)
    SetChrPos(0x102, 60000, 0, 42300, 90)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5111")
    SetChrPos(0x2, 59000, 0, 41300, 90)
    SetChrPos(0x3, 59000, 0, 42800, 90)
    Jump("loc_5130")

    label("loc_5111")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5130")
    SetChrPos(0x2, 59000, 0, 41300, 90)

    label("loc_5130")

    OP_0D()
    OP_62(0x16, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    OP_8E(0x16, 0x1016C, 0x0, 0x9DD0, 0xBB8, 0x0)
    TurnDirection(0x101, 0x16, 0)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(500)

    ChrTalk(    #268
        0x101,
        "#004F#6PThere's that cat again!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x16, 0)
    TurnDirection(0x16, 0x101, 0)
    OP_62(0x16, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_95(0x16, 0x0, 0x0, 0x0, 0x320, 0x2EE0)
    Sleep(500)
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #269
        0x102,
        (
            "#014FEstelle, wait a minute.\x02\x03",

            "#014FMaybe that kitten is trying to...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #270
        0x101,
        "#004F#6POh no, it's getting away!\x02",
    )

    CloseMessageWindow()
    OP_43(0x101, 0x0, 0x1, 0x22)
    OP_43(0x16, 0x0, 0x1, 0x1C)
    OP_A2(0x15)
    OP_A2(0x13)
    OP_A5(0x15)
    OP_A5(0x13)
    Sleep(500)

    ChrTalk(    #271
        0x101,
        (
            "#005FIt went toward the chapel!\x01",
            "Let's hurry and catch it!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #272
        0x102,
        "#017FHere we go again...\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x101, 0x40)
    ClearChrFlags(0x102, 0x40)
    Sleep(50)
    EventEnd(0x4)
    Jump("loc_52E8")

    label("loc_52E8")

    Return()

    # Function_31_5045 end

    def Function_32_52E9(): pass

    label("Function_32_52E9")

    OP_6D(64300, 0, 40200, 3000)
    Return()

    # Function_32_52E9 end

    def Function_33_52FB(): pass

    label("Function_33_52FB")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x64), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x64), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_531C")
    OP_6C(90000, 3000)
    Jump("loc_5325")

    label("loc_531C")

    OP_6C(270000, 3000)

    label("loc_5325")

    Return()

    # Function_33_52FB end

    def Function_34_5326(): pass

    label("Function_34_5326")

    OP_A6(0x13)
    OP_90(0x101, 0xBB8, 0x0, 0x0, 0x1B58, 0x0)
    OP_8C(0x101, 135, 400)
    OP_A3(0x13)
    Return()

    # Function_34_5326 end

    def Function_35_5348(): pass

    label("Function_35_5348")

    EventBegin(0x0)
    FadeToBright(1000, 0)
    OP_6C(45000, 0)
    OP_6D(36470, 0, 58400, 0)
    OP_67(0, 11530, -10000, 0)
    OP_6B(2150, 0)
    SetChrPos(0x101, 38560, 0, 57230, 270)
    SetChrPos(0x102, 37800, 0, 58080, 225)
    TurnDirection(0x14, 0x101, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_53E3")
    SetChrPos(0x2, 39290, 0, 58080, 211)
    SetChrPos(0x3, 40280, 0, 58050, 212)
    Jump("loc_5402")

    label("loc_53E3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5402")
    SetChrPos(0x2, 39290, 0, 58080, 211)

    label("loc_5402")

    SetChrPos(0x15, 36010, 0, 56150, 36)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x15, 0x8)
    ClearChrFlags(0x15, 0x40)
    TurnDirection(0x14, 0x102, 0)

    def lambda_542F():
        OP_6C(0, 4000)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_542F)
    OP_0D()
    Sleep(3000)

    ChrTalk(    #273
        0x102,
        (
            "#010F...and that's pretty much everything\x01",
            "that happened.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(1000)

    ChrTalk(    #274
        0x102,
        (
            "#010FI'm pretty sure that Aryll was on her\x01",
            "way back to see you from the beginning.\x02\x03",

            "#010FEach time we saw her she had been\x01",
            "walking toward the cafe.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #275
        0x101,
        (
            "#004FNow that you mention it...\x01",
            "that does seem like what happened.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #276
        0x102,
        (
            "#013FThere's a chance that because of us,\x01",
            "she ended up coming back this late...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x14, 0x102, 400)

    ChrTalk(    #277
        0x14,
        "Oh, don't be silly!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x14, 0)

    ChrTalk(    #278
        0x14,
        (
            "You two brought her back safe and sound.\x01",
            "I'm really grateful to the both of you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #279
        0x14,
        (
            "But especially you, Mr. Bracer.\x01",
            "You are just the cat's meow!\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x192, 0x0, 0x64)

    ChrTalk(    #280
        0x15,
        "Nyayayaa～～.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #281
        0x102,
        "#018FUh, I'll take that as a compliment.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 0)

    ChrTalk(    #282
        0x101,
        "#507F(You're blushing, Joshua.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #283
        0x14,
        (
            "I'd sure like to put a collar on you!\x01",
            "Then you'd be purrrrrrrrrrrrfect.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    ChrTalk(    #284
        0x102,
        (
            "#511FI-I apologize, but we're going to\x01",
            "need to get back and report to\x01",
            "the guild...\x02\x03",

            "H-Have a nice day!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x14, 0)

    ChrTalk(    #285
        0x101,
        "#508FSee you later!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #286
        0x14,
        (
            "Oh yes, I hope to be seeing\x01",
            "a lot more of Mr. Bracer!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5821():

        label("loc_5821")

        TurnDirection(0x0, 0x14, 0)
        OP_48()
        Jump("loc_5821")

    QueueWorkItem2(0x0, 1, lambda_5821)

    def lambda_5832():

        label("loc_5832")

        TurnDirection(0x1, 0x14, 0)
        OP_48()
        Jump("loc_5832")

    QueueWorkItem2(0x1, 1, lambda_5832)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5870")

    def lambda_5851():

        label("loc_5851")

        TurnDirection(0x2, 0x14, 0)
        OP_48()
        Jump("loc_5851")

    QueueWorkItem2(0x2, 1, lambda_5851)

    def lambda_5862():

        label("loc_5862")

        TurnDirection(0x3, 0x14, 0)
        OP_48()
        Jump("loc_5862")

    QueueWorkItem2(0x3, 1, lambda_5862)
    Jump("loc_588F")

    label("loc_5870")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_588F")

    def lambda_5884():

        label("loc_5884")

        TurnDirection(0x2, 0x14, 0)
        OP_48()
        Jump("loc_5884")

    QueueWorkItem2(0x2, 1, lambda_5884)

    label("loc_588F")

    SetChrFlags(0x15, 0x40)
    SetChrFlags(0x14, 0x40)

    def lambda_589F():
        OP_8E(0x15, 0x8AB6, 0x0, 0xC7EC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_589F)

    def lambda_58BA():
        OP_8E(0x14, 0x8ACA, 0x0, 0xC918, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_58BA)
    Sleep(400)
    WaitChrThread(0x14, 0x1)
    WaitChrThread(0x15, 0x1)
    OP_44(0x0, 0x1)
    OP_44(0x1, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_58FF")
    OP_44(0x2, 0x1)
    OP_44(0x3, 0x1)
    Jump("loc_5911")

    label("loc_58FF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5911")
    OP_44(0x2, 0x1)

    label("loc_5911")

    ClearChrFlags(0x15, 0x40)
    ClearChrFlags(0x14, 0x40)
    SetChrPos(0x14, 39420, 250, 51560, 315)
    SetChrPos(0x15, 38700, 0, 50720, 315)
    SetChrChipByIndex(0x14, 20)
    OP_22(0x17, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #287
        "\x07\x00Quest \x07\x02[Lost Kitten] \x07\x00completed!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    Sleep(1000)
    ClearMapFlags(0x400000)
    EventEnd(0x0)
    Return()

    # Function_35_5348 end

    SaveToFile()

Try(main)
