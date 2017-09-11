from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'C2219_1 ._SN',
        MapName             = 'Rolent',
        Location            = 'C2210.x',
        MapIndex            = 84,
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

    ScpFunction(
        "Function_0_66",           # 00, 0
        "Function_1_2011",         # 01, 1
        "Function_2_3964",         # 02, 2
        "Function_3_398C",         # 03, 3
        "Function_4_39B4",         # 04, 4
        "Function_5_39DC",         # 05, 5
    )


    def Function_0_66(): pass

    label("Function_0_66")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x1D, 0x0, 0x8)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x1D, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x1D, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1308")
    OP_28(0x1D, 0x4, 0x10)
    OP_28(0x1D, 0x1, 0x80)
    EventBegin(0x0)
    ClearMapFlags(0x1)
    Fade(1000)
    SetChrPos(0x101, -970, 0, 201500, 270)
    SetChrPos(0x102, -120, 0, 201000, 270)
    SetChrPos(0x105, 330, 0, 202500, 270)
    OP_69(0x8, 0x3E8)
    TalkBegin(0x8)

    ChrTalk(    #0
        0x101,
        "#001FWeeeeeee're back!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "Huh? Aren't ya them kids\x01",
            "from before...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x101,
        (
            "#001FTee hee. It's been a while since\x01",
            "we were last up this way.\x02\x03",

            "#006FAnd today, we're here on\x01",
            "another job.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x102,
        (
            "#010FA request came in to the Bracer\x01",
            "Guild, so we're here to deliver\x01",
            "this Maintenance Kit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x101,
        (
            "#000FHere ya go. It's a little heavy,\x01",
            "though, so be careful lifting it!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 400)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #5
        "\x07\x00Handed over \x07\x02Maintenance Kit\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3F(0x326, 1)

    ChrTalk(    #6
        0x8,
        "Yep, everything's here, all right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x8,
        (
            "I appreciate ya bringin' this all\x01",
            "the way over here.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x1D, 0x1, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_40(0x19A)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_6E1")

    ChrTalk(    #8
        0x101,
        (
            "#000FOh, no worries.\x01",
            "It's our job, after all!\x02\x03",

            "The townsfolk were actually really\x01",
            "worried about you, too, so I'm just\x01",
            "glad to see you're doing well!\x02\x03",

            "Work must be tough, so take care\x01",
            "of yourself, okay? Don't overexert\x01",
            "those old bones of yours!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x8,
        (
            "I'll do that. Thank ya for your\x01",
            "concern...blunt as it be.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x8,
        (
            "...So does this mean you're\x01",
            "startin' to understand what it\x01",
            "means to possess a caring soul?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x101,
        (
            "#506FUh...nope! Not really!\x02\x03",

            "I'm no good with those touchy-\x01",
            "feely concepts, I guess.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xFE,
        (
            "And here I thought you'd grown\x01",
            "up a bit...ah well!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xFE,
        (
            "Hmm...I guess you've still got\x01",
            "a ways to go before you can match\x01",
            "the level of THAT bracer...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        (
            "...Anyway, thank ya for bringing\x01",
            "this stuff all the way up here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xFE,
        (
            "I'd best get to work. Time to\x01",
            "start my rounds!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x101,
        (
            "#000FWell, you take care now, okay?\x01",
            "Don't break your hip!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x102,
        "#010FExcuse us, please.\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    OP_22(0x17, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #18
        "\x07\x00Quest \x07\x02[Maintenance Delivery] \x07\x00completed!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(100)
    EventEnd(0x0)
    TalkEnd(0x8)
    Jump("loc_1305")

    label("loc_6E1")


    ChrTalk(    #19
        0x101,
        (
            "#000FOh, no worries.\x01",
            "It's our job, after all!\x02\x03",

            "Uh, on another note, we actually\x01",
            "have something else for you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x8,
        "Ohh?\x02",
    )

    CloseMessageWindow()
    OP_90(0x105, 0xFFFFFCE0, 0x0, 0x0, 0x7D0, 0x0)
    OP_92(0x105, 0x8, 0x3E8, 0x7D0, 0x0)

    ChrTalk(    #21
        0x105,
        (
            "#040FHere you are, sir.\x02\x03",

            "It was entrusted to our care by\x01",
            "Primo, from Lavantar.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x105, 400)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #22
        "\x07\x00Handed over \x07\x02Azelia Rose\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3F(0x19A, 1)
    OP_28(0x1D, 0x1, 0x20)
    OP_91(0x105, 0x190, 0x0, 0x190, 0x7D0, 0x0)

    ChrTalk(    #23
        0x8,
        (
            "Oh, my, my, my!\x01",
            "It's Azelia Rose!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x8,
        (
            "I used to drink this all the time\x01",
            "while munching on anchovy dishes.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x391)"), scpexpr(EXPR_END)), "loc_B09")
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        0,
        (
            "[Hand over Salted Anchovy]\x01",      # 0
            "[Keep it]\x01",                       # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_935"),
        (1, "loc_AAB"),
        (SWITCH_DEFAULT, "loc_B06"),
    )


    label("loc_935")


    ChrTalk(    #25
        0x101,
        (
            "#001FHa-HA! ♪\x01",
            "I've got one of those for you, too!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 400)
    SetMessageWindowPos(-1, -1, -1, -1)
    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #26
        "\x07\x00Handed over \x07\x02Salted Anchovy\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3F(0x391, 1)
    OP_28(0x1D, 0x1, 0x40)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(400)

    ChrTalk(    #27
        0x8,
        "Ohh! OHHHH!!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x8,
        (
            "You've even brought me some munchies\x01",
            "to go with it! What thoughtful bracers\x01",
            "ya are!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x8,
        (
            "Man, this takes me back. How\x01",
            "are Primo and the others?\x01",
            "Are they doing well?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B06")

    label("loc_AAB")

    TurnDirection(0x8, 0x101, 400)

    ChrTalk(    #30
        0x8,
        (
            "Man, this takes me back. How\x01",
            "are Primo and the others?\x01",
            "Are they doing well?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B06")

    label("loc_B06")

    Jump("loc_B61")

    label("loc_B09")

    TurnDirection(0x8, 0x101, 400)

    ChrTalk(    #31
        0x8,
        (
            "Man, this takes me back. How\x01",
            "are Primo and the others?\x01",
            "Are they doing well?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B61")


    ChrTalk(    #32
        0x101,
        (
            "#000FYou bet! They're all worried about\x01",
            "you, too, Gramps.\x02\x03",

            "Work must be tough, so take care\x01",
            "of yourself, okay? Don't overexert\x01",
            "those old bones of yours!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x8,
        (
            "I...uh...won't? Well, blunt or no,\x01",
            "thank ya for the concern. I value\x01",
            "that even more than anchovies!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x8,
        (
            "...So does this mean you're\x01",
            "startin' to understand what it\x01",
            "means to possess a caring soul?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x101,
        (
            "#506FUh...nope! Not really!\x02\x03",

            "I'm no good with those touchy-\x01",
            "feely concepts, I guess.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0xFE,
        (
            "Well, I thought ya did a fine\x01",
            "job today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xFE,
        (
            "O' course, you could always\x01",
            "do better.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xFE,
        (
            "Oh, that reminds me...\x01",
            "Wait right there for a moment,\x01",
            "if ya would.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_DCA():

        label("loc_DCA")

        TurnDirection(0x102, 0x8, 400)
        OP_48()
        Jump("loc_DCA")

    QueueWorkItem2(0x102, 1, lambda_DCA)

    def lambda_DDB():

        label("loc_DDB")

        TurnDirection(0x101, 0x8, 400)
        OP_48()
        Jump("loc_DDB")

    QueueWorkItem2(0x101, 1, lambda_DDB)

    def lambda_DEC():

        label("loc_DEC")

        TurnDirection(0x105, 0x8, 400)
        OP_48()
        Jump("loc_DEC")

    QueueWorkItem2(0x105, 1, lambda_DEC)
    OP_8E(0x8, 0xFFFFF7E0, 0x0, 0x31A38, 0x7D0, 0x0)
    OP_8E(0x8, 0xFFFFF20E, 0x0, 0x31DBC, 0x7D0, 0x0)
    OP_8E(0x8, 0xFFFFE8D6, 0x0, 0x31C9A, 0x7D0, 0x0)
    OP_8C(0x8, 315, 0)
    Sleep(1000)
    OP_8E(0x8, 0xFFFFE8D6, 0x0, 0x31C9A, 0x7D0, 0x0)
    OP_8E(0x8, 0xFFFFF20E, 0x0, 0x31DBC, 0x7D0, 0x0)
    OP_8E(0x8, 0xFFFFF7E0, 0x0, 0x31A38, 0x7D0, 0x0)
    OP_8E(0x8, 0xFFFFF7A4, 0x0, 0x3131C, 0x7D0, 0x0)
    TurnDirection(0x8, 0x101, 400)
    OP_44(0x102, 0xFF)
    OP_44(0x101, 0xFF)
    OP_44(0x105, 0xFF)

    ChrTalk(    #39
        0x8,
        (
            "I have something for ya. Something\x01",
            "I once used a long, long time ago...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0xFE,
        (
            "I'd be pleased as plum if you'd accept\x01",
            "these for bringing all of these things\x01",
            "out here for me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x8,
        (
            "They may be a little old, but like\x01",
            "me, they'll still do the job,\x01",
            "sure as the day ya were born!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x1D, 0x1, 0x40)"), scpexpr(EXPR_END)), "loc_1047")
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #42
        "\x07\x00Received \x07\x02Work Helmet\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #43
        "\x07\x00Received \x07\x02Gladiator Headband\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x148, 1)
    OP_3E(0x146, 1)
    Jump("loc_1097")

    label("loc_1047")

    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #44
        "\x07\x00Received \x07\x02Work Helmet\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x148, 1)

    label("loc_1097")


    ChrTalk(    #45
        0x101,
        "#001FWhoa, awesome! Thanks!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x102,
        "#014FYou sure we can have these?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x102, 400)

    ChrTalk(    #47
        0x8,
        (
            "Absolutely! Not like I'll be setting\x01",
            "sail for wild, exotic lands again\x01",
            "any time soon!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0xFE,
        (
            "...Anyway, thank ya for bringing\x01",
            "this stuff all the way up here.\x01",
            "Now, I'd best get back to work.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(    #49
        0x8,
        (
            "I've basically been playing hooky this\x01",
            "whole time we've been talking! I stay here\x01",
            "any longer, and somebody's bound to notice!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x105,
        "#040FPlease take care of yourself.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x101,
        "#000FTake care, you old coot!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x102,
        "#010FPlease excuse us.\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    OP_22(0x17, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #53
        "\x07\x00Quest \x07\x02[Maintenance Delivery] \x07\x00completed!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(100)
    EventEnd(0x0)
    TalkEnd(0x8)

    label("loc_1305")

    Jump("loc_2010")

    label("loc_1308")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x88, 2)), scpexpr(EXPR_END)), "loc_17C8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8B, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_162A")
    OP_A2(0x458)
    OP_A2(0x0)

    ChrTalk(    #54
        0xFE,
        (
            "Oh, is it you kids again? It was\x01",
            "pretty rough the other night,\x01",
            "wasn't it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x101,
        (
            "#004FIt WAS pretty crazy. Speaking of\x01",
            "which, how are you holding up?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0xFE,
        (
            "I admit I was a tad fuzzy\x01",
            "until just a bit ago, but the ol'\x01",
            "noggin's back to normal now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0xFE,
        "Right as rain, I'd say.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x102,
        (
            "#013FIt looks like the anesthetic has\x01",
            "completely worn off, then.\x02\x03",

            "Luckily it was a pretty harmless\x01",
            "dose to begin with, so there\x01",
            "shouldn't be any lasting effects.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x101,
        "#501FThat's a relief to hear.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0xFE,
        (
            "Well then, I guess it's time\x01",
            "I get back to my work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x101,
        (
            "#000FDon't overdo it.\x02\x03",

            "You may feel fine now, but you\x01",
            "just got over the effects of the\x01",
            "drug.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0xFE,
        (
            "You know? Ya just may be right.\x02\x03",

            "Then I guess this old man'll take a\x01",
            "few more breathers than he normally\x01",
            "does. That should do the trick.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17C5")

    label("loc_162A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1721")
    OP_A2(0x0)

    ChrTalk(    #63
        0xFE,
        "Oh, is it you kids again?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0xFE,
        (
            "Whew... Looks like that stuff they\x01",
            "used on me has finally worn off.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0xFE,
        (
            "I was downright fuzzy before,\x01",
            "but now I feel like my old self\x01",
            "again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0xFE,
        (
            "Well, I guess it's about time\x01",
            "I got back to work.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17C5")

    label("loc_1721")


    ChrTalk(    #67
        0xFE,
        (
            "Looks like that stuff they used\x01",
            "on me has finally worn off.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0xFE,
        (
            "I finally feel like my old self\x01",
            "again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0xFE,
        (
            "Well, I guess it's about time\x01",
            "I got back to work.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17C5")

    Jump("loc_200D")

    label("loc_17C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 4)), scpexpr(EXPR_END)), "loc_1C93")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8B, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A98")
    OP_A2(0x458)
    OP_A2(0x0)

    ChrTalk(    #70
        0xFE,
        (
            "Oh, is it you kids again? It was\x01",
            "pretty rough the other night,\x01",
            "wasn't it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x101,
        (
            "#004FIt WAS pretty crazy. Speaking of\x01",
            "which, how are you holding up?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0xFE,
        "Not too bad, I guess.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0xFE,
        (
            "I still feel a little light in\x01",
            "the head, though...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x102,
        (
            "#013FIt looks like the anesthetic hasn't\x01",
            "completely worn off.\x02\x03",

            "Thankfully, it's a pretty harmless\x01",
            "drug, so you should be back to\x01",
            "normal in a little while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x101,
        "#501FThat's a relief to hear.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0xFE,
        (
            "Hmm...then maybe I should take a\x01",
            "little break before getting back\x01",
            "to work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0x101,
        (
            "#000FI think that's a good idea. Taking\x01",
            "it easy is probably the best thing\x01",
            "for you right now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0x102,
        "#010FPlease don't overdo it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0xFE,
        (
            "I think I'll just take your\x01",
            "advice, young man.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C90")

    label("loc_1A98")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1BC4")
    OP_A2(0x0)

    ChrTalk(    #80
        0xFE,
        (
            "Seems like the other night was\x01",
            "pretty rough for you kids.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0xFE,
        (
            "I confess my mind's still a bit\x01",
            "foggy about it all...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0xFE,
        (
            "For one thing, it seems like the\x01",
            "whole darn day passed in the\x01",
            "blink of an eye, quick as that!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0xFE,
        (
            "Hmm...it seems like I'm still\x01",
            "a bit fuzzy around the edges.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C90")

    label("loc_1BC4")


    ChrTalk(    #84
        0xFE,
        (
            "I can't really remember a thing\x01",
            "about last night.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0xFE,
        (
            "For one thing, it seems like the\x01",
            "whole darn day passed in the\x01",
            "blink of an eye.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0xFE,
        (
            "Hmm...it seems like I'm still\x01",
            "a bit fuzzy around the edges.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C90")

    Jump("loc_200D")

    label("loc_1C93")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_1ED0")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x1D, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1DAA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D2D")
    OP_A2(0x0)

    ChrTalk(    #87
        0xFE,
        (
            "Oh, is it you kids again?\x01",
            "Thanks for all your hard work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0xFE,
        (
            "Make sure to always show\x01",
            "your consideration for others.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DA7")

    label("loc_1D2D")


    ChrTalk(    #89
        0xFE,
        (
            "Well, I suppose once I've caught my\x01",
            "breath, I'll start the inspection.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0xFE,
        (
            "I swear, this work is hell\x01",
            "on my back...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1DA7")

    Jump("loc_1ECD")

    label("loc_1DAA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E5B")
    OP_A2(0x0)

    ChrTalk(    #91
        0xFE,
        (
            "Oho, it's you guys. Nice job\x01",
            "exterminating those monsters!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0xFE,
        (
            "You whippersnappers keep up that\x01",
            "pace, now, ya hear? But don't let\x01",
            "your guard down out there!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1ECD")

    label("loc_1E5B")


    ChrTalk(    #93
        0xFE,
        (
            "Well, guess it's time to start\x01",
            "making the rounds.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0xFE,
        (
            "Gotta get everything ready to go\x01",
            "before the delivery!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1ECD")

    Jump("loc_200D")

    label("loc_1ED0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x1C, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_200D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F8B")
    OP_A2(0x0)

    ChrTalk(    #95
        0xFE,
        (
            "Oho, it's you guys. Nice job\x01",
            "exterminating those monsters!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0xFE,
        (
            "You whippersnappers keep up that\x01",
            "pace, now, ya hear? But don't let\x01",
            "your guard down out there!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_200D")

    label("loc_1F8B")


    ChrTalk(    #97
        0xFE,
        (
            "Well, guess it's time to start\x01",
            "making the rounds.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0xFE,
        (
            "Before I get to shippin', though,\x01",
            "I should get myself ready for work!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_200D")

    TalkEnd(0x8)

    label("loc_2010")

    Return()

    # Function_0_66 end

    def Function_1_2011(): pass

    label("Function_1_2011")

    EventBegin(0x0)
    ClearMapFlags(0x1)
    ClearChrFlags(0x8, 0x80)
    TalkBegin(0x8)
    SetChrPos(0x8, 300, 0, 202000, 180)
    SetChrPos(0x101, 1750, 0, 203500, 180)
    SetChrPos(0x102, 2650, 0, 203000, 180)
    SetChrPos(0x105, 2550, 0, 205000, 180)
    OP_69(0x101, 0x0)
    FadeToBright(2000, 0)

    def lambda_207A():
        OP_8E(0x8, 0xFFFFF7A4, 0x0, 0x3131C, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_207A)

    def lambda_2095():
        OP_6D(-970, 0, 201500, 2000)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_2095)
    OP_43(0x101, 0x1, 0x1, 0x2)
    Sleep(200)
    OP_43(0x102, 0x1, 0x1, 0x3)
    Sleep(200)
    OP_43(0x105, 0x1, 0x1, 0x4)
    WaitChrThread(0x8, 0x1)
    OP_8C(0x8, 270, 400)
    Sleep(400)
    OP_8C(0x8, 270, 400)

    ChrTalk(    #99
        0x8,
        (
            "Man, feels like I haven't been\x01",
            "here in ages!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #100
        0x102,
        (
            "#010FI think we should get our work\x01",
            "finished ahead of time, Estelle.\x01",
            "Early bird catches the worm, right?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #101
        0x101,
        "#000FSomething like that, yeah!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x8, 400)
    TurnDirection(0x102, 0x8, 400)
    OP_92(0x101, 0x8, 0x3E8, 0x7D0, 0x0)

    ChrTalk(    #102
        0x101,
        (
            "#001FSalutations! I come on behalf\x01",
            "of the Bracer Guild, bearing a\x01",
            "package for you.\x02\x03",

            "It's a little heavy, though,\x01",
            "so be careful lifting it!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 400)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #103
        "\x07\x00Handed over \x07\x02Maintenance Kit\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3F(0x326, 1)

    ChrTalk(    #104
        0x8,
        "Yep, everything's here, all right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0x8,
        (
            "I appreciate ya bringin' this all\x01",
            "the way over here.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x1D, 0x1, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_40(0x19A)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_29C0")

    ChrTalk(    #106
        0x101,
        (
            "#000FOh, no worries.\x01",
            "It's our job, after all!\x02\x03",

            "The townsfolk were actually really\x01",
            "worried about you, too, so I'm just\x01",
            "glad to see you're doing well!\x02\x03",

            "Work must be tough, so take care\x01",
            "of yourself, okay? Don't overexert\x01",
            "those old bones of yours!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0x8,
        (
            "I'll do that. Thank ya for your\x01",
            "concern...blunt as it be.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0x8,
        (
            "...You startin' to understand what\x01",
            "it means to possess a caring soul?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0x101,
        (
            "#506FUh...nope! Not really!\x02\x03",

            "I'm no good with those touchy-\x01",
            "feely concepts, I guess.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0x8,
        (
            "And here I thought you'd grown\x01",
            "up a bit...ah well!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0x8,
        (
            "I guess you've still got a ways\x01",
            "to go before you can match the\x01",
            "level of THAT bracer...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0x101,
        (
            "#000FActually, I'd like to hear more\x01",
            "about him. What kind of bracer\x01",
            "was he?\x02\x03",

            "If the stories I've heard are true,\x01",
            "he was quite an amazing man!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0x8,
        (
            "He was a great help to me seven or\x01",
            "eight years ago. But sadly, I can't\x01",
            "even remember his name anymore...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0x8,
        (
            "He was a hell of a man, though.\x01",
            "No offense, but he made you guys\x01",
            "look like crap by comparison!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0x8,
        (
            "Though...there is a bit of a resemblance,\x01",
            "actually. He had reddish-brown hair just\x01",
            "like yours.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(400)

    ChrTalk(    #116
        0x8,
        (
            "In fact, even your eyes have\x01",
            "the same basic hue...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0x102,
        (
            "#014FReddish-brown hair, and the\x01",
            "same eye color as Estelle's...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0x101,
        "#004FCould that bracer have been...?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 400)

    ChrTalk(    #119
        0x105,
        "#044F...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0x8,
        (
            "I'm very much hoping you guys will\x01",
            "rise to his level, given the time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0x8,
        (
            "Though I suspect I may be wishing\x01",
            "for things that are never to be.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x8, 400)

    ChrTalk(    #122
        0x8,
        (
            "Aaaat any rate, thanks for all your\x01",
            "hard work, kids!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0x8,
        (
            "I'd best get to work.\x01",
            "Time to start my rounds!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0x101,
        (
            "#000FO-Oh, yeah. Well, you take care\x01",
            "now, okay? Don't break your hip!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0x102,
        "#010FExcuse us, please.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x3FC)
    NewScene("ED6_DT01/C2209   ._SN", 101, 0, 0)
    IdleLoop()
    TalkEnd(0x8)
    Jump("loc_395C")

    label("loc_29C0")


    ChrTalk(    #126
        0x101,
        (
            "#000FOh, no worries.\x01",
            "It's our job, after all!\x02\x03",

            "Uh, on another note, we actually\x01",
            "have something else for you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0x8,
        "Ohh?\x02",
    )

    CloseMessageWindow()
    OP_90(0x105, 0xFFFFFCE0, 0x0, 0x0, 0x7D0, 0x0)
    OP_92(0x105, 0x8, 0x3E8, 0x7D0, 0x0)

    ChrTalk(    #128
        0x105,
        (
            "#040FHere you are, sir.\x02\x03",

            "It was entrusted to our care by\x01",
            "Primo, from Lavantar.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x105, 400)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #129
        "\x07\x00Handed over \x07\x02Azelia Rose\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3F(0x19A, 1)
    OP_28(0x1D, 0x1, 0x20)
    OP_91(0x105, 0x190, 0x0, 0x190, 0x7D0, 0x0)

    ChrTalk(    #130
        0x8,
        (
            "Oh, my my my!\x01",
            "It's Azelia Rose!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0x8,
        (
            "I used to drink this all the time\x01",
            "while munching on things covered\x01",
            "in anchovies!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x391)"), scpexpr(EXPR_END)), "loc_2DF3")
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        0,
        (
            "[Hand over Salted Anchovy]\x01",      # 0
            "[Keep it]\x01",                       # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2C1F"),
        (1, "loc_2D95"),
        (SWITCH_DEFAULT, "loc_2DF0"),
    )


    label("loc_2C1F")


    ChrTalk(    #132
        0x101,
        (
            "#001FHa-HA! ♪\x01",
            "I've got one of those for you, too!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 400)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #133
        "\x07\x00Handed over \x07\x02Salted Anchovy\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3F(0x391, 1)
    OP_28(0x1D, 0x1, 0x40)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(400)

    ChrTalk(    #134
        0x8,
        "Ohh! OHHHH!!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0x8,
        (
            "You've even brought me some munchies\x01",
            "to go with it! What thoughtful bracers\x01",
            "ya are!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0x8,
        (
            "Man, this takes me back. How\x01",
            "are Primo and the others?\x01",
            "Are they doing well?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2DF0")

    label("loc_2D95")

    TurnDirection(0x8, 0x101, 400)

    ChrTalk(    #137
        0x8,
        (
            "Man, this takes me back. How\x01",
            "are Primo and the others?\x01",
            "Are they doing well?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2DF0")

    label("loc_2DF0")

    Jump("loc_2E4B")

    label("loc_2DF3")

    TurnDirection(0x8, 0x101, 400)

    ChrTalk(    #138
        0x8,
        (
            "Man, this takes me back. How\x01",
            "are Primo and the others?\x01",
            "Are they doing well?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E4B")


    ChrTalk(    #139
        0x101,
        (
            "#000FYou bet! They're all worried about\x01",
            "you, too, Gramps.\x02\x03",

            "Work must be tough, so take care\x01",
            "of yourself, okay? Don't overexert\x01",
            "those old bones of yours!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0x8,
        (
            "I...uh...won't? Well, blunt or no,\x01",
            "thank you for the concern. I value\x01",
            "that even more than anchovies!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0x8,
        (
            "...You startin' to understand what\x01",
            "it means to possess a caring soul?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0x101,
        (
            "#506FUh...nope! Not really!\x02\x03",

            "I'm no good with those touchy-\x01",
            "feely concepts, I guess.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0x8,
        (
            "And here I thought you'd grown\x01",
            "up a bit...ah well!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0x8,
        (
            "I guess you've still got a ways\x01",
            "to go before you can match the\x01",
            "level of THAT bracer...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0x101,
        (
            "#000FActually, I'd like to hear more\x01",
            "about him. What kind of bracer\x01",
            "was he?\x02\x03",

            "If the stories I've heard are true,\x01",
            "he was quite an amazing man!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #146
        0x8,
        (
            "He was a great help to me seven or\x01",
            "eight years ago. But sadly, I can't\x01",
            "even remember his name anymore...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0x8,
        (
            "He was a hell of a man, though.\x01",
            "No offense, but he made you guys\x01",
            "look like crap by comparison!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0x8,
        (
            "Though...there is a bit of a resemblance,\x01",
            "actually. He had reddish-brown hair just\x01",
            "like yours.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(400)

    ChrTalk(    #149
        0x8,
        (
            "In fact, even your eyes have\x01",
            "the same basic hue...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #150
        0x102,
        (
            "#014FReddish-brown hair, and the\x01",
            "same eye color as Estelle's...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #151
        0x101,
        "#004FCould that bracer have been...?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 400)

    ChrTalk(    #152
        0x105,
        "#044F...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0x8,
        (
            "I'm very much hoping you guys will\x01",
            "rise to his level, given the time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #154
        0x8,
        (
            "Though I suspect I may be wishing\x01",
            "for things that are never to be.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x8, 400)

    ChrTalk(    #155
        0x8,
        (
            "Aaaat any rate, thanks for all your\x01",
            "hard work, kids!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #156
        0x8,
        (
            "Ya even brought me some personal\x01",
            "items, outside the normal scope\x01",
            "of a bracer's duties!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #157
        0x8,
        (
            "...In fact, ya know what?\x01",
            "Wait right there for a moment,\x01",
            "if ya would!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_34AB():

        label("loc_34AB")

        TurnDirection(0x102, 0x8, 400)
        OP_48()
        Jump("loc_34AB")

    QueueWorkItem2(0x102, 1, lambda_34AB)

    def lambda_34BC():

        label("loc_34BC")

        TurnDirection(0x101, 0x8, 400)
        OP_48()
        Jump("loc_34BC")

    QueueWorkItem2(0x101, 1, lambda_34BC)

    def lambda_34CD():

        label("loc_34CD")

        TurnDirection(0x105, 0x8, 400)
        OP_48()
        Jump("loc_34CD")

    QueueWorkItem2(0x105, 1, lambda_34CD)
    OP_8E(0x8, 0xFFFFF7E0, 0x0, 0x31A38, 0x7D0, 0x0)
    OP_8E(0x8, 0xFFFFF20E, 0x0, 0x31DBC, 0x7D0, 0x0)
    OP_8E(0x8, 0xFFFFE8D6, 0x0, 0x31C9A, 0x7D0, 0x0)
    OP_8C(0x8, 315, 0)
    Sleep(1000)
    OP_8E(0x8, 0xFFFFE8D6, 0x0, 0x31C9A, 0x7D0, 0x0)
    OP_8E(0x8, 0xFFFFF20E, 0x0, 0x31DBC, 0x7D0, 0x0)
    OP_8E(0x8, 0xFFFFF7E0, 0x0, 0x31A38, 0x7D0, 0x0)
    OP_8E(0x8, 0xFFFFF7A4, 0x0, 0x3131C, 0x7D0, 0x0)
    TurnDirection(0x8, 0x101, 400)
    OP_44(0x102, 0xFF)
    OP_44(0x101, 0xFF)
    OP_44(0x105, 0xFF)

    ChrTalk(    #158
        0x8,
        (
            "I have something for ya. Something\x01",
            "I once used a long, long time ago...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #159
        0x8,
        (
            "Consider it a thank-you gift, for being\x01",
            "so kind to an old man like me. Save for\x01",
            "that old bones comment, anyway!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #160
        0x8,
        (
            "They're a little old, but like me,\x01",
            "they'll still do the job, sure as\x01",
            "the day you were born!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x1D, 0x1, 0x40)"), scpexpr(EXPR_END)), "loc_3736")
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #161
        "\x07\x00Received \x07\x02Work Helmet\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #162
        "\x07\x00Received \x07\x02Gladiator Headband\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x148, 1)
    OP_3E(0x146, 1)
    Jump("loc_3786")

    label("loc_3736")

    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #163
        "\x07\x00Received \x07\x02Work Helmet\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x148, 1)

    label("loc_3786")


    ChrTalk(    #164
        0x101,
        "#001FWhoa, awesome! Thanks!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #165
        0x102,
        "#014FYou sure we can have these?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x102, 400)

    ChrTalk(    #166
        0x8,
        (
            "Absolutely! Not like I'll be setting\x01",
            "sail for wild, exotic lands again\x01",
            "any time soon!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #167
        0x8,
        (
            "At any rate, I'd best get back\x01",
            "to work.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(    #168
        0x8,
        (
            "I've basically been playing hooky this\x01",
            "whole time we've been talking! I stay here\x01",
            "any longer, and somebody's bound to notice!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #169
        0x105,
        "#040FPlease take care of yourself.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #170
        0x101,
        "#000FTake care, you old coot!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #171
        0x102,
        "#010FPlease excuse us.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x3FC)
    NewScene("ED6_DT01/C2209   ._SN", 101, 0, 0)
    IdleLoop()
    TalkEnd(0x8)

    label("loc_395C")

    EventEnd(0x0)
    SetMapFlags(0x1)
    Return()

    # Function_1_2011 end

    def Function_2_3964(): pass

    label("Function_2_3964")


    def lambda_396A():
        OP_8E(0x101, 0xFFFFFC36, 0x0, 0x3131C, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_396A)
    WaitChrThread(0x101, 0x2)
    OP_8C(0x101, 270, 400)
    Return()

    # Function_2_3964 end

    def Function_3_398C(): pass

    label("Function_3_398C")


    def lambda_3992():
        OP_8E(0x102, 0xFFFFFF88, 0x0, 0x31128, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_3992)
    WaitChrThread(0x102, 0x2)
    OP_8C(0x102, 270, 400)
    Return()

    # Function_3_398C end

    def Function_4_39B4(): pass

    label("Function_4_39B4")


    def lambda_39BA():
        OP_8E(0x105, 0x14A, 0x0, 0x31830, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_39BA)
    WaitChrThread(0x105, 0x2)
    OP_8C(0x105, 270, 400)
    Return()

    # Function_4_39B4 end

    def Function_5_39DC(): pass

    label("Function_5_39DC")

    EventBegin(0x1)
    OP_0D()
    Sleep(400)
    OP_22(0x17, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #172
        "\x07\x05Defeated all the monsters!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    EventEnd(0x1)
    Return()

    # Function_5_39DC end

    SaveToFile()

Try(main)
