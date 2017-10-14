from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 柏斯

    CreateScenaFile(
        FileName            = 'T1131_1 ._SN',
        MapName             = 'Bose',
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
        "Function_1_216",          # 01, 1
        "Function_2_2F0",          # 02, 2
        "Function_3_4E5",          # 03, 3
        "Function_4_959",          # 04, 4
        "Function_5_BF3",          # 05, 5
        "Function_6_3E12",         # 06, 6
        "Function_7_4C14",         # 07, 7
        "Function_8_54AB",         # 08, 8
        "Function_9_5711",         # 09, 9
        "Function_10_7518",        # 0A, 10
        "Function_11_85A0",        # 0B, 11
        "Function_12_85FB",        # 0C, 12
        "Function_13_8623",        # 0D, 13
    )


    def Function_0_AA(): pass

    label("Function_0_AA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x13), scpexpr(EXPR_PUSH_LONG, 0x381), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B7")
    Return()

    label("loc_B7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x79, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x79, 0x0, 0x40)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_C9")
    Return()

    label("loc_C9")

    SetMapFlags(0x80)
    OP_C0(0x1, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Sleep(30)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CD(0x20)"), scpexpr(EXPR_END)), "loc_104")
    Call(0, 35)
    Jump("loc_20F")

    label("loc_104")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CD(0x1B)"), scpexpr(EXPR_END)), "loc_113")
    Call(1, 1)
    Jump("loc_20F")

    label("loc_113")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CD(0x3E8)"), scpexpr(EXPR_END)), "loc_122")
    Call(1, 1)
    Jump("loc_20F")

    label("loc_122")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CD(0x8)"), scpexpr(EXPR_END)), "loc_131")
    Call(1, 2)
    Jump("loc_20F")

    label("loc_131")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CD(0xFF)"), scpexpr(EXPR_END)), "loc_1B9")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CD(0x1C)"), scpexpr(EXPR_END)), "loc_144")
    TalkBegin(0x1C)

    label("loc_144")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #0
        "\x07\x05Tried showing them the photograph, but they didn't recognize her.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CD(0x1C)"), scpexpr(EXPR_END)), "loc_1B6")
    TalkEnd(0x1C)

    label("loc_1B6")

    Jump("loc_20F")

    label("loc_1B9")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        "\x07\x05There's no one to show the photograph to nearby.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    label("loc_20F")

    OP_0D()
    ClearMapFlags(0x80)
    Return()

    # Function_0_AA end

    def Function_1_216(): pass

    label("Function_1_216")

    TalkBegin(0x1B)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 2)), scpexpr(EXPR_END)), "loc_264")

    ChrTalk(    #2
        0x1B,
        "Sorry, I don't recognize her.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x1B,
        "Try asking someone else.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2EC")

    label("loc_264")


    ChrTalk(    #4
        0x1B,
        "Looking for someone, you say?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x1B,
        "She's certainly a cute kid!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x1B,
        (
            "She lost her parents in the war?\x01",
            "Curse that damned thing...\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1A)

    label("loc_2EC")

    TalkEnd(0x1B)
    Return()

    # Function_1_216 end

    def Function_2_2F0(): pass

    label("Function_2_2F0")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_396")

    ChrTalk(    #7
        0x8,
        (
            "Those eyes... This is really bothering\x01",
            "me. They're so familiar.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x8,
        (
            "I swear someone with eyes like hers has\x01",
            "visited our establishment. But who...?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4E1")

    label("loc_396")


    ChrTalk(    #9
        0x8,
        (
            "So you're looking for the girl in\x01",
            "this photo, hmm?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x8,
        (
            "Well, I don't recall seeing her back\x01",
            "then during the war, but it's just...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x8,
        (
            "Those EYES. Those green eyes of hers,\x01",
            "they jump out at me, and I don't\x01",
            "just mean they're cute or something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x8,
        (
            "I swear someone with eyes like hers\x01",
            "has visited the Anterose. But who...?\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_4E1")

    TalkEnd(0x8)
    Return()

    # Function_2_2F0 end

    def Function_3_4E5(): pass

    label("Function_3_4E5")

    EventBegin(0x0)
    Fade(1000)
    OP_8C(0x20, 270, 0)
    SetChrPos(0x101, 1120, 0, 1500, 90)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF7)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_547")
    SetChrPos(0xF8, 1000, 0, 110, 32)
    SetChrPos(0xF7, 10, 0, 1520, 90)
    SetChrPos(0xF9, -120, 0, 490, 90)
    Jump("loc_600")

    label("loc_547")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_58A")
    SetChrPos(0xF7, 1000, 0, 110, 32)
    SetChrPos(0xF8, 10, 0, 1520, 90)
    SetChrPos(0xF9, -120, 0, 490, 90)
    Jump("loc_600")

    label("loc_58A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5CD")
    SetChrPos(0xF7, 1000, 0, 110, 32)
    SetChrPos(0xF9, 10, 0, 1520, 90)
    SetChrPos(0xF8, -120, 0, 490, 90)
    Jump("loc_600")

    label("loc_5CD")

    SetChrPos(0xF7, 1000, 0, 110, 32)
    SetChrPos(0xF8, -120, 0, 490, 90)
    SetChrPos(0xF9, 10, 0, 1520, 90)

    label("loc_600")

    OP_6D(780, 0, 1170, 0)
    OP_67(0, 6150, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    OP_0D()

    ChrTalk(    #13
        0x101,
        "#1011F#6PPardon, can I have a moment?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        "Of course, what is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x101,
        (
            "#1000F#6PAre you Corna?\x02\x03",

            "We're from the Bracer Guild.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xFE,
        "Oh, my, yes! Thank you for coming.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0xFE,
        (
            "I've been waiting.\x01",
            "This must be about my request.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x101,
        (
            "#1011F#6PNice to meet you, then!\x01",
            "I'm Estelle Bright, senior bracer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0xFE,
        "My apologies for calling on you like this...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xFE,
        (
            "But I fear I have no other resources\x01",
            "left to me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0xFE,
        (
            "This will take some time to explain...\x01",
            "Can you hear me out?\x02",
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
            "Yes\x01",      # 0
            "No\x01",       # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_885")

    ChrTalk(    #22
        0x101,
        "#1006F#6POf course! Go ahead.\x02",
    )

    CloseMessageWindow()
    Call(1, 5)
    Jump("loc_956")

    label("loc_885")


    ChrTalk(    #23
        0x101,
        (
            "#1007F#6PErm, sorry.\x02\x03",

            "I'm not sure we have the time right now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0xFE,
        "Ah. I see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0xFE,
        (
            "Well, um, if you find the time,\x01",
            "please come by again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0xFE,
        "I will be waiting here.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x101,
        "#1000F#6PWe'll be back!\x02",
    )

    CloseMessageWindow()
    OP_28(0x79, 0x1, 0x8000)

    label("loc_956")

    EventEnd(0x0)
    Return()

    # Function_3_4E5 end

    def Function_4_959(): pass

    label("Function_4_959")

    EventBegin(0x0)
    Fade(1000)
    OP_8C(0x20, 270, 0)
    SetChrPos(0x101, 1120, 0, 1500, 90)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF7)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9BB")
    SetChrPos(0xF8, 1000, 0, 110, 32)
    SetChrPos(0xF7, 10, 0, 1520, 90)
    SetChrPos(0xF9, -120, 0, 490, 90)
    Jump("loc_A74")

    label("loc_9BB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9FE")
    SetChrPos(0xF7, 1000, 0, 110, 32)
    SetChrPos(0xF8, 10, 0, 1520, 90)
    SetChrPos(0xF9, -120, 0, 490, 90)
    Jump("loc_A74")

    label("loc_9FE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A41")
    SetChrPos(0xF7, 1000, 0, 110, 32)
    SetChrPos(0xF9, 10, 0, 1520, 90)
    SetChrPos(0xF8, -120, 0, 490, 90)
    Jump("loc_A74")

    label("loc_A41")

    SetChrPos(0xF7, 1000, 0, 110, 32)
    SetChrPos(0xF8, -120, 0, 490, 90)
    SetChrPos(0xF9, 10, 0, 1520, 90)

    label("loc_A74")

    OP_6D(780, 0, 1170, 0)
    OP_67(0, 6150, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    OP_0D()

    ChrTalk(    #28
        0xFE,
        "Hello again.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xFE,
        "Do you have time to hear me out?\x02",
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
            "Yes\x01",      # 0
            "No\x01",       # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B5F")

    ChrTalk(    #30
        0x101,
        "#1006F#6PYeah, we're okay now.\x02",
    )

    CloseMessageWindow()
    Call(1, 5)
    Jump("loc_BF0")

    label("loc_B5F")


    ChrTalk(    #31
        0x101,
        (
            "#1007F#6PWe're, uh, kinda snowed under at the\x01",
            "moment. Sorry.\x02\x03",

            "I promise we'll be back as soon as our\x01",
            "other stuff is done.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xFE,
        "Please do...\x02",
    )

    CloseMessageWindow()

    label("loc_BF0")

    EventEnd(0x0)
    Return()

    # Function_4_959 end

    def Function_5_BF3(): pass

    label("Function_5_BF3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C73")

    ChrTalk(    #33
        0x103,
        (
            "#020FIf this will take a while, there's\x01",
            "no need to stand around here.\x02\x03",

            "Let's have a seat and talk.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 400)
    Jump("loc_E53")

    label("loc_C73")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_CD3")

    ChrTalk(    #34
        0x106,
        (
            "#050FNo need to stand around like this.\x02\x03",

            "How about we have a seat?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x106, 400)
    Jump("loc_E53")

    label("loc_CD3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D40")

    ChrTalk(    #35
        0x108,
        (
            "#070FStanding will just tire us, I think.\x02\x03",

            "Why not take a seat before we begin?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x108, 400)
    Jump("loc_E53")

    label("loc_D40")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_DE6")

    ChrTalk(    #36
        0x105,
        (
            "#040FRather than talk on our feet, why don't\x01",
            "we find a place to sit?\x02\x03",

            "If we speak here, we'll end up clogging\x01",
            "the restaurant a little...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 400)
    Jump("loc_E53")

    label("loc_DE6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E53")

    ChrTalk(    #37
        0x104,
        (
            "#030FAh, but let us not speak on our feet.\x02\x03",

            "Come, let us sit, and speak at length.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x104, 400)

    label("loc_E53")


    ChrTalk(    #38
        0x101,
        (
            "#1000FGood idea!\x02\x03",

            "Lemme see if I can claim us a table.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrFlags(0x38, 0x80)
    OP_4A(0x20, 255)
    SetChrChipByIndex(0x20, 6)
    SetChrFlags(0x20, 0x4)
    SetChrPos(0x20, 3800, 120, -3550, 0)
    OP_D2(0x270003, 0x270007, 0x24)
    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF7)"), scpexpr(EXPR_END)),
        (2, "loc_EED"),
        (3, "loc_EFA"),
        (4, "loc_F07"),
        (5, "loc_F14"),
        (6, "loc_F21"),
        (7, "loc_F2E"),
        (8, "loc_F3B"),
        (SWITCH_DEFAULT, "loc_F48"),
    )


    label("loc_EED")

    OP_D2(0x70023, 0x7002B, 0x25)
    Jump("loc_F48")

    label("loc_EFA")

    OP_D2(0x70033, 0x7003B, 0x25)
    Jump("loc_F48")

    label("loc_F07")

    OP_D2(0x70043, 0x7004B, 0x25)
    Jump("loc_F48")

    label("loc_F14")

    OP_D2(0x70053, 0x7005B, 0x25)
    Jump("loc_F48")

    label("loc_F21")

    OP_D2(0x70063, 0x7006B, 0x25)
    Jump("loc_F48")

    label("loc_F2E")

    OP_D2(0x70073, 0x7007B, 0x25)
    Jump("loc_F48")

    label("loc_F3B")

    OP_D2(0x270083, 0x270087, 0x25)
    Jump("loc_F48")

    label("loc_F48")

    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_END)),
        (2, "loc_F6D"),
        (3, "loc_F7A"),
        (4, "loc_F87"),
        (5, "loc_F94"),
        (6, "loc_FA1"),
        (7, "loc_FAE"),
        (8, "loc_FBB"),
        (SWITCH_DEFAULT, "loc_FC8"),
    )


    label("loc_F6D")

    OP_D2(0x70023, 0x7002B, 0x26)
    Jump("loc_FC8")

    label("loc_F7A")

    OP_D2(0x70033, 0x7003B, 0x26)
    Jump("loc_FC8")

    label("loc_F87")

    OP_D2(0x70043, 0x7004B, 0x26)
    Jump("loc_FC8")

    label("loc_F94")

    OP_D2(0x70053, 0x7005B, 0x26)
    Jump("loc_FC8")

    label("loc_FA1")

    OP_D2(0x70063, 0x7006B, 0x26)
    Jump("loc_FC8")

    label("loc_FAE")

    OP_D2(0x70073, 0x7007B, 0x26)
    Jump("loc_FC8")

    label("loc_FBB")

    OP_D2(0x270083, 0x270087, 0x26)
    Jump("loc_FC8")

    label("loc_FC8")

    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_END)),
        (2, "loc_FED"),
        (3, "loc_FFA"),
        (4, "loc_1007"),
        (5, "loc_1014"),
        (6, "loc_1021"),
        (7, "loc_102E"),
        (8, "loc_103B"),
        (SWITCH_DEFAULT, "loc_1048"),
    )


    label("loc_FED")

    OP_D2(0x70023, 0x7002B, 0x27)
    Jump("loc_1048")

    label("loc_FFA")

    OP_D2(0x70033, 0x7003B, 0x27)
    Jump("loc_1048")

    label("loc_1007")

    OP_D2(0x70043, 0x7004B, 0x27)
    Jump("loc_1048")

    label("loc_1014")

    OP_D2(0x70053, 0x7005B, 0x27)
    Jump("loc_1048")

    label("loc_1021")

    OP_D2(0x70063, 0x7006B, 0x27)
    Jump("loc_1048")

    label("loc_102E")

    OP_D2(0x70073, 0x7007B, 0x27)
    Jump("loc_1048")

    label("loc_103B")

    OP_D2(0x270083, 0x270087, 0x27)
    Jump("loc_1048")

    label("loc_1048")

    SetChrChipByIndex(0x101, 36)
    SetChrChipByIndex(0xF7, 37)
    SetChrChipByIndex(0xF8, 38)
    SetChrChipByIndex(0xF9, 39)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0xF7, 0x4)
    SetChrFlags(0xF8, 0x4)
    SetChrFlags(0xF9, 0x4)
    SetChrPos(0x101, 2760, 200, -2500, 90)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF7)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10AC")
    SetChrPos(0xF7, 5100, 100, -950, 270)
    RunExpression(0x7, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1156")

    label("loc_10AC")

    SetChrPos(0xF7, 5100, 200, -950, 270)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF7)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10D7")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1156")

    label("loc_10D7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF7)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10F1")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1156")

    label("loc_10F1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF7)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_110B")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1156")

    label("loc_110B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF7)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1125")
    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1156")

    label("loc_1125")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF7)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_113F")
    RunExpression(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1156")

    label("loc_113F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF7)"), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1156")
    RunExpression(0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1156")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1181")
    SetChrPos(0xF8, 5100, 100, -2550, 270)
    RunExpression(0x7, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_122B")

    label("loc_1181")

    SetChrPos(0xF8, 5100, 200, -2550, 270)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11AC")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_122B")

    label("loc_11AC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11C6")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_122B")

    label("loc_11C6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11E0")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_122B")

    label("loc_11E0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11FA")
    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_122B")

    label("loc_11FA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1214")
    RunExpression(0x6, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_122B")

    label("loc_1214")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_122B")
    RunExpression(0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_122B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1256")
    SetChrPos(0xF9, 2900, 100, -900, 90)
    RunExpression(0x7, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1300")

    label("loc_1256")

    SetChrPos(0xF9, 2900, 200, -900, 90)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1281")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1300")

    label("loc_1281")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_129B")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1300")

    label("loc_129B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12B5")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1300")

    label("loc_12B5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12CF")
    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1300")

    label("loc_12CF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12E9")
    RunExpression(0x6, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1300")

    label("loc_12E9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1300")
    RunExpression(0x8, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1300")

    OP_6D(3330, 0, -1410, 0)
    SetChrSubChip(0x101, 2)
    SetChrSubChip(0xF9, 2)
    SetChrSubChip(0xF7, 1)
    SetChrSubChip(0xF8, 1)
    FadeToBright(1000, 0)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_13BD")

    ChrTalk(    #39
        0x106,
        (
            "#050FSo from your posting, ma'am, you're\x01",
            "searching for someone, right?\x02\x03",

            "Something about a person missing for\x01",
            "ten years?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15DC")

    label("loc_13BD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1439")

    ChrTalk(    #40
        0x103,
        (
            "#022FSo, ma'am, you're searching for someone,\x01",
            "yes?\x02\x03",

            "Someone you haven't seen in...\x01",
            "ten years, was it?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15DC")

    label("loc_1439")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_14BB")

    ChrTalk(    #41
        0x108,
        (
            "#070FIf I recall your posting, ma'am, you are\x01",
            "searching for someone.\x02\x03",

            "Someone you haven't met in ten years.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15DC")

    label("loc_14BB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_154A")

    ChrTalk(    #42
        0x105,
        (
            "#043FSo we read your posting... You're\x01",
            "searching for someone, correct?\x02\x03",

            "Someone you haven't seen for nearly\x01",
            "ten years...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15DC")

    label("loc_154A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_15DC")

    ChrTalk(    #43
        0x109,
        (
            "#1063FSo, sorry to cut to the point, but\x01",
            "you're lookin' for someone, yeah?\x02\x03",

            "Someone you haven't seen in, like,\x01",
            "a decade or so.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15DC")


    ChrTalk(    #44
        0xFE,
        "Yes, I'm searching for my niece.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xFE,
        "Her name is Raini.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0xFE,
        (
            "If she's alive, she would be\x01",
            "about twenty now.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)
    OP_63(0x101)

    ChrTalk(    #47
        0x101,
        (
            "#1015F#6PWait, 'if she's alive'?\x01",
            "I don't quite--\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1701")

    ChrTalk(    #48
        0x106,
        (
            "#053FWait... Ten years ago.\x02\x03",

            "#552FI think I get what this is about now.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_188D")

    label("loc_1701")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1765")

    ChrTalk(    #49
        0x103,
        (
            "#026FAh, wait. 'Ten years ago.'\x02\x03",

            "#522FI think I can guess what this is about.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_188D")

    label("loc_1765")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_17E2")

    ChrTalk(    #50
        0x108,
        (
            "#074FTen years... yes, I see.\x02\x03",

            "#072FOnly one thing could have happened\x01",
            "ten years ago in such a case...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_188D")

    label("loc_17E2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_183D")

    ChrTalk(    #51
        0x104,
        (
            "#032FI believe I see.\x02\x03",

            "Ten years ago...\x01",
            "You can only mean one thing.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_188D")

    label("loc_183D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_188D")

    ChrTalk(    #52
        0x107,
        (
            "#065FOh, oh, no!\x02\x03",

            "But if she's been missing for ten years...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_188D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_18CE")

    ChrTalk(    #53
        0x109,
        (
            "#1065F...\x02\x03",

            "The Hundred Days War, isn't it?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_19AF")

    label("loc_18CE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1904")

    ChrTalk(    #54
        0x105,
        "#042FThe Hundred Days War, yes?\x02",
    )

    CloseMessageWindow()
    Jump("loc_19AF")

    label("loc_1904")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1943")

    ChrTalk(    #55
        0x107,
        "#063FThe... The Hundred Days War, right?\x02",
    )

    CloseMessageWindow()
    Jump("loc_19AF")

    label("loc_1943")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1981")

    ChrTalk(    #56
        0x104,
        "#032FThe Hundred Days War... Of course.\x02",
    )

    CloseMessageWindow()
    Jump("loc_19AF")

    label("loc_1981")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_19AF")

    ChrTalk(    #57
        0x108,
        "#072FThe Hundred Days War.\x02",
    )

    CloseMessageWindow()

    label("loc_19AF")


    ChrTalk(    #58
        0x101,
        "#1026F#6POh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0xFE,
        "Yes, exactly.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0xFE,
        (
            "When hostilities broke out, my sister\x01",
            "was staying in this city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0xFE,
        (
            "She wasn't able to get out before the\x01",
            "Imperial Army reached the city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0xFE,
        (
            "Thanks to an acquaintance of my sister's,\x01",
            "I soon learned of her and her husband's...\x01",
            "passing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0xFE,
        (
            "And while I never had word of exactly\x01",
            "what happened to Raini... Well, it was\x01",
            "easy to just assume.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0xFE,
        "It's been ten long years...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0xFE,
        (
            "I'd completely given up, assuming Raini\x01",
            "had long since joined the Goddess.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0xFE,
        "But very recently, I learned something new.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0xFE,
        (
            "A source told me that Raini had not only\x01",
            "survived, but had been adopted by\x01",
            "someone here in Bose.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #68
        0x101,
        "#1004F#6PSo then you think Raini's alive?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0xFE,
        (
            "Honestly? I don't know.\x01",
            "I barely dare to hope.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0xFE,
        (
            "And what's worse, my source was vague.\x01",
            "I have no idea WHO adopted her!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x101,
        "#1007F#6POof, that makes things harder.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0xFE,
        (
            "But...my heart tells me to believe.\x01",
            "To believe the sweet little girl my\x01",
            "sister loved is still alive.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0xFE,
        (
            "I must believe, which is why I beg you,\x01",
            "help me.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1EA3")

    ChrTalk(    #74
        0x106,
        (
            "#050FThink we can all understand where you're\x01",
            "coming from, ma'am.\x02\x03",

            "I definitely think it's worth investigating.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E72")
    SetChrSubChip(0x101, 1)
    SetChrSubChip(0xF8, 2)
    SetChrSubChip(0xF9, 0)
    Jump("loc_1EA0")

    label("loc_1E72")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E91")
    SetChrSubChip(0x101, 0)
    SetChrSubChip(0xF7, 1)
    SetChrSubChip(0xF9, 2)
    Jump("loc_1EA0")

    label("loc_1E91")

    SetChrSubChip(0x101, 1)
    SetChrSubChip(0xF7, 0)
    SetChrSubChip(0xF8, 2)

    label("loc_1EA0")

    Jump("loc_21A5")

    label("loc_1EA3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1F54")

    ChrTalk(    #75
        0x103,
        (
            "#022FWe understand, ma'am, don't worry.\x02\x03",

            "It's definitely worth investigating.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1F23")
    SetChrSubChip(0x101, 1)
    SetChrSubChip(0xF8, 2)
    SetChrSubChip(0xF9, 0)
    Jump("loc_1F51")

    label("loc_1F23")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1F42")
    SetChrSubChip(0x101, 0)
    SetChrSubChip(0xF7, 1)
    SetChrSubChip(0xF9, 2)
    Jump("loc_1F51")

    label("loc_1F42")

    SetChrSubChip(0x101, 1)
    SetChrSubChip(0xF7, 0)
    SetChrSubChip(0xF8, 2)

    label("loc_1F51")

    Jump("loc_21A5")

    label("loc_1F54")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_201E")

    ChrTalk(    #76
        0x108,
        (
            "#070FI don't think anyone here will doubt you, ma'am.\x02\x03",

            "This is certainly something worth looking into.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1FED")
    SetChrSubChip(0x101, 1)
    SetChrSubChip(0xF8, 2)
    SetChrSubChip(0xF9, 0)
    Jump("loc_201B")

    label("loc_1FED")

    Jc((scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_200C")
    SetChrSubChip(0x101, 0)
    SetChrSubChip(0xF7, 1)
    SetChrSubChip(0xF9, 2)
    Jump("loc_201B")

    label("loc_200C")

    SetChrSubChip(0x101, 1)
    SetChrSubChip(0xF7, 0)
    SetChrSubChip(0xF8, 2)

    label("loc_201B")

    Jump("loc_21A5")

    label("loc_201E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_20E2")

    ChrTalk(    #77
        0x104,
        (
            "#032FIt is a feeling anyone who has loved\x01",
            "would understand.\x02\x03",

            "This certainly bears investigation.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_20B1")
    SetChrSubChip(0x101, 1)
    SetChrSubChip(0xF8, 2)
    SetChrSubChip(0xF9, 0)
    Jump("loc_20DF")

    label("loc_20B1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_20D0")
    SetChrSubChip(0x101, 0)
    SetChrSubChip(0xF7, 1)
    SetChrSubChip(0xF9, 2)
    Jump("loc_20DF")

    label("loc_20D0")

    SetChrSubChip(0x101, 1)
    SetChrSubChip(0xF7, 0)
    SetChrSubChip(0xF8, 2)

    label("loc_20DF")

    Jump("loc_21A5")

    label("loc_20E2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_21A5")

    ChrTalk(    #78
        0x109,
        (
            "#1060FSometimes, the Goddess speaks to our\x01",
            "hearts, y'know?\x02\x03",

            "This is definitely worth checkin' out.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x8), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2177")
    SetChrSubChip(0x101, 1)
    SetChrSubChip(0xF8, 2)
    SetChrSubChip(0xF9, 0)
    Jump("loc_21A5")

    label("loc_2177")

    Jc((scpexpr(EXPR_GET_RESULT, 0x8), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2196")
    SetChrSubChip(0x101, 0)
    SetChrSubChip(0xF7, 1)
    SetChrSubChip(0xF9, 2)
    Jump("loc_21A5")

    label("loc_2196")

    SetChrSubChip(0x101, 1)
    SetChrSubChip(0xF7, 0)
    SetChrSubChip(0xF8, 2)

    label("loc_21A5")


    ChrTalk(    #79
        0x101,
        (
            "#1015F#6PWe don't have much in the way of clues,\x01",
            "though.\x02\x03",

            "All we have is a name and an age, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0xFE,
        "I do have a photograph of Raini, as well.\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 2)
    Sleep(50)
    SetChrSubChip(0xF7, 1)
    Sleep(50)
    SetChrSubChip(0xF9, 2)
    SetChrSubChip(0xF8, 1)

    ChrTalk(    #81
        0x101,
        "#1011F#6PA photo? That'd help!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0xFE,
        "Yes, it's not much, but...\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_AD(0x240092, 0x0, 0x0, 0x1F4)
    Sleep(1000)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_22F9")
    SetMessageWindowPos(50, 50, -1, -1)
    SetChrName("Tita")

    AnonymousTalk(    #83
        "#560FOooh, she's so cute!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Jump("loc_24B0")

    label("loc_22F9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2339")
    SetMessageWindowPos(50, 50, -1, -1)
    SetChrName("Kloe")

    AnonymousTalk(    #84
        "#048FHaha, she's adorable.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Jump("loc_24B0")

    label("loc_2339")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2395")
    SetMessageWindowPos(50, 50, -1, -1)
    SetChrName("Scherazard")

    AnonymousTalk(    #85
        "#526FOh, my goodness, there goes my blood sugar.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Jump("loc_24B0")

    label("loc_2395")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_247B")
    SetMessageWindowPos(50, 50, -1, -1)
    SetChrName("Olivier")

    AnonymousTalk(    #86
        (
            "#033FOhhh, impressive indeed.\x02\x03",

            "#037FHeheh. I cannot wait to find her today.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(50, 340, -1, -1)
    SetChrName("Estelle")

    AnonymousTalk(    #87
        (
            "#1019FAnd what, EXACTLY, is that supposed to mean?\x02\x03",

            "#1000FShe IS really cute here, though.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Jump("loc_24B0")

    label("loc_247B")

    SetMessageWindowPos(50, 50, -1, -1)
    SetChrName("Estelle")

    AnonymousTalk(    #88
        "#1018FHaha, she's so cute! ㈱\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_24B0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_250E")
    SetMessageWindowPos(360, 340, -1, -1)
    SetChrName("Kevin")

    AnonymousTalk(    #89
        (
            "#1062FHaha! Seriously!\x02\x03",

            "So she'd be, what, ten in this?\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Jump("loc_26CB")

    label("loc_250E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2565")
    SetMessageWindowPos(360, 340, -1, -1)
    SetChrName("Zin")

    AnonymousTalk(    #90
        (
            "#070FHah, quite!\x02\x03",

            "I assume this is her at age ten?\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Jump("loc_26CB")

    label("loc_2565")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_25CA")
    SetMessageWindowPos(360, 340, -1, -1)
    SetChrName("Agate")

    AnonymousTalk(    #91
        (
            "#051FYeah, no kiddin'.\x02\x03",

            "She's, what, ten in this photo, right?\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Jump("loc_26CB")

    label("loc_25CA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2636")
    SetMessageWindowPos(360, 340, -1, -1)
    SetChrName("Olivier")

    AnonymousTalk(    #92
        (
            "#037FAh! She warms the heart.\x02\x03",

            "She would be ten in this photo, yes?\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Jump("loc_26CB")

    label("loc_2636")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_26CB")
    SetMessageWindowPos(360, 50, -1, -1)
    SetChrName("Scherazard")

    ChrTalk(    #93
        0x103,
        (
            "#021FYes, I may need to avoid sugar for\x01",
            "a little while after this.\x02\x03",

            "She would be...ten in this photo, yes?\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_26CB")

    SetMessageWindowPos(50, 340, -1, -1)
    SetChrName("Corna")

    AnonymousTalk(    #94
        "Yes, it was taken right on her tenth birthday.\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(50, 340, -1, -1)
    SetChrName("Corna")

    AnonymousTalk(    #95
        "Just before her family left on holiday.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_AE(0x1F4)
    FadeToBright(300, 0)

    ChrTalk(    #96
        0x101,
        "#1026F#6P...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_27DC")
    Jc((scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2796")
    SetChrSubChip(0x107, 1)
    Jump("loc_27B0")

    label("loc_2796")

    Jc((scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_27AB")
    SetChrSubChip(0x107, 0)
    Jump("loc_27B0")

    label("loc_27AB")

    SetChrSubChip(0x107, 2)

    label("loc_27B0")


    ChrTalk(    #97
        0x107,
        (
            "#064FHuuuh?\x02\x03",

            "Estelle, what's wrong?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_29B0")

    label("loc_27DC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_284B")
    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_27FF")
    SetChrSubChip(0x105, 1)
    Jump("loc_2819")

    label("loc_27FF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2814")
    SetChrSubChip(0x105, 0)
    Jump("loc_2819")

    label("loc_2814")

    SetChrSubChip(0x105, 2)

    label("loc_2819")


    ChrTalk(    #98
        0x105,
        "#043FEstelle, is something bothering you?\x02",
    )

    CloseMessageWindow()
    Jump("loc_29B0")

    label("loc_284B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_28C8")
    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_286E")
    SetChrSubChip(0x104, 1)
    Jump("loc_2888")

    label("loc_286E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2883")
    SetChrSubChip(0x104, 0)
    Jump("loc_2888")

    label("loc_2883")

    SetChrSubChip(0x104, 2)

    label("loc_2888")


    ChrTalk(    #99
        0x104,
        (
            "#033FEstelle, you seem distracted.\x02\x03",

            "Is something amiss?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_29B0")

    label("loc_28C8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2933")
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_28EB")
    SetChrSubChip(0x103, 1)
    Jump("loc_2905")

    label("loc_28EB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2900")
    SetChrSubChip(0x103, 0)
    Jump("loc_2905")

    label("loc_2900")

    SetChrSubChip(0x103, 2)

    label("loc_2905")


    ChrTalk(    #100
        0x103,
        (
            "#023FMm?\x02\x03",

            "Estelle, are you all right?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_29B0")

    label("loc_2933")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_29B0")
    Jc((scpexpr(EXPR_GET_RESULT, 0x8), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2956")
    SetChrSubChip(0x109, 1)
    Jump("loc_2970")

    label("loc_2956")

    Jc((scpexpr(EXPR_GET_RESULT, 0x8), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_296B")
    SetChrSubChip(0x109, 0)
    Jump("loc_2970")

    label("loc_296B")

    SetChrSubChip(0x109, 2)

    label("loc_2970")


    ChrTalk(    #101
        0x109,
        (
            "#1063FEh?\x02\x03",

            "Estelle, you okay?\x01",
            "Lookin' kinda shaken, there.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_29B0")

    SetChrSubChip(0xF7, 1)
    SetChrSubChip(0xF8, 0)
    SetChrSubChip(0xF9, 2)
    SetChrSubChip(0x101, 0)

    ChrTalk(    #102
        0x101,
        (
            "#1025F#6POh, uh, it's nothing, really.\x01",
            "I was just kinda...mad, I guess.\x02\x03",

            "An innocent kid like that, caught up\x01",
            "in that stupid war...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2BD7")
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2A70")
    SetChrSubChip(0x106, 1)
    Jump("loc_2A8A")

    label("loc_2A70")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2A85")
    SetChrSubChip(0x106, 0)
    Jump("loc_2A8A")

    label("loc_2A85")

    SetChrSubChip(0x106, 2)

    label("loc_2A8A")


    ChrTalk(    #103
        0x106,
        (
            "#552FYeah... Know what you mean, Estelle.\x02\x03",

            "#053FWhich is why it's our duty to reunite\x01",
            "this girl with her family.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B15")
    SetChrSubChip(0x101, 1)
    Jump("loc_2B2F")

    label("loc_2B15")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B2A")
    SetChrSubChip(0x101, 0)
    Jump("loc_2B2F")

    label("loc_2B2A")

    SetChrSubChip(0x101, 1)

    label("loc_2B2F")


    ChrTalk(    #104
        0x101,
        (
            "#1025F#6PAh...\x02\x03",

            "#1006FYeah... yeah!\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 2)
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B72")
    SetChrSubChip(0x106, 1)
    Jump("loc_2B8C")

    label("loc_2B72")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B87")
    SetChrSubChip(0x106, 1)
    Jump("loc_2B8C")

    label("loc_2B87")

    SetChrSubChip(0x106, 2)

    label("loc_2B8C")


    ChrTalk(    #105
        0x106,
        (
            "#051FWe'd like to borrow the photograph,\x01",
            "if you don't mind, ma'am.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3297")

    label("loc_2BD7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2D3A")
    Jc((scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2BFA")
    SetChrSubChip(0x108, 1)
    Jump("loc_2C14")

    label("loc_2BFA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2C0F")
    SetChrSubChip(0x108, 0)
    Jump("loc_2C14")

    label("loc_2C0F")

    SetChrSubChip(0x108, 2)

    label("loc_2C14")


    ChrTalk(    #106
        0x108,
        (
            "#074FIt IS hard to find the words.\x02\x03",

            "#070FIt falls to us, then, to make it right.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2C7F")
    SetChrSubChip(0x101, 1)
    Jump("loc_2C99")

    label("loc_2C7F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2C94")
    SetChrSubChip(0x101, 0)
    Jump("loc_2C99")

    label("loc_2C94")

    SetChrSubChip(0x101, 1)

    label("loc_2C99")


    ChrTalk(    #107
        0x101,
        (
            "#1011F#6PAh...\x02\x03",

            "#1006FYeah... yeah!\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 2)
    Jc((scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2CDC")
    SetChrSubChip(0x108, 1)
    Jump("loc_2CF6")

    label("loc_2CDC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2CF1")
    SetChrSubChip(0x108, 1)
    Jump("loc_2CF6")

    label("loc_2CF1")

    SetChrSubChip(0x108, 2)

    label("loc_2CF6")


    ChrTalk(    #108
        0x108,
        (
            "#070FMa'am, we will take the photograph,\x01",
            "if you don't mind.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3297")

    label("loc_2D3A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2EB5")
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2D5D")
    SetChrSubChip(0x103, 1)
    Jump("loc_2D77")

    label("loc_2D5D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2D72")
    SetChrSubChip(0x103, 0)
    Jump("loc_2D77")

    label("loc_2D72")

    SetChrSubChip(0x103, 2)

    label("loc_2D77")


    ChrTalk(    #109
        0x103,
        (
            "#522FIt is a story too many of us know too well.\x02\x03",

            "#020FWe must find this girl and return her\x01",
            "to her family. Right, Estelle?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2E0D")
    SetChrSubChip(0x101, 1)
    Jump("loc_2E27")

    label("loc_2E0D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2E22")
    SetChrSubChip(0x101, 0)
    Jump("loc_2E27")

    label("loc_2E22")

    SetChrSubChip(0x101, 1)

    label("loc_2E27")


    ChrTalk(    #110
        0x101,
        (
            "#1011F#6PAh...\x02\x03",

            "#1006FYeah... yeah!\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 2)
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2E6A")
    SetChrSubChip(0x103, 1)
    Jump("loc_2E84")

    label("loc_2E6A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2E7F")
    SetChrSubChip(0x103, 1)
    Jump("loc_2E84")

    label("loc_2E7F")

    SetChrSubChip(0x103, 2)

    label("loc_2E84")


    ChrTalk(    #111
        0x103,
        "#020FCorna, may we take this photograph?\x02",
    )

    CloseMessageWindow()
    Jump("loc_3297")

    label("loc_2EB5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_30AE")
    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2ED8")
    SetChrSubChip(0x104, 1)
    Jump("loc_2EF2")

    label("loc_2ED8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2EED")
    SetChrSubChip(0x104, 0)
    Jump("loc_2EF2")

    label("loc_2EED")

    SetChrSubChip(0x104, 2)

    label("loc_2EF2")


    ChrTalk(    #112
        0x104,
        (
            "#035FMmm. Finding words for such injustice...\x01",
            "One never feels adequate to the task.\x02\x03",

            "As a citizen of the Empire, I feel I bear\x01",
            "some responsibility for this tragedy...\x02\x03",

            "#030FSo let us conduct our own campaign\x01",
            "to locate this lost child, hmm?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2FFC")
    SetChrSubChip(0x101, 1)
    Jump("loc_3016")

    label("loc_2FFC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3011")
    SetChrSubChip(0x101, 0)
    Jump("loc_3016")

    label("loc_3011")

    SetChrSubChip(0x101, 1)

    label("loc_3016")


    ChrTalk(    #113
        0x101,
        (
            "#1011F#6PAh...\x02\x03",

            "#1006FYeah, definitely.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 2)
    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_305D")
    SetChrSubChip(0x104, 1)
    Jump("loc_3077")

    label("loc_305D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3072")
    SetChrSubChip(0x104, 1)
    Jump("loc_3077")

    label("loc_3072")

    SetChrSubChip(0x104, 2)

    label("loc_3077")


    ChrTalk(    #114
        0x104,
        "#030FMy lady, may we take this memory with us?\x02",
    )

    CloseMessageWindow()
    Jump("loc_3297")

    label("loc_30AE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3297")
    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_30D1")
    SetChrSubChip(0x105, 1)
    Jump("loc_30EB")

    label("loc_30D1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_30E6")
    SetChrSubChip(0x105, 0)
    Jump("loc_30EB")

    label("loc_30E6")

    SetChrSubChip(0x105, 2)

    label("loc_30EB")


    ChrTalk(    #115
        0x105,
        (
            "#049FIt is hard to find the words, isn't it?\x01",
            "One war caused so much suffering...\x02\x03",

            "#047FBut I'm sure it is Aidios' guidance that\x01",
            "put us on this trail...\x02\x03",

            "#040FI want to help this girl find her family again.\x01",
            "No matter what. Right, Estelle?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_31F3")
    SetChrSubChip(0x101, 1)
    Jump("loc_320D")

    label("loc_31F3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3208")
    SetChrSubChip(0x101, 0)
    Jump("loc_320D")

    label("loc_3208")

    SetChrSubChip(0x101, 1)

    label("loc_320D")


    ChrTalk(    #116
        0x101,
        (
            "#1011F#6PKloe...\x02\x03",

            "#1006FYeah, definitely.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 2)
    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3256")
    SetChrSubChip(0x105, 1)
    Jump("loc_3270")

    label("loc_3256")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_326B")
    SetChrSubChip(0x105, 1)
    Jump("loc_3270")

    label("loc_326B")

    SetChrSubChip(0x105, 2)

    label("loc_3270")


    ChrTalk(    #117
        0x105,
        "#040FMay we take this photograph?\x02",
    )

    CloseMessageWindow()

    label("loc_3297")


    ChrTalk(    #118
        0xFE,
        "Please, by all means.\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #119
        "\x07\x00Received #897i.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x381, 1)
    SetChrSubChip(0x101, 0)

    ChrTalk(    #120
        0x101,
        (
            "#1015F#6PWell, we know what she looks\x01",
            "like now, but...\x02\x03",

            "How are we actually gonna do this?\x01",
            "Raini could be anywhere.\x01",
            "She might not even be IN Bose anymore!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_347F")
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_33C2")
    SetChrSubChip(0x103, 1)
    Jump("loc_33DC")

    label("loc_33C2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_33D7")
    SetChrSubChip(0x103, 0)
    Jump("loc_33DC")

    label("loc_33D7")

    SetChrSubChip(0x103, 2)

    label("loc_33DC")


    ChrTalk(    #121
        0x103,
        (
            "#020FWe do have the photograph. It's very possible\x01",
            "someone will remember her.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_344E")
    SetChrSubChip(0x101, 1)
    SetChrSubChip(0xF8, 2)
    SetChrSubChip(0xF9, 0)
    Jump("loc_347C")

    label("loc_344E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_346D")
    SetChrSubChip(0x101, 0)
    SetChrSubChip(0xF7, 1)
    SetChrSubChip(0xF9, 2)
    Jump("loc_347C")

    label("loc_346D")

    SetChrSubChip(0x101, 1)
    SetChrSubChip(0xF7, 0)
    SetChrSubChip(0xF8, 2)

    label("loc_347C")

    Jump("loc_3875")

    label("loc_347F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3582")
    Jc((scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_34A2")
    SetChrSubChip(0x108, 1)
    Jump("loc_34BC")

    label("loc_34A2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_34B7")
    SetChrSubChip(0x108, 0)
    Jump("loc_34BC")

    label("loc_34B7")

    SetChrSubChip(0x108, 2)

    label("loc_34BC")


    ChrTalk(    #122
        0x108,
        (
            "#070FHmm. We do, at least, have the photograph.\x02\x03",

            "Someone may recognize her from that time.\x01",
            "We should ask around.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3551")
    SetChrSubChip(0x101, 1)
    SetChrSubChip(0xF8, 2)
    SetChrSubChip(0xF9, 0)
    Jump("loc_357F")

    label("loc_3551")

    Jc((scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3570")
    SetChrSubChip(0x101, 0)
    SetChrSubChip(0xF7, 1)
    SetChrSubChip(0xF9, 2)
    Jump("loc_357F")

    label("loc_3570")

    SetChrSubChip(0x101, 1)
    SetChrSubChip(0xF7, 0)
    SetChrSubChip(0xF8, 2)

    label("loc_357F")

    Jump("loc_3875")

    label("loc_3582")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3686")
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_35A5")
    SetChrSubChip(0x106, 1)
    Jump("loc_35BF")

    label("loc_35A5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_35BA")
    SetChrSubChip(0x106, 0)
    Jump("loc_35BF")

    label("loc_35BA")

    SetChrSubChip(0x106, 2)

    label("loc_35BF")


    ChrTalk(    #123
        0x106,
        (
            "#050FIf nothin' else, we do have that photo.\x01",
            "We can show it around and see if anyone\x01",
            "remembers or recognizes her.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3655")
    SetChrSubChip(0x101, 1)
    SetChrSubChip(0xF8, 2)
    SetChrSubChip(0xF9, 0)
    Jump("loc_3683")

    label("loc_3655")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3674")
    SetChrSubChip(0x101, 0)
    SetChrSubChip(0xF7, 1)
    SetChrSubChip(0xF9, 2)
    Jump("loc_3683")

    label("loc_3674")

    SetChrSubChip(0x101, 1)
    SetChrSubChip(0xF7, 0)
    SetChrSubChip(0xF8, 2)

    label("loc_3683")

    Jump("loc_3875")

    label("loc_3686")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3778")
    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_36A9")
    SetChrSubChip(0x104, 1)
    Jump("loc_36C3")

    label("loc_36A9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_36BE")
    SetChrSubChip(0x104, 0)
    Jump("loc_36C3")

    label("loc_36BE")

    SetChrSubChip(0x104, 2)

    label("loc_36C3")


    ChrTalk(    #124
        0x104,
        (
            "#030FWe do have a memory, saved to paper.\x02\x03",

            "Perhaps we can use it to jog the\x01",
            "memories of others.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3747")
    SetChrSubChip(0x101, 1)
    SetChrSubChip(0xF8, 2)
    SetChrSubChip(0xF9, 0)
    Jump("loc_3775")

    label("loc_3747")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3766")
    SetChrSubChip(0x101, 0)
    SetChrSubChip(0xF7, 1)
    SetChrSubChip(0xF9, 2)
    Jump("loc_3775")

    label("loc_3766")

    SetChrSubChip(0x101, 1)
    SetChrSubChip(0xF7, 0)
    SetChrSubChip(0xF8, 2)

    label("loc_3775")

    Jump("loc_3875")

    label("loc_3778")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3875")
    Jc((scpexpr(EXPR_GET_RESULT, 0x8), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_379B")
    SetChrSubChip(0x109, 1)
    Jump("loc_37B5")

    label("loc_379B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x8), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_37B0")
    SetChrSubChip(0x109, 0)
    Jump("loc_37B5")

    label("loc_37B0")

    SetChrSubChip(0x109, 2)

    label("loc_37B5")


    ChrTalk(    #125
        0x109,
        (
            "#1067FMmm, good point.\x02\x03",

            "#1062FWe got the photo, at least. We can show\x01",
            "it around, see if anyone remembers her.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x8), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3847")
    SetChrSubChip(0x101, 1)
    SetChrSubChip(0xF8, 2)
    SetChrSubChip(0xF9, 0)
    Jump("loc_3875")

    label("loc_3847")

    Jc((scpexpr(EXPR_GET_RESULT, 0x8), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3866")
    SetChrSubChip(0x101, 0)
    SetChrSubChip(0xF7, 1)
    SetChrSubChip(0xF9, 2)
    Jump("loc_3875")

    label("loc_3866")

    SetChrSubChip(0x101, 1)
    SetChrSubChip(0xF7, 0)
    SetChrSubChip(0xF8, 2)

    label("loc_3875")


    ChrTalk(    #126
        0x101,
        "#1004F#6PDo you think that'll work?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_394D")

    ChrTalk(    #127
        0x103,
        (
            "#020FWell, it has only been ten years.\x02\x03",

            "Even if no one remembers exactly what\x01",
            "happened to her, there's a fair chance\x01",
            "someone will at least remember her.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C4D")

    label("loc_394D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_39EC")

    ChrTalk(    #128
        0x108,
        (
            "#070FIn a way, ten years is not that long.\x02\x03",

            "Someone should at least remember her, even if\x01",
            "they do not know precisely what became of her.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C4D")

    label("loc_39EC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3A9E")

    ChrTalk(    #129
        0x106,
        (
            "#050FYeah, should. I mean, in some ways\x01",
            "ten years ain't THAT long.\x02\x03",

            "Even if they don't remember exactly where\x01",
            "she is, they'll at least remember WHO she is.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C4D")

    label("loc_3A9E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3B7B")

    ChrTalk(    #130
        0x104,
        (
            "#030FTen years is a shorter span in the gulf\x01",
            "of time than one may think.\x02\x03",

            "Even if we do not find someone who remembers\x01",
            "everything that happened to her, we will likely\x01",
            "find someone who remembers her.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C4D")

    label("loc_3B7B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3C4D")

    ChrTalk(    #131
        0x109,
        (
            "#1060FAin't a bad place to start. I mean, people's\x01",
            "memories don't fade THAT much in ten years.\x02\x03",

            "Even if we don't find her immediately,\x01",
            "I bet we can find someone who at least\x01",
            "remembers Raini.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3C4D")


    ChrTalk(    #132
        0x101,
        (
            "#1006F#6PIt is our best shot, I guess.\x02\x03",

            "Let's start asking around, then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0xFE,
        "Please, you are my only hope.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0xFE,
        (
            "If you find anything out,\x01",
            "come by here again.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 2)
    SetChrSubChip(0xF7, 1)
    Sleep(40)
    SetChrSubChip(0xF9, 2)
    SetChrSubChip(0xF8, 1)

    ChrTalk(    #135
        0x101,
        "#1000F#6PWe will!\x02",
    )

    CloseMessageWindow()
    OP_28(0x79, 0x4, 0x8)
    OP_28(0x79, 0x4, 0x4)
    OP_28(0x79, 0x1, 0x1)
    OP_28(0x79, 0x1, 0x2)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrChipByIndex(0x20, 20)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0xF7, 65535)
    SetChrChipByIndex(0xF8, 65535)
    SetChrChipByIndex(0xF9, 65535)
    ClearChrFlags(0x20, 0x4)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0xF7, 0x4)
    ClearChrFlags(0xF8, 0x4)
    ClearChrFlags(0xF9, 0x4)
    SetChrPos(0x20, 2400, 0, 1370, 0)
    OP_4B(0x20, 255)
    SetChrPos(0x101, 360, 0, -2430, 180)
    SetChrPos(0xF7, 360, 0, -2430, 180)
    SetChrPos(0xF8, 360, 0, -2430, 180)
    SetChrPos(0xF9, 360, 0, -2430, 180)
    OP_69(0x101, 0x0)
    OP_30(0x0)
    OP_8C(0x101, 180, 0)
    OP_8C(0xF7, 180, 0)
    OP_8C(0xF8, 180, 0)
    OP_8C(0xF9, 180, 0)
    OP_4A(0x0, 255)
    OP_4A(0x1, 255)
    OP_4A(0x2, 255)
    OP_4A(0x3, 255)
    ClearChrFlags(0x38, 0x80)
    FadeToBright(1000, 0)
    OP_0D()
    Return()

    # Function_5_BF3 end

    def Function_6_3E12(): pass

    label("Function_6_3E12")

    EventBegin(0x0)
    ClearChrFlags(0x27, 0x80)
    ClearChrFlags(0x26, 0x80)
    SetChrPos(0x20, -230, 0, -650, 180)
    SetChrPos(0x27, -230, 0, -1730, 0)
    SetChrPos(0x26, -1280, 0, -2300, 0)
    OP_4A(0x20, 255)
    SetChrPos(0x101, 1710, 0, 0, 270)
    SetChrPos(0xF7, 2009, 0, -1460, 270)
    SetChrPos(0xF8, 2210, 0, -3180, 315)
    SetChrPos(0xF9, 2600, 0, -230, 270)
    SetChrFlags(0x1C, 0x80)
    SetChrFlags(0x38, 0x80)
    OP_4A(0x1B, 255)
    OP_6D(-1220, 0, -240, 0)
    OP_67(0, 4240, -10000, 0)
    OP_6B(2680, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    OP_0D()

    ChrTalk(    #136
        0x20,
        "#2PI see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0x20,
        "#2PTo think things got so complicated...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0x20,
        (
            "#2PRaini... I'm so, so sorry we didn't\x01",
            "come looking for you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0x20,
        "#2PI wish we could have found you sooner.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0x27,
        (
            "#621F#3PNo, Auntie, don't apologize.\x02\x03",

            "It wasn't anyone's fault, except maybe\x01",
            "that of the times.\x02\x03",

            "And over the last ten years...\x02\x03",

            "I can honestly say I've been very happy.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x20, 0x26, 400)

    ChrTalk(    #141
        0x20,
        "#2PMiss Maybelle... Thank you, so very much!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0x20,
        (
            "#2PI owe you and your father a debt that\x01",
            "can never be repaid!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x26, 0x20, 400)

    ChrTalk(    #143
        0x26,
        (
            "#610F#3PNo, not at all.\x02\x03",

            "If anything, I should be grateful to you,\x01",
            "and your sister and her husband.\x02\x03",

            "Lila has been such an important part\x01",
            "of my life...\x02\x03",

            "#615FEr, ahem! I should say Raini.\x01",
            "I'm sorry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0x20,
        "#2PNo, please, call her as you have.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0x20,
        (
            "#2PThat is the name she has here,\x01",
            "after all.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x20, 0x27, 400)

    ChrTalk(    #146
        0x20,
        (
            "#2PI am just glad to know she has been\x01",
            "safe and happy...no matter her name.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0x20,
        "#2PMiss Maybelle, I beg you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0x20,
        "#2PPlease continue to take care of her.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0x26,
        (
            "#613F#3PEr, well. I would certainly love for her\x01",
            "to remain with us, but...\x02\x03",

            "Do you not intend to take her home with you?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x20, 0x26, 400)

    ChrTalk(    #150
        0x20,
        (
            "#2POh, I planned to at first, of course.\x01",
            "But...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #151
        0x20,
        "#2PSeeing her now... I couldn't be so cruel.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #152
        0x20,
        (
            "#2PTo continue living here, with the people\x01",
            "she loves and all her friends...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0x20,
        (
            "#2PNo one who loves her could take that\x01",
            "away from her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #154
        0x27,
        "#625F#3PAuntie Corna...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x20, 0x27, 400)

    ChrTalk(    #155
        0x20,
        (
            "#2PNow, now, dumpling. Don't make\x01",
            "that face.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #156
        0x20,
        (
            "#2POf course, I do hope you'll visit your\x01",
            "uncle and me every once in a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #157
        0x20,
        (
            "#2PI know the distance will make it\x01",
            "difficult, but we would both love it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #158
        0x26,
        "#610F#3PWhy would distance be an issue?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x20, 0x26, 400)

    ChrTalk(    #159
        0x20,
        (
            "#2PAh, I didn't mention, but our home is\x01",
            "quite far away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #160
        0x20,
        (
            "#2PYou know where the Leman State is,\x01",
            "I take it?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #161
        0x101,
        (
            "#1004F#4PThe Leman State?\x01",
            "Of course I've heard of it!\x02\x03",

            "That's where the guild has its training\x01",
            "ground and headquarters!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_468A")

    ChrTalk(    #162
        0x106,
        "#051FYeah, think most bracers know about it.\x02",
    )

    CloseMessageWindow()
    Jump("loc_478E")

    label("loc_468A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_46C9")

    ChrTalk(    #163
        0x103,
        "#020FMost bracers have heard of it, yes.\x02",
    )

    CloseMessageWindow()
    Jump("loc_478E")

    label("loc_46C9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_470E")

    ChrTalk(    #164
        0x108,
        "#070FAny bracer worth his salt knows about it.\x02",
    )

    CloseMessageWindow()
    Jump("loc_478E")

    label("loc_470E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4751")

    ChrTalk(    #165
        0x104,
        "#030FI should think bracers know of it, yes.\x02",
    )

    CloseMessageWindow()
    Jump("loc_478E")

    label("loc_4751")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_478E")

    ChrTalk(    #166
        0x105,
        "#040FI've heard of it as well, of course.\x02",
    )

    CloseMessageWindow()

    label("loc_478E")


    ChrTalk(    #167
        0x101,
        (
            "#1015F#4PI see, so Lila's not from Liberl!\x02\x03",

            "(That does sort of explain the kinda unique\x01",
            "feeling she's always given off.)\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x20, 0x27, 400)

    ChrTalk(    #168
        0x20,
        "#2PEven by airship, it is quite a trip.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #169
        0x20,
        "#2PI do hope you will come and visit some day.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #170
        0x20,
        "#2PBut even then, I will still keep in touch.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #171
        0x27,
        (
            "#621F#3PI will too.\x02\x03",

            "And I promise I'll find time to visit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #172
        0x20,
        "#2PI'll be counting the days until then.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #173
        0x20,
        "#2PNow, Raini...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #174
        0x20,
        "#2PLet me get another good look at you.\x02",
    )

    CloseMessageWindow()
    OP_94(0x1, 0x20, 0x0, 0xC8, 0x3E8, 0x0)
    Sleep(1000)

    ChrTalk(    #175
        0x20,
        (
            "#2PAh, you really are the image of your\x01",
            "mother...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x27, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #176
        0x27,
        "#622F#3PI look like...Mother?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #177
        0x20,
        (
            "#2PThat you do. Not just in appearance,\x01",
            "but even in the way you move, your\x01",
            "speech...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #178
        0x20,
        (
            "#2PYou really are so like your mother\x01",
            "when she was your age.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #179
        0x27,
        "#623F#3P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #180
        0x20,
        "#2PI'm sure she has been watching over you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #181
        0x20,
        (
            "#2PYour wonderful new friends and family...\x01",
            "it's what she would have wanted.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #182
        0x20,
        (
            "#2PLive happily, my Raini...\x01",
            "for your mother's sake as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #183
        0x27,
        (
            "#626F#3PI will, Auntie...\x02\x03",

            "I promise I will.\x02",
        )
    )

    CloseMessageWindow()
    OP_3F(0x381, 1)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(1500)
    OP_3F(0x381, 1)
    OP_3E(0x41B, 1)
    OP_22(0x17, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #184
        "Quest #2C[Memories of a Distant Day] #0Ccompleted!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_28(0x79, 0x4, 0x10)
    OP_28(0x79, 0x1, 0x40)
    ClearMapFlags(0x2000000)
    OP_A2(0x10F2)
    NewScene("ED6_DT21/T1101   ._SN", 111, 0, 0)
    IdleLoop()
    Return()

    # Function_6_3E12 end

    def Function_7_4C14(): pass

    label("Function_7_4C14")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CD(0x13)"), scpexpr(EXPR_END)), "loc_4C24")
    OP_A2(0xF)
    Jump("loc_4C2F")

    label("loc_4C24")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CD(0x14)"), scpexpr(EXPR_END)), "loc_4C2F")
    OP_A3(0xF)

    label("loc_4C2F")

    ClearChrFlags(0x13, 0x10)
    ClearChrFlags(0x14, 0x10)
    OP_4A(0x13, 255)
    OP_4A(0x14, 255)
    Fade(1000)
    SetChrPos(0x106, -45770, 0, -2880, 270)
    SetChrPos(0x101, -45760, 0, -1750, 270)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4C9A")
    SetChrPos(0x105, -44380, 0, -1770, 270)
    SetChrPos(0xF9, -44510, 0, -2770, 270)
    Jump("loc_4CEE")

    label("loc_4C9A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4CCC")
    SetChrPos(0x105, -44380, 0, -1770, 270)
    SetChrPos(0xF8, -44510, 0, -2770, 270)
    Jump("loc_4CEE")

    label("loc_4CCC")

    SetChrPos(0xF8, -44380, 0, -1770, 270)
    SetChrPos(0xF9, -44510, 0, -2770, 270)

    label("loc_4CEE")

    SetChrFlags(0xC, 0x80)
    OP_6D(-46730, 0, -2460, 0)
    OP_67(0, 6760, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_END)), "loc_4E0A")

    ChrTalk(    #185
        0x13,
        (
            "#4PBuy some time, somehow.\x01",
            "Stall them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #186
        0x13,
        "#4PI've already taken action on my end.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #187
        0x101,
        "#1011FUm, excuse me!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x13, 0x101, 400)
    TurnDirection(0x14, 0x101, 400)

    ChrTalk(    #188
        0x13,
        "What is it? My time is--\x02",
    )

    CloseMessageWindow()
    OP_62(0x13, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(    #189
        0x13,
        "Oh! Wait, you're...\x02",
    )

    CloseMessageWindow()
    Jump("loc_4F1D")

    label("loc_4E0A")


    ChrTalk(    #190
        0x14,
        (
            "If we do not find the mistress,\x01",
            "it will all be for naught.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #191
        0x14,
        "We must do something soon...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #192
        0x101,
        "#1011FUm, excuse me!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x14, 0x101, 400)

    ChrTalk(    #193
        0x14,
        "Yes? Who might you be?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #194
        0x101,
        (
            "#1000FSorry to interrupt!\x02\x03",

            "We're from the Bracer Guild.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x13, 0x101, 400)
    OP_62(0x13, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(    #195
        0x13,
        "Oh! Wait, you're...\x02",
    )

    CloseMessageWindow()

    label("loc_4F1D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x34A, 4)), scpexpr(EXPR_END)), "loc_5038")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4FB5")
    TurnDirection(0x101, 0x13, 400)

    ChrTalk(    #196
        0x101,
        "#1001FHi again!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #197
        0x105,
        "#040FHello, Reina.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x13, 0x105, 400)

    ChrTalk(    #198
        0x13,
        "Even Kloe is here? Goodness.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #199
        0x101,
        "#1011FWhat's going on, Reina?\x02",
    )

    CloseMessageWindow()
    Jump("loc_5035")

    label("loc_4FB5")

    TurnDirection(0x101, 0x13, 400)

    ChrTalk(    #200
        0x101,
        (
            "#1001FAhaha, yeah, it's kind of been a while.\x01",
            "I guess we last met at the academy.\x02\x03",

            "#1011FSo what's going on, Reina?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5035")

    Jump("loc_51FF")

    label("loc_5038")

    TurnDirection(0x101, 0x13, 400)

    ChrTalk(    #201
        0x101,
        (
            "#1004FHuh?\x02\x03",

            "Hey, you're Reina, right?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5153")

    ChrTalk(    #202
        0x105,
        (
            "#040FYes, that's Reina. You met her during\x01",
            "our investigation of the academy.\x02\x03",

            "Hello, Reina.\x01",
            "I didn't expect to meet you here.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x13, 0x105, 400)

    ChrTalk(    #203
        0x13,
        "Even Kloe is here? Goodness.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #204
        0x101,
        "#1011FSo, uh, what ARE you doing here?\x02",
    )

    CloseMessageWindow()
    Jump("loc_51FF")

    label("loc_5153")

    TurnDirection(0x106, 0x101, 400)

    ChrTalk(    #205
        0x106,
        "#052FYou know each other?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x106, 400)

    ChrTalk(    #206
        0x101,
        "#1000FUh, yeah, she's a student at the royal academy.\x02",
    )

    CloseMessageWindow()

    def lambda_51C1():
        TurnDirection(0x106, 0x13, 400)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_51C1)
    TurnDirection(0x101, 0x13, 400)

    ChrTalk(    #207
        0x101,
        "#1011FBut what are you doing here, Reina?\x02",
    )

    CloseMessageWindow()

    label("loc_51FF")

    TurnDirection(0x13, 0x101, 400)

    ChrTalk(    #208
        0x13,
        "It's quite a long story.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #209
        0x13,
        "I assume you saw our posting?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #210
        0x101,
        "#1000FWell, yeah, that's why we're here.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #211
        0x13,
        (
            "I would like for you to handle this mission\x01",
            "as quickly as possible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #212
        0x13,
        "Will you accept it? Right now?\x02",
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
            "Yes\x01",      # 0
            "No\x01",       # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5365")

    ChrTalk(    #213
        0x101,
        (
            "#1006FSounds pretty urgent.\x01",
            "Let's get to it!\x02",
        )
    )

    CloseMessageWindow()
    Call(1, 9)
    Jump("loc_5498")

    label("loc_5365")


    ChrTalk(    #214
        0x101,
        (
            "#1007FEr, sorry. Dunno if we can do it,\x01",
            "like, right this second.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #215
        0x13,
        "Really? That is a problem.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #216
        0x13,
        (
            "Will your other business be handled soon?\x01",
            "Very soon?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #217
        0x101,
        (
            "#1015FWell, maybe.\x02\x03",

            "#1000FI'll try and hurry back as soon as I can.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #218
        0x13,
        "Please do so.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #219
        0x13,
        (
            "Another time, then.\x01",
            "Do hurry.\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x7A, 0x1, 0x8000)
    OP_8C(0x13, 180, 0)
    OP_8C(0x14, 0, 0)

    label("loc_5498")

    OP_4B(0x13, 255)
    OP_4B(0x14, 255)
    ClearChrFlags(0xC, 0x80)
    OP_A2(0x1A55)
    EventEnd(0x0)
    Return()

    # Function_7_4C14 end

    def Function_8_54AB(): pass

    label("Function_8_54AB")

    EventBegin(0x0)
    OP_4A(0x13, 255)
    OP_4A(0x14, 255)
    ClearChrFlags(0x13, 0x10)
    ClearChrFlags(0x14, 0x10)
    Fade(1000)
    SetChrPos(0x106, -45770, 0, -2880, 270)
    SetChrPos(0x101, -45760, 0, -1750, 270)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5518")
    SetChrPos(0x105, -44380, 0, -1770, 270)
    SetChrPos(0xF9, -44510, 0, -2770, 270)
    Jump("loc_556C")

    label("loc_5518")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_554A")
    SetChrPos(0x105, -44380, 0, -1770, 270)
    SetChrPos(0xF8, -44510, 0, -2770, 270)
    Jump("loc_556C")

    label("loc_554A")

    SetChrPos(0xF8, -44380, 0, -1770, 270)
    SetChrPos(0xF9, -44510, 0, -2770, 270)

    label("loc_556C")

    SetChrFlags(0xC, 0x80)
    OP_6D(-46730, 0, -2460, 0)
    OP_67(0, 6760, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    TurnDirection(0x13, 0x101, 0)
    TurnDirection(0x14, 0x101, 0)
    OP_0D()

    ChrTalk(    #220
        0x14,
        "Ah, they've returned.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #221
        0x13,
        "Are you ready to take the mission?\x02",
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
            "Yes\x01",      # 0
            "No\x01",       # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5692")

    ChrTalk(    #222
        0x101,
        (
            "#1006FSounds like it's pretty urgent,\x01",
            "so yeah, let's do it.\x02",
        )
    )

    CloseMessageWindow()
    Call(1, 9)
    Jump("loc_5701")

    label("loc_5692")


    ChrTalk(    #223
        0x101,
        "#1015FS-Sorry, we're still busy.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #224
        0x13,
        (
            "Still? Blast it...\x02\x03",

            "Another time, then, but do hurry.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x13, 180, 0)
    OP_8C(0x14, 0, 0)

    label("loc_5701")

    OP_4B(0x13, 255)
    OP_4B(0x14, 255)
    ClearChrFlags(0xC, 0x80)
    EventEnd(0x0)
    Return()

    # Function_8_54AB end

    def Function_9_5711(): pass

    label("Function_9_5711")

    EventBegin(0x0)

    ChrTalk(    #225
        0x14,
        (
            "You accept, then!\x01",
            "Oh, thank you...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x13, 0x14, 400)

    ChrTalk(    #226
        0x13,
        "#4PI will explain the situation to the bracers.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #227
        0x13,
        "#4PYou go deal with the rest of them.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x14, 0x13, 400)

    ChrTalk(    #228
        0x14,
        "As you wish, miss.\x02",
    )

    CloseMessageWindow()
    OP_8C(0x14, 90, 400)

    ChrTalk(    #229
        0x14,
        "Please, take care of our mistress.\x02",
    )

    CloseMessageWindow()

    def lambda_57F6():

        label("loc_57F6")

        TurnDirection(0x13, 0x14, 400)
        OP_48()
        Jump("loc_57F6")

    QueueWorkItem2(0x13, 1, lambda_57F6)

    def lambda_5807():

        label("loc_5807")

        TurnDirection(0x101, 0x14, 400)
        OP_48()
        Jump("loc_5807")

    QueueWorkItem2(0x101, 1, lambda_5807)

    def lambda_5818():

        label("loc_5818")

        TurnDirection(0x106, 0x14, 400)
        OP_48()
        Jump("loc_5818")

    QueueWorkItem2(0x106, 1, lambda_5818)

    def lambda_5829():

        label("loc_5829")

        TurnDirection(0xF8, 0x14, 400)
        OP_48()
        Jump("loc_5829")

    QueueWorkItem2(0xF8, 1, lambda_5829)

    def lambda_583A():

        label("loc_583A")

        TurnDirection(0xF9, 0x14, 400)
        OP_48()
        Jump("loc_583A")

    QueueWorkItem2(0xF9, 1, lambda_583A)
    OP_43(0x14, 0x1, 0x1, 0xB)
    OP_43(0x13, 0x2, 0x1, 0xC)
    OP_6D(-43450, 0, -1960, 3000)
    OP_44(0x101, 0x1)
    OP_44(0x106, 0x1)
    OP_44(0xF8, 0x1)
    OP_44(0xF9, 0x1)
    Sleep(1000)
    OP_6D(-46730, 0, -2460, 3000)

    def lambda_5890():
        TurnDirection(0x101, 0x13, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5890)
    Sleep(100)

    def lambda_58A3():
        TurnDirection(0x106, 0x13, 400)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_58A3)
    Sleep(100)

    def lambda_58B6():
        TurnDirection(0xF8, 0x13, 400)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_58B6)
    TurnDirection(0xF9, 0x13, 400)
    SetChrPos(0x14, -33780, 1500, 2840, 0)

    ChrTalk(    #230
        0x101,
        "#1016FErrrr...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x13, 0x101, 400)

    ChrTalk(    #231
        0x13,
        "Yes?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #232
        0x101,
        (
            "#1015FWho...was that, exactly?\x01",
            "I feel like I've missed something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #233
        0x13,
        "A servant of the house, like me.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #234
        0x13,
        (
            "We are both charged with caring\x01",
            "for the mistress.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #235
        0x101,
        "#1004FCharged with...uh.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #236
        0x13,
        "Yes, ah, I'm getting ahead of myself.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #237
        0x13,
        (
            "Let me explain what's happened\x01",
            "from the beginning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #238
        0x101,
        "#1002FPlease.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #239
        0x13,
        (
            "Right, then...\x01",
            "Estelle, you remember Felicity, yes?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x7A, 0x1, 0x4000)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5BD3")

    ChrTalk(    #240
        0x101,
        (
            "#1011FFelicity?\x02\x03",

            "#1006FUh... yeah, actually!\x01",
            "Think I'd know her if I saw her.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5B12")

    ChrTalk(    #241
        0x105,
        "#040FWe met while investigating the ghost story.\x02",
    )

    CloseMessageWindow()
    Jump("loc_5BA3")

    label("loc_5B12")


    ChrTalk(    #242
        0x106,
        "#050F#6PYet another student, I'm guessing?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #243
        0x13,
        "Correct.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #244
        0x13,
        (
            "If nothing else, you can identify her by\x01",
            "her uniform--it is the same as mine.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5BA3")


    ChrTalk(    #245
        0x101,
        "#1000FSo what's Felicity done, exactly?\x02",
    )

    CloseMessageWindow()
    Jump("loc_5E7E")

    label("loc_5BD3")


    ChrTalk(    #246
        0x101,
        (
            "#1011FFelicity?\x02\x03",

            "#1006FYeah, sure, we said hi to her\x01",
            "back at the Krone Pass.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x13, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #247
        0x13,
        "WH-WHAT?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #248
        0x13,
        (
            "You met Felicity recently?!\x01",
            "You said the Krone Pass?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #249
        0x101,
        (
            "#1015FEr, whoa, yeah. She was kind of loitering\x01",
            "around the guard post. Doing some\x01",
            "'social observations' or something, I think?\x02\x03",

            "#1011F...Why do I get the feeling that's super\x01",
            "important?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #250
        0x13,
        "Because it most certainly is!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #251
        0x13,
        "The mission is to find Felicity, after all!\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #252
        0x101,
        "#1004FPardon?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #253
        0x106,
        (
            "#051F#6PHah, how's that for luck?\x02\x03",

            "Found her before we knew we were\x01",
            "lookin' for her!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #254
        0x101,
        (
            "#1002FBut why the heck would Felicity go to\x01",
            "a border garrison post, unannounced?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5E7E")


    ChrTalk(    #255
        0x13,
        "She ran away.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #256
        0x101,
        "#1011FEh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #257
        0x13,
        "As I said, she ran away.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #258
        0x13,
        "Specifically, from here at the Anterose.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #259
        0x101,
        (
            "#1004FShe ran away from the restaurant?\x02\x03",

            "Why would she need to do that?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5FE4")

    ChrTalk(    #260
        0x104,
        (
            "#031FAhhh, I believe I understand what happened.\x02\x03",

            "It's what you might call a, ah,\x01",
            "dine-and-dash, no?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x104, 400)

    ChrTalk(    #261
        0x101,
        "#1019FThat's what YOU do, you glutton.\x02",
    )

    CloseMessageWindow()

    label("loc_5FE4")


    ChrTalk(    #262
        0x13,
        (
            "Why did she flee?\x01",
            "I would like to ask her that myself.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x13, 400)

    ChrTalk(    #263
        0x13,
        (
            "After all, today is a most auspicious\x01",
            "day for our mistress.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #264
        0x106,
        "#555F#6PAnd what's that supposed to mean?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #265
        0x13,
        "Take a look over there by the corner.\x02",
    )

    CloseMessageWindow()
    OP_4A(0x16, 255)
    OP_6D(-32900, 1500, 3980, 3000)
    Sleep(2000)
    OP_8C(0x101, 45, 0)
    OP_8C(0x106, 45, 0)
    OP_8C(0xF8, 45, 0)
    OP_8C(0xF9, 45, 0)
    OP_8C(0x13, 90, 0)
    Fade(1000)
    OP_6D(-46730, 0, -2460, 0)
    OP_0D()
    OP_4B(0x16, 255)

    ChrTalk(    #266
        0x101,
        "#1011F#6PHang on, that's--\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #267
        0x13,
        "The son of a certain Erebonian noble, yes.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #268
        0x13,
        (
            "He has traveled far, into what most Erebonians\x01",
            "consider a barbarian hinterland, for a wedding\x01",
            "conference with our mistress.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #269
        0x101,
        "#1000F#6POh, okay, I...see...\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    TurnDirection(0x101, 0x13, 400)

    ChrTalk(    #270
        0x101,
        (
            "#1020F#3SA WEDDING CO...?! You mean like an\x01",
            "arranged marriage?!\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    def lambda_6288():
        TurnDirection(0x106, 0x13, 400)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_6288)
    Sleep(100)

    def lambda_629B():
        TurnDirection(0xF8, 0x13, 400)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_629B)
    TurnDirection(0xF9, 0x13, 400)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_62E5")

    ChrTalk(    #271
        0x105,
        "#044FFelicity's...being married off?\x02",
    )

    CloseMessageWindow()
    Jump("loc_63DE")

    label("loc_62E5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_632D")

    ChrTalk(    #272
        0x103,
        "#023FThis girl's being forced into a marriage...?\x02",
    )

    CloseMessageWindow()
    Jump("loc_63DE")

    label("loc_632D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6363")

    ChrTalk(    #273
        0x107,
        "#064FFelicity has to marry him?\x02",
    )

    CloseMessageWindow()
    Jump("loc_63DE")

    label("loc_6363")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_63DE")

    ChrTalk(    #274
        0x104,
        (
            "#033FAh... Now I see. Young Felicity is of\x01",
            "Erebonian background as well, then.\x01",
            "Which would mean... Hmm.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_63DE")


    ChrTalk(    #275
        0x13,
        (
            "Student she may be, but the mistress\x01",
            "is sixteen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #276
        0x13,
        (
            "As a daughter of a noble house of the\x01",
            "Erebonian Empire, it is shameful for her\x01",
            "to have no proposals.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #277
        0x101,
        (
            "#1022FNow just a freakin' second.\x02\x03",

            "#1002FThere are KINDA more important things\x01",
            "than your family's high-and-mighty honor\x01",
            "or whatever!\x02\x03",

            "Have you considered what she thinks?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #278
        0x13,
        (
            "This proposal comes from a person of\x01",
            "notable lineage and personal status.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #279
        0x13,
        (
            "If milady Felicity meets him, I am\x01",
            "sure she will find him compatible.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #280
        0x101,
        (
            "#1007FThat's SO not the problem here...\x02\x03",

            "Man, I can kinda see why she fled\x01",
            "at this point.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_674D")

    ChrTalk(    #281
        0x105,
        (
            "#045FSo can I, to tell the truth...\x02\x03",

            "I think I'd try to flee from something\x01",
            "like this myself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #282
        0x106,
        (
            "#552F#6PDon't think any of us can blame her.\x02\x03",

            "I just wish she'd thought about how this'd\x01",
            "get people other than herself wrapped\x01",
            "up in the mess...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6B70")

    label("loc_674D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_685E")

    ChrTalk(    #283
        0x103,
        (
            "#027FSo she took a stand and fled from getting\x01",
            "shoehorned into being a trophy wife?\x02\x03",

            "#021FHeh! If anything, I'm more tempted to\x01",
            "cheer her on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #284
        0x106,
        (
            "#551F#6PI am so not in the mood to joke\x01",
            "about this.\x02\x03",

            "Man, I hate getting wrapped up in\x01",
            "stuff like this.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6B70")

    label("loc_685E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6A35")

    ChrTalk(    #285
        0x104,
        (
            "#031FFleeing from an undesired proposal,\x01",
            "desperately seeking free love...\x02\x03",

            "Ah! The subject of a hundred romantic epics\x01",
            "in Erebonia. It reminds me of my own youth.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x104, 400)

    ChrTalk(    #286
        0x101,
        (
            "#1019FLemme guess, you just tried to shove off\x01",
            "a proposal on some older woman to get\x01",
            "out of it all.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x101, 400)

    ChrTalk(    #287
        0x104,
        "#033FOh? How did you know?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #288
        0x106,
        (
            "#551F#6PWhatever, it's a pain in the ass no\x01",
            "matter what.\x02\x03",

            "Man, I hate getting wrapped up in\x01",
            "stuff like this.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_6A23():
        TurnDirection(0x104, 0x13, 400)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_6A23)
    TurnDirection(0x101, 0x13, 400)
    Jump("loc_6B70")

    label("loc_6A35")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6B70")

    ChrTalk(    #289
        0x108,
        (
            "#070FShe's run away from a marriage proposal\x01",
            "she doesn't want, then.\x02\x03",

            "I can understand how she feels, but what\x01",
            "she's done IS rather impulsive.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #290
        0x106,
        (
            "#551F#6PYeah, I feel for her, but she didn't\x01",
            "really think it through.\x02\x03",

            "Wish she'd thought about how this'd get\x01",
            "other people wrapped up in the mess.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6B70")


    ChrTalk(    #291
        0x13,
        (
            "You are, of course, entitled to your\x01",
            "own opinions.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #292
        0x13,
        "I will refrain from voicing my objections.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #293
        0x13,
        (
            "What matters now is not a debate over the\x01",
            "merits of free love, but bringing back\x01",
            "Mistress Felicity.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x7A, 0x1, 0x4000)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7179")

    ChrTalk(    #294
        0x106,
        (
            "#050F#6PYeah, moral debates aside, her being out\x01",
            "on her own, outta contact with everyone,\x01",
            "isn't helping anybody, least of all her.\x02\x03",

            "Any idea where she would've gone to?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #295
        0x13,
        (
            "Felicity's personality is such that she\x01",
            "tends to go off as far as she can once\x01",
            "she has committed to something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #296
        0x13,
        (
            "I suspect she has gone quite some\x01",
            "way at this point.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #297
        0x101,
        (
            "#1015FQuite some way, huh?\x02\x03",

            "#1002FOther side of the city, maybe?\x01",
            "She wouldn't go onto the roads--\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #298
        0x13,
        (
            "Quite the opposite, in fact.\x01",
            "We know she is nowhere in town.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #299
        0x13,
        (
            "In other words, she has taken to\x01",
            "the roads by default. On foot.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #300
        0x101,
        (
            "#1020FWhat?! But that's REALLY dangerous right\x01",
            "now with the monsters the way they are!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #301
        0x13,
        "Ergo, my request.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #302
        0x13,
        (
            "Do you understand, now, how severe\x01",
            "the situation is?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #303
        0x106,
        (
            "#057F#6PDamn, say that first, instead of distracting\x01",
            "us with this wedding stuff.\x02\x03",

            "Any idea where this girl went?\x01",
            "I'd take a vague direction at this point.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #304
        0x13,
        (
            "The mistress said again and again she was\x01",
            "returning to the academy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #305
        0x13,
        "Beyond that, I fear I cannot help you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #306
        0x101,
        (
            "#1002FThe academy... So towards Ruan.\x01",
            "That'd be to the west from here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #307
        0x106,
        (
            "#050F#6PYeah, we should check the road to\x01",
            "Ruan first.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #308
        0x101,
        (
            "#1002FIt's a plan.\x02\x03",

            "Okay, Reina. I still don't really like this,\x01",
            "but we'll go find her.\x02\x03",

            "Anything else before we go?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7299")

    label("loc_7179")


    ChrTalk(    #309
        0x106,
        (
            "#050F#6PWe don't have to like it, but fine.\x02\x03",

            "Let's head back to the Pass and see\x01",
            "if we can convince her to return.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #310
        0x101,
        (
            "#1015FI'm...not really sure she'll come back\x01",
            "easily, though.\x02\x03",

            "I mean, given the reason, I sure know I'd\x01",
            "tell any bracer sent to 'fetch' me to go\x01",
            "jump in the lake.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7299")


    ChrTalk(    #311
        0x13,
        "Yes, hmm.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #312
        0x13,
        (
            "Given everything, may I ask you to\x01",
            "convey a message to her?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #313
        0x101,
        "#1011FSure. What's up?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #314
        0x13,
        "If you would...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #315
        0x13,
        "Tell her, 'You're such a coward.' That is all.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #316
        0x101,
        (
            "#1019FUh, what?\x02\x03",

            "You're...REALLY sure you want\x01",
            "us to deliver that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #317
        0x13,
        (
            "I am sure.\x01",
            "Call it a calculated action.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x7A, 0x1, 0x4000)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7450")

    ChrTalk(    #318
        0x106,
        (
            "#057F#6PTch, fine, whatever.\x02\x03",

            "Let's just get this done.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x106, 400)

    ChrTalk(    #319
        0x101,
        "#1002FYeah, fine.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x13, 400)

    ChrTalk(    #320
        0x101,
        "#1002FWe're off, then.\x02",
    )

    CloseMessageWindow()
    Jump("loc_74C2")

    label("loc_7450")


    ChrTalk(    #321
        0x106,
        (
            "#053F#6PIf that's what the client wants,\x01",
            "it's what the client will get.\x02\x03",

            "#050FWe'll give her that...message.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_74C2")


    ChrTalk(    #322
        0x13,
        "Good luck to you, then.\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0x14, 0x10)
    SetChrFlags(0x13, 0x10)
    OP_28(0x7A, 0x4, 0x4)
    OP_28(0x7A, 0x4, 0x8)
    OP_28(0x7A, 0x1, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x7A, 0x1, 0x4000)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_750E")
    OP_28(0x7A, 0x1, 0x2)
    Jump("loc_7514")

    label("loc_750E")

    OP_28(0x7A, 0x1, 0x4)

    label("loc_7514")

    OP_A2(0x13)
    Return()

    # Function_9_5711 end

    def Function_10_7518(): pass

    label("Function_10_7518")

    FadeToDark(0, 0, -1)
    EventBegin(0x0)
    SetChrFlags(0x8, 0x8)
    SetChrPos(0x13, -44110, 0, 0, 180)
    SetChrPos(0x14, -43150, 0, 610, 180)
    SetChrPos(0x12, -44180, 0, -1550, 0)
    SetChrPos(0x101, -43640, 0, -3030, 0)
    SetChrPos(0x106, -44730, 0, -3030, 0)
    SetChrPos(0xF8, -43160, 0, -4320, 0)
    SetChrPos(0xF9, -45180, 0, -4320, 0)
    SetChrChipByIndex(0x12, 33)
    SetChrFlags(0x12, 0x1)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x12, 0x10)
    ClearChrFlags(0x12, 0x40)
    ClearChrFlags(0x12, 0x4)
    ClearChrFlags(0x14, 0x10)
    ClearChrFlags(0x16, 0x10)
    OP_4A(0x13, 255)
    OP_4A(0x14, 255)
    SetChrFlags(0xC, 0x80)
    OP_6D(-43590, 11050, -920, 0)
    OP_67(0, 6760, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    FadeToBright(2000, 0)
    OP_6D(-44180, 0, -1060, 5000)
    OP_0D()
    Sleep(500)

    ChrTalk(    #323
        0x14,
        (
            "Ah, mistress...\x01",
            "I am glad to see you are well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #324
        0x13,
        "...As am I. We've been waiting.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x7A, 0x1, 0x20)"), scpexpr(EXPR_END)), "loc_7774")

    ChrTalk(    #325
        0x12,
        (
            "#6PI'm not returning of my own free will,\x01",
            "you know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #326
        0x12,
        (
            "#6PIt'd just be more trouble to try to\x01",
            "avoid this, so let's get it over with.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #327
        0x13,
        "That is acceptable.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #328
        0x13,
        (
            "Nothing can happen unless you attend,\x01",
            "after all.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7784")

    label("loc_7774")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x7A, 0x1, 0x10)"), scpexpr(EXPR_END)), "loc_7784")
    OP_2B(0x7A, 0x2)

    label("loc_7784")


    ChrTalk(    #329
        0x12,
        "#6P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #330
        0x12,
        "#6PReina, let me be clear on one thing.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #331
        0x12,
        "#6PI still haven't even remotely forgiven you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #332
        0x13,
        "Yes... I'm well aware.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #333
        0x13,
        "We can, however, discuss that later.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #334
        0x12,
        "#6PYeah. I suppose we can.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #335
        0x12,
        (
            "#6PThis isn't something we can do\x01",
            "in five or ten minutes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #336
        0x13,
        "Well, then. Lead the mistress to her seat.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #337
        0x14,
        "Of course.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #338
        0x14,
        "Mistress Felicity, please, this way.\x02",
    )

    CloseMessageWindow()
    OP_8C(0x12, 180, 400)

    ChrTalk(    #339
        0x12,
        "#4PAll right...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #340
        0x12,
        (
            "#4PI'm sorry I put you guys through\x01",
            "so much trouble.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #341
        0x101,
        (
            "#1006F#1PNo, trust us, we understand.\x02\x03",

            "Good luck in there, okay?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_79DB")

    ChrTalk(    #342
        0x105,
        "#040FI'll see you back at school, Felicity.\x02",
    )

    CloseMessageWindow()

    label("loc_79DB")


    ChrTalk(    #343
        0x12,
        (
            "#4PYeah, see you there. Bye,\x01",
            "everyone!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_7A0D():

        label("loc_7A0D")

        TurnDirection(0x13, 0x12, 400)
        OP_48()
        Jump("loc_7A0D")

    QueueWorkItem2(0x13, 1, lambda_7A0D)

    def lambda_7A1E():

        label("loc_7A1E")

        TurnDirection(0xFE, 0x12, 400)
        OP_48()
        Jump("loc_7A1E")

    QueueWorkItem2(0x0, 1, lambda_7A1E)

    def lambda_7A2F():

        label("loc_7A2F")

        TurnDirection(0xFE, 0x12, 400)
        OP_48()
        Jump("loc_7A2F")

    QueueWorkItem2(0x1, 1, lambda_7A2F)

    def lambda_7A40():

        label("loc_7A40")

        TurnDirection(0xFE, 0x12, 400)
        OP_48()
        Jump("loc_7A40")

    QueueWorkItem2(0x2, 1, lambda_7A40)

    def lambda_7A51():

        label("loc_7A51")

        TurnDirection(0xFE, 0x12, 400)
        OP_48()
        Jump("loc_7A51")

    QueueWorkItem2(0x3, 1, lambda_7A51)
    Sleep(400)
    OP_8C(0x12, 45, 400)

    def lambda_7A6E():
        OP_8E(0x12, 0xFFFF5D3A, 0x0, 0x1F4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_7A6E)
    OP_8C(0x14, 90, 400)
    OP_43(0x13, 0x2, 0x1, 0xD)

    def lambda_7A97():
        OP_8E(0x14, 0xFFFF83F0, 0x5DC, 0x1F4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_7A97)
    WaitChrThread(0x12, 0x1)
    OP_8E(0x12, 0xFFFF8009, 0x5DC, 0x1F4, 0x7D0, 0x0)
    OP_44(0x13, 0x1)
    OP_44(0x0, 0x1)
    OP_44(0x1, 0x1)
    OP_44(0x2, 0x1)
    OP_44(0x3, 0x1)
    OP_8C(0x13, 180, 400)
    OP_8E(0x13, 0xFFFF536C, 0x0, 0xFFFFFDDA, 0x3E8, 0x0)
    OP_8C(0x13, 180, 400)
    WaitChrThread(0x13, 0x2)
    Sleep(1000)

    ChrTalk(    #344
        0x13,
        "You performed well, bracers.\x02",
    )

    CloseMessageWindow()

    def lambda_7B2D():
        OP_8C(0x101, 0, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7B2D)
    Sleep(100)

    def lambda_7B40():
        OP_8C(0x106, 0, 400)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_7B40)
    Sleep(100)

    def lambda_7B53():
        OP_8C(0xF8, 0, 400)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_7B53)
    OP_8C(0xF9, 0, 400)

    ChrTalk(    #345
        0x13,
        (
            "In the place of my lord, allow me to offer\x01",
            "our gratitude for your efforts.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x7A, 0x1, 0x20)"), scpexpr(EXPR_END)), "loc_7C57")

    ChrTalk(    #346
        0x101,
        (
            "#1015F#6PYeah, uh, thanks for that.\x01",
            "But, uh...\x02\x03",

            "#1002FReina, are you okay?\x02\x03",

            "Your relationship with Felicity kind\x01",
            "of seems to be, y'know. A wreck.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7DC4")

    label("loc_7C57")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x7A, 0x1, 0x10)"), scpexpr(EXPR_END)), "loc_7DC4")

    ChrTalk(    #347
        0x13,
        (
            "It may not be much, but this is a token\x01",
            "of our thanks.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #348
        0x13,
        "Please, take it.\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #349
        "\x07\x00Received #344i.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x158, 1)

    ChrTalk(    #350
        0x101,
        (
            "#1011F#6PUh, yeah, thanks.\x02\x03",

            "#1015FWell, that's the job settled.\x01",
            "For better or worse. But, uh...\x02\x03",

            "#1002FReina, are you okay?\x02\x03",

            "Your relationship with Felicity kind of seems\x01",
            "to be, y'know. A wreck.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7DC4")


    ChrTalk(    #351
        0x13,
        "This is all for Felicity's sake.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #352
        0x13,
        (
            "It is the fate of we servants to be\x01",
            "hated by those we serve.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7E97")

    ChrTalk(    #353
        0x105,
        (
            "#043FOh, Reina...\x02\x03",

            "Haven't you ever considered that Felicity\x01",
            "doesn't think that way?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7F0B")

    label("loc_7E97")


    ChrTalk(    #354
        0x101,
        (
            "#1003F#6PUhhhh... Reina...\x02\x03",

            "Have you never, ever considered that,\x01",
            "just maybe, Felicity DOESN'T think that\x01",
            "way?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7F0B")


    ChrTalk(    #355
        0x13,
        "I...don't understand what you mean.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #356
        0x101,
        (
            "#1002F#6PFelicity thought of you as a friend, okay?\x01",
            "Like, it's really obvious.\x02\x03",

            "If you thought your role was to be hated...\x01",
            "I think that's where you two slipped away\x01",
            "from each other.\x02\x03",

            "#1015FMmm, maybe it's a little big-headed of\x01",
            "me to be saying all this, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #357
        0x13,
        "...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #358
        0x13,
        "No. It is...something worth thinking about.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #359
        0x13,
        (
            "I believe Felicity and I WILL need to sit\x01",
            "down and talk for a while, after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #360
        0x13,
        "However, for now, if you'll pardon me.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #361
        0x101,
        "#1011F#6POh, yeah. Good luck.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_815D")

    ChrTalk(    #362
        0x105,
        "#040FI'll see you at school, too, Reina.\x02",
    )

    CloseMessageWindow()
    Jump("loc_8171")

    label("loc_815D")


    ChrTalk(    #363
        0x106,
        "#050F#3PRight.\x02",
    )

    CloseMessageWindow()

    label("loc_8171")


    ChrTalk(    #364
        0x13,
        "Farewell.\x02",
    )

    CloseMessageWindow()

    def lambda_8186():

        label("loc_8186")

        TurnDirection(0xFE, 0x13, 400)
        OP_48()
        Jump("loc_8186")

    QueueWorkItem2(0x0, 1, lambda_8186)

    def lambda_8197():

        label("loc_8197")

        TurnDirection(0xFE, 0x13, 400)
        OP_48()
        Jump("loc_8197")

    QueueWorkItem2(0x1, 1, lambda_8197)

    def lambda_81A8():

        label("loc_81A8")

        TurnDirection(0xFE, 0x13, 400)
        OP_48()
        Jump("loc_81A8")

    QueueWorkItem2(0x2, 1, lambda_81A8)

    def lambda_81B9():

        label("loc_81B9")

        TurnDirection(0xFE, 0x13, 400)
        OP_48()
        Jump("loc_81B9")

    QueueWorkItem2(0x3, 1, lambda_81B9)
    Sleep(400)
    OP_8C(0x13, 90, 400)
    OP_8E(0x13, 0xFFFF7748, 0x0, 0xFFFFFDDA, 0x7D0, 0x0)
    OP_44(0x0, 0x1)
    OP_44(0x1, 0x1)
    OP_44(0x2, 0x1)
    OP_44(0x3, 0x1)

    ChrTalk(    #365
        0x101,
        (
            "#1007F#5PWell, that's another tempest waiting to\x01",
            "rage in a teapot.\x02\x03",

            "I kinda hope they can rebuild their\x01",
            "friendship, but, man...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_82B2")

    ChrTalk(    #366
        0x105,
        "#043FIt is all rather dire, isn't it?\x02",
    )

    CloseMessageWindow()

    label("loc_82B2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_832F")

    ChrTalk(    #367
        0x103,
        (
            "#020FI'm afraid this is where our involvement\x01",
            "has to come to a close, though.\x02\x03",

            "The rest is up to them.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8420")

    label("loc_832F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_83B8")

    ChrTalk(    #368
        0x108,
        (
            "#070FOur involvement in this draws to\x01",
            "a close here, though.\x02\x03",

            "The karma between those two must be\x01",
            "balanced by them.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8420")

    label("loc_83B8")


    ChrTalk(    #369
        0x106,
        (
            "#050FI know how you feel, but this is as far\x01",
            "as it goes for us.\x02\x03",

            "The rest has gotta be up to them.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8420")

    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrChipByIndex(0x12, 14)
    ClearChrFlags(0x12, 0x1)
    SetChrFlags(0x12, 0x10)
    SetChrFlags(0x12, 0x40)
    SetChrFlags(0x12, 0x4)
    SetChrPos(0x13, -33800, 1500, 1300, 0)
    SetChrPos(0x14, -31760, 1500, 1300, 0)
    SetChrPos(0x12, -32930, 1600, 2650, 0)
    OP_4B(0x13, 255)
    OP_4B(0x14, 255)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0x8, 0x8)
    OP_22(0x17, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #370
        "Quest #2C[The Missing Lady] #0Ccompleted!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_28(0x7A, 0x4, 0x10)
    SetChrPos(0x0, -43590, 0, -1450, 180)
    SetChrPos(0x1, -43590, 0, -1450, 180)
    SetChrPos(0x2, -43590, 0, -1450, 180)
    SetChrPos(0x3, -43590, 0, -1450, 180)
    OP_4A(0x0, 255)
    OP_4A(0x1, 255)
    OP_4A(0x2, 255)
    OP_4A(0x3, 255)
    OP_69(0x101, 0x0)
    OP_30(0x0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_69(0x101, 0x0)
    OP_30(0x0)
    OP_8C(0x101, 180, 0)
    OP_8C(0xF7, 180, 0)
    OP_8C(0xF8, 180, 0)
    OP_8C(0xF9, 180, 0)
    OP_4A(0x0, 255)
    OP_4A(0x1, 255)
    OP_4A(0x2, 255)
    OP_4A(0x3, 255)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_10_7518 end

    def Function_11_85A0(): pass

    label("Function_11_85A0")

    OP_8C(0xFE, 135, 400)
    OP_8E(0x14, 0xFFFF49A8, 0x0, 0xFFFFF1C8, 0x7D0, 0x0)
    OP_8E(0x14, 0xFFFF5560, 0x0, 0xFFFFF1C8, 0x7D0, 0x0)
    OP_8E(0x14, 0xFFFF5FD8, 0x0, 0xFFFFFF38, 0x7D0, 0x0)
    OP_A2(0x22)
    OP_8E(0x14, 0xFFFF6EE2, 0x5DC, 0xFFFFFF38, 0x7D0, 0x0)
    Return()

    # Function_11_85A0 end

    def Function_12_85FB(): pass

    label("Function_12_85FB")

    OP_A6(0x22)
    OP_44(0x13, 0x1)
    OP_8E(0x13, 0xFFFF46A6, 0x0, 0xFFFFF722, 0x3E8, 0x0)
    Sleep(150)
    OP_8C(0x13, 90, 400)
    Return()

    # Function_12_85FB end

    def Function_13_8623(): pass

    label("Function_13_8623")

    OP_6D(-41920, 0, 210, 2000)
    Sleep(1500)
    OP_6D(-44560, 0, -2000, 2000)
    Return()

    # Function_13_8623 end

    SaveToFile()

Try(main)
