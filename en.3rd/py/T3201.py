from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 蔡斯

    CreateScenaFile(
        FileName            = 'T3201   ._SN',
        MapName             = 'Zeiss',
        Location            = 'T3201.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60084",
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
        'Zin',                                  # 9
        'Kilika',                               # 10
        'Target Camera',                        # 11
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
        'ED6_DT07/CH00070 ._CH',             # 00
        'ED6_DT07/CH02610 ._CH',             # 01
    )

    AddCharChipPat(
        'ED6_DT07/CH00070P._CP',             # 00
        'ED6_DT07/CH02610P._CP',             # 01
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x80,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_11A",          # 00, 0
        "Function_1_13A",          # 01, 1
        "Function_2_13B",          # 02, 2
        "Function_3_C46",          # 03, 3
        "Function_4_C62",          # 04, 4
    )


    def Function_0_11A(): pass

    label("Function_0_11A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_139")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 7)), scpexpr(EXPR_END)), "loc_139")
    OP_A3(0x2507)
    SetMapFlags(0x10000000)
    Event(0, 4)

    label("loc_139")

    Return()

    # Function_0_11A end

    def Function_1_13A(): pass

    label("Function_1_13A")

    Return()

    # Function_1_13A end

    def Function_2_13B(): pass

    label("Function_2_13B")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 50900, 2500, -2400, 0)
    OP_6D(50730, 2500, 2180, 0)
    OP_67(0, 7220, -10000, 0)
    OP_6B(2830, 0)
    OP_6C(141000, 0)
    OP_6E(411, 0)

    def lambda_1B4():
        OP_6E(324, 5000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_1B4)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x0, 0x0)
    Fade(1000)
    OP_6D(51440, 2500, -3490, 0)
    OP_67(0, 5710, -10000, 0)
    OP_6B(2570, 0)
    OP_6C(141000, 0)
    OP_6E(298, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(    #0
        0x11,
        "#790F#5P...\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_72(0x806, 0x0)
    ExitThread()
    OP_72(0x1006, 0x0)
    ExitThread()
    OP_6F(0x6, 0)
    OP_70(0x6, 0x1D)
    OP_73(0x6)
    Sleep(200)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 60800, 2500, -3050, 270)

    def lambda_269():
        OP_8E(0xFE, 0xD638, 0x9C4, 0xFFFFF4DE, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_269)

    def lambda_284():
        OP_6D(54110, 2500, -4810, 3000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_284)

    def lambda_29C():
        OP_67(0, 4019, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_29C)

    def lambda_2B4():
        OP_6B(2710, 3000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_2B4)

    def lambda_2C4():
        OP_6E(313, 3000)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_2C4)
    Sleep(1000)
    OP_6F(0x6, 29)
    OP_70(0x6, 0x0)
    OP_23(0x6)
    OP_22(0x7, 0x0, 0x64)
    WaitChrThread(0x0, 0x0)
    WaitChrThread(0x10, 0x1)
    OP_8C(0x11, 90, 400)
    Sleep(200)

    ChrTalk(    #1
        0x11,
        (
            "#790F#4PYou're out rather fast... Have you finished in the\x01",
            "bath already?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x10,
        (
            "#070F#5PFast? Seriously?\x02\x03",

            "I was in there for a whole hour!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x11,
        "#790F#4POh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x10,
        (
            "#070F#5PMan, it's not often I see you looking this deep in \x01",
            "thought.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)

    def lambda_3F5():
        OP_6D(53380, 2500, -5270, 2000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_3F5)

    def lambda_40D():
        OP_67(0, 4490, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_40D)

    def lambda_425():
        OP_6B(2760, 2000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_425)

    def lambda_435():
        OP_6E(325, 2000)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_435)
    OP_43(0x10, 0x0, 0x0, 0x3)
    WaitChrThread(0x10, 0x0)
    WaitChrThread(0x0, 0x0)
    OP_8C(0x11, 0, 400)

    ChrTalk(    #5
        0x11,
        (
            "#790FI suppose you don't...\x02\x03",

            "...I feel like I'm one step away from making a\x01",
            "decision, but just need one last push to take it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x10,
        "#070F#5POh, right...\x02",
    )

    CloseMessageWindow()
    Sleep(200)
    OP_8C(0x10, 0, 400)
    Sleep(1500)

    ChrTalk(    #7
        0x10,
        (
            "#070F#5PStill... Being here like this with you really\x01",
            "takes me back. Hard to believe it's been six\x01",
            "whole years since Master Ryuga's passing.\x02\x03",

            "Sounds like you went on quite the journey between \x01",
            "then and becoming a bracer, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x11,
        (
            "#790FI suppose you could say that.\x02\x03",

            "Going on a journey makes it sound like something\x01",
            "I did deliberately, though. In reality it was a\x01",
            "lot less cool than that.\x02\x03",

            "I just kind of drifted from place to place, then\x01",
            "finally ended up being drawn to one point where\x01",
            "I settled.\x02\x03",

            "Kind of like a leaf falling from a tree and ending\x01",
            "up floating down a river.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x10,
        (
            "#070F#5PI see...\x02\x03",

            "Then don't you think it's about time you started\x01",
            "picking yourself up...\x02\x03",

            "...and looking for a path of your own?\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x11, 90, 400)

    ChrTalk(    #10
        0x11,
        (
            "#790F#4POh my...\x02\x03",

            "Are you trying to give me a push in the right\x01",
            "direction?\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x10, 315, 400)

    ChrTalk(    #11
        0x10,
        (
            "#070F#5PUgh... Sorry for not being able to do a better job\x01",
            "of it.\x02\x03",

            "S-Still... All I'm really trying to say is...\x02\x03",

            "I think you've spent enough time here already.\x02\x03",

            "Enough time to heal the scars of the past, at\x01",
            "least.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x11,
        (
            "#790F#4PYes, I suppose...\x02\x03",

            "I suppose you're right.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_8C(0x11, 0, 400)
    Sleep(2000)

    ChrTalk(    #13
        0x11,
        "#790F...Say, Zin.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x10,
        "#070F#5PHmm?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x11,
        "#790FWould you be happy if I returned to Calvard?\x02",
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 2300, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #16
        0x10,
        "#070F#5PWh-What brought that on?\x02",
    )

    CloseMessageWindow()
    OP_8C(0x11, 90, 400)
    Sleep(300)

    ChrTalk(    #17
        0x11,
        "#790F#4PIt doesn't matter. Just answer the question.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x10,
        (
            "#070F#5PW-Well...\x02\x03",

            "If I had to pick, I guess you'd rather be back\x01",
            "in Calvard, yeah.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x11,
        "#790F#4P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x10,
        "#070F#5PWh-Why do you ask?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x11,
        (
            "#790F#4POh, no reason...\x02\x03",

            "I've decided I'm going to accept the president's\x01",
            "proposal.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #22
        0x10,
        (
            "#070F#5PWh-What?!\x02\x03",

            "You didn't pick that because of what I just said,\x01",
            "did you? Because...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x11,
        (
            "#790F#4PNo.\x02\x03",

            "I just wanted some kind of reason to bring this\x01",
            "journey to an end.\x02\x03",

            "As well as a place to make better use of my\x01",
            "skills.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_20(0x7D0)
    Sleep(2000)
    OP_A2(0x2508)
    NewScene("ED6_DT21/T3200   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_2_13B end

    def Function_3_C46(): pass

    label("Function_3_C46")

    OP_8E(0xFE, 0xCABC, 0x9C4, 0xFFFFF448, 0x5DC, 0x0)
    OP_8C(0xFE, 315, 400)
    Return()

    # Function_3_C46 end

    def Function_4_C62(): pass

    label("Function_4_C62")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_22(0x1CF, 0x0, 0x64)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 50900, 2500, -2400, 0)
    OP_6D(48910, 380, 2620, 0)
    OP_67(0, 5410, -10000, 0)
    OP_6B(1660, 0)
    OP_6C(143000, 0)
    OP_6E(731, 0)
    StopSound(0xC8, 0x1D4C0, 0x0)

    def lambda_CED():
        OP_6D(53710, 380, -6310, 6000)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_CED)

    def lambda_D05():
        OP_67(0, 5410, -10000, 6000)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_D05)

    def lambda_D1D():
        OP_6B(1400, 6000)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_D1D)

    def lambda_D2D():
        OP_6C(143000, 6000)
        ExitThread()

    QueueWorkItem(0x12, 3, lambda_D2D)

    def lambda_D3D():
        OP_6E(731, 6000)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_D3D)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x12, 0x0)
    Sleep(1000)

    ChrTalk(    #24
        0x11,
        "#793F#11P...\x02",
    )

    CloseMessageWindow()
    OP_72(0x806, 0x0)
    ExitThread()
    OP_72(0x1006, 0x0)
    ExitThread()
    OP_6F(0x6, 0)
    OP_70(0x6, 0x1D)
    OP_73(0x6)
    Sleep(300)
    ClearChrFlags(0x10, 0x80)
    OP_9F(0x10, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x10, 60800, 2500, -3050, 270)

    def lambda_DB6():
        OP_8E(0xFE, 0xD638, 0x9C4, 0xFFFFF4DE, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_DB6)

    def lambda_DD1():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_DD1)

    def lambda_DE3():
        OP_6D(54110, 2500, -4810, 3000)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_DE3)

    def lambda_DFB():
        OP_67(0, 4019, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_DFB)

    def lambda_E13():
        OP_6B(1430, 3000)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_E13)

    def lambda_E23():
        OP_6E(720, 3000)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_E23)
    Sleep(1000)
    OP_72(0x6, 0x8)
    ExitThread()
    OP_6F(0x6, 29)
    OP_70(0x6, 0x0)
    OP_22(0x7, 0x0, 0x64)
    WaitChrThread(0x12, 0x0)
    WaitChrThread(0x10, 0x1)
    OP_8C(0x11, 90, 400)
    Sleep(300)

    ChrTalk(    #25
        0x11,
        (
            "#791F#12PYou're out rather fast... Have you finished\x01",
            "in the bath already?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x10,
        (
            "#073F#5PFast? Seriously?\x02\x03",

            "#070FI was in there for an hour!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x11,
        "#792F#12POh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x10,
        (
            "#070F#5PMan, it's not often I see you looking this\x01",
            "deep in thought.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_F53():
        OP_6D(52580, 2500, -4620, 3000)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_F53)

    def lambda_F6B():
        OP_67(0, 3840, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_F6B)

    def lambda_F83():
        OP_6B(1260, 3000)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_F83)

    def lambda_F93():
        OP_6E(731, 3000)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_F93)
    OP_43(0x10, 0x0, 0x0, 0x3)
    WaitChrThread(0x10, 0x0)
    WaitChrThread(0x12, 0x0)
    OP_8C(0x11, 0, 400)
    Sleep(500)

    ChrTalk(    #29
        0x11,
        (
            "#792F#6PI suppose you don't...\x02\x03",

            "#793FI feel like I'm one step away from making a decision\x01",
            "but just need one last push to take it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x10,
        "#074F#5POh. Right...\x02",
    )

    CloseMessageWindow()
    OP_20(0x7D0)
    OP_8C(0x10, 0, 300)
    OP_21()
    OP_1D(0xB7)
    Sleep(500)

    ChrTalk(    #31
        0x10,
        (
            "#074F#5PStill...being here like this with you really takes me\x01",
            "back. Hard to believe it's been six years now since\x01",
            "Master Ryuga's passing.\x02\x03",

            "#070FSounds like you went on a hell of a journey between\x01",
            "then and joining the guild, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x11,
        (
            "#791FYou could say that.\x02\x03",

            "#792FGoing on a journey makes it sound like something\x01",
            "I did deliberately, though. In reality, it wasn't quite\x01",
            "as organized as that.\x02\x03",

            "I simply drifted from place to place before ending\x01",
            "up being drawn to one point where I settled.\x02\x03",

            "#793FMuch in the way a leaf that fell from a tree ends\x01",
            "up floating down the river.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x10,
        (
            "#074F#5P...\x02\x03",

            "#070FWere you able to find that answer you\x01",
            "mentioned a while back?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x11,
        (
            "#792FHaha. No. I still haven't.\x02\x03",

            "#794FStill...\x02\x03",

            "...I do feel as though I've found a conclusion\x01",
            "of sorts.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x10,
        "#072F#5PWhat's that supposed to mean?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x11,
        (
            "#791FSay, Zin...\x02\x03",

            "Why do you think I chose to take on a noncombat\x01",
            "position like guild receptionist to begin with?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x10,
        (
            "#073F#5PHmm...\x02\x03",

            "#573FBecause you didn't want to follow the same path\x01",
            "as idiots like me and Walter?\x02\x03",

            "#070FI wouldn't follow us either if I were in your shoes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x11,
        (
            "#794FHaha...\x02\x03",

            "#792FNot quite, although I'm not going to deny that the\x01",
            "two of you are idiots.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 2300, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #39
        0x10,
        "#075F#5PHey! That was the one part I DID want you to deny!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x11,
        (
            "#793F...\x02\x03",

            "#792FI wanted to find out the meaning of the Living Fist\x01",
            "ideology my father advocated.\x02\x03",

            "I still believe that being able to better oneself through\x01",
            "combat, while your opponent does the same, is a good\x01",
            "thing in itself.\x02\x03",

            "#793FAs a warrior, it's probably close to the ideal way.\x02\x03",

            "#790F...Still, I couldn't help but wonder why the ideology\x01",
            "had to be based around the premise of fighting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x10,
        "#072F#5PHmm...\x02",
    )

    CloseMessageWindow()

    def lambda_171E():
        OP_6B(1210, 30000)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_171E)
    Sleep(500)

    ChrTalk(    #42
        0x11,
        (
            "#792FI can certainly understand the significance of living\x01",
            "and dying as a warrior.\x02\x03",

            "I can also understand how one who lived that way\x01",
            "would have no regrets when the time to pass away\x01",
            "came.\x02\x03",

            "Nothing has changed within me in that regard since\x01",
            "the days we trained together.\x02\x03",

            "#793FYet with Father dead and Walter gone, I couldn't\x01",
            "help but wonder...\x02\x03",

            "#794FWonder whether there was some way to make use\x01",
            "of the Living Fist without having to fight.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x10,
        "#073F#5P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x11,
        (
            "#793FThat was when I started roaming the continent in\x01",
            "search of one. \x02\x03",

            "And as I roamed, I found myself face to face with\x01",
            "countless conflicts and acts of violence, and I felt\x01",
            "powerless every time I did.\x02\x03",

            "#792FThat was how I came to encounter Liberl's guild.\x01",
            "They had arrived to quell one of those conflicts.\x02\x03",

            "Something about their ideology--putting the safety\x01",
            "of civilians over all else--made me feel that perhaps\x01",
            "working under them may give me my answer.\x02\x03",

            "So that was what led me to start working for the\x01",
            "guild.\x02\x03",

            "#794F...But even then, I wasn't able to run away from\x01",
            "fighting completely.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x10,
        (
            "#572F#5P#572F...\x02\x03",

            "#074F'The nature of humanity means that as long as we\x01",
            "exist, conflict will never cease.'\x02\x03",

            "'Instead, what's important is not blindly preaching\x01",
            "idealism...'\x02\x03",

            "'...but preaching ideals while keeping a firm eye on\x01",
            "the reality of how to quell conflict.'\x02\x03",

            "#072FMaster Ryuga's words have never left me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x11,
        (
            "#791FNor have they left me.\x02\x03",

            "#793FBut all the same...\x02\x03",

            "#792F...I've been looking away from reality all this time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x10,
        "#075F#5PCome on, now...\x02",
    )

    CloseMessageWindow()
    OP_8C(0x10, 315, 400)
    Sleep(300)

    ChrTalk(    #48
        0x10,
        (
            "#072F#5PYou know full well that's not actually true.\x02\x03",

            "When he says 'reality', he's not saying fighting\x01",
            "is the be-all, end-all of quelling conflict.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x11,
        (
            "#792FThat's not what I'm trying to say.\x02\x03",

            "#793FAll these years, I haven't been trying to walk on\x01",
            "my own two feet. Not at all.\x02\x03",

            "I've just been using trying to find a new way to \x01",
            "live by Father's Living Fist ideology as an excuse\x01",
            "to stand still.\x02\x03",

            "#794FAll while indulging myself in the comfortable\x01",
            "environment the guild gave me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x10,
        "#572F#5P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x11,
        (
            "#794FIn that sense, I must be the biggest failure of \x01",
            "Father's students.\x02\x03",

            "#792FI might not agree with the path Walter took...\x02\x03",

            "...but he, like you, has chosen his own path and\x01",
            "started walking forward along it.\x02\x03",

            "You two have been facing up to the Living Fist\x01",
            "ideal of Father's and slowly reaching your own\x01",
            "conclusions on it.\x02\x03",

            "In your own ways, you've been able to face up\x01",
            "to reality.\x02\x03",

            "#793FAnd I haven't. I've been standing still the whole\x01",
            "time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x10,
        "#074F#5P...\x02",
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 2300, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x10)
    Sleep(500)

    ChrTalk(    #53
        0x10,
        (
            "#573F#5PThat's the biggest load of crock I've ever heard.\x02\x01",

            "#070FYou've been walking forward just like we have.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x11, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x11, 90, 500)

    ChrTalk(    #54
        0x11,
        "#790FIn what way?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x10,
        (
            "#573F#5PIt's just that the path you've been walking has been\x01",
            "one for others rather than yourself.\x02\x03",

            "That river you think you've been helplessly drifting\x01",
            "through? You've actually been building a bridge so\x01",
            "others can easily cross it behind you.\x02\x03",

            "#070FWhen the road is hard, you soften the ground so\x01",
            "your fellow guildmates have an easier trek. There's\x01",
            "no shame in your way of the Living Fist--it's as true\x01",
            "as mine and Walter's.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x11,
        (
            "#790F...\x02\x03",

            "#792FHeehee...\x02\x03",

            "#794FAre you trying to comfort me?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x10,
        (
            "#072F#5PUgh... Sorry for not having a way with words.\x02\x03",

            "#074FA-Anyway, all I'm trying to say is this...you\x01",
            "know.\x02\x03",

            "#072FAs a person, you're way too strong and way\x01",
            "too serious.\x02\x03",

            "And at times, it's like those two things just\x01",
            "end up restricting you and stop you from\x01",
            "seeing things you otherwise could.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x11,
        "#793F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x10,
        (
            "#573F#5PSo try and relax a little, all right?\x02\x03",

            "Just a little.\x02\x03",

            "#070FIf you do, I'll bet you'll start seeing\x01",
            "things you couldn't before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x11,
        "#792F#6P...\x02",
    )

    CloseMessageWindow()
    OP_8C(0x11, 0, 300)
    Sleep(500)
    OP_62(0x11, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x11)
    Sleep(500)

    ChrTalk(    #61
        0x11,
        "#792FSay, Zin.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x10,
        "#070F#5PHmm? What is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x11,
        "#791FWould you be happy if I returned to Calvard?\x02",
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 2300, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #64
        0x10,
        "#073F#5PWh-What brought that on?\x02",
    )

    CloseMessageWindow()
    OP_8C(0x11, 90, 400)

    ChrTalk(    #65
        0x11,
        "#790F#6PIt doesn't matter. Just answer the question.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x10,
        (
            "#073F#5PO-Okay...\x02\x03",

            "#074FIf I had to pick, I guess you'd rather be back\x01",
            "home, yeah.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x11,
        "#792F#6P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x10,
        "#072F#5PWhy do you ask?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x11,
        (
            "#792F#6POh, no reason.\x02\x03",

            "#791FI've decided I'm going to accept the president's\x01",
            "proposal.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #70
        0x10,
        (
            "#073F#5PWh-What?!\x02\x03",

            "J-Just because of what I said...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x11,
        (
            "#792F#6PDon't misunderstand me.\x02\x03",

            "All I wanted was some kind of reason to bring\x01",
            "this journey to an end.\x02\x03",

            "#791FAs well as a place to make better use of my\x01",
            "skills.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_287F():
        OP_6B(1180, 3000)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_287F)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_20(0xFA0)
    OP_24(0x1CF, 0x5A)
    Sleep(400)
    OP_24(0x1CF, 0x50)
    Sleep(400)
    OP_24(0x1CF, 0x46)
    Sleep(400)
    OP_24(0x1CF, 0x3C)
    Sleep(400)
    OP_24(0x1CF, 0x32)
    Sleep(400)
    OP_24(0x1CF, 0x28)
    Sleep(400)
    OP_24(0x1CF, 0x1E)
    Sleep(400)
    OP_24(0x1CF, 0x14)
    Sleep(400)
    OP_24(0x1CF, 0xA)
    Sleep(400)
    OP_23(0x1CF)
    OP_21()
    OP_A2(0x2508)
    NewScene("ED6_DT21/T3200   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_4_C62 end

    SaveToFile()

Try(main)
