from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 洛连特

    CreateScenaFile(
        FileName            = 'T0136_1 ._SN',
        MapName             = 'Rolent',
        Location            = 'C0403.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60010",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            'ED6_DT21/T0136_1 ._SN',
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
        "Function_1_563",          # 01, 1
        "Function_2_761",          # 02, 2
        "Function_3_1227",         # 03, 3
    )


    def Function_0_AA(): pass

    label("Function_0_AA")

    EventBegin(0x0)
    OP_8C(0xB, 270, 0)
    Fade(1000)
    SetChrPos(0x101, -84710, 0, 119250, 270)
    SetChrPos(0x103, -85200, 0, 120650, 225)
    SetChrPos(0xF8, -83460, 0, 119250, 270)
    SetChrPos(0xF9, -83730, 0, 120510, 225)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12B")
    SetChrPos(0xF9, -83460, 0, 119250, 270)
    SetChrPos(0xF8, -83730, 0, 120510, 225)

    label("loc_12B")

    OP_6D(-85090, 0, 119630, 0)
    OP_67(0, 6150, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x9, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_176")
    OP_A2(0x4)

    label("loc_176")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F0")
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Cleared Kitten Search\x01",            # 0
            "Did Not Clear Kitten Search\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1E4"),
        (1, "loc_1EA"),
        (SWITCH_DEFAULT, "loc_1F0"),
    )


    label("loc_1E4")

    OP_A2(0x4)
    Jump("loc_1F0")

    label("loc_1EA")

    OP_A3(0x4)
    Jump("loc_1F0")

    label("loc_1F0")


    ChrTalk(    #0
        0xB,
        "#7POooh, what to do, what to do...\x02",
    )

    CloseMessageWindow()
    OP_62(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_63(0xB)
    TurnDirection(0xB, 0x101, 400)

    ChrTalk(    #1
        0xB,
        "Oh? You all are...?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_2A7")

    ChrTalk(    #2
        0x101,
        (
            "#7P#1006FHey! It's been a while.\x02\x03",

            "We saw the job posted on the board.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E6")

    label("loc_2A7")


    ChrTalk(    #3
        0x101,
        (
            "#7P#1000FWe saw the job posted on the board.\x02\x03",

            "You're Ida?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E6")


    ChrTalk(    #4
        0xB,
        (
            "Oh, my, my, I'm so sorry to call you\x01",
            "out so late at night!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xB,
        (
            "I know it's sudden, buuuuut would\x01",
            "you go find Aryll for me?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_3E3")

    ChrTalk(    #6
        0x101,
        (
            "#7P#1004FA-Aryll...\x02\x03",

            "#1016FThat cat... Gone again, I take it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xB,
        (
            "How about it? Will you find my\x01",
            "little Aryll?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3E3")

    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Sure!\x01",      # 0
            "Nope.\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_439")
    Call(1, 2)
    Jump("loc_560")

    label("loc_439")


    ChrTalk(    #8
        0x101,
        (
            "#7P#1015FAh, sorry. We've got other stuff we're\x01",
            "busy with right now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xB,
        "Awww. That's a shame.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xB,
        (
            "I know that you all must be so terribly\x01",
            "busy. Trust me, I understand.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x103,
        "#7P#020FWe thank you for your understanding.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x101,
        "#7P#1000FWe'll be back as soon as we can.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xB,
        "Thank you!\x02",
    )

    CloseMessageWindow()
    OP_28(0x74, 0x1, 0x8000)

    label("loc_560")

    EventEnd(0x0)
    Return()

    # Function_0_AA end

    def Function_1_563(): pass

    label("Function_1_563")

    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x101, -84710, 0, 119250, 270)
    SetChrPos(0x103, -85200, 0, 120650, 225)
    SetChrPos(0xF8, -83460, 0, 119250, 270)
    SetChrPos(0xF9, -83730, 0, 120510, 225)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5DD")
    SetChrPos(0xF9, -83460, 0, 119250, 270)
    SetChrPos(0xF8, -83730, 0, 120510, 225)

    label("loc_5DD")

    TurnDirection(0xB, 0x101, 0)
    OP_6D(-85090, 0, 119630, 0)
    OP_67(0, 6150, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    OP_0D()

    ChrTalk(    #14
        0xB,
        "Hello there, bracers!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xB,
        (
            "Have you decided to look for\x01",
            "my little Aryll?\x02",
        )
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
            "Sure!\x01",      # 0
            "Nope.\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6C6")
    Call(1, 2)
    Jump("loc_75E")

    label("loc_6C6")


    ChrTalk(    #16
        0x101,
        "#7P#1015FSorry. We're still a bit tied up.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0xB,
        "Awww. That's a shame.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x101,
        (
            "#7P#1000FOnce we have some time,\x01",
            "we'll come right back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0xB,
        "Please do.\x02",
    )

    CloseMessageWindow()

    label("loc_75E")

    EventEnd(0x0)
    Return()

    # Function_1_563 end

    def Function_2_761(): pass

    label("Function_2_761")


    ChrTalk(    #20
        0x101,
        (
            "#7P#1000FYeah... We should be able to\x01",
            "handle the job right now.\x02\x03",

            "#1015FGiven the circumstances, though,\x01",
            "I'm wondering if now's the right time...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 400)

    ChrTalk(    #21
        0x103,
        (
            "#7P#026FResponding to complex situations is\x01",
            "an important part of a bracer's job.\x02\x03",

            "#027FWe'll assist you as much as we can.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xB,
        "Wonderful.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0xB, 400)

    ChrTalk(    #23
        0x103,
        (
            "#7P#020FIf you can, could you provide some\x01",
            "details?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_944")

    ChrTalk(    #24
        0x106,
        (
            "#050FWe know that you're looking for a cat.\x02\x03",

            "Is that 'Aryll' you mentioned the cat in\x01",
            "question?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AA3")

    label("loc_944")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9BA")

    ChrTalk(    #25
        0x108,
        (
            "#070FWe know that you're looking for a cat.\x02\x03",

            "Is that 'Aryll' you mentioned the cat in\x01",
            "question?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AA3")

    label("loc_9BA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A30")

    ChrTalk(    #26
        0x104,
        (
            "#030FWe know that you're looking for a cat.\x02\x03",

            "Is that 'Aryll' you mentioned the cat in\x01",
            "question?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AA3")

    label("loc_A30")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_AA3")

    ChrTalk(    #27
        0x105,
        (
            "#040FWe know that you're looking for a cat.\x02\x03",

            "Is that 'Aryll' you mentioned the cat in\x01",
            "question?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AA3")


    ChrTalk(    #28
        0xB,
        "Yes, that's right. My little Aryll's run off.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xB,
        (
            "She disappeared while I was taking\x01",
            "an afternoon nap. Oops.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_B6C")
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #30
        0x101,
        "#7P#1007F(This sure seems mighty familiar...)\x02",
    )

    CloseMessageWindow()

    label("loc_B6C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BD6")

    ChrTalk(    #31
        0x107,
        (
            "#064FSo she's been gone the whole\x01",
            "afternoon?\x02\x03",

            "#063FI'd start to get worried, too...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D27")

    label("loc_BD6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C46")

    ChrTalk(    #32
        0x105,
        (
            "#043FThat would mean she been gone\x01",
            "for half a day.\x02\x03",

            "I can see why you're getting worried.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D27")

    label("loc_C46")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_CB4")

    ChrTalk(    #33
        0x104,
        (
            "#032FI see. She's been gone nearly half the day.\x02\x03",

            "That would be cause for some concern.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D27")

    label("loc_CB4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D27")

    ChrTalk(    #34
        0x108,
        (
            "#074FSo about half a day's passed since she\x01",
            "disappeared.\x02\x03",

            "Now I get why you're getting worried.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D27")


    ChrTalk(    #35
        0x103,
        (
            "#7P#022FDo you have any idea where she\x01",
            "might have gone?\x02\x03",

            "If you can think of any spots she might\x01",
            "have gone to, that would help.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x103, 400)

    ChrTalk(    #36
        0xB,
        "Hmm... I miiight have an idea.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xB,
        (
            "From what I found out, the landing\x01",
            "port seems suspicious...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x101,
        "#7P#1011FThe landing port?!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x101, 400)

    ChrTalk(    #39
        0xB,
        (
            "I poked around there a bit and asked\x01",
            "one of the engineers, and they said\x01",
            "someone saw a cat.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0xB,
        (
            "They said it was a light brown kitty,\x01",
            "so it must be Aryll.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x101,
        (
            "#7P#1002FI-I see...\x02\x03",

            "#1015FOh, I should write down the color\x01",
            "of the cat's fur.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F9F")

    ChrTalk(    #42
        0x108,
        (
            "#070FThis is all good to know.\x02\x03",

            "Why don't we investigate and\x01",
            "see where it takes us?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10C6")

    label("loc_F9F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_FFB")

    ChrTalk(    #43
        0x106,
        (
            "#051FSounds like a lead to me.\x02\x03",

            "We'll look into it right away, ma'am.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10C6")

    label("loc_FFB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_105A")

    ChrTalk(    #44
        0x104,
        (
            "#030FOoh, that is valuable information.\x02\x03",

            "We're off to a promising start.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10C6")

    label("loc_105A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10C6")

    ChrTalk(    #45
        0x105,
        (
            "#040FThat's very useful information. Thank you.\x02\x03",

            "Shall we start the investigation there?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10C6")


    ChrTalk(    #46
        0x103,
        (
            "#7P#020FYes, I think it's worth investigating.\x02\x03",

            "Let's ask around at the landing port.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 400)

    ChrTalk(    #47
        0x101,
        "#1006FCouldn't agree more.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0xB,
        "I'm glad I was able to help.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0xB,
        (
            "I'll be waiting here for word\x01",
            "of my little Aryll.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0xB,
        "Good luck!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xB, 400)

    ChrTalk(    #51
        0x101,
        "#7P#1006FWe'll report once we've found her.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x103,
        "#7P#020FYes. Until then.\x02",
    )

    CloseMessageWindow()
    OP_28(0x74, 0x1, 0x1)
    OP_28(0x74, 0x1, 0x2)
    OP_28(0x74, 0x1, 0x4)
    OP_28(0x74, 0x4, 0x4)
    OP_28(0x74, 0x4, 0x8)
    OP_A2(0x3)
    Return()

    # Function_2_761 end

    def Function_3_1227(): pass

    label("Function_3_1227")

    FadeToDark(0, 0, -1)
    EventBegin(0x0)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0xC, 0x40)
    SetChrFlags(0xD, 0x4)
    SetChrFlags(0xE, 0x4)
    SetChrFlags(0xF, 0x4)
    SetChrPos(0xB, -85600, 0, 119540, 90)
    SetChrPos(0xC, -85720, 0, 120310, 90)
    SetChrPos(0xF, -84190, 0, 123070, 330)
    SetChrPos(0xE, -83500, 580, 117300, 270)
    SetChrPos(0xD, -83030, 580, 116830, 315)
    OP_43(0xF, 0x1, 0x0, 0x2)
    OP_43(0xE, 0x1, 0x0, 0x3)
    OP_43(0xD, 0x1, 0x0, 0x3)
    OP_4A(0xB, 255)
    SetChrPos(0x101, -83980, 0, 119500, 270)
    SetChrPos(0x103, -83580, 0, 120500, 273)
    SetChrPos(0xF8, -82420, 0, 119000, 270)
    SetChrPos(0xF9, -82100, 0, 120000, 270)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_133C")
    SetChrPos(0xF9, -82420, 0, 119000, 270)
    SetChrPos(0xF8, -82100, 0, 120000, 270)

    label("loc_133C")

    OP_6D(-85080, 0, 120200, 0)
    OP_67(0, 6150, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #53
        0xB,
        "Ooooh, what a surprise!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0xB,
        (
            "Aryll's up and become a mother,\x01",
            "heehee.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x101,
        (
            "#1016F#7PWe were just as surprised as you.\x02\x03",

            "Didn't see that coming, not one bit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x103,
        (
            "#020F#7PBoth mother and children appear to\x01",
            "be healthy.\x02\x03",

            "Raise them with care.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0xB,
        (
            "Why, but of course! They're as precious\x01",
            "to me as grandchildren.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0xB,
        "Now comes the REAL challenge.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0xB,
        (
            "I need to come up with the perfect\x01",
            "name for each and every one of them.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_156E")

    ChrTalk(    #60
        0x107,
        "#560FI'm sure their names'll be really cute!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1645")

    label("loc_156E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_15B0")

    ChrTalk(    #61
        0x105,
        "#040FI'm sure their names will be adorable.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1645")

    label("loc_15B0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1612")

    ChrTalk(    #62
        0x104,
        (
            "#030FI expect most wondrous names.\x01",
            "Perhaps something noble, like 'Tiddles.'\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1645")

    label("loc_1612")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1645")

    ChrTalk(    #63
        0x108,
        "#070FYeah, give 'em good names.\x02",
    )

    CloseMessageWindow()

    label("loc_1645")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x9, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1652")
    OP_A2(0x4)

    label("loc_1652")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16CC")
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Cleared Kitten Search\x01",            # 0
            "Did not clear Kitten Search\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_16C0"),
        (1, "loc_16C6"),
        (SWITCH_DEFAULT, "loc_16CC"),
    )


    label("loc_16C0")

    OP_A2(0x4)
    Jump("loc_16CC")

    label("loc_16C6")

    OP_A3(0x4)
    Jump("loc_16CC")

    label("loc_16CC")


    ChrTalk(    #64
        0xB,
        "No problems there! Leave it to me.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_18EF")

    ChrTalk(    #65
        0xB,
        "Oh, and one last thing before you go!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0xB,
        (
            "Heehee. It simply wouldn't do to have\x01",
            "you on your way just yet.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #67
        0x101,
        "#1015F#7PUm, did you need something else?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0xB,
        (
            "Mm-hmm! This is the second time\x01",
            "you've helped me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0xB,
        "Here! It's only right for you to take this. ㈱\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #70
        "\x07\x00Received #343i.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x157, 1)

    ChrTalk(    #71
        0xB,
        (
            "It's something I've used often when\x01",
            "praying.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0xB,
        "It's very calming. ㈱\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x101,
        (
            "#1011F#7POh, neat.\x02\x03",

            "#1000FThanks. We appreciate it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18EF")


    ChrTalk(    #74
        0xB,
        (
            "Well, then, please take care on\x01",
            "your way home.\x02",
        )
    )

    CloseMessageWindow()
    OP_4A(0xC, 255)
    TurnDirection(0xC, 0x101, 400)
    OP_22(0x192, 0x0, 0x64)

    ChrTalk(    #75
        0xC,
        "Nya～on.\x02",
    )

    CloseMessageWindow()
    OP_4A(0xD, 255)
    TurnDirection(0xD, 0x101, 400)
    OP_22(0x15C, 0x0, 0x64)

    ChrTalk(    #76
        0xD,
        "Mya～u.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F3)
    NewScene("ED6_DT21/T0101   ._SN", 116, 0, 0)
    IdleLoop()
    Return()

    # Function_3_1227 end

    SaveToFile()

Try(main)
