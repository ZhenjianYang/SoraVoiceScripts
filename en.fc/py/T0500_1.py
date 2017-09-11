from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'T0500_1 ._SN',
        MapName             = 'Rolent',
        Location            = 'T0500.x',
        MapIndex            = 18,
        MapDefaultBGM       = "ed60016",
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
        "Function_1_C5C",          # 01, 1
        "Function_2_C66",          # 02, 2
        "Function_3_C78",          # 03, 3
        "Function_4_CF6",          # 04, 4
        "Function_5_D74",          # 05, 5
        "Function_6_DF2",          # 06, 6
    )


    def Function_0_66(): pass

    label("Function_0_66")

    EventBegin(0x0)
    SetMapFlags(0x400000)
    ClearMapFlags(0x1)
    SetChrPos(0x101, -4900, 0, -22400, 90)
    SetChrPos(0x102, -4900, 0, -24400, 90)
    SetChrPos(0x8, 3000, 0, -22400, 270)
    SetChrPos(0x9, 3000, 0, -24400, 270)
    ClearChrFlags(0xA, 0x8)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, -1000, 0, -20400, 180)
    OP_44(0x8, 0xFF)
    OP_44(0x9, 0xFF)
    OP_44(0xA, 0xFF)
    OP_44(0x8, 0xFF)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_6C(45000, 0)
    OP_6B(2500, 0)
    OP_6D(-20400, 0, -18400, 0)
    FadeToBright(3000, 0)
    OP_43(0xA, 0x1, 0x1, 0x1)
    OP_43(0xA, 0x2, 0x1, 0x2)
    OP_6C(315000, 6000)
    Sleep(1500)
    OP_31(0x0, 0xFE, 0x0)
    OP_31(0x1, 0xFE, 0x0)

    ChrTalk(    #0
        0xA,
        "All right, training begins now.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xA,
        "Everyone advance five steps forward.\x02",
    )

    CloseMessageWindow()
    OP_43(0x8, 0x2, 0x1, 0x3)
    OP_43(0x9, 0x2, 0x1, 0x4)
    OP_43(0x102, 0x2, 0x1, 0x5)
    OP_43(0x101, 0x2, 0x1, 0x6)
    Sleep(5000)

    ChrTalk(    #2
        0xA,
        "Ready yourselves!\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    Fade(500)
    SetChrPos(0x11, -1900, 0, -22400, 90)
    ClearChrFlags(0x11, 0x8)
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x101, 0x8)
    SetChrFlags(0x101, 0x40)
    SetChrPos(0x12, -1900, 0, -24400, 90)
    ClearChrFlags(0x12, 0x8)
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x102, 0x8)
    SetChrFlags(0x102, 0x40)
    SetChrPos(0xF, 0, 0, -22400, 270)
    ClearChrFlags(0xF, 0x8)
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0x8, 0x8)
    SetChrFlags(0x8, 0x40)
    SetChrPos(0x10, 0, 0, -24400, 270)
    ClearChrFlags(0x10, 0x8)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x9, 0x8)
    SetChrFlags(0x9, 0x40)
    OP_0D()

    ChrTalk(    #3
        0xF,
        "I know I was bored before, but...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x10,
        (
            "#6PI-I know it's just training and all,\x01",
            "but it still scares the living daylights\x01",
            "out of me...\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xA, 135, 400)

    ChrTalk(    #5
        0xA,
        (
            "This is a training exercise,\x01",
            "so please refrain from speaking!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xA,
        (
            "You all need to take this seriously\x01",
            "as if this were a real battle!\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xA, 180, 400)

    ChrTalk(    #7
        0xA,
        (
            "Estelle and Joshua, you don't\x01",
            "need to hold back on my men.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x11,
        (
            "#006FThat was my intention from\x01",
            "the beginning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x12,
        "#012FWe'll do as you request.\x02",
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(400)

    ChrTalk(    #10
        0x10,
        "Yikes!\x02",
    )

    CloseMessageWindow()
    Sleep(700)

    ChrTalk(    #11
        0xA,
        "Forward!\x02",
    )

    CloseMessageWindow()
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x11, 0xFF)
    OP_44(0x12, 0xFF)
    OP_44(0xF, 0xFF)
    OP_44(0x10, 0xFF)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Battle(0x3ED, 0x0, 0x0, 0x0, 0xFF)
    EventBegin(0x0)
    OP_1D(0x10)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_497"),
        (2, "loc_8A5"),
        (1, "loc_8A5"),
        (SWITCH_DEFAULT, "loc_BE5"),
    )


    label("loc_497")

    FadeToBright(2000, 0)
    SetChrPos(0x13, 0, 0, -22400, 270)
    SetChrPos(0x14, 0, 0, -24400, 270)
    SetChrSubChip(0x13, 3)
    SetChrSubChip(0x14, 3)
    ClearChrFlags(0x13, 0x8)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x8)
    ClearChrFlags(0x14, 0x80)
    SetChrFlags(0xF, 0x8)
    SetChrFlags(0xF, 0x40)
    SetChrFlags(0x10, 0x8)
    SetChrFlags(0x10, 0x40)
    SetChrPos(0x101, -1900, 0, -22400, 90)
    SetChrPos(0x102, -1900, 0, -24400, 90)
    ClearChrFlags(0x101, 0x8)
    ClearChrFlags(0x102, 0x8)
    ClearChrFlags(0x101, 0x40)
    ClearChrFlags(0x102, 0x40)
    SetChrFlags(0x11, 0x8)
    SetChrFlags(0x12, 0x8)
    SetChrFlags(0x11, 0x40)
    SetChrFlags(0x12, 0x40)
    OP_0D()
    Sleep(700)
    OP_28(0x8, 0x1, 0x2)
    OP_2C(0x8, 0xC8)
    OP_2B(0x8, 0x2)

    ChrTalk(    #12
        0xA,
        "Cease fighting!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xA,
        "This training is over.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x13,
        "Owowowow...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x14,
        "Oh my goodness. It's finally over...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x102,
        "#010FGood job, everyone.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x101,
        (
            "#007FCan I say pathetic?\x02\x03",

            "Are you guys really supposed\x01",
            "to be soldiers?\x02",
        )
    )

    CloseMessageWindow()
    OP_99(0x13, 0x3, 0x0, 0x7D0)
    SetChrFlags(0x13, 0x8)
    SetChrFlags(0x13, 0x80)
    SetChrChipByIndex(0x8, 5)
    ClearChrFlags(0x8, 0x8)
    ClearChrFlags(0x8, 0x40)

    ChrTalk(    #18
        0x8,
        "H-Hey! You be quiet!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x8,
        "We're not all feral kids like you!\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(400)

    ChrTalk(    #20
        0x101,
        (
            "#005FHow about you try and say that\x01",
            "one more time?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0xA,
        (
            "Knock it off, Scott.\x01",
            "Training is over!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #22
        0x102,
        (
            "#017FYou seriously need to cool down\x01",
            "too, Estelle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x101,
        "#009FI hate sore losers.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x8, 400)

    ChrTalk(    #24
        0xA,
        "Private Scott, Private Harold...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0xA,
        (
            "I think what Estelle said just a\x01",
            "moment ago is how the citizens\x01",
            "of this region really feel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0xA,
        (
            "Do you really have what it takes\x01",
            "to protect them...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xA,
        (
            "It seems as though the both\x01",
            "of you need to take another\x01",
            "look in the mirror.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x8,
        "...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x14,
        "...Y-Yes, sir!\x02",
    )

    CloseMessageWindow()
    Jump("loc_BE5")

    label("loc_8A5")

    FadeToBright(2000, 0)
    SetChrPos(0x15, -1900, 0, -22400, 90)
    OP_99(0x15, 0x3, 0x3, 0x0)
    ClearChrFlags(0x15, 0x8)
    ClearChrFlags(0x15, 0x80)
    SetChrFlags(0x11, 0x40)
    SetChrFlags(0x11, 0x8)
    SetChrPos(0x102, -1900, 0, -24400, 90)
    ClearChrFlags(0x102, 0x8)
    ClearChrFlags(0x102, 0x40)
    SetChrFlags(0x12, 0x8)
    SetChrFlags(0x12, 0x40)
    SetChrChipByIndex(0x8, 5)
    SetChrChipByIndex(0x9, 5)
    ClearChrFlags(0x8, 0x8)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x8)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0xF, 0x8)
    SetChrFlags(0xF, 0x40)
    SetChrFlags(0x10, 0x8)
    SetChrFlags(0x10, 0x40)
    OP_0D()
    Sleep(700)
    OP_28(0x8, 0x1, 0x4)

    ChrTalk(    #30
        0xA,
        "Cease fighting!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xA,
        "This training is over.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x15,
        (
            "#007FI'm going to feel those bruises\x01",
            "tomorrow...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x15, 400)

    ChrTalk(    #33
        0x102,
        (
            "#017FWe lost?\x02\x03",

            "I guess we were a bit careless...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x9,
        "Oh, man. W-We're finally done.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x8,
        (
            "I'm too drained to even take\x01",
            "another step.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x8, 400)

    ChrTalk(    #36
        0xA,
        (
            "What do I hear you saying,\x01",
            "Private Scott?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xA,
        (
            "If this were a real battle, this would\x01",
            "be about the time a second wave\x01",
            "of enemies would be showing up!\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x9, 0)
    TurnDirection(0x9, 0xA, 400)

    ChrTalk(    #38
        0x8,
        "...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x9,
        "Y-Yes, sir...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0xA,
        "Private Scott, Private Harold...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0xA,
        (
            "Do you really think you have what\x01",
            "it takes to protect the citizens of\x01",
            "Rolent...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0xA,
        (
            "I think it's about time you asked\x01",
            "yourselves this question.\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x8, 0)
    TurnDirection(0x8, 0xA, 400)

    ChrTalk(    #43
        0x8,
        "U-Understood, sir.\x02",
    )

    CloseMessageWindow()
    Jump("loc_BE5")

    label("loc_BE5")


    ChrTalk(    #44
        0xA,
        (
            "Very good. Do not forget what you\x01",
            "learned today and strive to fulfill\x01",
            "your duties.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(1000)
    FadeToDark(3000, 0, -1)
    OP_28(0x8, 0x1, 0x4000)
    NewScene("ED6_DT01/T0510   ._SN", 101, 0, 0)
    IdleLoop()
    Return()

    # Function_0_66 end

    def Function_1_C5C(): pass

    label("Function_1_C5C")

    OP_6B(2800, 6000)
    Return()

    # Function_1_C5C end

    def Function_2_C66(): pass

    label("Function_2_C66")

    OP_6D(-1600, 0, -22400, 6000)
    Return()

    # Function_2_C66 end

    def Function_3_C78(): pass

    label("Function_3_C78")

    Sleep(500)
    OP_90(0x8, 0xFFFFFDA8, 0x0, 0x0, 0x7D0, 0x0)
    Sleep(340)
    OP_90(0x8, 0xFFFFFDA8, 0x0, 0x0, 0x7D0, 0x0)
    Sleep(330)
    OP_90(0x8, 0xFFFFFDA8, 0x0, 0x0, 0x7D0, 0x0)
    Sleep(340)
    OP_90(0x8, 0xFFFFFDA8, 0x0, 0x0, 0x7D0, 0x0)
    Sleep(335)
    OP_90(0x8, 0xFFFFFDA8, 0x0, 0x0, 0x7D0, 0x0)
    Return()

    # Function_3_C78 end

    def Function_4_CF6(): pass

    label("Function_4_CF6")

    Sleep(700)
    OP_90(0x9, 0xFFFFFDA8, 0x0, 0x0, 0x7D0, 0x0)
    Sleep(300)
    OP_90(0x9, 0xFFFFFDA8, 0x0, 0x0, 0x7D0, 0x0)
    Sleep(300)
    OP_90(0x9, 0xFFFFFDA8, 0x0, 0x0, 0x7D0, 0x0)
    Sleep(300)
    OP_90(0x9, 0xFFFFFDA8, 0x0, 0x0, 0x7D0, 0x0)
    Sleep(300)
    OP_90(0x9, 0xFFFFFDA8, 0x0, 0x0, 0x7D0, 0x0)
    Return()

    # Function_4_CF6 end

    def Function_5_D74(): pass

    label("Function_5_D74")

    Sleep(550)
    OP_90(0x102, 0x258, 0x0, 0x0, 0x7D0, 0x0)
    Sleep(300)
    OP_90(0x102, 0x258, 0x0, 0x0, 0x7D0, 0x0)
    Sleep(300)
    OP_90(0x102, 0x258, 0x0, 0x0, 0x7D0, 0x0)
    Sleep(300)
    OP_90(0x102, 0x258, 0x0, 0x0, 0x7D0, 0x0)
    Sleep(300)
    OP_90(0x102, 0x258, 0x0, 0x0, 0x7D0, 0x0)
    Return()

    # Function_5_D74 end

    def Function_6_DF2(): pass

    label("Function_6_DF2")

    Sleep(550)
    OP_90(0x101, 0x258, 0x0, 0x0, 0x7D0, 0x0)
    Sleep(300)
    OP_90(0x101, 0x258, 0x0, 0x0, 0x7D0, 0x0)
    Sleep(300)
    OP_90(0x101, 0x258, 0x0, 0x0, 0x7D0, 0x0)
    Sleep(300)
    OP_90(0x101, 0x258, 0x0, 0x0, 0x7D0, 0x0)
    Sleep(300)
    OP_90(0x101, 0x258, 0x0, 0x0, 0x7D0, 0x0)
    Return()

    # Function_6_DF2 end

    SaveToFile()

Try(main)
