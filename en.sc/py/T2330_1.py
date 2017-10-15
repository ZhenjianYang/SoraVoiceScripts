from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 洛连特

    CreateScenaFile(
        FileName            = 'T2330_1 ._SN',
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
        "Function_1_7A6",          # 01, 1
        "Function_2_85F",          # 02, 2
        "Function_3_15BD",         # 03, 3
        "Function_4_1953",         # 04, 4
        "Function_5_1A46",         # 05, 5
    )


    def Function_0_AA(): pass

    label("Function_0_AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_117")
    TalkBegin(0xB)

    ChrTalk(    #0
        0xB,
        "Great job, everyone!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xB,
        (
            "I'll let you know when I've got\x01",
            "another job lined up for you.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xB)
    Jump("loc_7A5")

    label("loc_117")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x65, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_68D")
    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_1FC")
    OP_A2(0x5)

    ChrTalk(    #2
        0xB,
        "My next deal is in Bose.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xB,
        (
            "I still have quite some time\x01",
            "before the next liner comes,\x01",
            "however.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xB,
        (
            "Might as well kill some time in\x01",
            "Ruan since I'm in the area.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xB,
        "Perhaps I should depart early.\x02",
    )

    CloseMessageWindow()
    Jump("loc_687")

    label("loc_1FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_3D8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_2E5")

    ChrTalk(    #6
        0xB,
        (
            "I'd like to one day try the local rarities\x01",
            "after they're prepared by a first-class\x01",
            "chef.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xB,
        (
            "A worthy goal, if I do say so myself!\x01",
            "Orvid Co., Ltd. must step ever forward\x01",
            "for the sake of life's little luxuries!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3D5")

    label("loc_2E5")

    OP_A2(0x5)

    ChrTalk(    #8
        0xB,
        (
            "Truly, the wild bounty of local regions\x01",
            "have enough value to be worth all the\x01",
            "trials and tribulations in the world.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xB,
        (
            "It would certainly be nice if said rare\x01",
            "bounties could be had any time at\x01",
            "high-class restaurants, though, hmm?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3D5")

    Jump("loc_687")

    label("loc_3D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 4)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_557")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_46A")

    ChrTalk(    #10
        0xB,
        (
            "When I went out to scavenge for\x01",
            "ingredients on my own, my niece,\x01",
            "Amelia, stopped me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xB,
        "That's why I asked the guild.\x02",
    )

    CloseMessageWindow()
    Jump("loc_554")

    label("loc_46A")

    OP_A2(0x5)

    ChrTalk(    #12
        0xB,
        (
            "I intended to go out scavenging\x01",
            "myself this time, but my niece,\x01",
            "Amelia, stopped me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xB,
        "That's why I hired the guild.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xB,
        (
            "I'm well aware of how much she\x01",
            "worries over me, and there's no harm\x01",
            "in listening to her now and then.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_554")

    Jump("loc_687")

    label("loc_557")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_602")

    ChrTalk(    #15
        0xB,
        (
            "Blessings of the sea, river, and the\x01",
            "mountain, even. So many rare treats\x01",
            "abound!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xB,
        (
            "Heh! I wouldn't plant my roots on\x01",
            "a lesser place than good, ol' Ruan.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_687")

    label("loc_602")

    OP_A2(0x5)

    ChrTalk(    #17
        0xB,
        "Ruan is a land rich in variety.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xB,
        (
            "I'd nearly forgotten, but one look at\x01",
            "my ingredients list and it's all come\x01",
            "back to me.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_687")

    TalkEnd(0xB)
    Jump("loc_7A5")

    label("loc_68D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x65, 0x0, 0x8)"), scpexpr(EXPR_END)), "loc_69E")
    Call(1, 4)
    Jump("loc_7A5")

    label("loc_69E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x65, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_6AF")
    Call(1, 2)
    Jump("loc_7A5")

    label("loc_6AF")

    SetChrFlags(0xB, 0x10)
    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_70A")

    ChrTalk(    #19
        0xB,
        (
            "Hmm... I need to complete this list\x01",
            "before my next business deal...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_79D")

    label("loc_70A")

    OP_A2(0x5)

    ChrTalk(    #20
        0xB,
        (
            "Hmm... No matter how I look at it,\x01",
            "there are still missing items...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0xB,
        (
            "I need to complete this list soon\x01",
            "before my next business deal...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_79D")

    TalkEnd(0xB)
    ClearChrFlags(0xB, 0x10)

    label("loc_7A5")

    Return()

    # Function_0_AA end

    def Function_1_7A6(): pass

    label("Function_1_7A6")

    SetChrPos(0x101, 650, 0, 880, 0)
    SetChrPos(0xF7, 1540, 0, 670, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7FB")
    SetChrPos(0x104, 650, 0, -380, 0)
    SetChrPos(0x105, 1490, 0, -570, 0)
    Jump("loc_84D")

    label("loc_7FB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x26)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_82E")
    SetChrPos(0x104, 650, 0, -380, 0)
    SetChrPos(0x127, 1490, 0, -570, 0)
    Jump("loc_84D")

    label("loc_82E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_84D")
    SetChrPos(0x109, 1095, 0, -475, 0)

    label("loc_84D")

    OP_6D(90, 0, 1990, 0)
    Return()

    # Function_1_7A6 end

    def Function_2_85F(): pass

    label("Function_2_85F")

    OP_4A(0xB, 0)
    EventBegin(0x0)
    Fade(1000)
    Call(1, 1)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x65, 0x1, 0x8000)"), scpexpr(EXPR_END)), "loc_8BD")
    TurnDirection(0xB, 0x101, 400)
    Sleep(500)

    ChrTalk(    #22
        0xB,
        (
            "#4POh, it's you guys.\x02\x03",

            "Well, do you have time?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C8E")

    label("loc_8BD")


    ChrTalk(    #23
        0x101,
        "#1011F#1PUm, got a minute?\x02",
    )

    CloseMessageWindow()
    OP_62(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xB, 0x101, 400)
    Sleep(500)

    ChrTalk(    #24
        0xB,
        "#4PHm...?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x5, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x1F, 0x0, 0x10)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_926")
    OP_A2(0x7)
    Jump("loc_929")

    label("loc_926")

    OP_A3(0x7)

    label("loc_929")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9D6")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        0,
        (
            "Set previous game's related quest(s) as cleared\x01",          # 0
            "Set previous game's related quest(s) as not cleared\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9D3")
    OP_A2(0x7)
    Jump("loc_9D6")

    label("loc_9D3")

    OP_A3(0x7)

    label("loc_9D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_BBD")

    ChrTalk(    #25
        0xB,
        "#4POh, what a surprise!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0xB,
        (
            "#4PDo you remember me? I asked\x01",
            "you to do a job for me a while ago.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xF7, 0x101, 400)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_A74")

    ChrTalk(    #27
        0x106,
        "#052F#2PWhat, you know him?\x02",
    )

    CloseMessageWindow()
    Jump("loc_A96")

    label("loc_A74")


    ChrTalk(    #28
        0x103,
        "#023F#2POh, an acquaintance?\x02",
    )

    CloseMessageWindow()

    label("loc_A96")

    TurnDirection(0x101, 0xF7, 400)

    ChrTalk(    #29
        0x101,
        "#1016F#1PYeah. He's a merchant...kinda.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xB, 400)

    ChrTalk(    #30
        0x101,
        "#1000F#1PIt really has been a while, huh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xB,
        (
            "#4PYes, last we met was before the\x01",
            "birthday celebrations, I believe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xB,
        (
            "#4PIf you don't mind, I'd like to get\x01",
            "things underway immediately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xB,
        "#4PDo you have the time right now?\x02",
    )

    CloseMessageWindow()
    Jump("loc_C8E")

    label("loc_BBD")


    ChrTalk(    #34
        0xB,
        "#4POh, are you kids bracers?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xB,
        "#4PHave you seen my request, then?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x101,
        "#1000F#1PSure have, sir.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xB,
        (
            "#4PGood, good! I'd like to get things\x01",
            "underway immediately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xB,
        "#4PDo you have the time right now?\x02",
    )

    CloseMessageWindow()

    label("loc_C8E")

    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
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
    OP_5F(0xFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D8C")
    OP_28(0x65, 0x1, 0x8000)

    ChrTalk(    #39
        0x101,
        (
            "#1007F#1PHmmm, sorry. Right now isn't\x01",
            "a great time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0xB,
        (
            "#4PThat's a shame.\x02\x03",

            "If you can, come by again\x01",
            "once you have some time.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15AD")

    label("loc_D8C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x5, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x1F, 0x0, 0x10)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_DC0")

    ChrTalk(    #41
        0x101,
        "#1006F#1PSure, no problem.\x02",
    )

    CloseMessageWindow()
    Jump("loc_DE0")

    label("loc_DC0")


    ChrTalk(    #42
        0x101,
        "#1006F#1PSure, no problem.\x02",
    )

    CloseMessageWindow()

    label("loc_DE0")

    TurnDirection(0xF7, 0xB, 400)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_E12")

    ChrTalk(    #43
        0x106,
        "#050F#5PSo, what's the job?\x02",
    )

    CloseMessageWindow()
    Jump("loc_E3B")

    label("loc_E12")


    ChrTalk(    #44
        0x103,
        "#020F#5PSo, what kind of job is it?\x02",
    )

    CloseMessageWindow()

    label("loc_E3B")


    ChrTalk(    #45
        0xB,
        "#4PAll right, listen carefully.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0xB,
        (
            "#4PI'm currently putting together a list\x01",
            "of ingredients obtainable across the\x01",
            "entire Ruan region.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0xB,
        (
            "#4PProblem is, there've been lots of dangerous\x01",
            "monsters out there lately, and I haven't been\x01",
            "able to go out investigating on my own.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0xB,
        (
            "#4PThat's where you bracers come in--\x01",
            "I'd like for you to assist me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x101,
        (
            "#1015F#1PSounds easy enough.\x02\x03",

            "#1000FWhat do you want us to do,\x01",
            "specifically?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0xB,
        (
            "#4PFirst, take a look at this tentative\x01",
            "ingredient list I've put together:\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #51
        (
            "\x07\x05Savory Pinion, Leathery Tail, Gummy Eyeball,\x01",
            "Monster Carapace, Beast Flesh, Prickly Seed,\x01",
            "Fish Fillet, Clear Gelatin\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(    #52
        0x101,
        (
            "#1015F#1PEr, all right. I've written it down,\x01",
            "but is this the list you were talking\x01",
            "about?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0xB,
        "#4PYes, though it's incomplete.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0xB,
        (
            "#4PI want you to find ingredients from\x01",
            "monsters that aren't on this list and\x01",
            "bring them to me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0xB,
        (
            "#4PDid you get that? Ingredients that are\x01",
            "NOT on the list. Make sure you don't\x01",
            "get that wrong.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0xB,
        (
            "#4PIf you find ingredients that aren't on it,\x01",
            "come here to report.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0xB,
        (
            "#4POf course, you're also welcome\x01",
            "to get a bunch together and report\x01",
            "before you're completely done.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0xB,
        (
            "#4PHowever, I will need one of the\x01",
            "ingredients as a sample, so do be\x01",
            "careful not to eat too much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x101,
        (
            "#1006F#1PGet ingredients not on this list\x01",
            "and come here to report, then?\x02\x03",

            "#1015FHow many types do you want?\x01",
            "Of the ones not on this list, I mean.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0xB,
        (
            "#4PMmm... Can't be sure of how much\x01",
            "is out there, but I'd be happy if you\x01",
            "found five or six new ingredients.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0xB,
        (
            "#4PIf you can find even half of that, I'd\x01",
            "be willing to pay you for your time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0xB,
        "#4PIs there anything else you'd like to ask?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x101,
        (
            "#1000F#1PNo, I think we've got it.\x02\x03",

            "We'll look around and see\x01",
            "what we can find.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0xB,
        (
            "#4PYes, please do. And no need to rush.\x01",
            "It's not an urgent job.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0xB,
        (
            "#4PStill, I can't wait to see what\x01",
            "you report!\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x65, 0x4, 0x4)
    OP_28(0x65, 0x4, 0x8)
    OP_28(0x65, 0x1, 0x1)
    OP_28(0x65, 0x1, 0x2)

    label("loc_15AD")

    OP_30(0x0)
    OP_4B(0xB, 0)
    OP_8C(0xB, 0, 0)
    EventEnd(0x0)
    Return()

    # Function_2_85F end

    def Function_3_15BD(): pass

    label("Function_3_15BD")

    EventBegin(0x0)
    Fade(1000)
    OP_8C(0xB, 180, 0)
    OP_4A(0xB, 255)
    Call(1, 1)
    OP_69(0xB, 0x0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #66
        0xB,
        "#4POh, did you find something?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x101,
        (
            "#1015F#3PNo, that's not it.\x02\x03",

            "Actually, something's come up...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0xB,
        (
            "#4PIs that so? Does that mean you\x01",
            "won't be able to finish the job?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x101,
        (
            "#1007F#3PYeah, that's right.\x02\x03",

            "Sorry, I know we're leaving this\x01",
            "kind of incomplete.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0xB,
        "#4PNo, it's all right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0xB,
        (
            "#4PYou've already put together as\x01",
            "much as I requested, so I'm plenty\x01",
            "satisfied as it is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0xB,
        (
            "#4PI'll notify the guild that the job's\x01",
            "complete.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0xB,
        (
            "#4PYou should be able to pick up\x01",
            "the payment for your time there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x101,
        "#1000F#3PThanks, I appreciate it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0xB,
        (
            "#4PNo problem. You did a fine job,\x01",
            "as far as I'm concerned.\x02\x03",

            "#4PI'll call for you again if something\x01",
            "else comes up!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x101,
        "#1000F#3PSure! Later.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_18C1")

    ChrTalk(    #77
        0x106,
        "#051F#5PTill next time.\x02",
    )

    CloseMessageWindow()
    Jump("loc_18DE")

    label("loc_18C1")


    ChrTalk(    #78
        0x103,
        "#020F#5PTill next time.\x02",
    )

    CloseMessageWindow()

    label("loc_18DE")

    OP_22(0x17, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #79
        "Quest #2C[Come, Ingredient Hunters!] #0Ccompleted!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x4)
    OP_4B(0xB, 255)
    OP_8C(0xB, 0, 0)
    EventEnd(0x0)
    Return()

    # Function_3_15BD end

    def Function_4_1953(): pass

    label("Function_4_1953")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x65, 0x1, 0x4000)"), scpexpr(EXPR_END)), "loc_19ED")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "Report\x01",                 # 0
            "End Investigation\x01",      # 1
            "Leave\x01",                  # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_19C8")
    Call(1, 5)
    Jump("loc_19EA")

    label("loc_19C8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_19EA")
    Call(1, 3)
    OP_28(0x65, 0x4, 0x10)
    OP_28(0x65, 0x1, 0x400)
    OP_A2(0x4)
    Jump("loc_19EA")

    label("loc_19EA")

    Jump("loc_1A42")

    label("loc_19ED")

    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "Report\x01",      # 0
            "Leave\x01",       # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1A3E")
    Jump("loc_1A42")

    label("loc_1A3E")

    Call(1, 5)

    label("loc_1A42")

    TalkEnd(0xB)
    Return()

    # Function_4_1953 end

    def Function_5_1A46(): pass

    label("Function_5_1A46")

    OP_4A(0xB, 255)

    ChrTalk(    #80
        0xB,
        "Oh, did you find something?\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #81
        "\x07\x05Estelle showed the ingredients they gathered to Orvid.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x3A1, 0x0)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x65, 0x1, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1AE2")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_1AE2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x3A3, 0x0)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x65, 0x1, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1AFE")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_1AFE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x39E, 0x0)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x65, 0x1, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1B1A")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_1B1A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x3A7, 0x0)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x65, 0x1, 0x20)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1B36")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_1B36")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x3AA, 0x0)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x65, 0x1, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1B52")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_1B52")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x3A9, 0x0)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x65, 0x1, 0x80)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1B6E")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_1B6E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2B20")
    OP_62(0xB, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_63(0xB)
    Sleep(400)
    OP_62(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #82
        0xB,
        "Oh...?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0xB,
        "This ingredient wasn't on the list.\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x3A1, 0x0)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x65, 0x1, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1C3B")
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #84
        "\x07\x00Reported about #929i!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_28(0x65, 0x1, 0x4)

    label("loc_1C3B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x3A3, 0x0)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x65, 0x1, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1C80")
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #85
        "\x07\x00Reported about #931i!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_28(0x65, 0x1, 0x8)

    label("loc_1C80")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x39E, 0x0)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x65, 0x1, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1CC5")
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #86
        "\x07\x00Reported about #926i!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_28(0x65, 0x1, 0x10)

    label("loc_1CC5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x3A7, 0x0)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x65, 0x1, 0x20)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1D0A")
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #87
        "\x07\x00Reported about #935i!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_28(0x65, 0x1, 0x20)

    label("loc_1D0A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x3AA, 0x0)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x65, 0x1, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1D4F")
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #88
        "\x07\x00Reported about #938i!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_28(0x65, 0x1, 0x40)

    label("loc_1D4F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x3A9, 0x0)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x65, 0x1, 0x80)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1D94")
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #89
        "\x07\x00Reported about #937i!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_28(0x65, 0x1, 0x80)

    label("loc_1D94")

    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_0D()
    Sleep(400)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x65, 0x1, 0x4)"), scpexpr(EXPR_END)), "loc_1DCB")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_1DCB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x65, 0x1, 0x8)"), scpexpr(EXPR_END)), "loc_1DE0")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_1DE0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x65, 0x1, 0x10)"), scpexpr(EXPR_END)), "loc_1DF5")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_1DF5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x65, 0x1, 0x20)"), scpexpr(EXPR_END)), "loc_1E0A")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_1E0A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x65, 0x1, 0x40)"), scpexpr(EXPR_END)), "loc_1E1F")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_1E1F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x65, 0x1, 0x80)"), scpexpr(EXPR_END)), "loc_1E34")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_1E34")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2359")
    FadeToDark(1000, 0, -1)
    OP_0D()
    EventBegin(0x0)
    OP_8C(0xB, 180, 0)
    Call(1, 1)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #90
        0xB,
        (
            "#4PYes... Yes! This is incredible!\x01",
            "Far beyond my expectations.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0xB,
        (
            "#4PI'd say the list is good enough\x01",
            "to be considered complete.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0xB,
        (
            "#4POh, my dear bracers.\x01",
            "What a stunning haul!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0x101,
        (
            "#1001F#1PAwww! Nah, it was nothin'.\x02\x03",

            "Guess this means the job's\x01",
            "complete?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0xB,
        (
            "#4PYes, and beyond my wildest dreams!\x01",
            "Allow me to offer you a well-earned bonus\x01",
            "for your contributions to the culinary world.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0xB,
        (
            "#4PThey're the cream of my trade, and I hope\x01",
            "you'll eat each and every one of them to the\x01",
            "last OOZING morsel.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #96
        "\x07\x00Received #927i x20.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x39F, 20)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x26)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_20FB")

    ChrTalk(    #97
        0x127,
        (
            "#153F#1PWh-Whaaaa...?!\x02\x03",

            "You can eat this?!\x01",
            "Woooooooooooow.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_20FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_2118")

    ChrTalk(    #98
        0x106,
        "#053F#5P(...)\x02",
    )

    CloseMessageWindow()
    Jump("loc_212B")

    label("loc_2118")


    ChrTalk(    #99
        0x103,
        "#026F#5P(...)\x02",
    )

    CloseMessageWindow()

    label("loc_212B")


    ChrTalk(    #100
        0x101,
        (
            "#1008F#1PAh... Ahaha...\x02\x03",

            "Oh, ah, n-no, sir. I couldn't possibly...\x01",
            "(Please don't make me take all this...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0xB,
        (
            "#4PHahaha! No, I'll not hear of it!\x01",
            "You did the job beautifully,\x01",
            "and you WILL be rewarded for it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0xB,
        (
            "#4PNo need to hold back on my\x01",
            "account. Go on! Take it!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0x101,
        "#1016F#1POh, boy... Th-Thanks.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0xB,
        "#4PYou've done very well this time.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0xB,
        (
            "#4PI'll be sure to call on you when\x01",
            "a new job's come up. Until then!\x02",
        )
    )

    CloseMessageWindow()
    OP_2B(0x65, 0x1)
    OP_2C(0x65, 0x3E8)
    OP_28(0x65, 0x4, 0x10)
    OP_28(0x65, 0x1, 0x400)
    OP_A2(0x4)
    OP_22(0x17, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #106
        "Quest #2C[Come, Ingredient Hunters!] #0Ccompleted!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x4)
    EventEnd(0x0)
    Jump("loc_2B1D")

    label("loc_2359")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_EXEC_OP, "OP_29(0x65, 0x1, 0x4000)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2AC3")
    FadeToDark(1000, 0, -1)
    OP_0D()
    EventBegin(0x0)
    OP_8C(0xB, 180, 0)
    Call(1, 1)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #107
        0xB,
        (
            "#4PGoodness! Looks like you found\x01",
            "quite a bit out there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0xB,
        (
            "#4PThe list is nearly complete.\x01",
            "You've done some excellent work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0x101,
        (
            "#1000F#1PGuess this means the job's\x01",
            "complete?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0xB,
        "#4PI suppose... Still...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0xB,
        (
            "#4POh, why not? Any chance you're up\x01",
            "for going at it a little while longer?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0x101,
        "#1004F#1PHuh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0xB,
        (
            "#4PI'm asking if you'd like to see\x01",
            "this list completed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0xB,
        (
            "#4PI have a feeling there are still\x01",
            "a few more ingredients out there\x01",
            "that haven't been found.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0xB,
        (
            "#4PIf you can find all of them, I'll offer\x01",
            "you a nice little bonus...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0xB,
        "#4PWell, how about it?\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "End Investigation\x01",           # 0
            "Continue Investigation\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_28B6")

    ChrTalk(    #117
        0x101,
        (
            "#1015F#1PI think we're gonna have to end\x01",
            "it here.\x02\x03",

            "We've got other jobs that need\x01",
            "doing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0xB,
        (
            "#4PHmph! What a disappointing lack\x01",
            "of culinary passion.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0xB,
        (
            "#4PI won't push the issue any further.\x01",
            "Consider the job complete.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0xB,
        "#4PAs agreed, I'll pay you the full amount.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0xB,
        (
            "#4PYou've done some fine work. I'll be sure\x01",
            "to let you know if I've got any other jobs\x01",
            "for you in the future.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_27E5")

    ChrTalk(    #122
        0x106,
        "#051F#5PYeah, later.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2816")

    label("loc_27E5")


    ChrTalk(    #123
        0x103,
        "#020F#5PHopefully we'll see you again soon.\x02",
    )

    CloseMessageWindow()

    label("loc_2816")


    ChrTalk(    #124
        0x101,
        "#1006F#1PGood luck with your work!\x02",
    )

    CloseMessageWindow()
    OP_28(0x65, 0x4, 0x10)
    OP_28(0x65, 0x1, 0x400)
    OP_A2(0x4)
    OP_22(0x17, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #125
        "Quest #2C[Come, Ingredient Hunters!] #0Ccompleted!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x4)
    Jump("loc_2ABE")

    label("loc_28B6")

    OP_28(0x65, 0x1, 0x4000)

    ChrTalk(    #126
        0x101,
        (
            "#1006F#1PAll right. I'll give it a try.\x02\x03",

            "Might as well ride this thing\x01",
            "to the end.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0xB,
        "#4PExcellent! I knew you'd say that!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0xB,
        (
            "#4PI'll ask that you continue reporting\x01",
            "to me as before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0xB,
        (
            "#4PIf some urgent business comes\x01",
            "up and you can't continue after all,\x01",
            "just say so.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0xB,
        (
            "#4PI'll come up with a different plan at\x01",
            "that point. Payment will be as we\x01",
            "originally agreed upon.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_2A5B")

    ChrTalk(    #131
        0x106,
        "#051F#5PGot it.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2A74")

    label("loc_2A5B")


    ChrTalk(    #132
        0x103,
        "#020F#5PUnderstood.\x02",
    )

    CloseMessageWindow()

    label("loc_2A74")


    ChrTalk(    #133
        0x101,
        "#1006F#1POkay! We're off.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0xB,
        "#4PI can't wait to see what you find!\x02",
    )

    CloseMessageWindow()

    label("loc_2ABE")

    EventEnd(0x0)
    Jump("loc_2B1D")

    label("loc_2AC3")


    ChrTalk(    #135
        0xB,
        (
            "There should still be a few\x01",
            "ingredients not on the list.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0xB,
        "Keep up the good work.\x02",
    )

    CloseMessageWindow()

    label("loc_2B1D")

    Jump("loc_2BC3")

    label("loc_2B20")

    OP_62(0xB, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_63(0xB)
    Sleep(400)

    ChrTalk(    #137
        0xB,
        "Hmm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0xB,
        (
            "Unfortunately, nothing you have\x01",
            "seems all that new.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0xB,
        (
            "Come by and report again once\x01",
            "you've found something new.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2BC3")

    OP_4B(0xB, 0)
    OP_8C(0xB, 0, 0)
    Return()

    # Function_5_1A46 end

    SaveToFile()

Try(main)
