from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 卢安

    CreateScenaFile(
        FileName            = 'T2513   ._SN',
        MapName             = 'Ruan',
        Location            = 'T2513.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60014",
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


    AddCharChip(
        'ED6_DT27/CH03003 ._CH',             # 00
        'ED6_DT07/CH00043 ._CH',             # 01
    )

    AddCharChipPat(
        'ED6_DT27/CH03003P._CP',             # 00
        'ED6_DT07/CH00043P._CP',             # 01
    )

    ScpFunction(
        "Function_0_BA",           # 00, 0
        "Function_1_111",          # 01, 1
        "Function_2_16A",          # 02, 2
        "Function_3_1AB2",         # 03, 3
        "Function_4_1ACE",         # 04, 4
        "Function_5_1AEA",         # 05, 5
        "Function_6_1B06",         # 06, 6
        "Function_7_1B22",         # 07, 7
        "Function_8_1B3E",         # 08, 8
    )


    def Function_0_BA(): pass

    label("Function_0_BA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x69), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CF")
    OP_4F(0x31, (scpexpr(EXPR_PUSH_LONG, 0x5F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_E5")
    OP_A3(0x10F0)
    SetMapFlags(0x10000000)
    Event(0, 8)
    Jump("loc_110")

    label("loc_E5")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (108, "loc_FD"),
        (109, "loc_FD"),
        (112, "loc_FD"),
        (113, "loc_FD"),
        (SWITCH_DEFAULT, "loc_110"),
    )


    label("loc_FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x244, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_10D")
    Event(0, 2)

    label("loc_10D")

    Jump("loc_110")

    label("loc_110")

    Return()

    # Function_0_BA end

    def Function_1_111(): pass

    label("Function_1_111")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x244, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_129")
    OP_B1("t2513_y")
    Jump("loc_132")

    label("loc_129")

    OP_B1("t2513_n")

    label("loc_132")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_13C")
    Jump("loc_169")

    label("loc_13C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x403, 7)), scpexpr(EXPR_END)), "loc_154")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x59), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x2000000)
    Jump("loc_169")

    label("loc_154")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 3)), scpexpr(EXPR_END)), "loc_169")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x6E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x2000000)

    label("loc_169")

    Return()

    # Function_1_111 end

    def Function_2_16A(): pass

    label("Function_2_16A")

    EventBegin(0x0)
    ClearMapFlags(0x1)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (108, "loc_189"),
        (109, "loc_1AE"),
        (112, "loc_1D3"),
        (113, "loc_1F8"),
        (SWITCH_DEFAULT, "loc_21D"),
    )


    label("loc_189")

    SetChrPos(0x101, 56060, 1000, 17010, 126)
    SetChrPos(0x105, 55790, 1000, 15650, 126)
    Jump("loc_21D")

    label("loc_1AE")

    SetChrPos(0x101, 63650, 1000, 17010, 206)
    SetChrPos(0x105, 63920, 1000, 15650, 206)
    Jump("loc_21D")

    label("loc_1D3")

    SetChrPos(0x101, 56840, 1000, 12230, 52)
    SetChrPos(0x105, 55920, 1000, 12290, 52)
    Jump("loc_21D")

    label("loc_1F8")

    SetChrPos(0x101, 63220, 1000, 12000, 325)
    SetChrPos(0x105, 64230, 1000, 11610, 325)
    Jump("loc_21D")

    label("loc_21D")

    Sleep(500)

    ChrTalk(    #0
        0x101,
        "#1026FOh, this is the auditorium.\x02",
    )

    CloseMessageWindow()
    Sleep(100)

    def lambda_254():
        OP_6D(58730, 2850, 2760, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_254)

    def lambda_26C():
        OP_6C(18000, 4000)
        ExitThread()

    QueueWorkItem(0x105, 3, lambda_26C)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (108, "loc_28E"),
        (109, "loc_2A4"),
        (112, "loc_2BA"),
        (113, "loc_2D0"),
        (SWITCH_DEFAULT, "loc_2E6"),
    )


    label("loc_28E")

    OP_43(0x101, 0x1, 0x0, 0x3)
    Sleep(800)
    OP_43(0x105, 0x1, 0x0, 0x4)
    Jump("loc_2E6")

    label("loc_2A4")

    OP_43(0x101, 0x1, 0x0, 0x3)
    Sleep(800)
    OP_43(0x105, 0x1, 0x0, 0x5)
    Jump("loc_2E6")

    label("loc_2BA")

    OP_43(0x101, 0x1, 0x0, 0x3)
    Sleep(800)
    OP_43(0x105, 0x1, 0x0, 0x6)
    Jump("loc_2E6")

    label("loc_2D0")

    OP_43(0x101, 0x1, 0x0, 0x3)
    Sleep(800)
    OP_43(0x105, 0x1, 0x0, 0x7)
    Jump("loc_2E6")

    label("loc_2E6")

    WaitChrThread(0x105, 0x1)
    WaitChrThread(0x105, 0x3)

    ChrTalk(    #1
        0x101,
        "#1025FMmm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x105,
        (
            "#542FIt's strange, isn't it?\x02\x03",

            "It was only a few months ago,\x01",
            "and yet you can't help but reminisce.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x101,
        "#1025FYeah...\x02",
    )

    CloseMessageWindow()
    OP_AD(0x2400C0, 0x0, 0x0, 0x1F4)
    Sleep(1000)
    Sleep(2000)
    OP_AE(0x1F4)
    Sleep(1000)

    def lambda_3A3():

        label("loc_3A3")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_3A3")

    QueueWorkItem2(0x105, 1, lambda_3A3)

    def lambda_3B4():
        OP_8E(0xFE, 0xEAEC, 0x3E8, 0x2CEC, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3B4)

    def lambda_3CF():
        OP_6D(60140, 700, 12000, 3500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3CF)

    def lambda_3E7():
        OP_6C(0, 3500)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_3E7)
    WaitChrThread(0x101, 0x1)
    OP_44(0x105, 0x1)
    WaitChrThread(0x101, 0x2)
    SetChrFlags(0x101, 0x4)
    OP_96(0x101, 0xEAEC, 0x2BC, 0x2ADA, 0xC8, 0xFA0)
    SetChrChipByIndex(0x101, 0)
    Sleep(500)

    ChrTalk(    #4
        0x101,
        (
            "#1025F#6PA whole lot happened after that...\x02\x03",

            "Our calm, serene princess,\x01",
            "Joshua, has left us.\x02\x03",

            "Now it's just us on the stage.\x02\x03",

            "#1016FHaving no 'supporting cast'\x01",
            "feels kinda strange, y'know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x105,
        (
            "#047FIt does...\x02\x03",

            "#040FSay, Estelle?\x01",
            "May I make a small confession?\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x101, 0x10)
    TurnDirection(0x101, 0x105, 0)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x4), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_551")
    SetChrSubChip(0x101, 2)
    Jump("loc_56C")

    label("loc_551")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_567")
    SetChrSubChip(0x101, 2)
    Jump("loc_56C")

    label("loc_567")

    SetChrSubChip(0x101, 1)

    label("loc_56C")

    OP_8C(0x101, 180, 0)
    SetChrFlags(0x101, 0x10)

    ChrTalk(    #6
        0x101,
        "#1004F#6PUh, sure?\x02",
    )

    CloseMessageWindow()
    OP_20(0x7D0)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (108, "loc_5AD"),
        (109, "loc_5EA"),
        (112, "loc_627"),
        (113, "loc_664"),
        (SWITCH_DEFAULT, "loc_6A1"),
    )


    label("loc_5AD")

    OP_8E(0x105, 0xE786, 0x0, 0x2CEC, 0x7D0, 0x0)
    SetChrFlags(0x105, 0x4)
    OP_96(0x105, 0xE786, 0x2BC, 0x2ADA, 0xC8, 0xFA0)
    SetChrChipByIndex(0x105, 1)
    Sleep(500)
    Jump("loc_6A1")

    label("loc_5EA")

    OP_8E(0x105, 0xEE8E, 0x0, 0x2CEC, 0x7D0, 0x0)
    SetChrFlags(0x105, 0x4)
    OP_96(0x105, 0xEE8E, 0x2BC, 0x2ADA, 0xC8, 0xFA0)
    SetChrChipByIndex(0x105, 1)
    Sleep(500)
    Jump("loc_6A1")

    label("loc_627")

    OP_8E(0x105, 0xE786, 0x0, 0x2CEC, 0x7D0, 0x0)
    SetChrFlags(0x105, 0x4)
    OP_96(0x105, 0xE786, 0x2BC, 0x2ADA, 0xC8, 0xFA0)
    SetChrChipByIndex(0x105, 1)
    Sleep(500)
    Jump("loc_6A1")

    label("loc_664")

    OP_8E(0x105, 0xEE8E, 0x0, 0x2CEC, 0x7D0, 0x0)
    SetChrFlags(0x105, 0x4)
    OP_96(0x105, 0xEE8E, 0x2BC, 0x2ADA, 0x1F4, 0xFA0)
    SetChrChipByIndex(0x105, 1)
    Sleep(500)
    Jump("loc_6A1")

    label("loc_6A1")

    OP_21()
    OP_1D(0x76)
    Sleep(500)

    ChrTalk(    #7
        0x105,
        (
            "#540FI...liked Joshua.\x01",
            "I mean, you know...um...affectionately.\x02\x03",

            "I was a bit attracted to him\x01",
            "from the moment we met.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x101,
        (
            "#1004F#6PWha...\x02\x03",

            "#1025FI...see.\x02\x03",

            "#1016FHaha, I actually kinda figured.\x01",
            "It always sorta seemed that way...\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x105, 0x10)
    TurnDirection(0x105, 0x101, 0)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x105, 0x4), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_7B4")
    SetChrSubChip(0x105, 2)
    Jump("loc_7CF")

    label("loc_7B4")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x105, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7CA")
    SetChrSubChip(0x105, 2)
    Jump("loc_7CF")

    label("loc_7CA")

    SetChrSubChip(0x105, 1)

    label("loc_7CF")

    OP_8C(0x105, 180, 0)
    SetChrFlags(0x105, 0x10)

    ChrTalk(    #9
        0x105,
        (
            "#542FThat kiss scene at the end of the play...\x01",
            "I won't deny, it sent my heart racing.\x02\x03",

            "I kept apologizing quietly to you even\x01",
            "as I threw myself into the role...\x02\x03",

            "#045FI was all set to really kiss him\x01",
            "at the end, not just pretend.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x101,
        (
            "#1013F#6PR-Really?\x02\x03",

            "You're a lot braver than I thought, Kloe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x105,
        (
            "#542FEh-heh... Julia says I always do\x01",
            "things that make her worry.\x02\x03",

            "#047FBut then when Mayor Dalmore pointed\x01",
            "that gun at you, Estelle...\x02\x03",

            "Joshua's eyes... I've never seen eyes\x01",
            "so full of...m-murderous rage...\x02\x03",

            "And it was all because you're\x01",
            "that important to him.\x02\x03",

            "#542FThat's when I gave up, because I realized\x01",
            "I never had a chance against that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x101,
        (
            "#1015F#6PU-Umm...\x02\x03",

            "I dunno, I think it might be a little\x01",
            "too early for you to give up.\x02\x03",

            "#1007FI mean, honestly, Kloe, I can't\x01",
            "hope to compare to you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x105,
        (
            "#048FOh, Estelle, you're so silly when\x01",
            "it comes to this sort of thing.\x02\x03",

            "You really have no idea just\x01",
            "how charming you are.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x101,
        (
            "#1019F#6PMan, I pay you a compliment and you poke\x01",
            "fun at me. Come on, Kloe, I was serious.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x105,
        (
            "#045FHeehee! But that's just it... So was I.\x02\x03",

            "#542FI love that about you, Estelle.\x01",
            "Your open honesty.\x02\x03",

            "And I think Joshua feels the same way.\x02\x03",

            "I guess Joshua and I are\x01",
            "a bit alike in that sense...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x101,
        (
            "#1004F#6PYou know, I did notice that, kind of.\x02\x03",

            "#1015FYou're both smart, level-headed,\x01",
            "polite...\x02\x03",

            "To be honest, I totally told Joshua\x01",
            "you two would be great together\x01",
            "because of that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x105,
        (
            "#049FUntil I met everyone here,\x01",
            "I was...very lonely.\x02\x03",

            "I think, in that sense, I was a little\x01",
            "like Joshua, before he met you.\x02\x03",

            "#047FIf there's a difference between us...\x01",
            "it would be our strength.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x101,
        "#1004F#6PYour strength? Like how?\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x105, 0)
    Sleep(500)

    ChrTalk(    #19
        0x105,
        (
            "#043FGrandmother wishes, very much,\x01",
            "to name me the next queen.\x01",
            "Especially after what happened recently.\x02\x03",

            "I guess it would be for the best,\x01",
            "all things considered, but...\x02\x03",

            "#047FIf I become queen, I'll never be Kloe Rinz again.\x02\x03",

            "I will be Klaudia von Auslese forevermore,\x01",
            "burdened with power and responsibility.\x02\x03",

            "I'd never again get to hug those orphans,\x01",
            "or talk to my friends casually, or attend\x01",
            "class...\x02\x03",

            "#049FThe very idea...terrifies me.\x02\x03",

            "Yet, I feel so pathetic for not having\x01",
            "the strength to return to that solitude\x01",
            "when it's necessary.\x02\x03",

            "I still haven't given Grandmother\x01",
            "a proper answer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x101,
        "#1026F#6PKloe...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x105,
        (
            "#542FIn that sense, Joshua is stronger\x01",
            "than I could ever hope to be.\x02\x03",

            "I'm sure that he, more than anyone,\x01",
            "didn't want to be separated from you.\x02\x03",

            "But even so, he disappeared so\x01",
            "as to not involve you in what he\x01",
            "felt was his own problem...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x101,
        (
            "#1003F#6PJoshua's...strong, on some level, yeah.\x02\x03",

            "#1010FBut I don't think that's the kind\x01",
            "of strength you should admire.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x105, 0x1), scpexpr(EXPR_PUSH_LONG, 0xEAEC), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1252")
    SetChrSubChip(0x105, 1)
    Jump("loc_1257")

    label("loc_1252")

    SetChrSubChip(0x105, 2)

    label("loc_1257")

    Sleep(500)

    ChrTalk(    #23
        0x105,
        "#044FHmm...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x101,
        (
            "#1025F#6PIt's the role of a queen to rule a whole country.\x01",
            "Of course you're hesitating, it's natural!\x02\x03",

            "Heck, what'd be really worrying would be if\x01",
            "you wanted it without hesitating, like Dunan.\x02\x03",

            "Being worried and unsure about whether\x01",
            "you'll be good, and still trying anyway...\x01",
            "that's why you'll be an amazing queen, Kloe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x105,
        "#542FEstelle...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x101,
        (
            "#1002F#6PBut Joshua...\x02\x03",

            "Joshua didn't hesitate.\x02\x03",

            "He barely thought twice. He left me...\x01",
            "left us...behind as if it were the most\x01",
            "natural thing in the world.\x02\x03",

            "#1003FThat... That's something I can't forgive him for.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x105,
        (
            "#043FEstelle...\x02\x03",

            "#047FYou're right... It IS unforgivable.\x02\x03",

            "#042FWhy is it the cute ones are always the ones\x01",
            "who don't understand a girl's feelings?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x105, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x101)
    OP_63(0x105)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (108, "loc_1583"),
        (112, "loc_1583"),
        (109, "loc_1612"),
        (113, "loc_1612"),
        (SWITCH_DEFAULT, "loc_164F"),
    )


    label("loc_1583")


    ChrTalk(    #28
        0x105,
        (
            "#045F#3P#1KEspecially the ones who...\x01",
            "*snerk* are cuter than... Heehee!\x02",
        )
    )


    ChrTalk(    #29
        0x101,
        (
            "#1016F#4P#1KAnd don't forget the...\x01",
            "*snicker* teeheehee...!\x02",
        )
    )

    Jump("loc_164F")

    label("loc_1612")


    ChrTalk(    #30
        0x101,
        "#1016F#3P#1KTeeheehee!\x02",
    )


    ChrTalk(    #31
        0x105,
        "#045F#4P#1KHahahaha! Ah...\x02",
    )

    Jump("loc_164F")

    label("loc_164F")

    Sleep(1000)
    OP_56(0x1)
    OP_59()
    Sleep(500)

    ChrTalk(    #32
        0x101,
        (
            "#1017F#6PI'm so glad we're friends, Kloe.\x02\x03",

            "I don't have many people I can\x01",
            "open up to quite like this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x105,
        (
            "#041FHaha! Neither do I.\x02\x03",

            "#542FAlthough, all we've been talking about\x01",
            "are embarrassing things, really...\x02\x03",

            "Oh, um, please don't misunderstand me,\x01",
            "though!\x02\x03",

            "I don't feel, um, that way about\x01",
            "Joshua at all now...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x101,
        (
            "#1016F#6PAh, don't worry, it's okay.\x02\x03",

            "#1017FI...kinda learned the hard way\x01",
            "that love isn't something you\x01",
            "should try and hold back.\x02\x03",

            "Haha... I guess my dad would totally\x01",
            "call us both a couple of dumb kids...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x105,
        (
            "#045FThank you, Estelle.\x02\x03",

            "#540FWell...to be honest, if I said I didn't\x01",
            "have any feelings left toward him,\x01",
            "I'd be lying.\x02\x03",

            "But more than anything, I want to\x01",
            "see you two happy together, and--\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x101,
        (
            "#1012F#6PDon't worry. I get it.\x02\x03",

            "#1006FAnyway! We've spent a bit too\x01",
            "much time with girl talk, I think.\x02\x03",

            "Wanna get back to interviewing\x01",
            "the students?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x105,
        (
            "#045FYes, we should.\x02\x03",

            "Let's try to talk to everyone before nightfall.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_20(0x7D0)
    OP_0D()
    OP_6D(60140, 1000, 12380, 0)
    OP_67(0, 2930, -10000, 0)
    OP_6B(1420, 0)
    OP_6C(0, 0)
    OP_6E(673, 0)
    SetChrSubChip(0x101, 0)
    SetChrSubChip(0x105, 0)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0x105, 65535)
    SetChrPos(0x101, 60140, 1000, 12380, 180)
    SetChrPos(0x105, 60140, 1000, 12380, 180)
    Sleep(500)
    OP_21()
    OP_1D(0xE)
    FadeToBright(1000, 0)
    OP_A2(0x1220)
    EventEnd(0x0)
    Return()

    # Function_2_16A end

    def Function_3_1AB2(): pass

    label("Function_3_1AB2")

    OP_8E(0xFE, 0xEAEC, 0x0, 0x391C, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 400)
    Return()

    # Function_3_1AB2 end

    def Function_4_1ACE(): pass

    label("Function_4_1ACE")

    OP_8E(0xFE, 0xE786, 0x0, 0x3C8C, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 400)
    Return()

    # Function_4_1ACE end

    def Function_5_1AEA(): pass

    label("Function_5_1AEA")

    OP_8E(0xFE, 0xEE8E, 0x0, 0x3C8C, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 400)
    Return()

    # Function_5_1AEA end

    def Function_6_1B06(): pass

    label("Function_6_1B06")

    OP_8E(0xFE, 0xE786, 0x0, 0x3624, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 400)
    Return()

    # Function_6_1B06 end

    def Function_7_1B22(): pass

    label("Function_7_1B22")

    OP_8E(0xFE, 0xEE8E, 0x0, 0x3624, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 400)
    Return()

    # Function_7_1B22 end

    def Function_8_1B3E(): pass

    label("Function_8_1B3E")

    EventBegin(0x0)
    SetChrFlags(0x102, 0x80)
    OP_6D(1070, -250, -3000, 0)
    OP_67(0, 5920, -10000, 0)
    OP_6B(3300, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)

    def lambda_1B88():
        OP_6D(1580, -250, 13840, 5000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1B88)
    FadeToBright(1000, 0)
    WaitChrThread(0x102, 0x1)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10FE)
    OP_A2(0x10FB)
    NewScene("ED6_DT21/T2500   ._SN", 125, 0, 0)
    IdleLoop()
    Return()

    # Function_8_1B3E end

    SaveToFile()

Try(main)
