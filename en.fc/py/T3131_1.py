from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 蔡斯

    CreateScenaFile(
        FileName            = 'T3131_1 ._SN',
        MapName             = 'Zeiss',
        Location            = 'T3131.x',
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
        "Function_1_AB",           # 01, 1
        "Function_2_AC",           # 02, 2
    )


    def Function_0_AA(): pass

    label("Function_0_AA")

    Return()

    # Function_0_AA end

    def Function_1_AB(): pass

    label("Function_1_AB")

    Return()

    # Function_1_AB end

    def Function_2_AC(): pass

    label("Function_2_AC")

    EventBegin(0x0)
    OP_67(0, 5630, -10000, 1000)
    OP_4A(0x9, 255)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9E3")

    ChrTalk(    #0
        0x9,
        "Ah, hello there.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_170")

    ChrTalk(    #1
        0x102,
        (
            "#010FSorry to bother you when\x01",
            "you're working.\x02\x03",

            "We saw your request on the bulletin\x01",
            "board and brought some ingredients.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D8")

    label("loc_170")


    ChrTalk(    #2
        0x101,
        (
            "#000FDo you have a minute?\x02\x03",

            "We saw the posting on the bulletin\x01",
            "board and brought some ingredients.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D8")


    ChrTalk(    #3
        0x101,
        (
            "#000FWe're kind of in a hurry, so\x01",
            "can you go ahead and take a\x01",
            "look?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x101, 400)

    ChrTalk(    #4
        0x9,
        (
            "Is that so?\x01",
            "Please, let me see.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)

    ChrTalk(    #5
        0x9,
        "Hmm...\x02",
    )

    CloseMessageWindow()
    OP_63(0x9)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x385)"), scpexpr(EXPR_END)), "loc_8F4")
    OP_62(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(800)

    ChrTalk(    #6
        0x9,
        "...Hmm?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x9,
        (
            "May I see that tomato for\x01",
            "a moment?\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #8
        "\x07\x00Handed over \x07\x02Acerbic Tomato\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(100)

    ChrTalk(    #9
        0x9,
        "Let's have a taste...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x9,
        "...\x02",
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(800)

    ChrTalk(    #11
        0x9,
        (
            "...AAACCCKKK!!!\x01",
            "*pthbbttbtbttt*\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(400)

    ChrTalk(    #12
        0x9,
        (
            "What IS this? It's terrible! My\x01",
            "taste buds have been VIOLATED!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x101,
        "#506FSee? It's just gross.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x9,
        (
            "Hmm... Well, it sure\x01",
            "can't be eaten as is...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x9,
        (
            "But it certainly has an interesting flavor and\x01",
            "scent. With the right preparation, it COULD\x01",
            "be a useful ingredient for cooking...maybe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x101,
        (
            "#501FDoesn't it worry you to eat\x01",
            "something that nasty?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x9,
        (
            "No... I've found that strongly bitter foods\x01",
            "tend to be very good for one's health...\x01",
            "when they don't kill you, anyway.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x9,
        (
            "And traditional Zeissian cooking\x01",
            "calls for some VERY strong\x01",
            "ingredients.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x101,
        (
            "#509FI'm not sure I'd want to\x01",
            "try that...\x02\x03",

            "S-So does that mean we\x01",
            "got what you needed?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x9,
        (
            "Yes, but wait there for\x01",
            "a moment.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 2000, 0x22, 0x24, 0xFA, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(800)

    ChrTalk(    #21
        0x9,
        (
            "There. That should be just the\x01",
            "right level of bitter to nicely\x01",
            "complement the dish.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x9,
        (
            "Here. You can be the\x01",
            "first to try it out.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #23
        "\x07\x00Received \x07\x02Tomato Sandwich\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(100)

    ChrTalk(    #24
        0x101,
        (
            "#506FUm, ha ha ha... I think I'll,\x01",
            "uh, save this for later...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x9,
        (
            "All right. Be sure to eat it\x01",
            "while it's still fresh or it won't\x01",
            "flay your tongue properly!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x9,
        (
            "As for me, I need to get back\x01",
            "to work. Thank you for your\x01",
            "time and effort.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x101,
        "#000FOkay. See you later.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x102,
        "#010FExcuse us.\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    OP_3F(0x385, 1)
    OP_3E(0x199, 1)
    OP_22(0x17, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #29
        "\x07\x00Quest \x07\x02[Potent Ingredient] \x07\x00completed!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_28(0x2B, 0x4, 0x10)
    OP_28(0x2B, 0x1, 0x4)
    OP_28(0x2B, 0x1, 0x8)
    OP_A2(0xA)
    Jump("loc_9E0")

    label("loc_8F4")


    ChrTalk(    #30
        0x9,
        "Hmm... Not very good.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x9,
        (
            "I need something with a little more...pizzazz.\x01",
            "Something...that makes your toes curl in an\x01",
            "involuntary reaction to the pain in your mouth.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x101,
        (
            "#505FThat's too bad.\x02\x03",

            "#000FWe'll be back, then.\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x2B, 0x1, 0x1)
    OP_28(0x2B, 0x1, 0x2)

    label("loc_9E0")

    Jump("loc_134A")

    label("loc_9E3")


    ChrTalk(    #33
        0x9,
        "Ah, hello there.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A84")

    ChrTalk(    #34
        0x102,
        (
            "#010FSorry to bother you when\x01",
            "you're working.\x02\x03",

            "We saw your request on the bulletin\x01",
            "board and brought some ingredients.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B44")

    label("loc_A84")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AD5")

    ChrTalk(    #35
        0x107,
        (
            "#060FHi, Mr. Ben!\x02\x03",

            "We brought you some ingredients\x01",
            "to try...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B44")

    label("loc_AD5")


    ChrTalk(    #36
        0x101,
        (
            "#000FDo you have a minute?\x02\x03",

            "We saw the posting on the bulletin\x01",
            "board and brought some ingredients.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x101, 400)

    label("loc_B44")


    ChrTalk(    #37
        0x9,
        "Please, let me see.\x02",
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)

    ChrTalk(    #38
        0x9,
        "Hmm...\x02",
    )

    CloseMessageWindow()
    OP_63(0x9)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x385)"), scpexpr(EXPR_END)), "loc_125E")
    OP_62(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(800)

    ChrTalk(    #39
        0x9,
        "...Hmm?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x9,
        (
            "May I see that tomato for\x01",
            "a moment?\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #41
        "\x07\x00Handed over \x07\x02Acerbic Tomato\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(100)

    ChrTalk(    #42
        0x9,
        (
            "Smells nothing like a regular\x01",
            "tomato...much stronger than\x01",
            "I'm used to.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x9,
        "Let me try it...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x9,
        "...\x02",
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(800)

    ChrTalk(    #45
        0x9,
        (
            "...AAACCCKKK!!!\x01",
            "*pthbbttbtbttt*\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(400)

    ChrTalk(    #46
        0x9,
        (
            "What IS this? It's terrible! My\x01",
            "taste buds have been VIOLATED!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x101,
        (
            "#506FSee? It's just gross.\x02\x03",

            "Maybe it'll be good for research, \x01",
            "but I can't see anyone wanting\x01",
            "to eat it.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x101, 400)

    ChrTalk(    #48
        0x9,
        (
            "Hmm... Well, it sure\x01",
            "can't be eaten as is...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x9,
        (
            "But it certainly has an interesting flavor and\x01",
            "scent. With the right preparation, it COULD\x01",
            "be a useful ingredient for cooking...maybe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x101,
        (
            "#501FDoesn't it worry you to eat\x01",
            "something that nasty?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x9,
        (
            "No... I've found that strongly bitter foods\x01",
            "tend to be very good for one's health...\x01",
            "when they don't kill you, anyway.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x9,
        (
            "And traditional Zeissian cooking\x01",
            "calls for some VERY strong\x01",
            "ingredients.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x101,
        (
            "#509FI'm not sure I'd want to\x01",
            "try that...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_FCA")

    ChrTalk(    #54
        0x107,
        "#067FAh...ha ha...\x02",
    )

    CloseMessageWindow()

    label("loc_FCA")

    OP_62(0x9, 0x0, 2000, 0x22, 0x24, 0xFA, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(800)

    ChrTalk(    #55
        0x9,
        (
            "There. That should be just the\x01",
            "right level of bitter to nicely\x01",
            "complement the dish.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x9,
        (
            "Here. You can be the first\x01",
            "to try out my newest dish.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x9,
        (
            "Consider it my thanks for \x01",
            "introducing me to such an\x01",
            "amazing food.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #58
        "\x07\x00Received \x07\x02Tomato Sandwich\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(100)

    ChrTalk(    #59
        0x101,
        (
            "#506FUm, ha ha ha... I think I'll,\x01",
            "uh, save this for later...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x9,
        (
            "Now, I need to get back\x01",
            "to work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x9,
        "Thanks for everything today.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x101,
        "#000FOkay. See you later.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x102,
        "#010FExcuse us.\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    OP_3F(0x385, 1)
    OP_3E(0x199, 1)
    OP_22(0x17, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #64
        "\x07\x00Quest \x07\x02[Potent Ingredient] \x07\x00completed!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_28(0x2B, 0x4, 0x10)
    OP_28(0x2B, 0x1, 0x4)
    OP_28(0x2B, 0x1, 0x8)
    OP_A2(0xA)
    Jump("loc_134A")

    label("loc_125E")


    ChrTalk(    #65
        0x9,
        "Hmm... Not very good.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x9,
        (
            "I need something with a little more...pizzazz.\x01",
            "Something...that makes your toes curl in an\x01",
            "involuntary reaction to the pain in your mouth.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x101,
        (
            "#505FThat's too bad.\x02\x03",

            "#000FWe'll be back, then.\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x2B, 0x1, 0x1)
    OP_28(0x2B, 0x1, 0x2)

    label("loc_134A")

    EventEnd(0x1)
    OP_4B(0x9, 255)
    Return()

    # Function_2_AC end

    SaveToFile()

Try(main)
