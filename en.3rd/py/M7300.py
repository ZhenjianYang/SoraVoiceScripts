from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'M7300   ._SN',
        MapName             = 'Gaiden3',
        Location            = 'M7300.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60175",
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
        Unknown_08              = 0,
        Unknown_0C              = 4,
        Unknown_0E              = 5,
        Unknown_10              = 0,
        Unknown_14              = 9500,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 2500,
        Unknown_28              = 2800,
        Unknown_2C              = 262,
        Unknown_30              = 45,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 1,
        Unknown_3A              = 1,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT26/CH20722 ._CH',             # 00
        'ED6_DT26/CH20718 ._CH',             # 01
    )

    AddCharChipPat(
        'ED6_DT26/CH20722P._CP',             # 00
        'ED6_DT26/CH20718P._CP',             # 01
    )

    DeclActor(
        TriggerX            = 3410,
        TriggerZ            = 4950,
        TriggerY            = 27060,
        TriggerRange        = 1000,
        ActorX              = 3410,
        ActorZ              = 5800,
        ActorY              = 27060,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_DE",           # 00, 0
        "Function_1_FB",           # 01, 1
        "Function_2_11F",          # 02, 2
        "Function_3_1805",         # 03, 3
        "Function_4_184A",         # 04, 4
        "Function_5_1861",         # 05, 5
        "Function_6_1878",         # 06, 6
    )


    def Function_0_DE(): pass

    label("Function_0_DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_FA")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 2)

    label("loc_FA")

    Return()

    # Function_0_DE end

    def Function_1_FB(): pass

    label("Function_1_FB")

    OP_16(0x2, 0xFA0, 0xFFFE0C00, 0xFFFE0C00, 0x230093)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x581, 3)), scpexpr(EXPR_END)), "loc_11E")
    OP_22(0x17B, 0x1, 0x64)
    SetMapFlags(0x100000)

    label("loc_11E")

    Return()

    # Function_1_FB end

    def Function_2_11F(): pass

    label("Function_2_11F")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x109, 440, 1550, -12260, 180)
    SetChrPos(0x10F, 440, 1550, -12260, 90)
    SetChrFlags(0x109, 0x8)
    SetChrChipByIndex(0x10F, 0)
    SetChrSubChip(0x10F, 0)
    SetChrFlags(0x10F, 0x2)
    SetChrFlags(0x10F, 0x800)
    OP_6D(-350, 1550, -11450, 0)
    OP_67(0, 6760, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(315000, 0)
    OP_6E(266, 0)
    SetMessageWindowPos(250, 100, -1, -1)
    SetChrName("Young Man's Voice")

    AnonymousTalk(    #0
        (
            "\x07\x00...Hey...\x02\x03",

            "...Hey, Ries...\x01",
            "...ke...up...\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(120, 300, -1, -1)
    SetChrName("Ries")

    AnonymousTalk(    #1
        (
            "\x07\x00#1633F#40WMm...\x02\x03",

            "#1632F...Kev...in...?\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_43(0x109, 0x3, 0x0, 0x3)

    def lambda_239():
        OP_6B(2500, 3000)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_239)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0xEE, 0x0)
    OP_51(0x10F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(200)
    OP_51(0x10F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x20), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(200)
    OP_51(0x10F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x21), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(200)
    OP_51(0x10F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x22), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(200)
    Sleep(300)

    ChrTalk(    #2
        0x10F,
        "#1631F#6P#40W...Ah...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x109,
        "#1840F#2PYou okay? Feeling any pain?\x02",
    )

    CloseMessageWindow()
    OP_51(0x10F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x21), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(150)
    OP_51(0x10F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x20), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(150)
    OP_51(0x10F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(300)
    OP_51(0x10F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(150)
    OP_51(0x10F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(150)
    OP_51(0x10F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(300)
    Sleep(300)

    ChrTalk(    #4
        0x10F,
        "#1635F#6P#40WN-No... I'm okay...I think.\x02",
    )

    CloseMessageWindow()
    OP_51(0x10F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(150)
    OP_51(0x10F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x28), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(150)
    OP_51(0x10F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x29), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(150)
    OP_51(0x10F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(150)
    OP_51(0x10F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x29), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(150)
    OP_51(0x10F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x28), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(150)
    OP_51(0x10F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(500)
    Sleep(300)

    ChrTalk(    #5
        0x10F,
        (
            "#1632F#6P#40WBut why...are you...?\x02\x03",

            "I fell through...that crack...alone.\x02\x03",

            "#1634FSo why...are you....?\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #6
        0x109,
        "#1069F#2P#4SYou big dummy!\x02",
    )

    OP_7C(0x0, 0x12C, 0xBB8, 0x64)
    CloseMessageWindow()
    Sleep(150)
    OP_99(0x10F, 0x3, 0x6, 0x3E8)
    OP_22(0x19E, 0x0, 0x64)
    OP_99(0x10F, 0x7, 0xF, 0x5DC)
    Sleep(300)

    ChrTalk(    #7
        0x10F,
        "#1631F#6P...Me?\x02",
    )

    CloseMessageWindow()
    OP_1D(0xAD)
    Sleep(500)

    ChrTalk(    #8
        0x109,
        (
            "#1069F#2PWhat were you thinking with all that taunting?!\x02\x03",

            "'Go ahead and do your worst!'?!\x02\x03",

            "'Drop me wherever you like! I'll live!'?!\x02\x03",

            "And just how do you know you'll live?!\x01",
            "Oh, right. YOU DON'T.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    OP_51(0x10F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x11), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(300)
    Sleep(300)

    ChrTalk(    #9
        0x10F,
        "#1634F#6P...B-But...\x02",
    )

    CloseMessageWindow()
    OP_51(0x10F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x12), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(150)
    OP_51(0x10F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x13), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(300)
    Sleep(300)

    ChrTalk(    #10
        0x109,
        (
            "#1069F#2PYou're a squire, aren't you?!\x02\x03",

            "A rookie like you with no experience or\x01",
            "proper judgment has no business making\x01",
            "calls that put her own safety at risk!\x02\x03",

            "If you can't promise to NEVER do that again,\x01",
            "then you and I both know you're not cut out\x01",
            "to be part of the Gralsritter!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x10F,
        "#1632F#6P...\x02",
    )

    CloseMessageWindow()
    Sleep(150)
    OP_51(0x10F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x13), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(120)
    OP_51(0x10F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(120)
    OP_51(0x10F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x15), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(120)
    OP_51(0x10F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x25), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(120)
    OP_51(0x10F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x26), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(500)

    ChrTalk(    #12
        0x109,
        (
            "#1841F#2P...That's probably what I should be saying,\x01",
            "anyway, but it'd be real rich coming from me,\x01",
            "huh?\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    OP_51(0x10F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x25), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(150)
    OP_51(0x10F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x15), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(300)
    Sleep(300)

    ChrTalk(    #13
        0x109,
        "#1840F#2PSo I'll let you off with that little bop there.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x10F,
        "#1631F#6P...Huh?\x02",
    )

    CloseMessageWindow()
    OP_99(0x10F, 0x15, 0x17, 0x3E8)
    OP_22(0x8F, 0x0, 0x64)
    Sleep(300)
    OP_99(0x10F, 0x17, 0x19, 0x5DC)
    Sleep(300)
    Fade(250)
    SetChrSubChip(0x10F, 26)
    ClearChrFlags(0x109, 0x8)
    SetChrPos(0x109, 450, 1550, -11800, 180)
    SetChrChipByIndex(0x109, 65535)
    SetChrSubChip(0x109, 0)
    OP_0D()
    OP_8C(0x109, 90, 400)

    def lambda_8AA():
        OP_8E(0xFE, 0x8C0, 0x60E, 0xFFFFD256, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_8AA)

    def lambda_8C5():
        OP_6D(600, 1550, -11450, 2000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_8C5)
    OP_99(0x10F, 0x1A, 0x1D, 0x5DC)
    WaitChrThread(0x109, 0x0)
    WaitChrThread(0x109, 0x1)
    Sleep(500)

    ChrTalk(    #15
        0x109,
        (
            "#1067F#5PLook around us.\x02\x03",

            "This is it. The seventh plane.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x10F,
        "#1634F#5PWow...\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(1000)
    OP_6D(600, 1550, -11450, 0)
    OP_67(0, 9250, -10000, 0)
    OP_6B(3100, 0)
    OP_6C(315000, 0)
    OP_6E(335, 0)
    OP_43(0x109, 0x2, 0x0, 0x4)

    def lambda_996():
        OP_6B(7000, 6000)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_996)

    def lambda_9A6():
        OP_6C(330000, 6000)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_9A6)
    OP_C8(0x200, 0x46, "C_PLAC37._CH", 0x0, 0x7D0)
    WaitChrThread(0xEE, 0x0)
    Sleep(1000)
    Fade(1000)
    OP_6D(600, 1550, -11450, 0)
    OP_67(0, 6760, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(315000, 0)
    OP_6E(266, 0)
    OP_43(0x109, 0x2, 0x0, 0x5)
    OP_0D()
    Sleep(500)
    Fade(250)
    SetChrChipByIndex(0x10F, 1)
    SetChrSubChip(0x10F, 0)
    ClearChrFlags(0x10F, 0x2)
    ClearChrFlags(0x10F, 0x800)
    SetChrPos(0x10F, 500, 1550, -12260, 90)
    OP_0D()
    Sleep(300)

    def lambda_A54():
        OP_6D(1040, 1550, -11290, 1500)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_A54)

    def lambda_A6C():
        OP_8E(0xFE, 0x7E4, 0x60E, 0xFFFFCE14, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_A6C)
    WaitChrThread(0x10F, 0x0)
    WaitChrThread(0xEE, 0x0)
    Sleep(500)

    ChrTalk(    #17
        0x10F,
        "#1630F#5PGehenna...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x109,
        (
            "#1065F#5PYep. It's just like the Testaments brought to life.\x02\x03",

            "#1067FAnd I'm the one responsible for bringing it all.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x10F, 0, 400)
    Sleep(300)

    ChrTalk(    #19
        0x10F,
        "#1634F#6POh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x109,
        (
            "#1067F#5PAfter all, if there's one place that's possible, it's\x01",
            "Phantasma.\x02\x03",

            "I don't know how Rufina came back, but she did,\x01",
            "with both memories and personality intact.\x02\x03",

            "And now I have the good fortune of being punished\x01",
            "by one of the very people I wronged.\x02\x03",

            "#1065FI really couldn't think of a more fitting punishment\x01",
            "for a bastard like me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x10F,
        "#1632F#6P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x109,
        (
            "#1075F#5PEverything she said was dead on. More than\x01",
            "anything, I wanted to be punished.\x02\x03",

            "I figured that by accepting that punishment,\x01",
            "all of this would be done, and everyone else\x01",
            "could go back to their lives.\x02\x03",

            "I thought I could be just like her: sacrificing\x01",
            "my own life so everyone else could be saved.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x109, 180, 400)
    Sleep(300)

    ChrTalk(    #23
        0x109,
        (
            "#1840F#11PBut that wouldn't make me like her at all,\x01",
            "would it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x10F,
        (
            "#1635F#6PNo...\x02\x03",

            "#1632FShe might have given up her life to save ours...\x02\x03",

            "...but that wasn't because she was happy to\x01",
            "throw away her life to protect someone else's;\x01",
            "it was because she saw literally no other option.\x02\x03",

            "#1633FWith me unconscious, she didn't even have the\x01",
            "choice to retreat.\x02\x03",

            "There was no way out of the situation without\x01",
            "one of the three of us losing our lives.\x02\x03",

            "#1630FThat's the only reason she chose to do what\x01",
            "she did.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x109,
        (
            "#1075F#11P...Yeah.\x02\x03",

            "She was never the kind of person who would\x01",
            "praise self-sacrifice as some kind of virtue.\x02\x03",

            "#1840FShe'd only ever accept it as an option if all the\x01",
            "others had been exhausted, and it was truly the\x01",
            "only way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x10F,
        (
            "#1633F#6PRight. But this time, that's not the case.\x02\x03",

            "You're here. I'm here. All of our friends are here.\x02\x03",

            "#1632FIf we put our heads together, I'm sure we could\x01",
            "have found another way out of here.\x02\x03",

            "One where no one would have to die.\x02\x03",

            "You must have realized that...and yet you\x01",
            "tried to take the easy way out.\x02\x03",

            "#1635FDidn't you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x109,
        (
            "#1841F#11PI hate to say it, but yeah. I did.\x02\x03",

            "That's a pretty shameful thing for a Dominion\x01",
            "to be doing, huh?\x02\x03",

            "#1840FHaha... See? I've got no right to be criticizing\x01",
            "you. I'm even less fit to be a knight than you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x10F,
        "#1634F#6P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x109,
        (
            "#1075F#11PStill, standing around lamenting my own failings\x01",
            "isn't gonna get us anywhere.\x02\x03",

            "#1078FSo if you're up for walking, let's get ourselves\x01",
            "out of here.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #30
        0x10F,
        "#1631F#6P...Come again?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x109,
        (
            "#1840F#11PWhat're you looking so surprised for?\x02\x03",

            "You didn't think I was gonna stay here and accept\x01",
            "being punished for all eternity, did you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x10F,
        (
            "#1632F#6P...Well...\x02\x03",

            "Either that, or stay here and wait for Rufina to\x01",
            "show up again...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x109,
        (
            "#1075F#11PListen here, Ries.\x02\x03",

            "#1840FI'm not gonna deny that there's a part of me--\x01",
            "a big part--that wants to be punished for what\x01",
            "I did.\x02\x03",

            "Or that there's a part of me that was overjoyed\x01",
            "to see Rufina again, however it came to be.\x02\x03",

            "#1065FBut I'm not alone down here. You're here with\x01",
            "me, and believe me, that changes EVERYTHING.\x02\x03",

            "#1063FAs long as you're here, I'm not staying in this\x01",
            "hellhole a second longer than I have to.\x02\x03",

            "#1069FWe're getting out of here, you and me. No matter\x01",
            "what it takes!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x10F,
        (
            "#1631F#6P...!\x02\x03",

            "#1635FRight... Right!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_16EF():
        OP_6B(3500, 3000)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_16EF)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_20(0x1388)
    OP_21()
    OP_44(0xEE, 0x0)
    OP_A2(0x2C0B)
    OP_BB(0xE, 0x1, 0x16)
    OP_BD()
    OP_AA(65282)
    OP_28(0x3C, 0x4, 0x10)
    OP_28(0x3C, 0x4, 0x20)
    OP_28(0x3D, 0x4, 0x4)
    OP_28(0x3D, 0x4, 0x8)
    OP_28(0x3D, 0x1, 0x1)
    OP_6D(10, 1550, -11670, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(4000, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, 0, 1550, -11670, 0)
    SetChrPos(0x1, 0, 1550, -11670, 0)
    SetChrChipByIndex(0x0, 65535)
    SetChrChipByIndex(0x1, 65535)
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    OP_69(0x0, 0x0)
    OP_E6(0x2)
    OP_C0(0x15, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Sleep(1000)
    OP_1D(0xAF)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0xAF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_24(0x17B, 0x64)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    SetMapFlags(0x100000)
    Return()

    # Function_2_11F end

    def Function_3_1805(): pass

    label("Function_3_1805")

    OP_22(0x17B, 0x1, 0x0)
    Sleep(300)
    OP_24(0x17B, 0xA)
    Sleep(300)
    OP_24(0x17B, 0x14)
    Sleep(300)
    OP_24(0x17B, 0x1E)
    Sleep(300)
    OP_24(0x17B, 0x28)
    Sleep(300)
    OP_24(0x17B, 0x32)
    Sleep(300)
    OP_24(0x17B, 0x3C)
    Sleep(300)
    OP_24(0x17B, 0x46)
    Return()

    # Function_3_1805 end

    def Function_4_184A(): pass

    label("Function_4_184A")

    OP_24(0x17B, 0x50)
    Sleep(300)
    OP_24(0x17B, 0x5A)
    Sleep(300)
    OP_24(0x17B, 0x64)
    Return()

    # Function_4_184A end

    def Function_5_1861(): pass

    label("Function_5_1861")

    OP_24(0x17B, 0x5A)
    Sleep(300)
    OP_24(0x17B, 0x50)
    Sleep(300)
    OP_24(0x17B, 0x46)
    Return()

    # Function_5_1861 end

    def Function_6_1878(): pass

    label("Function_6_1878")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #35
        "\x07\x05Strange power is overflowing from the orb.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        1,
        -1,
        150,
        1,
        (
            "Rest\x01",        # 0
            "Cancel\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x1)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1914"),
        (1, "loc_19B2"),
        (SWITCH_DEFAULT, "loc_19B2"),
    )


    label("loc_1914")

    PlayEffect(0x86, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(300)
    OP_20(0x3E8)
    OP_22(0xC, 0x0, 0x64)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_22(0xD, 0x0, 0x64)
    OP_C0(0x15, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_30(0x1)
    Sleep(3500)
    OP_82(0x86, 0x0)
    OP_1D(0xAF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToBright(1000, 0)
    OP_0D()

    label("loc_19B2")

    TalkEnd(0xFF)
    SetMapFlags(0x100000)
    Return()

    # Function_6_1878 end

    SaveToFile()

Try(main)
