from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 洛连特

    CreateScenaFile(
        FileName            = 'T1122_1 ._SN',
        MapName             = 'Rolent',
        Location            = 'T1122.x',
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
        "Function_1_7B0",          # 01, 1
        "Function_2_FE9",          # 02, 2
    )


    def Function_0_66(): pass

    label("Function_0_66")

    ClearMapFlags(0x1)
    EventBegin(0x0)
    OP_4A(0xC, 255)
    OP_A2(0x5)
    OP_A2(0x4)
    OP_28(0x11, 0x4, 0x4)
    OP_28(0x11, 0x4, 0x2)
    OP_28(0x11, 0x4, 0x8)
    OP_28(0x11, 0x1, 0x1)
    OP_28(0x11, 0x1, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_103")
    Fade(1000)
    SetChrPos(0x101, 6800, 0, 6600, 90)
    SetChrPos(0x102, 6600, 0, 5600, 90)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E0")
    SetChrPos(0x103, 5400, 0, 6400, 90)

    label("loc_E0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_100")
    SetChrPos(0x104, 5200, 0, 5400, 90)

    label("loc_100")

    Jump("loc_16A")

    label("loc_103")

    Fade(1000)
    SetChrPos(0x101, 10200, 0, 5800, 315)
    SetChrPos(0x102, 9500, 0, 4800, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14A")
    SetChrPos(0x103, 10400, 0, 4200, 0)

    label("loc_14A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16A")
    SetChrPos(0x104, 9500, 0, 3600, 0)

    label("loc_16A")

    OP_69(0x101, 0x0)
    TurnDirection(0xC, 0x101, 0)
    OP_0D()

    ChrTalk(    #0
        0xC,
        "Can I help you find something?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xC,
        "My medicine works wonders.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x101,
        (
            "#000FUm, we came here after seeing\x01",
            "something posted on the bulletin\x01",
            "board at the Bracer Guild.\x02\x03",

            "Could you by any chance be\x01",
            "Spence?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xC,
        "Oh, you're bracers, are you?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xC,
        (
            "I've been waiting for you\x01",
            "to come.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x102,
        (
            "#010FGuess we can dispense with the formalities, then.\x01",
            "I understand you're trying to find places where\x01",
            "the Bear Claw grows, correct?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_328")
    TurnDirection(0xC, 0x102, 400)

    label("loc_328")


    ChrTalk(    #6
        0xC,
        (
            "Yes. The Bear Claw is a medicinal\x01",
            "herb that's difficult to find in\x01",
            "these parts.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xC,
        (
            "Up until now I had been having\x01",
            "them shipped from Rolent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xC,
        (
            "But just recently I was asked by\x01",
            "Father Holstein to prepare a new\x01",
            "medicine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xC,
        (
            "So it seems like I'm going to be\x01",
            "using more of these than before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xC,
        (
            "That's why I decided to find my\x01",
            "own sources.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x50, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x50, 5)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x50, 6)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x50, 7)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_504")

    ChrTalk(    #11
        0x101,
        (
            "#505FHmm... The Bear Claw, huh?\x02\x03",

            "If I remember right, it grows in\x01",
            "the forest of Mistwald in Rolent.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_563")

    label("loc_504")


    ChrTalk(    #12
        0x101,
        (
            "#505FHmm... The Bear Claw, huh?\x02\x03",

            "I haven't seen any growing around\x01",
            "here, that's for sure.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_563")

    TurnDirection(0xC, 0x101, 400)

    ChrTalk(    #13
        0xC,
        (
            "The Bear Claw is said to grow\x01",
            "well in humid locations.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xC,
        (
            "I'm pretty sure it probably grows\x01",
            "in a place like that in Bose.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x101,
        (
            "#007FMan, I guess all we can do is hit\x01",
            "the road and start conducting a\x01",
            "thorough search.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_708")

    ChrTalk(    #16
        0x103,
        (
            "#020FSuch investigations are an important\x01",
            "part of a bracer's work.\x02\x03",

            "Just think of it as a good\x01",
            "opportunity to learn.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 400)

    ChrTalk(    #17
        0x101,
        (
            "#505FI guess there's no other option,\x01",
            "huh?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_708")


    ChrTalk(    #18
        0x102,
        (
            "#010FAll right, if we come across any\x01",
            "Bear Claw flowers, we'll come\x01",
            "and let you know.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xC, 400)

    ChrTalk(    #19
        0xC,
        (
            "Okay, I'm counting on you kids.\x01",
            "And be careful out there.\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x0)
    OP_4B(0xC, 255)
    Return()

    # Function_0_66 end

    def Function_1_7B0(): pass

    label("Function_1_7B0")

    ClearMapFlags(0x1)
    EventBegin(0x0)
    OP_4A(0xC, 255)
    OP_A2(0x5)
    OP_28(0x11, 0x4, 0x10)
    OP_28(0x11, 0x4, 0x4)
    OP_28(0x11, 0x4, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_83E")
    Fade(1000)
    SetChrPos(0x101, 6800, 0, 6600, 90)
    SetChrPos(0x102, 6600, 0, 5600, 90)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_81B")
    SetChrPos(0x103, 5400, 0, 6400, 90)

    label("loc_81B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_83B")
    SetChrPos(0x104, 5200, 0, 5400, 90)

    label("loc_83B")

    Jump("loc_8A5")

    label("loc_83E")

    Fade(1000)
    SetChrPos(0x101, 10200, 0, 5800, 315)
    SetChrPos(0x102, 9500, 0, 4800, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_885")
    SetChrPos(0x103, 10400, 0, 4200, 0)

    label("loc_885")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8A5")
    SetChrPos(0x104, 9500, 0, 3600, 0)

    label("loc_8A5")

    OP_69(0x101, 0x0)
    TurnDirection(0xC, 0x101, 0)
    OP_0D()

    ChrTalk(    #20
        0xC,
        "Can I help you find something?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0xC,
        "My medicine works wonders.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x101,
        (
            "#000FUm, we came here after seeing\x01",
            "something posted on the bulletin\x01",
            "board at the Bracer Guild.\x02\x03",

            "Could you by any chance be\x01",
            "Spence?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xC,
        "Oh, you're bracers, are you?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0xC,
        (
            "I've been waiting for you\x01",
            "to come.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x102,
        (
            "#010FGuess we can dispense with the formalities, then.\x01",
            "I understand you're trying to find places where\x01",
            "the Bear Claw grows, correct?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A63")
    TurnDirection(0xC, 0x102, 400)

    label("loc_A63")


    ChrTalk(    #26
        0xC,
        (
            "Yes. The Bear Claw is a medicinal\x01",
            "herb that's difficult to find in\x01",
            "these parts.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xC,
        (
            "Up until now I had been having\x01",
            "them shipped from Rolent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0xC,
        (
            "But just recently I was asked by\x01",
            "Father Holstein to prepare a new\x01",
            "medicine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xC,
        (
            "So it seems like I'm going to be\x01",
            "using more of these than before.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x11, 0x1, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CE5")
    OP_28(0x11, 0x1, 0x20)
    OP_28(0x11, 0x1, 0x40)
    OP_62(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(400)

    ChrTalk(    #30
        0x101,
        "#505FNow that you mention it...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #31
        0x101,
        (
            "#000FHey, Joshua. Didn't we see a\x01",
            "Bear Claw just recently?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #32
        0x102,
        (
            "#010FYep, we found some in the\x01",
            "Nebel Valley.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xC,
        "Really?\x02",
    )

    CloseMessageWindow()

    def lambda_C75():
        TurnDirection(0x101, 0xC, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_C75)
    TurnDirection(0x102, 0xC, 400)

    ChrTalk(    #34
        0x102,
        (
            "#010FThere weren't many of them...\x02\x03",

            "But there should be enough to\x01",
            "use for your medicine.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DEC")

    label("loc_CE5")

    OP_28(0x11, 0x1, 0x10)

    ChrTalk(    #35
        0x101,
        (
            "#001FTee hee. Well, then you're in\x01",
            "luck.\x02\x03",

            "You can find the Bear Claw in\x01",
            "the Bose region, too.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x101, 400)

    ChrTalk(    #36
        0xC,
        "Really?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x102,
        (
            "#010FWe found some growing in the\x01",
            "Nebel Valley.\x02\x03",

            "There weren't many of them...\x02\x03",

            "But there should be enough to\x01",
            "use for your medicine.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DEC")

    TurnDirection(0xC, 0x102, 400)

    ChrTalk(    #38
        0xC,
        "This is wonderful news!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xC,
        (
            "It has been said that the Bear\x01",
            "Claw grows well in humid places.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0xC,
        (
            "Now that I think about it, the Nebel\x01",
            "Valley is the perfect place for them\x01",
            "to grow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0xC,
        (
            "I appreciate you helping me out\x01",
            "like this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0xC,
        (
            "Now I can put my full effort into\x01",
            "preparing this new medicine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x101,
        (
            "#006FGreat!♪\x02\x03",

            "Good luck with your work and have\x01",
            "a wonderful day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x102,
        "#010FWe'll be going then.\x02",
    )

    CloseMessageWindow()
    OP_22(0x17, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #45
        "\x07\x00Quest \x07\x02[Bear Claw Survey] \x07\x00completed!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    EventEnd(0x0)
    OP_4B(0xC, 255)
    Return()

    # Function_1_7B0 end

    def Function_2_FE9(): pass

    label("Function_2_FE9")

    ClearMapFlags(0x1)
    EventBegin(0x0)
    OP_4A(0xC, 255)
    OP_A2(0x5)
    OP_28(0x11, 0x4, 0x10)
    OP_28(0x11, 0x1, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_1073")
    Fade(1000)
    SetChrPos(0x101, 6800, 0, 6600, 90)
    SetChrPos(0x102, 6600, 0, 5600, 90)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1050")
    SetChrPos(0x103, 5400, 0, 6400, 90)

    label("loc_1050")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1070")
    SetChrPos(0x104, 5200, 0, 5400, 90)

    label("loc_1070")

    Jump("loc_10DA")

    label("loc_1073")

    Fade(1000)
    SetChrPos(0x101, 10200, 0, 5800, 315)
    SetChrPos(0x102, 9500, 0, 4800, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10BA")
    SetChrPos(0x103, 10400, 0, 4200, 0)

    label("loc_10BA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10DA")
    SetChrPos(0x104, 9500, 0, 3600, 0)

    label("loc_10DA")

    OP_69(0x101, 0x0)
    TurnDirection(0xC, 0x101, 0)
    OP_0D()

    ChrTalk(    #46
        0x101,
        "#508FGood afternoon, Mr. Spence!♪\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0xC,
        "Oh, it's you bracers again, is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0xC,
        (
            "Have you made any progress in\x01",
            "your search?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x101,
        (
            "#001FYou bet we did!\x02\x03",

            "It looks like there's a habitat for\x01",
            "Bear Claw flowers in the Bose\x01",
            "region as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x102,
        (
            "#010FWe found some growing in the\x01",
            "Nebel Valley.\x02\x03",

            "There weren't many of them...\x02\x03",

            "But there should be enough to\x01",
            "use for your medicine.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_126F")
    TurnDirection(0xC, 0x102, 400)

    label("loc_126F")


    ChrTalk(    #51
        0xC,
        "This is wonderful news!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0xC,
        (
            "I see... The Bear Claw has been said\x01",
            "to grow well in humid places.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0xC,
        (
            "Now that I think about it, the Nebel\x01",
            "Valley is the perfect place for them\x01",
            "to grow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0xC,
        (
            "I appreciate you helping me out\x01",
            "like this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0xC,
        (
            "Now I can put my full effort into\x01",
            "preparing this new medicine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x101,
        (
            "#006FGreat!♪\x02\x03",

            "Good luck with your work and have\x01",
            "a wonderful day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x102,
        "#010FWe'll be going then.\x02",
    )

    CloseMessageWindow()
    OP_22(0x17, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #58
        "\x07\x00Quest \x07\x02[Bear Claw Survey] \x07\x00completed!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    EventEnd(0x0)
    OP_4B(0xC, 255)
    Return()

    # Function_2_FE9 end

    SaveToFile()

Try(main)
