from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 洛连特

    CreateScenaFile(
        FileName            = 'T1131_1 ._SN',
        MapName             = 'Rolent',
        Location            = 'T1131.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60011",
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
    )


    def Function_0_66(): pass

    label("Function_0_66")


    ChrTalk(    #0
        0xFE,
        "Yes, can I help you?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DB")

    ChrTalk(    #1
        0x101,
        (
            "#508FHello.\x02\x03",

            "We're here with the Bracer Guild,\x01",
            "and we have a delivery.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_187")

    label("loc_DB")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12F")

    ChrTalk(    #2
        0x102,
        (
            "#010FYou're Gwen, I presume.\x02\x03",

            "Here are the items you requested.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_187")

    label("loc_12F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_187")

    ChrTalk(    #3
        0x103,
        (
            "#020FYou're Gwen, right?\x02\x03",

            "We've brought the ingredients you\x01",
            "requested.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_187")

    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #4
        "\x07\x00Handed over \x07\x02Tender Poultry\x07\x00 x5.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3F(0x3A7, 5)

    ChrTalk(    #5
        0xFE,
        (
            "Oh, thank you so much for going\x01",
            "to all the trouble.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xFE,
        (
            "I'm sure you must have been\x01",
            "busy with your other work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x101,
        (
            "#006FIt was no problem at all.\x02\x03",

            "Helping those in need is what our\x01",
            "job as bracers is all about.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x103,
        (
            "#020FYes, it's just like Estelle said.\x02\x03",

            "And now with the airliners at a\x01",
            "standstill, it's a difficult time\x01",
            "for all of us.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x103, 400)

    ChrTalk(    #9
        0xFE,
        (
            "I really appreciate you saying\x01",
            "that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xFE,
        (
            "But the little bit of mira I'm\x01",
            "paying just doesn't seem like\x01",
            "enough...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0x22, 0x24, 0xFA, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(800)

    ChrTalk(    #11
        0xFE,
        "Oh, I know!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xFE,
        (
            "Please let me do this for you,\x01",
            "too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x101,
        "#004FHuh? Do what?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #14
        0xFE,
        (
            "I'll teach you how to make my\x01",
            "specialty omelets.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x101,
        (
            "#004FYou mean the ones served here\x01",
            "at Anterose?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xFE,
        "Yes, that's exactly what I'm saying.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x101,
        (
            "#000FIs it okay for you to be giving out\x01",
            "your recipes like that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xFE,
        "Don't worry, it's not a problem.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0xFE,
        (
            "Even if you make a dish just like\x01",
            "the recipe says, it doesn't mean\x01",
            "that you'll get the same taste.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0xFE, 400)

    ChrTalk(    #20
        0x103,
        (
            "#020FSounds like you've got a lot of\x01",
            "confidence in your cooking.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x103, 400)

    ChrTalk(    #21
        0xFE,
        (
            "Remember: it's not about\x01",
            "whether you're good or bad.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xFE,
        (
            "It's like the relationship between a\x01",
            "musician and her sheet of music.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xFE,
        (
            "Depending on the person, the song will\x01",
            "sound different--even though the music\x01",
            "is exactly the same.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x101,
        "#505FThat's pretty profound.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #25
        0xFE,
        (
            "A recipe, in the end, is nothing\x01",
            "more than a framework to make\x01",
            "something delicious.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0xFE,
        (
            "By only following the rules you'd\x01",
            "be surprised at how many different\x01",
            "ways the end flavor turns out.\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x20D)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_819")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_AC(0xC)"), scpexpr(EXPR_END)), "loc_7EB")
    Jump("loc_819")

    label("loc_7EB")

    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #27
        "\x07\x00Learned '\x07\x02Liberl Omelet\x07\x00' recipe.\x02",
    )

    CloseMessageWindow()

    label("loc_819")

    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_62(0x101, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(800)

    ChrTalk(    #28
        0x101,
        (
            "#001FScore!\x02\x03",

            "We'll have to give this a try\x01",
            "later on.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #29
        0x102,
        (
            "#018F...\x02\x03",

            "Estelle... Now this is just a little pre-cooking\x01",
            "advice, so don't take it the wrong way, but\x01",
            "please read the recipe before you try it.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    TurnDirection(0x101, 0x102, 400)
    Sleep(400)

    ChrTalk(    #30
        0x101,
        (
            "#005FHow rude! \x02\x03",

            "What are you trying to say?\x01",
            "That I'm the worst cook ever?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x102,
        (
            "#017FThen make sure you measure how\x01",
            "much seasoning you put in.\x02\x03",

            "A 'pinch' of salt doesn't mean that\x01",
            "you should drop a fistful in there,\x01",
            "you know.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(400)

    ChrTalk(    #32
        0x101,
        "#009FI'll show you a fistful...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #33
        0xFE,
        (
            "Well, following the setup of any\x01",
            "recipe is important, but enjoying\x01",
            "what you cook comes first.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xFE,
        (
            "Surprisingly, that's probably the\x01",
            "best framework for any recipe.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xFE, 400)

    ChrTalk(    #35
        0x101,
        (
            "#001FSee? Now that's what I'm talking\x01",
            "about! I totally agree.♪\x02\x03",

            "And thanks for the new recipe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0xFE,
        "My pleasure.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xFE,
        (
            "Come and enjoy a bite to eat here\x01",
            "every once in a while, too.\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x17, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #38
        "\x07\x00Quest \x07\x02[Ingredient Seeker] \x07\x00completed!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_28(0x12, 0x4, 0x10)
    OP_A2(0xA)
    OP_28(0x12, 0x1, 0x1)
    TalkEnd(0x11)
    Return()

    # Function_0_66 end

    SaveToFile()

Try(main)
