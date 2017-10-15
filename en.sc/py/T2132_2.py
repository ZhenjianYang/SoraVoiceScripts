from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 卢安

    CreateScenaFile(
        FileName            = 'T2132_2 ._SN',
        MapName             = 'Ruan',
        Location            = 'T2132.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60012",
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
        Unknown_30              = 35,
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
        "Function_1_18C",          # 01, 1
        "Function_2_3A7",          # 02, 2
        "Function_3_8DB",          # 03, 3
        "Function_4_1D66",         # 04, 4
        "Function_5_1FA4",         # 05, 5
        "Function_6_240E",         # 06, 6
        "Function_7_2626",         # 07, 7
        "Function_8_26DF",         # 08, 8
    )


    def Function_0_AA(): pass

    label("Function_0_AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_127")
    TalkBegin(0x10)
    TurnDirection(0x10, 0x0, 0)

    ChrTalk(    #0
        0x10,
        "It's gotten pretty loud outside...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x10,
        (
            "Do you know if something\x01",
            "happened out there?\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x10, 346, 0)
    TalkEnd(0x10)
    Jump("loc_18B")

    label("loc_127")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x66, 0x1, 0x4)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x66, 0x1, 0x8)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_147")
    EventBegin(0x0)
    OP_4A(0x10, 255)
    Call(2, 6)
    Jump("loc_18B")

    label("loc_147")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x66, 0x0, 0x8)"), scpexpr(EXPR_END)), "loc_164")
    EventBegin(0x0)
    OP_4A(0x10, 255)
    Call(2, 5)
    OP_4B(0x10, 255)
    EventEnd(0x0)
    Jump("loc_18B")

    label("loc_164")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x66, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_181")
    EventBegin(0x0)
    OP_4A(0x10, 255)
    Call(2, 2)
    OP_4B(0x10, 255)
    EventEnd(0x0)
    Jump("loc_18B")

    label("loc_181")

    TalkBegin(0x10)
    Call(2, 1)
    TalkEnd(0x10)

    label("loc_18B")

    Return()

    # Function_0_AA end

    def Function_1_18C(): pass

    label("Function_1_18C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_1FB")

    ChrTalk(    #2
        0x10,
        (
            "I'm waiting for someone, but they're\x01",
            "taking their sweet time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x10,
        "Man, I wish they'd hurry up!\x02",
    )

    CloseMessageWindow()
    Jump("loc_3A6")

    label("loc_1FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_339")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_299")

    ChrTalk(    #4
        0x10,
        (
            "There sure have been a lot of\x01",
            "dangerous monsters around\x01",
            "lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x10,
        (
            "Just thinking of going out there\x01",
            "on my own makes me nervous...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_336")

    label("loc_299")

    OP_A2(0x7)

    ChrTalk(    #6
        0x10,
        (
            "I heard from the guild that there've\x01",
            "been a lot of dangerous monsters\x01",
            "around lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x10,
        (
            "It's even gotten too dangerous to\x01",
            "walk the highways alone.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_336")

    Jump("loc_3A6")

    label("loc_339")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_END)), "loc_3A6")
    OP_8C(0x10, 346, 0)

    ChrTalk(    #8
        0x10,
        (
            "Let's see, I've got my camera ready,\x01",
            "spares of photo-quartz...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x10,
        "All right! I'm ready.\x02",
    )

    CloseMessageWindow()

    label("loc_3A6")

    Return()

    # Function_1_18C end

    def Function_2_3A7(): pass

    label("Function_2_3A7")

    Call(2, 7)
    Sleep(400)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x66, 0x1, 0x4000)"), scpexpr(EXPR_END)), "loc_41F")

    ChrTalk(    #10
        0x10,
        "Huh? What's up?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x10,
        (
            "Oh! Did you guys have finally wrap\x01",
            "up that stuff you mentioned before?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5EE")

    label("loc_41F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x66, 0x1, 0x8000)"), scpexpr(EXPR_END)), "loc_47B")

    ChrTalk(    #12
        0x10,
        (
            "Hey there! Nice to see you bracers\x01",
            "again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x10,
        "Schedule free enough now?\x02",
    )

    CloseMessageWindow()
    Jump("loc_5EE")

    label("loc_47B")


    ChrTalk(    #14
        0x101,
        "#1011F#4PExcuse me, can we have a moment?\x02",
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0x10, 0x101, 400)
    Sleep(400)

    ChrTalk(    #15
        0x10,
        "Sure. What's going on?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x101,
        (
            "#1015F#4PYou wouldn't happen to be Santos,\x01",
            "would you? We saw your request on\x01",
            "the board.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #17
        0x10,
        "Oh, you're bracers!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x10,
        "Phew! Fiiinally. I was getting worried.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x10,
        (
            "If you're free, I'd like to get right down\x01",
            "to business. How 'bout it?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5EE")

    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Yes\x01",      # 0
            "No\x01",       # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_665")
    OP_28(0x66, 0x1, 0x1)
    OP_28(0x66, 0x1, 0x2)
    OP_28(0x66, 0x4, 0x4)
    OP_28(0x66, 0x4, 0x8)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x66, 0x1, 0x4000)"), scpexpr(EXPR_END)), "loc_65E")
    Call(2, 4)
    Jump("loc_662")

    label("loc_65E")

    Call(2, 3)

    label("loc_662")

    Jump("loc_8D6")

    label("loc_665")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x66, 0x1, 0x4000)"), scpexpr(EXPR_END)), "loc_74E")

    ChrTalk(    #20
        0x101,
        (
            "#1007F#4PHmmm. Right now? Sorry, I don't\x01",
            "know if we can just yet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x10,
        "Awww, really?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x10,
        (
            "Guess you just wanted to check\x01",
            "in. No worries. Let me know when\x01",
            "you're ready to go.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x101,
        "#1000F#4PSure! We'll be back soon.\x02",
    )

    CloseMessageWindow()
    Jump("loc_8D6")

    label("loc_74E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x66, 0x1, 0x8000)"), scpexpr(EXPR_END)), "loc_834")

    ChrTalk(    #24
        0x101,
        "#1015F#4PSorry... We're still pretty busy.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x10,
        "Still no good, huh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x10,
        (
            "It's nice that you're checking up on\x01",
            "me, but I don't mind waiting until your\x01",
            "schedule's opened up some.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x101,
        "#1007F#4PAll righty. Thanks.\x02",
    )

    CloseMessageWindow()
    Jump("loc_8D6")

    label("loc_834")

    OP_28(0x66, 0x1, 0x8000)

    ChrTalk(    #28
        0x101,
        "#1007F#4PSorry... We can't right this second.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x10,
        "Awww, really?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x10,
        (
            "Well, try and come by when you\x01",
            "have the time, okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x101,
        "#1006F#4PYeah, we will.\x02",
    )

    CloseMessageWindow()

    label("loc_8D6")

    Call(2, 8)
    Return()

    # Function_2_3A7 end

    def Function_3_8DB(): pass

    label("Function_3_8DB")


    ChrTalk(    #32
        0x101,
        (
            "#1006F#4PYup! We're good to go.\x02\x03",

            "So what's the job?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x10,
        (
            "Okay! Here's what I need:\x01",
            "I want you to take a photograph\x01",
            "of something in Sapphirl Tower.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x10,
        (
            "And that 'something' is, specifically,\x01",
            "on the roof of the tower.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_A16")

    ChrTalk(    #35
        0x106,
        (
            "#050FSapphirl Tower, huh?\x02\x03",

            "That old ruin just off the Aurian Causeway,\x01",
            "right?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A6A")

    label("loc_A16")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_A6A")

    ChrTalk(    #36
        0x103,
        (
            "#020FSapphirl Tower, hmm?\x02\x03",

            "The same one off the Aurian Causeway,\x01",
            "right?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A6A")


    ChrTalk(    #37
        0x10,
        "Bingo! Figured you'd know about it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x101,
        (
            "#1011F#4PWhat do you want a photo of the\x01",
            "tower for?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x22, 0x24, 0xFA, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #39
        0x101,
        "#1018F#4PIs it for an editorial, maybe?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x10,
        "No, no, not at all.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x10,
        (
            "I was dispatched by the History\x01",
            "Museum in the capital.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x10,
        "This task is for research purposes.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_BD6")

    ChrTalk(    #43
        0x104,
        "#030FAhhh, so it's an academic investigation.\x02",
    )

    CloseMessageWindow()
    Jump("loc_C13")

    label("loc_BD6")


    ChrTalk(    #44
        0x101,
        (
            "#1008F#4PAaah, got'cha. It's an academic\x01",
            "investigation.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C13")


    ChrTalk(    #45
        0x10,
        "Bingo again!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x10,
        (
            "I'll admit, this isn't exactly your\x01",
            "run of the mill research, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x101,
        "#1011F#4PRun of the mill?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_CF4")

    ChrTalk(    #48
        0x106,
        (
            "#053FLet's worry about that later.\x02\x03",

            "#050FFirst, let's go over the details\x01",
            "of the job.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D56")

    label("loc_CF4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_D56")

    ChrTalk(    #49
        0x103,
        (
            "#026FLet's save that for later.\x02\x03",

            "#020FFirst, I'd like to hear the details\x01",
            "of the job.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D56")

    SetChrName("Santos")

    ChrTalk(    #50
        0x10,
        (
            "Oops! Sorry. Got a bit sidetracked.\x01",
            "Haha.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x10,
        "Er, how much have I said so far?\x02",
    )

    CloseMessageWindow()

    def lambda_DB9():
        TurnDirection(0xF7, 0x10, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_DB9)
    TurnDirection(0x101, 0x10, 400)

    ChrTalk(    #52
        0x101,
        (
            "#1011F#4PYou want us to climb to the top of the\x01",
            "tower and photograph 'something.'\x02\x03",

            "#1015FWe just need to know what that\x01",
            "something is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x10,
        (
            "Okay, so there're these mysterious\x01",
            "objects on the roof of the towers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x10,
        (
            "We know they're ancient artifacts\x01",
            "of some kind, but outside of that?\x01",
            "We've got nothing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x10,
        (
            "Without much else to go on, the only\x01",
            "thing we researchers can conclude is\x01",
            "that they're devices of some kind.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x101,
        (
            "#1011F#4PActually, I might have an idea\x01",
            "of what you're talking about...\x02\x03",

            "They look like weird pedestals,\x01",
            "right?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(400)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x66, 0x1, 0x2000)"), scpexpr(EXPR_END)), "loc_114A")

    ChrTalk(    #57
        0x10,
        "Oh, you know about them?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x10,
        (
            "Bingo, bingo, bingo! They look\x01",
            "exactly like pedestals.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x101,
        (
            "#1002F#4POh, cool! Then, yeah, I've seen them\x01",
            "around before.\x02\x03",

            "Those things have been emanating\x01",
            "some kind of strange light lately, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x10,
        "So we noticed.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x10,
        (
            "The museum's received a report\x01",
            "about that from a reputable source.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1373")

    label("loc_114A")


    ChrTalk(    #62
        0x10,
        "Oh, you know about them?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x10,
        (
            "Bingo, bingo, bingo! They look\x01",
            "exactly like pedestals.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x101,
        (
            "#1001F#4POh, cool! Then, yeah, I've seen\x01",
            "them around before.\x02\x03",

            "I don't think they work anymore,\x01",
            "though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x10,
        "...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x10,
        "Actually, about that...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x10,
        "That might not be entirely true.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x101,
        "#1011F#4PHuh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x10,
        "The device on Sapphirl Tower...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x10,
        "...has reportedly been activated.\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #71
        0x101,
        (
            "#1004F#4PWhat?!\x02\x03",

            "It's actually WORKING?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x10,
        (
            "The museum's received a report\x01",
            "about that from a very reliable source.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x10,
        "I doubt they were mistaken.\x02",
    )

    CloseMessageWindow()

    label("loc_1373")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_13D9")

    ChrTalk(    #74
        0x106,
        (
            "#053FHuh. Interestin'.\x02\x03",

            "#050FSo that's why you wanted us\x01",
            "to check this out so quickly.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_141A")

    label("loc_13D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_141A")

    ChrTalk(    #75
        0x103,
        (
            "#027FI see...\x02\x03",

            "So that's why you're in such a hurry.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_141A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x66, 0x1, 0x2000)"), scpexpr(EXPR_END)), "loc_15C5")

    ChrTalk(    #76
        0x10,
        "Exactly.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0x10,
        (
            "Anyway, we need to record the\x01",
            "current state of the device.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0x101,
        "#1003F#4PTalk about spooky...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x10,
        (
            "We don't suspect it poses any danger\x01",
            "for now, but you never know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0x10,
        (
            "We can't say for sure--anything could\x01",
            "happen, so be very careful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0x101,
        (
            "#1002F#4POf course. I've got no intentions\x01",
            "of letting my guard down.\x02\x03",

            "Just to double check: you only\x01",
            "need a photograph of the device\x01",
            "in question, right?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17E5")

    label("loc_15C5")


    ChrTalk(    #82
        0x10,
        "Exactly.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0x10,
        (
            "Anyway, we need to record the\x01",
            "current state of the device.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0x101,
        (
            "#1002F#4PTalk about spooky... Yeah, probably\x01",
            "a good idea to look into it.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_168F")

    ChrTalk(    #85
        0x106,
        "#050FIs the device dangerous?\x02",
    )

    CloseMessageWindow()
    Jump("loc_16B9")

    label("loc_168F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_16B9")

    ChrTalk(    #86
        0x103,
        "#022FIs the device dangerous?\x02",
    )

    CloseMessageWindow()

    label("loc_16B9")


    ChrTalk(    #87
        0x10,
        (
            "We don't suspect it poses any danger\x01",
            "for now, but you never know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0x10,
        (
            "We can't say for sure--anything could\x01",
            "happen, so be very careful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0x101,
        (
            "#1002F#4POf course. I've got no intentions\x01",
            "of letting my guard down.\x02\x03",

            "Just to double check: you only\x01",
            "need a photograph of the device\x01",
            "in question, right?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17E5")


    ChrTalk(    #90
        0x10,
        (
            "Yep. Please bring the photograph\x01",
            "straight to me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0x10,
        (
            "I'm going to lend you a camera, too,\x01",
            "but I'll need you to return it once you're\x01",
            "back.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x10, 346, 400)
    Sleep(1000)
    TurnDirection(0x10, 0x101, 400)
    OP_92(0x10, 0x101, 0x2BC, 0x7D0, 0x0)
    Sleep(400)

    ChrTalk(    #92
        0x10,
        "All right! I'm counting on you!\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #93
        "\x07\x00Received #562i.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x232, 1)
    Sleep(400)
    OP_8F(0x10, 0xFFFF4B3B, 0x0, 0x1108, 0x3E8, 0x0)
    Sleep(400)
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(400)

    ChrTalk(    #94
        0x101,
        "#1016F#4PTh-This is...pretty clunky.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x26)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1A6B")

    ChrTalk(    #95
        0x127,
        (
            "#150FSure is! It's a top-class model used\x01",
            "for archive photographs, after all.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x127, 400)

    ChrTalk(    #96
        0x101,
        "#1011FHuh, so it's a good camera?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0x127,
        (
            "#151FYes, indeedy! She's a very honest,\x01",
            "goooood girl.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #98
        0x101,
        "#1007FG-Good girl...?\x02",
    )

    CloseMessageWindow()
    Jump("loc_1AC2")

    label("loc_1A6B")


    ChrTalk(    #99
        0x10,
        (
            "Well, yeah, if you want research quality,\x01",
            "you need a hunk of machinery like this.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1AC2")


    ChrTalk(    #100
        0x10,
        (
            "Oh, by the way, I've already set the\x01",
            "photo-quartz.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0x10,
        "All you need to do is snap the shutter.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x10, 400)

    ChrTalk(    #102
        0x101,
        (
            "#1000F#4PYeah, got it.\x02\x03",

            "#1015FOkay, one more time:\x02\x03",

            "I need to go to the top of Sapphirl Tower,\x01",
            "take a picture of the device on the roof...\x02\x03",

            "...then return here with the photo and\x01",
            "return the camera. That about the size\x01",
            "of it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0x10,
        "Perfect!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0x10,
        "And one more thing.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0x10,
        (
            "No need for fancy or tricky angles.\x01",
            "A simple composition for the photo\x01",
            "is best.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0x10,
        (
            "This is for research purposes only,\x01",
            "so just try and get the most head-on\x01",
            "shot that you can.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0x101,
        (
            "#1000F#4POkay. Keep it simple.\x02\x03",

            "#1000FNo problem.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0x10,
        (
            "Can't wait to see the photo!\x01",
            "Stay safe up there.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x10, 346, 0)
    Return()

    # Function_3_8DB end

    def Function_4_1D66(): pass

    label("Function_4_1D66")


    ChrTalk(    #109
        0x10,
        (
            "Er, I've already explained everything,\x01",
            "right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0x101,
        (
            "#1011F#4PI think so.\x02\x03",

            "#1015FLet's go over it one more time,\x01",
            "just in case:\x02\x03",

            "I need to go to the top of Sapphirl\x01",
            "Tower, take a picture of the device\x01",
            "on the roof...\x02\x03",

            "...then return here with the photo\x01",
            "and return the camera. That about\x01",
            "the size of it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0x10,
        "Perfect!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0x10,
        "All right, here's the camera.\x02",
    )

    CloseMessageWindow()
    OP_92(0x10, 0x101, 0x2BC, 0x7D0, 0x0)
    Sleep(400)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #113
        "\x07\x00Received #562i.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x232, 1)
    Sleep(400)
    OP_8F(0x10, 0xFFFF4B3B, 0x0, 0x1108, 0x3E8, 0x0)
    Sleep(1000)

    ChrTalk(    #114
        0x10,
        "Stay safe out there.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0x10,
        "Can't wait to see the photo!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0x101,
        "#1006F#4PSee you in a bit!\x02",
    )

    CloseMessageWindow()
    OP_8C(0x10, 346, 0)
    Return()

    # Function_4_1D66 end

    def Function_5_1FA4(): pass

    label("Function_5_1FA4")

    Call(2, 7)

    ChrTalk(    #117
        0x10,
        "How're things going?\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        0,
        (
            "Confirm Request\x01",      # 0
            "Cancel Job\x01",           # 1
            "Nothing\x01",              # 2
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2036"),
        (1, "loc_21D1"),
        (SWITCH_DEFAULT, "loc_23B3"),
    )


    label("loc_2036")


    ChrTalk(    #118
        0x10,
        (
            "I need you to photograph that\x01",
            "pedestal-like device at the top\x01",
            "of Sapphirl Tower.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0x10,
        (
            "The Sapphirl Tower itself is down a\x01",
            "side road off the Aurian Causeway.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0x10,
        (
            "This photo's only going to be used\x01",
            "for research purposes; no need to\x01",
            "be fancy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0x10,
        (
            "Avoid complex angles, and just go\x01",
            "for a simple composition.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0x10,
        (
            "Once you've finished taking the\x01",
            "photo, come back here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0x10,
        "All right, stay safe out there.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2409")

    label("loc_21D1")

    OP_28(0x66, 0x3, 0x8)
    OP_28(0x66, 0x1, 0x4000)

    ChrTalk(    #124
        0x101,
        (
            "#1007F#4PI really sorry, but something's\x01",
            "come up...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0x10,
        "Oh... You have to cancel the job?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0x10,
        "Aww. That's too bad.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0x101,
        "#1000F#4PHere, I'll return your camera for now.\x02",
    )

    CloseMessageWindow()
    OP_92(0x101, 0x10, 0x2BC, 0x7D0, 0x0)
    Sleep(400)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #128
        "\x07\x00Returned #562i.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3F(0x232, 1)
    Sleep(400)
    OP_8F(0x101, 0xFFFF4F84, 0x0, 0xE42, 0x3E8, 0x0)
    Sleep(1000)

    ChrTalk(    #129
        0x10,
        (
            "Once you've finished your other\x01",
            "business, come back, please.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0x10,
        (
            "But, do hurry if you can. I have\x01",
            "other sites that need investigating\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0x101,
        "#1006F#4PRight, of course.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2409")

    label("loc_23B3")


    ChrTalk(    #132
        0x10,
        (
            "We don't know enough about this\x01",
            "thing to say what it can do. Be very\x01",
            "careful.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2409")

    label("loc_2409")

    Call(2, 8)
    Return()

    # Function_5_1FA4 end

    def Function_6_240E(): pass

    label("Function_6_240E")

    Call(2, 7)

    ChrTalk(    #133
        0xFE,
        "Hey, guys! Welcome back.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0xFE,
        "Did you take the photo?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0x101,
        (
            "#1001F#4PSure did!\x02\x03",

            "#1011FBut first, let me return your camera.\x02",
        )
    )

    CloseMessageWindow()
    OP_92(0x101, 0x10, 0x2BC, 0x7D0, 0x0)
    Sleep(400)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #136
        "\x07\x00Returned #562i.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3F(0x232, 1)
    Sleep(400)
    OP_8F(0x101, 0xFFFF4F84, 0x0, 0xE42, 0x3E8, 0x0)
    Sleep(1000)

    ChrTalk(    #137
        0xFE,
        "Thanks.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0xFE,
        "And now, it's off we go!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0x101,
        (
            "#1004F#4PEr... What?\x02\x03",

            "Where're we going?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0xFE,
        "The orbal factory, of course.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0xFE,
        (
            "We've got to develop the photo-\x01",
            "quartz if we want to see the picture.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0x101,
        (
            "#1016F#4PAhahaha... True.\x02\x03",

            "#1006FI'm right behind you.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_A2(0x10F2)
    NewScene("ED6_DT21/T2120   ._SN", 101, 0, 0)
    IdleLoop()
    Return()

    # Function_6_240E end

    def Function_7_2626(): pass

    label("Function_7_2626")

    Fade(1000)
    OP_6D(-45110, 0, 4019, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x26)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_265A")
    SetChrPos(0x127, -43820, 0, 3580, 307)

    label("loc_265A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2678")
    SetChrPos(0x104, -43810, 0, 2360, 299)

    label("loc_2678")

    SetChrPos(0x101, -45180, 0, 3650, 289)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_26A4")
    SetChrPos(0x106, -44880, 0, 2770, 280)
    Jump("loc_26BC")

    label("loc_26A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_26BC")
    SetChrPos(0x103, -44880, 0, 2770, 280)

    label("loc_26BC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x66, 0x1, 0x4000)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x66, 0x1, 0x8000)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_29(0x66, 0x0, 0x8)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_26DD")
    TurnDirection(0x10, 0x101, 0)

    label("loc_26DD")

    OP_0D()
    Return()

    # Function_7_2626 end

    def Function_8_26DF(): pass

    label("Function_8_26DF")

    OP_30(0x0)
    OP_8C(0x10, 346, 0)
    Return()

    # Function_8_26DF end

    SaveToFile()

Try(main)
